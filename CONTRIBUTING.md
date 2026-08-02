# Contributing

Contributions are welcome, especially regional guidance, accessibility improvements, parser fixtures, and factuality evaluations.

## Ground rules

- Use synthetic, consented, de-identified, or clearly licensed fixtures.
- Do not commit real phone numbers, addresses, private employment records, IDs, or unredacted resumes.
- Cite new factual guidance in references/sources.md.
- Separate documented facts from conventions and opinions.
- Do not add claims that a template is “100% ATS compatible” or guarantees interviews.
- Do not add automatic metric invention or keyword-stuffing behavior.

## Development

    python -m pip install -r requirements.txt
    python -m unittest discover -s tests -v

Render the synthetic sample and inspect every page before proposing layout changes.

