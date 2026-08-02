# GitHub publishing

Use these settings when creating the public repository.

## Repository identity

- Display title: **No. 1 Resume Builder Skill**
- Repository slug: `no1-resume-builder-skill`
- Visibility: Public
- License: MIT
- Default branch: `main`

Recommended description:

> Open-source Codex skill that builds truthful, job-tailored, ATS-readable resumes and interview practice from an upload or from scratch.

“ATS-readable” refers to restrained formatting and observable extraction checks. It is not a promise of an ATS score or employer outcome.

## Suggested topics

```text
resume
resume-builder
cv
codex
codex-skill
open-source
job-search
career
interview-preparation
ats
docx
pdf
python
```

## About-section settings

- Website: leave empty unless the project later has a maintained documentation site.
- Releases: enabled.
- Issues: enabled.
- Discussions: optional; useful for domain and country guidance requests.
- Wiki: unnecessary while versioned documentation lives in `docs/`.

## Current release

- Tag: `v1.3.0`
- Title: `No. 1 Resume Builder Skill v1.3.0`

Suggested release summary:

> Faster confirmation-first release of the evidence-first Resume Builder Codex skill. It confirms material facts and assumptions before layout, then writes and renders the final resume once. Marked previews remain available only when the candidate explicitly requests one.

Attach:

- `no1-resume-builder-skill-v1.3.0.skill`
- `no1-resume-builder-skill-v1.3.0-source.zip`
- `no1-resume-builder-skill-v1.3.0-SHA256SUMS.txt`

## Social preview

Use `docs/assets/sample-resume-preview.png` only as an example screenshot inside the README. A future social card should use the project title and evidence-first tagline rather than showing synthetic contact information.

## Pre-publication checklist

- [ ] README links work from the repository root.
- [ ] All examples are synthetic or explicitly consented.
- [ ] No intake session or real candidate record is committed.
- [ ] `python -m unittest discover -s tests -v` passes.
- [ ] `python scripts/release_check.py` passes.
- [ ] The runtime skill passes the official skill validator.
- [ ] The `.skill` archive extracts with one top-level `resume-builder/` directory.
- [ ] Release hashes match the published assets.
- [ ] The repository description and topics are applied.
- [ ] The README states that no interview, job or ATS rank is guaranteed.
