# ATS and parsing reality

Last verified: 2026-08-01

## What can be known

Applicant tracking systems differ by vendor, customer configuration, workflow, and parser version. A general-purpose skill cannot predict a company's ranking rules or guarantee that a resume will pass.

It can test observable properties:

- whether text is selectable and extractable;
- whether extraction order is logical;
- whether standard section labels survive;
- whether names, employers, titles, dates, and bullets are present;
- whether the document follows the employer's accepted file types;
- whether layout features known to cause parsing problems are absent.

Call this an extraction or compatibility report, not an ATS score.

## Safe default layout

For an ordinary private-sector application:

- one column;
- no layout tables;
- no text boxes;
- no images, charts, skill bars, logos, or icon-only contact links;
- no material information in headers or footers;
- standard section names;
- ordinary Unicode text and real bullet paragraphs;
- 10–12 pt professional type;
- approximately 0.65–1.0 inch margins;
- black text on white;
- consistent month/year dates;
- selectable text, not a scanned image.

This is a conservative interoperability profile, not a law of hiring.

## File type decision

1. Follow the job posting or application form.
2. If it names DOCX, submit DOCX.
3. If it names PDF and the generated PDF is selectable, submit PDF.
4. If it accepts both and no preference is stated, provide a text-selectable PDF for stable appearance and keep DOCX ready as a fallback.
5. If the application system visibly misparses one format, use another accepted format and manually correct populated fields when possible.

Greenhouse lists DOC, DOCX, PDF, RTF, and TXT among supported candidate uploads. Lever documents Word and PDF parsing and suggests checking whether PDF text can be selected. These examples show why “always PDF” is too strong.

## Common parse risks

Greenhouse identifies these common causes of unsuccessful parsing:

- columns;
- tables;
- headers and footers;
- text boxes;
- graphics or images;
- contact information inside headers or footers;
- image-only scans;
- unusually large files or files outside supported types.

Do not claim every parser fails on every one of these features. Use them as risk factors.

## Keywords

Use the exact language of the job posting where:

- it describes evidence the candidate genuinely has;
- it is the conventional name for the skill or responsibility;
- it improves clarity for both parser and reader.

Do not:

- paste invisible keywords;
- repeat keywords unnaturally;
- claim tools merely because the role normally uses them;
- add a skills list that is contradicted by the experience section.

## Verification report

The bundled verifier measures:

- extracted character count;
- token recall against the canonical record;
- presence of expected anchors;
- page count for PDF.

It does not evaluate recruiter preference, semantic job fit, visual polish, truthfulness outside the evidence ledger, or proprietary ATS ranking.

## Sources

- Greenhouse supported formats: https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-formats-for-resumes-cover-letters-and-other-candidate-uploads
- Greenhouse parsing failures: https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse
- Lever parsing: https://help.lever.co/hc/en-us/articles/20087345054749-Understanding-resume-parsing
- Indeed ATS template guidance: https://www.indeed.com/career-advice/resumes-cover-letters/ats-resume-template

