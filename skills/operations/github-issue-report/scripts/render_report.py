#!/usr/bin/env python3
"""Render a reconciled issue report as one continuous A4-width PDF. No network."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape

from PIL import Image as PILImage
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import FloatObject, NameObject
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Flowable, Image, Paragraph, Spacer, Table, TableStyle

WIDTH = 210 / 25.4 * 72
MARGIN = 12 / 25.4 * 72
CONTENT = WIDTH - MARGIN * 2
INK = colors.HexColor('#20252b')
MUTED = colors.HexColor('#57606a')


def filename(title):
    separators = [value for value in (os.sep, os.altsep) if value]
    if not title.strip() or '\x00' in title or any(c in title for c in separators):
        raise ValueError('Title needs a filename exception; preserve the exact title and ask about the minimum substitution.')
    if os.name == 'nt' and (any(c in title for c in '<>:"|?*') or title.endswith((' ', '.'))):
        raise ValueError('Title is not a valid filename on this platform.')
    name = title + '.pdf'
    if len(name.encode('utf-8')) > 255:
        raise ValueError('Exact filename exceeds the filesystem limit.')
    return name


def font_pair(regular=None, bold=None):
    if bool(regular) != bool(bold):
        raise ValueError('Provide both font paths.')
    bundled = Path.home() / '.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype'
    pairs = [(regular, bold)] if regular else [
        (str(bundled / 'NotoSans-Regular.ttf'), str(bundled / 'NotoSans-Bold.ttf')),
        ('/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf', '/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf'),
        ('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'),
        ('/System/Library/Fonts/Supplemental/Arial.ttf', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'),
    ]
    for a, b in pairs:
        if a and b and Path(a).is_file() and Path(b).is_file():
            pdfmetrics.registerFont(TTFont('Report', a))
            pdfmetrics.registerFont(TTFont('ReportBold', b))
            return [str(a), str(b)]
    raise ValueError('No supported TrueType pair found. Supply --font-regular and --font-bold.')


class Checkbox(Flowable):
    def __init__(self, checked):
        super().__init__()
        self.checked = checked
        self.width, self.height = 17, 16

    def draw(self):
        c = self.canv
        c.setLineWidth(.8)
        c.setStrokeColor(INK if self.checked else colors.HexColor('#8c959f'))
        c.roundRect(.5, 3.5, 8.5, 8.5, 1, fill=0, stroke=1)
        if self.checked:
            c.setStrokeColor(INK)
            c.setLineWidth(1.1)
            p = c.beginPath()
            p.moveTo(2, 7.5)
            p.lineTo(4, 5.5)
            p.lineTo(7.5, 10)
            c.drawPath(p)


def render(source, output_dir, regular=None, bold=None):
    source = source.resolve()
    raw = source.read_bytes()
    d = json.loads(raw)
    title, url = d['title'], d['issue_url']
    parsed = urlsplit(url)
    if parsed.scheme != 'https' or not parsed.hostname or '/issues/' not in parsed.path or parsed.query:
        raise ValueError('Use the canonical HTTPS issue URL.')
    dest = output_dir.resolve() / filename(title)
    if dest.exists():
        raise FileExistsError(f'Preserve existing output; use another issue-specific folder: {dest}')
    fonts = font_pair(regular, bold)
    body = ParagraphStyle('Body', fontName='Report', fontSize=11, leading=16, textColor=INK, splitLongWords=True)
    small = ParagraphStyle('Small', parent=body, fontSize=9.5, leading=13, textColor=MUTED)
    heading = ParagraphStyle('Heading', parent=body, fontName='ReportBold', fontSize=15, leading=20)
    title_style = ParagraphStyle('Title', parent=heading, fontSize=22, leading=27)
    blocks, expected, proofs = [], [], []

    def add(flow, kind, text=None, **extra):
        blocks.append((flow, {'kind': kind, **extra}))
        if text:
            expected.append(text)

    def para(text, style=body):
        return Paragraph(escape(text).replace('\n', '<br/>'), style)

    def gap(h):
        add(Spacer(1, h), 'space')

    def section(text):
        gap(13)
        add(para(text, heading), 'heading', text)
        gap(9)

    def row(prefix, text, kind, **extra):
        table = Table([[prefix, para(text)]], colWidths=[21, CONTENT - 21])
        table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                   ('LEFTPADDING', (0, 0), (-1, -1), 0),
                                   ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                                   ('TOPPADDING', (0, 0), (-1, -1), 0),
                                   ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
        add(table, kind, text, **extra)
        gap(6)

    add(para(title, title_style), 'title', title)
    gap(10)
    add(Paragraph('<link href="' + escape(url, {'"': '&quot;'}) + '" color="#0969da">' + escape(url) + '</link>', small), 'issue_url', url)
    gap(18)
    if not d['description'] or not d['outcomes'] or not d['tasks']:
        raise ValueError('Description, outcomes and task checklist must be nonempty.')
    for text in d['description']:
        add(para(text), 'description', text)
        gap(8)
    section('Outcomes')
    for i, text in enumerate(d['outcomes'], 1):
        row(para(str(i) + '.'), text, 'outcome', number=i)
    section('Task checklist')
    for task in d['tasks']:
        if type(task.get('done')) is not bool or not task.get('source_refs'):
            raise ValueError('Each task needs a boolean done and supporting source_refs.')
        row(Checkbox(task['done']), task['text'], 'task', done=task['done'])
    section('Proof of work')
    if d.get('proof_note'):
        add(para(d['proof_note'], small), 'proof_note', d['proof_note'])
        gap(13)
    seen = set()
    for i, proof in enumerate(d['proof'], 1):
        path = Path(proof['path'])
        if not path.is_absolute():
            path = source.parent / path
        path = path.resolve()
        data = path.read_bytes()
        sha = hashlib.sha256(data).hexdigest()
        if sha in seen:
            raise ValueError('Duplicate image bytes; reconcile the proof manifest before rendering.')
        seen.add(sha)
        image_url = urlsplit(proof['source_url'])
        if image_url.scheme != 'https' or image_url.query or image_url.hostname == 'private-user-images.githubusercontent.com':
            raise ValueError('Use a permanent proof URL without expiring access material.')
        with PILImage.open(path) as im:
            w, h = im.size
        caption = f"{i:02d}. {proof['caption']}"
        add(para(caption, small), 'caption', caption, index=i)
        gap(7)
        add(Image(str(path), width=CONTENT, height=CONTENT * h / w), 'proof', index=i, source_url=proof['source_url'])
        gap(18)
        proofs.append({'index': i, 'path': str(path), 'sha256': sha, 'source_url': proof['source_url'], 'caption': proof['caption']})

    for name in ('Report', 'ReportBold'):
        chars = pdfmetrics.getFont(name).face.charToGlyph
        missing = sorted({ch for text in expected for ch in text if not ch.isspace() and ord(ch) not in chars})
        if missing:
            raise ValueError(f'Font lacks required characters: {missing}')
    measured = [(flow, meta, flow.wrap(CONTENT, 10**9)[1]) for flow, meta in blocks]
    height = MARGIN * 2 + sum(h for _, _, h in measured)
    output_dir.mkdir(parents=True, exist_ok=True)
    work = output_dir / '.report-work'
    work.mkdir(exist_ok=True)
    raw_pdf = work / 'raw.pdf'
    c = canvas.Canvas(str(raw_pdf), pagesize=(WIDTH, height), pageCompression=1, pdfVersion=(1, 7))
    c.setTitle(title)
    c.setAuthor('')
    c.setFillColor(colors.white)
    c.rect(0, 0, WIDTH, height, fill=1, stroke=0)
    y = height - MARGIN
    bounds = []
    for flow, meta, h in measured:
        top = height - y
        flow.drawOn(c, MARGIN, y - h)
        if meta['kind'] == 'proof':
            c.linkURL(meta['source_url'], (MARGIN, y - h, WIDTH - MARGIN, y), relative=0)
        bounds.append({**meta, 'top_pt': top, 'height_pt': h})
        y -= h
    c.showPage()
    c.save()
    reader = PdfReader(raw_pdf)
    unit = max(1, math.ceil(height / 14400))
    writer = PdfWriter()
    writer.pdf_header = '%PDF-1.7'
    page = writer.add_blank_page(width=WIDTH / unit, height=height / unit)
    if unit > 1:
        page[NameObject('/UserUnit')] = FloatObject(unit)
    page.merge_transformed_page(reader.pages[0], Transformation().scale(1 / unit))
    writer.add_metadata({'/Title': title})
    with dest.open('wb') as f:
        writer.write(f)
    saved = PdfReader(dest)
    p = saved.pages[0]
    effective_width = float(p.mediabox.width) * float(p.get('/UserUnit', 1))
    assert len(saved.pages) == 1 and abs(effective_width - WIDTH) < .01
    text = ' '.join((p.extract_text() or '').split())
    for item in expected:
        assert ' '.join(item.split()) in text, f'Text missing: {item}'
    assert any(a.get_object().get('/A', {}).get('/URI') == url for a in p.get('/Annots', []))
    receipt = {'pdf': str(dest), 'title': title, 'source_sha256': hashlib.sha256(raw).hexdigest(),
               'pages': 1, 'width_mm': effective_width / 72 * 25.4, 'height_pt': height,
               'user_unit': unit, 'fonts': fonts, 'proof_count': len(proofs),
               'completed_tasks': sum(t['done'] for t in d['tasks']), 'total_tasks': len(d['tasks']),
               'expected_text': expected, 'proof': proofs, 'elements': bounds}
    (work / 'layout.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')
    return {k: receipt[k] for k in ('pdf', 'pages', 'width_mm', 'proof_count', 'completed_tasks', 'total_tasks')}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', required=True, type=Path)
    p.add_argument('--output-dir', required=True, type=Path)
    p.add_argument('--font-regular')
    p.add_argument('--font-bold')
    a = p.parse_args()
    print(json.dumps(render(a.input, a.output_dir, a.font_regular, a.font_bold), ensure_ascii=False))


if __name__ == '__main__':
    main()
