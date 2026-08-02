# Maintainer guide

## Principles

- Keep the runtime skill focused.
- Keep repository documentation, tests, and evaluations outside the skill folder.
- Use synthetic, consented, de-identified, or clearly licensed fixtures.
- Treat all intake sessions as private working data.
- Cite current employer-system, government, regulatory, and regional guidance.
- Prefer observable extraction tests to ungrounded ATS claims.

## Runtime skill boundary

The distributable folder is:

    skills/resume-builder/

It should contain only instructions and resources needed at runtime:

- SKILL.md;
- agents/openai.yaml;
- scripts;
- schemas;
- references;
- minimal examples;
- renderer requirements.

## Tests

Run:

    python -m unittest discover -s tests -v

Run the repository check:

    python scripts/release_check.py

Render the synthetic fixture and visually inspect DOCX and PDF pages before changing templates.

## Versioning

Use semantic versioning:

- patch: corrections without workflow/schema breakage;
- minor: compatible domain, interaction, or output features;
- major: breaking schema, CLI, or interaction changes.

Update VERSION and CHANGELOG.md.

## Domain review

A domain contribution should be reviewed for:

- accurate terminology;
- useful evidence prompts;
- appropriate section priorities;
- confidentiality, safety, and licensing concerns;
- geographic variation;
- stereotypes or assumptions;
- router collisions.

