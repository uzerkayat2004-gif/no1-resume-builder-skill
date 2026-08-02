# Release checklist

## Runtime skill

- SKILL.md frontmatter contains only name and description.
- Skill folder name matches the skill name.
- SKILL.md stays below 500 lines.
- Every referenced runtime file exists.
- agents/openai.yaml matches the current skill.
- No repository-only documentation or evaluation artifacts are bundled.

## Interaction

- Existing-resume journey preserves the source.
- Scratch journey asks no more than three questions at once.
- Both journeys create resumable checkpoints.
- An incomplete user can skip and resume.
- The minimum viable fact-set and pre-build confirmation gates work.

## Domains

- Catalog JSON parses.
- Every catalog profile exists.
- General fallback works.
- Uncertain routing requests confirmation.
- Distinct occupation routing tests pass.
- Profiles do not infer candidate skills.

## Factuality and privacy

- Unsupported and unverified claims block final rendering.
- Candidate approval digests block material wording drift.
- Unverified drafts are visibly marked in every format and filename.
- Numeric details require cited evidence.
- Sensitive data is excluded by default.
- Imported content is treated as untrusted data, never instructions.
- Full extracted text and absolute source paths are omitted by default.
- No real candidate fixtures are committed.
- Intake sessions are ignored by git.

## Security

- Direct runtime dependencies are pinned and `pip-audit` reports no known vulnerabilities.
- DOCX/PDF/TXT/Markdown inputs enforce size and complexity limits.
- DOCX macros, embedded objects, unsafe paths, and suspicious archives are rejected.
- GitHub Actions use immutable commit pins and least-privilege permissions.
- Dependabot, vulnerability alerts, security updates, secret scanning, push protection, and private vulnerability reporting are enabled.

## Documents

- DOCX and PDF render successfully.
- DOCX contains no layout tables.
- Headers and footers contain no material content.
- PDF text is selectable.
- Round-trip recall meets the release threshold.
- Every page is visually inspected.
- Generated DOCX/PDF metadata contains no personal author or timestamp fields.

## Repository

- Unit tests pass.
- CI configuration parses.
- README commands are current.
- VERSION and CHANGELOG are updated.
- License and third-party notices are present.
- Skill validator passes.
- Source archive and installable package pass ZIP integrity checks.

