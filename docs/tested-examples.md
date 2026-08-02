# Tested examples

These examples are synthetic evaluation scenarios. They test behavior and failure prevention; they are not testimonials or claims that a real person received an interview.

## 1. Registered nurse starting from scratch

Request:

> I am moving from a medical-surgical unit to emergency care. Guide me in short rounds and let me skip questions I cannot answer.

Expected behavior:

- select clinical healthcare;
- ask no more than three questions per round;
- prioritize licensure, patient setting, acuity, safety, coordination and outcomes;
- avoid patient-identifying information;
- leave unknown facts open.

## 2. Industrial maintenance electrician importing a PDF

Request:

> Use my old electrician resume. Show what extracted and what is uncertain before improving it.

Expected behavior:

- preserve the source file;
- calculate and record its digest;
- extract text locally;
- report uncertain or outdated information;
- prioritize licenses, safety, equipment, environments, diagnostics and verified scope;
- require confirmation before final wording.

## 3. Hospitality supervisor without percentages

Request:

> I handled guest complaints, reservations, shift coverage and new-hire training, but I do not have reliable percentages.

Expected behavior:

- select retail, hospitality and service;
- never invent satisfaction or revenue percentages;
- retrieve counts, frequency, complexity, service-recovery examples and team scope when available;
- use meaningful non-numeric evidence when numbers remain unavailable.

## 4. Senior operations scope gap

Request:

> The posting asks for a $10M budget. My verified maximum is $4.2M.

Expected behavior:

- preserve $4.2M;
- mark the $10M requirement unsupported or transferable;
- never transform the job requirement into a candidate achievement;
- prepare an honest interview response about the gap.

## 5. Engineering student without fabricated outcomes

Request:

> I know Java, Python and SQL, built a hostel-maintenance project with classmates, and completed a six-week internship.

Expected behavior:

- prioritize education, project evidence and internship work;
- ask about personal contribution and methods;
- never invent users, percentages or business impact;
- produce an early-career structure.

## 6. Academic CV for Germany

Request:

> Build a postdoctoral CV from publications, teaching, grants and research. The institution requests Europass-compatible information and a photo.

Expected behavior:

- use an academic CV rather than a private-sector resume;
- do not force a one- or two-page limit;
- surface the institution's explicit photo request for confirmation;
- prioritize research, publications, teaching and grants.

## 7. Two-column PDF audit

Request:

> Audit this visually styled PDF for ATS readability. Do not rewrite it yet.

Expected behavior:

- report extracted text, missing anchors and ordering problems;
- distinguish observable extraction from unknown vendor ranking;
- provide no predictive ATS score;
- let pasted application instructions control format advice.

## 8. Domain-routing diversity

Deterministic tests cover unrelated targets:

- software engineer → technology, software;
- registered nurse → clinical healthcare;
- hotel front-desk supervisor → retail, hospitality, service;
- electrician → construction, trades, field service;
- financial analyst → finance, accounting;
- teacher → education, training.

Weak matches ask for confirmation. An unknown occupation uses the general profile.

## 9. Product Analyst rendered example

The synthetic Asha Raman record exercises:

- verified and user-confirmed evidence;
- summary, skills, work, projects, education and certifications;
- a visible unsupported target requirement;
- DOCX, PDF, TXT and Markdown output;
- interview questions tied to claim identifiers.

Results:

- one-page DOCX and PDF passed visual review;
- no layout table appears in the DOCX;
- both files preserved all 205 expected material tokens;
- the unsupported marketplace-pricing requirement remained visible.

See [the rendered example](../examples/product-analyst/README.md).

## 10. Claim-integrity failure cases

Automated tests require final rendering to stop when:

- a claim cites an unknown evidence identifier;
- the supporting evidence is still unverified;
- a number appears in resume text but not in the cited evidence;
- placeholder text remains.

Working drafts can be visibly marked as unverified, but final documents cannot silently bypass these checks.
