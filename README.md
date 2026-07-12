# Hung Q. Nguyen — Academic Personal Website

A lightweight static website for:

`https://kuniong.github.io`

The design is intentionally academic and restrained: clear typography, simple navigation, conventional content hierarchy, and no corporate-style hero graphics or marketing sections. Applied projects remain visible, but they are presented as research case studies rather than a commercial portfolio.

## Site structure

- **Home** — short academic profile, research interests, selected publications, selected applied research, news, and contact
- **Research** — three connected research themes with related papers and projects
- **Publications** — filterable publication list with brief contribution notes
- **Projects** — selected applied and industrial research at a confidentiality-safe level
- **Teaching (hidden from navigation)** — retained for possible future use
- **CV** — printable web CV
- **Work detail pages** — deeper explanations of selected papers and applied projects

The `/teaching/` and `/experience/` pages are retained but are not placed in the main navigation; professional appointments are also shown in the CV.

## Deploy to GitHub Pages

1. Create a public repository named exactly `kuniong.github.io`.
2. Upload the **contents of this folder** to the repository root.
3. Commit and push to `main`.
4. Open **Settings → Pages → Build and deployment**.
5. Choose **Deploy from a branch**, then `main` and `/(root)`.
6. Save.

The `.nojekyll` file is intentional. No build process is required on GitHub Pages.

## Preview locally

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Editing

For quick edits, change the generated HTML files directly.

For structured edits, modify `build_site.py` and run:

```bash
python -m pip install -r requirements.txt
python build_site.py
```

## Information still worth adding later

- A preferred permanent academic email address when available
- Current academic title and affiliation after an appointment change
- Talks and seminars, once there is enough material for a separate page
- Public code/data repositories for individual papers
- Company-approved quantitative outcomes, only where disclosure is explicitly safe

## Confidentiality choices

Industrial project pages intentionally omit client identities, proprietary data, operational parameters, internal screenshots, system architecture, reconstructive algorithm details, and non-public KPIs. They show the problem class, your role, broad methods, and the nature of the outcome.
