# Changelog

## 1.2.1 — 2026-08-02

- Fixed DOCX metadata scrubbing so generated resumes remain compatible with Microsoft Word.
- Preserved required Word XML namespace declarations while still removing author, timestamp, revision, and session identifiers.
- Added a regression check for namespace integrity and verified a generated resume by opening and exporting it through Microsoft Word.

## 1.2.0 — 2026-08-02

- Added candidate-approval digests that block silent changes to material resume facts.
- Forced every unverified output to display a prominent draft warning and draft filename.
- Added an untrusted-document boundary, privacy-minimized intake sessions, and import summaries.
- Added file-size, PDF-page, extracted-text, DOCX archive, macro, and embedded-object limits.
- Pinned patched dependencies, added dependency auditing and Dependabot, and pinned CI actions.
- Removed document timestamps/revision metadata and expanded evidence-linked interview practice.
- Expanded the automated adversarial and rendering suite from 10 to 19 tests.

## 1.1.0 — 2026-08-02

- Published the GitHub wrapper as “No. 1 Resume Builder Skill.”
- Added a source-to-design decision register with short attributable quotations.
- Added tested scenario documentation covering healthcare, trades, hospitality, students, executives, academic CVs, PDF audits, and unknown occupations.
- Added public synthetic DOCX/PDF/TXT/Markdown and interview examples.
- Added GitHub repository metadata and release instructions.
- Kept the installable skill ID stable as `resume-builder`.

## 1.0.0 — 2026-08-02

- Added two explicit entry journeys: existing-resume import and scratch intake.
- Added resumable private intake sessions with progress and next-question reporting.
- Added transparent domain routing and a general fallback.
- Added guidance for technology, data, security, product, project, design, go-to-market, finance, consulting, legal, operations, industrial, trades, healthcare, life sciences, education, research, public sector, nonprofit, service, administration, and executive work.
- Added career-stage overlays.
- Separated repository documentation and evaluations from the runtime skill.
- Added CI, release checks, contribution templates, and repository documentation.
- Preserved evidence gating, numeric grounding, DOCX/PDF rendering, extraction verification, and interview practice.
