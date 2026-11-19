# Needs image (do not merge until files exist)

This PR only adds article thumbnails for two existing money pages. Leave it **open** until the coordinator ChatGPT batch drops the WebP files.

| Page | Expected path | Scene |
| --- | --- | --- |
| `/money/medicare-part-b-premium-2027/` | `assets/img/medicare-part-b-premium-2027.webp` (+ optional `assets/img/og-medicare-part-b-premium-2027.jpg`) | Photoreal news still: Medicare / benefits paperwork and a pen on a kitchen table in soft natural daylight; no faces, logos, or readable text |
| `/money/2027-tax-numbers/gift-estate-tax-2027/` | `assets/img/gift-estate-tax-2027.webp` (+ optional `assets/img/og-gift-estate-tax-2027.jpg`) | Photoreal news still: estate-planning papers and a calculator on a wooden desk in soft daylight; no faces, logos, or readable text |

Also register both WebPs in `.legal-gate/image-provenance.json` as AI-generated before merge.
