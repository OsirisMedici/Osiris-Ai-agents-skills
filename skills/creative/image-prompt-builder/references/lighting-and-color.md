# Lighting and color

The highest-leverage section of any image prompt. Higgsfield responds strongly to specific lighting direction + color temperature + hex codes. Vague lighting language is the #1 reason AI image output looks generic.

## Lighting direction

| Setup | Description | Visual signature |
|---|---|---|
| **Rembrandt** | 45° camera side, 45° above; small triangle of light under eye on shadow side | Classic portraiture, introspective mood |
| **Butterfly (Paramount)** | Frontal, high — shadow under nose shaped like a butterfly | Glamour, beauty, magazine cover |
| **Split** | 90° side — half face lit, half shadow | Dramatic, editorial, masculine |
| **Loop** | 30°–45° side, moderate — small nose shadow loops off to shadow side | Natural portrait, flattering |
| **Broad** | Light on side of face toward camera | Widens subject, casual |
| **Short** | Light on side of face away from camera | Narrows subject, slimming, moody |
| **Backlit / rim** | Light behind subject, rim of highlight around silhouette | Silhouette effect, halo, sunset shoots |
| **Top-down** | Light directly above | Harsh shadows under brow, noir |
| **Underlight** | Light from below | Horror / theatrical / unnatural |
| **Front-flat** | Flat frontal light | Fashion flash, bold flat editorial |
| **Cross-light** | Two opposing side lights | Sculpts form, product photography |
| **Window light (natural)** | Diffused from a large window | Editorial lifestyle default, soft wrap |
| **Open shade** | Outdoor, shaded from sun | Even, cool, flattering |

For architecture/interiors:

| Setup | Description |
|---|---|
| **North light** | Cool, even, no direct sun — classic studio/atelier window |
| **Directional sun** | Hard shadows through windows, angular graphic shapes |
| **Golden hour** | Low warm directional sun, long shadows, orange-gold cast |
| **Blue hour** | Post-sunset ambient blue + interior tungsten glow |
| **Overcast** | Soft diffused, shadowless, muted |
| **Practicals as key** | Interior lamps drive the scene, exterior is dark or dim |

## Lighting quality

- **Hard**: Small source relative to subject, sharp-edged shadows, high contrast
- **Soft**: Large source relative to subject, gradual shadow falloff, flattering
- **Diffused**: Soft + directional weakened, even illumination
- **Dappled**: Broken by foliage, blinds, or screen — pattern of light and shadow
- **Specular**: Glossy highlights, reflective surfaces emphasized
- **Wrapped**: Soft light curving around subject, low shadow density

## Color temperature (Kelvin)

| Kelvin | Name | Feel |
|---|---|---|
| 1800K–2500K | Candle, sunset, firelight | Deeply warm, orange-red, intimate |
| 2700K | Warm tungsten | Classic interior lamp, cozy, residential |
| 3200K | Tungsten standard | Film/cinema tungsten key |
| 4000K | Warm white fluorescent | Neutral-warm, office-ish |
| 5000K | Daylight balanced | Studio standard, neutral |
| 5600K | Midday sun | Clean, neutral daylight |
| 6500K | Overcast daylight | Slightly cool, flat |
| 7500K+ | Shade, twilight | Blue-cast, cold |
| 10000K+ | Deep blue hour | Icy blue, moody |

**Mixed-temperature scenes** are a signature of editorial architecture: `warm 2700K interior tungsten practicals against cool 10000K blue-hour exterior through a window`.

## Key highlight + shadow hex codes

Every strong reference has a dominant **highlight tone** and a dominant **shadow tone**. Name both as hex codes. A few useful examples:

| Mood | Highlight hex | Shadow hex |
|---|---|---|
| Warm tungsten editorial | `#F5E6C8` | `#1A1A2E` |
| Cool editorial daylight | `#EDF1F3` | `#242936` |
| Golden hour architecture | `#F4C57B` | `#3A2A1E` |
| Moody interior | `#D9B380` | `#0F0D0B` |
| High-key fashion | `#FFFFFF` | `#C8C4B8` |
| Film noir B&W | `#F0F0EC` | `#0A0A0A` |
| Teal & orange cinema | `#F1A66A` | `#0D2A33` |
| Wes Anderson pastel | `#F7D7A8` | `#C78F67` |
| A24 muted | `#D4C4A8` | `#3D3428` |

## Color grading presets (hex triads)

Each "preset" is a 3-5 color mood. Use these as shorthand in Section 2 of the prompt:

**Teal & orange (modern cinema)**
- Highlights `#F1A66A`
- Midtones `#8B7355`
- Shadows `#0D2A33`
- Skin lean warm, shadows lean teal

**Kodak warm (editorial comfort)**
- `#F5E6C8`, `#D4A574`, `#8B6F47`, `#2C1F14`
- Skin glows, materials feel tactile, blacks are warm not neutral

**A24 muted (contemporary indie)**
- `#D4C4A8`, `#A69377`, `#5C5140`, `#2A2620`
- Desaturated, earthy, slight green undertone

**Wes Anderson pastel**
- `#F2D6A4`, `#C78F67`, `#8A6A4A`, `#EDB5A3`
- Flat lighting, symmetry, dollhouse unreality

**High-contrast B&W**
- `#FFFFFF`, `#888888`, `#000000` (no midtone mush)
- Split between pure highlight and deep shadow

**Desaturated earth**
- `#C9B896`, `#7A6A52`, `#3F3628`, `#1C1610`
- Documentary, National Geographic feel

**Moody editorial (Architectural Digest night shoot)**
- `#E8DCC4`, `#C9A961`, `#2B1810`, `#0A0706`
- Low key, luxury, quiet

**Monochromatic (tonal)**
- Single hue at multiple values, e.g., all sepia, all cyan, all rose
- Strong stylistic signature

## Gels and tints

Sometimes lights are colored — either practicals, gels over studio lights, or post-grade:

| Gel | Hex | Use |
|---|---|---|
| Warm amber (CTO) | `#E8A85C` | Makes daylight look like tungsten |
| Cool blue (CTB) | `#6EA8D4` | Makes tungsten look like daylight |
| Magenta | `#D4479A` | Editorial pop, neon club |
| Teal | `#3FA89E` | Cinematic cool, tech |
| Green | `#7FC242` | Unnatural, horror, surveillance |
| Red | `#D4352E` | Warning, intensity, darkroom |

Name the gel *and* the hex. Higgsfield parses both.

## Contrast and saturation

- **High contrast**: blacks crushed, highlights blown, little midtone
- **Medium contrast**: full tonal range, balanced
- **Low contrast (flat)**: lifted blacks, protected highlights, creamy midtone
- **Vivid saturation**: all colors pumped
- **Natural saturation**: what the eye would see
- **Muted saturation**: pulled back, painterly
- **Desaturated**: near-B&W with color hints

Specify both. Example: `medium contrast with crushed shadows only in the deepest corners, muted saturation except for the brass lamp which stays warm-saturated`.

## Writing lighting into prompts

Strong: `light falling from camera-left at approximately 30° through a tall window, hard quality with specular highlights on the travertine coffee table, 2700K warm tungsten practicals on the wall sconces, key highlights at #F5E6C8 and shadow tone at #1A1A2E, medium contrast, muted saturation`

Weak: `moody warm lighting`

---
— Add new entries here —
