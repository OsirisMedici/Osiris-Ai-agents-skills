#!/usr/bin/env python3
"""Join zero-margin A4-width browser print pages into one continuous vector PDF."""

import argparse
import math
import os
from pathlib import Path
import re
from urllib.parse import urlsplit
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import ArrayObject, FloatObject, NameObject

A4_WIDTH = 210 / 25.4 * 72


def output_name(title):
    separators = [value for value in (os.sep, os.altsep) if value]
    if not title or any(value in title for value in separators) or '\x00' in title:
        raise ValueError('Exact title cannot be a filename here; resolve the minimum necessary substitution with the user.')
    if os.name == 'nt' and (any(char in title for char in '<>:"|?*') or title.endswith((' ', '.'))):
        raise ValueError('Exact title contains a Windows-invalid filename character; do not silently rename it.')
    name = title + '.pdf'
    if len(name.encode('utf-8')) > 255:
        raise ValueError('Exact filename exceeds the filesystem component limit; do not silently truncate it.')
    return name


def join_pdf(source, destination, title):
    reader = PdfReader(source)
    if not reader.pages:
        raise ValueError('Source PDF has no pages')
    widths = [float(p.mediabox.width) * float(p.get('/UserUnit', 1)) for p in reader.pages]
    if any(abs(w - A4_WIDTH) > 1 for w in widths):
        raise ValueError('Input must already be A4 width; reflow the browser content instead of scaling a wide sidebar layout.')
    if any(p.rotation for p in reader.pages):
        raise ValueError('Resolve source page rotation before joining')
    # Chromium rounds paper dimensions. Normalize that sub-point discrepancy,
    # never a genuinely wide browser layout, to exactly 210 mm.
    scales = [A4_WIDTH / width for width in widths]
    heights = [float(p.mediabox.height) * float(p.get('/UserUnit', 1)) * scale
               for p, scale in zip(reader.pages, scales)]
    total_height = sum(heights)
    # Keep PDF coordinates within 200 inches while preserving physical A4 width.
    unit = max(1, math.ceil(total_height / 14400))
    writer = PdfWriter()
    target = writer.add_blank_page(width=A4_WIDTH / unit, height=total_height / unit)
    if unit > 1:
        target[NameObject('/UserUnit')] = FloatObject(unit)
        writer.pdf_header = '%PDF-1.7'
    cursor = total_height
    for page, height, scale in zip(reader.pages, heights, scales):
        cursor -= height
        source_unit = float(page.get('/UserUnit', 1))
        transform = Transformation().scale(source_unit * scale / unit).translate(0, cursor / unit)
        target.merge_transformed_page(page, transform)
    if '/Annots' in target:
        kept = []
        for reference in target['/Annots']:
            annotation = reference.get_object()
            uri = annotation.get('/A', {}).get('/URI', '')
            parsed = urlsplit(str(uri))
            if parsed.hostname == 'private-user-images.githubusercontent.com' and parsed.query:
                continue
            kept.append(reference)
        target[NameObject('/Annots')] = ArrayObject(kept)
    writer.add_metadata({'/Title': title})
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open('wb') as handle:
        writer.write(handle)
    check = PdfReader(destination)
    assert len(check.pages) == 1
    physical_width = float(check.pages[0].mediabox.width) * float(check.pages[0].get('/UserUnit', 1))
    assert abs(physical_width - A4_WIDTH) < 0.01
    # A coordinate transform can change pypdf's inferred line-break spacing.
    # Compare every non-whitespace character; visual QA still checks layout.
    before = re.sub(r'\s+', '', '\n'.join(p.extract_text() or '' for p in reader.pages))
    after = re.sub(r'\s+', '', check.pages[0].extract_text() or '')
    assert before == after, 'Printed text changed during joining'
    return {'pages': 1, 'width_mm': physical_width / 72 * 25.4,
            'height_points': total_height, 'user_unit': unit, 'path': str(destination)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--title', required=True)
    args = parser.parse_args()
    try:
        destination = args.output_dir / output_name(args.title)
        if destination.resolve() == args.input.resolve():
            raise ValueError('Keep browser input and final output separate')
        import json
        print(json.dumps(join_pdf(args.input, destination, args.title)))
    except (ValueError, AssertionError, OSError) as error:
        parser.exit(2, str(error) + '\n')


if __name__ == '__main__':
    main()
