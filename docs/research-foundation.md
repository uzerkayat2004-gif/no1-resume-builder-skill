# Research foundation

Last verified: 2026-08-02

This skill is based on authoritative career-service guidance, employer ATS support documentation, large-scale observational data, open occupational taxonomies, and lessons from established open-source resume tools. It does not train on or redistribute scraped personal resumes.

## The base

The best base is not a famous person's PDF. It is an evidence-backed career record that can produce a restrained, reverse-chronological, one-column application document.

The canonical record is JSON. It keeps facts, sources, job variants, and interview evidence separate from layout. JSON Resume demonstrates the value of an open, machine-readable resume schema. This project uses familiar portable section names plus an evidence ledger that blocks unsupported claims.

The normal delivery set is DOCX plus a text-selectable PDF, with TXT for extraction inspection. Greenhouse supports DOC, DOCX, PDF, RTF, and TXT uploads, while Lever documents support for Word and PDF parsing and advises applicants to check whether PDF text is selectable. Therefore the application instructions—not a global “PDF is best” claim—control the final file type.

## What the evidence supports

- Clear, standard structures improve the probability of clean parsing. Greenhouse lists columns, tables, headers/footers, text boxes, graphics, and contact information placed in headers/footers among common causes of parse failures.
- Tailoring matters more than keyword stuffing. Huntr reports that, in its 2025 platform data, tailored resumes converted to interviews/offers/hires at 5.8% versus 3.73% for untailored resumes. This is observational commercial-platform data, not proof that tailoring alone caused the difference.
- Page count is contextual. In Huntr's North-America- and tech-heavy sample, two-page resumes were common and had a slightly higher interview rate than one-page resumes, while three or more pages performed worse. The skill therefore treats one or two pages as normal private-sector outcomes rather than enforcing one page.
- Achievements should have clarity and depth. Huntr's interviewed resumes averaged slightly fewer but slightly longer achievement bullets than non-advancing resumes; its own report cautions that relevance and precision matter more than density.
- Spelling and grammar assistance can help. A field experiment summarized by MIT Sloan, involving nearly 500,000 job seekers, found algorithmic writing assistance associated with a 7.8% increase in hires. It supports quality editing, not factual invention.
- Skills-based evidence matters. NACE reported that almost two-thirds of surveyed employers use skills-based hiring to help identify candidates.

## What celebrity examples do not prove

The widely circulated one-page “Elon Musk resume” was produced by a resume company as a design exercise, not verified as Musk's real application resume. Bill Gates's public 1974 resume is a historical artifact with period-specific personal details and conventions. These examples have strong survivor and celebrity bias. They can illustrate specificity or career progression, but they should not define the base template, page count, or content rules for ordinary applicants.

Executive guidance is more useful when it comes from career services. Stanford Graduate School of Business describes a resume as a targeted marketing document rather than a biography and publishes separate executive resume examples. The design uses that principle without copying any person's document.

## Lessons from open-source builders

- JSON Resume: use an open, machine-readable record for interoperability.
- Reactive Resume: privacy and self-hosting are important; structured import/export and job-specific variants are valuable.
- OpenResume: a builder and parser should be paired so users can inspect extraction rather than trust a visual preview alone.
- RenderCV: content-as-data, strict validation, version control, multilingual output, and deterministic rendering are strong architectural patterns.

This project does not copy their code. THIRD_PARTY_NOTICES.md records the projects and licenses reviewed.

## Why not scrape “the whole internet”

Personal resumes often contain names, phone numbers, addresses, employment histories, and other personal data. Public availability does not remove privacy, copyright, consent, provenance, or bias concerns. A huge uncurated corpus would also amplify stale formatting advice, fabricated examples, geographic bias, and outcome-free templates.

The safer and more useful data strategy is:

1. use consented, de-identified, licensed, or synthetic resume fixtures;
2. use aggregate findings instead of redistributing individual documents;
3. use O*NET and ESCO for occupational vocabulary, never as proof the candidate has a skill;
4. evaluate with extraction tests, factuality checks, human review, and job-specific evidence coverage;
5. document sample composition and regional limits.

## Primary and high-value sources

- OpenAI Codex skills manual: https://developers.openai.com/codex/codex-manual.md
- Greenhouse supported formats: https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-formats-for-resumes-cover-letters-and-other-candidate-uploads
- Greenhouse parse failures: https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse
- Lever resume parsing: https://help.lever.co/hc/en-us/articles/20087345054749-Understanding-resume-parsing
- Harvard career services: https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/
- Stanford GSB resumes: https://www.gsb.stanford.edu/alumni/career-resources/job-search/resumes
- Yale impactful bullets: https://ocs.yale.edu/resources/writing-impactful-resume-bullets/
- Berkeley tailoring: https://www.career.berkeley.edu/prepare-for-success/resumes/
- USAJOBS federal resume requirements: https://help.usajobs.gov/faq/application/documents/resume/what-to-include
- OPM structured interviews: https://www.opm.gov/policy-data-oversight/assessment-and-selection/structured-interviews
- Europass CV: https://europass.europa.eu/en/create-europass-cv
- O*NET database: https://www.onetcenter.org/database.html
- ESCO API: https://esco.ec.europa.eu/en/use-esco/use-esco-services-api/esco-web-service-api
- Huntr 2025 report: https://api.huntr.co/research/2025-annual-job-search-trends-report
- MIT Sloan field experiment summary: https://mitsloan.mit.edu/ideas-made-to-matter/job-seekers-ai-boosted-resumes-more-likely-to-be-hired
- NACE skills-based hiring: https://www.naceweb.org/job-market/trends-and-predictions/almost-two-thirds-of-employers-use-skills-based-hiring-to-help-identify-job-candidates
- JSON Resume schema: https://jsonresume.org/schema
- Reactive Resume: https://github.com/AmruthPillai/Reactive-Resume
- OpenResume: https://github.com/xitanggg/open-resume
- RenderCV: https://github.com/rendercv/rendercv
- GDPR overview: https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/application-gdpr_en
- U.S. Copyright Office fair use FAQ: https://www.copyright.gov/help/faq/faq-fairuse.html
