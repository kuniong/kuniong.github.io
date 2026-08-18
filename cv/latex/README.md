# Detailed LaTeX CV

The editable source is `Hung_Q_Nguyen_CV.tex`. The build creates:

- `build/Hung_Q_Nguyen_CV.pdf` — the compiler output
- `../Hung_Q_Nguyen_CV.pdf` — the easy-to-find final PDF

## Build in VS Code

Use **Terminal → Run Build Task** or press **Ctrl+Shift+B**, then choose **Build detailed LaTeX CV**. The first build downloads the single-file Tectonic LaTeX engine into the ignored `.tools` directory. Later builds reuse it.

You can also build from a PowerShell terminal:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\hung-q-nguyen-academic-site\cv\latex\build_cv.ps1
```

Open `cv/Hung_Q_Nguyen_CV.pdf` in VS Code to preview the result.

## Editing notes

- The content is a snapshot of the website information as of August 2026.
- The detailed PDF includes the VietDevelopers teaching/research role and language competencies supplied for this CV, although those sections remain hidden on the current web CV.
- The patent attachment did not include application numbers, filing dates, inventor order, assignees, or public links. Add those details when they are available.
- Two invention entries are marked **Filing planned**. They are included in this local working draft, but should be removed or cleared with the relevant employer/IP representative before the PDF is shared publicly.
- Confirm the official English patent titles before distribution. In particular, the Japanese source for the LLM-serving invention appears to say “queue-value cache,” while the CV uses the technically conventional “key-value cache”; “unmeasured lateral contributions” may also need to be replaced by “unmeasured lateral inflows” if that is the intended hydrological term.
- Rebuild after every edit to the `.tex` file.
