# Sources and design decisions

Last reviewed: 2026-08-02

This document explains what was researched, what each source supports, what was implemented, and where the evidence has limits. It is not a claim that any source endorses this project.

## Contents

1. [Research method](#research-method)
2. [Employer systems](#employer-systems)
3. [Career services](#career-services)
4. [Government and regional guidance](#government-and-regional-guidance)
5. [Occupational taxonomies](#occupational-taxonomies)
6. [Research and aggregate reports](#research-and-aggregate-reports)
7. [Open-source implementation references](#open-source-implementation-references)
8. [Celebrity examples](#celebrity-examples)
9. [Social-media advice supplied during design](#social-media-advice-supplied-during-design)
10. [What the evidence does not prove](#what-the-evidence-does-not-prove)

## Research method

The project prioritizes sources in this order:

1. application instructions and official employer-system documentation;
2. government and institutional requirements;
3. university career-service guidance;
4. occupational taxonomies and regulated-role terminology;
5. peer-reviewed or clearly described research;
6. aggregate commercial-platform data with stated sampling limits;
7. open-source architecture and implementation patterns;
8. social-media or celebrity examples only as hypotheses to verify.

Sources were compared rather than merged blindly. Conflicting advice became a contextual rule instead of a universal rule.

## Employer systems

### Greenhouse: supported candidate uploads

Source: https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-formats-for-resumes-cover-letters-and-other-candidate-uploads

Observed guidance: Greenhouse accepts DOC, DOCX, PDF, RTF and TXT candidate documents.

Implementation:

- produce editable DOCX and text-selectable PDF;
- preserve TXT for extraction inspection;
- let the employer's instructions control the submitted format.

### Greenhouse: unsuccessful parsing

Source: https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse

Short source language: “Complex resumes with tables, headers, and footers.”

Observed causes also include graphics, photos, image-only files, text boxes, columns, unclear sectioning, and contact details placed in headers or footers.

Implementation:

- ordinary application resumes use one column and no layout tables;
- contact information stays in the document body;
- the renderer creates selectable text;
- the verifier reports extracted text, anchor preservation and token recall;
- the report explicitly says it is not an ATS score.

### Lever: parsing guidance

Source: https://help.lever.co/hc/en-us/articles/20087345054749-Understanding-resume-parsing

Implementation:

- accept Word and PDF sources;
- inspect whether PDF text is selectable;
- report extraction limitations before rewriting.

## Career services

### Harvard

Source: https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/

Short source language: “Specific rather than general,” “Active rather than passive,” and “Fact-based.”

Implementation:

- default to specific, active and evidence-grounded writing;
- tailor content to the target role;
- preserve readability and consistent formatting;
- use reverse chronology as an ordinary private-sector default, not a universal mandate.

Harvard also cautions that generative AI should help edit authentic material rather than become the generic primary author. The skill therefore starts with the candidate's evidence.

### Yale

Source: https://ocs.yale.edu/resources/writing-impactful-resume-bullets/

Short source language: “Action + Project + Result.”

Implementation:

- ask what the person did, what problem or project was involved, how they did it, and what changed;
- distinguish personal contribution from team outcomes;
- quantify when possible, never when unsupported.

The skill uses a flexible pattern rather than forcing every bullet into an identical formula.

### Berkeley

Source: https://www.career.berkeley.edu/prepare-for-success/resumes/

Implementation:

- emphasize relevance, tailoring and readable organization;
- allow students and early-career candidates to lead with education, projects or experience according to their strongest evidence.

### Stanford Graduate School of Business

Source: https://www.gsb.stanford.edu/alumni/career-resources/job-search/resumes

Implementation:

- treat an executive resume as a targeted leadership document, not a compressed biography;
- prioritize leadership scope, enterprise outcomes, transformation and governance where supported.

## Government and regional guidance

### USAJOBS

Source: https://help.usajobs.gov/faq/application/documents/resume/what-to-include

Observed guidance: applicants must address the announcement, use plain language, and provide required work details. Current guidance limits federal resumes to two pages and may require month/year dates, hours per week, series and grade, or supporting documents.

Implementation:

- a dedicated US-federal reference overrides private-sector defaults;
- the announcement's qualifications and required documents become explicit requirements;
- classified, sensitive and unnecessary personal information is excluded.

### Europass

Source: https://europass.europa.eu/en/create-europass-cv

Short source language: “Focus on facts and main points.”

Observed guidance: maintain a reusable profile, create multiple CVs, tailor to the vacancy, use clear language and reverse chronology.

Implementation:

- maintain a reusable master career record;
- generate target-specific variants;
- use the Europe or academic profile when the institution requests Europass-compatible information.

### Regional files

The runtime skill contains guidance for:

- neutral/default contexts;
- India;
- UK and Ireland;
- Europe;
- US and Canada;
- US federal applications;
- academic CVs.

Application instructions always override a regional default.

## Occupational taxonomies

### O*NET

Source: https://www.onetcenter.org/database.html

O*NET supplies structured occupation, task, work-activity, skill, knowledge, ability, education and tool data for the US economy.

### ESCO

Source: https://esco.ec.europa.eu/en/use-esco/use-esco-services-api/esco-web-service-api

ESCO supplies versioned European occupation, skill, competence and qualification concepts.

Implementation:

- 26 transparent domain routes select relevant evidence questions;
- profiles cover evidence priorities, useful sections and domain cautions;
- the router returns matches, confidence and alternatives;
- uncertain matches require confirmation;
- a general profile handles uncommon and emerging occupations.

Boundary: taxonomy data describes occupations. It never proves that a candidate possesses a skill, license, qualification or authorization.

## Research and aggregate reports

### Algorithmic writing assistance field experiment

Sources:

- https://mitsloan.mit.edu/ideas-made-to-matter/job-seekers-ai-boosted-resumes-more-likely-to-be-hired
- https://arxiv.org/abs/2301.08083

The reported experiment covered 480,948 job seekers on an online labor market. Writing assistance improved spelling, grammar, punctuation, usage and style; the assisted group received 7.8% more job offers.

Implementation:

- use AI for clarity, editing and evidence retrieval;
- block invented qualifications and outcomes;
- keep employer satisfaction and hiring predictions outside the skill's claims.

### Huntr 2025 report

Source: https://api.huntr.co/research/2025-annual-job-search-trends-report

The report analyzes platform data including approximately 1.7 million applications and 243,973 resumes. It reports stronger conversion for tailored resumes and emphasizes relevance over excess.

Limit: the report describes a North American- and technology-heavy platform sample and says findings are indicative rather than definitive.

Implementation:

- support a stable base record and job-specific variants;
- avoid keyword stuffing and arbitrary density targets;
- do not enforce a universal one-page rule.

### Skills-based hiring

Source: https://www.naceweb.org/job-market/trends-and-predictions/almost-two-thirds-of-employers-use-skills-based-hiring-to-help-identify-job-candidates

Implementation:

- express capabilities through concrete evidence rather than titles alone;
- include projects, volunteering, placements, training and transferable evidence when relevant.

## Open-source implementation references

No source code from these projects is copied.

### JSON Resume

Source: https://github.com/jsonresume/resume-schema

Lesson: structured career information enables validation, portability and multiple renderers.

Implementation: canonical JSON career record plus a stricter claim-evidence extension.

### Reactive Resume

Source: https://github.com/AmruthPillai/Reactive-Resume

Lesson: privacy, self-hosting, ownership, structured import/export and multiple formats matter.

Implementation: local-first helpers, no uploads, and reusable structured data.

### OpenResume

Source: https://github.com/xitanggg/open-resume

Lesson: a builder and parser should work together so users can inspect imported content.

Implementation: existing-resume path, extraction report and confirmation before rewriting.

### RenderCV

Source: https://github.com/rendercv/rendercv

Lesson: content-as-data, schema validation, deterministic rendering and version control are durable patterns.

Implementation: validated JSON input and reproducible DOCX/PDF/TXT/Markdown output.

## Celebrity examples

Examples attributed to famous executives were reviewed as design artifacts, not outcome evidence.

The widely circulated Elon Musk one-page resume is presented by a commercial resume company as a famous-person resume example. It is not treated as Musk's verified job application. Bill Gates's historical resume reflects its period and a highly unusual career trajectory.

Implementation:

- do not use celebrity status, survivor bias or promotional examples to set a universal page count;
- retain the useful principle of making scope and progression concrete;
- use institutional executive guidance for executive-specific structure.

## Social-media advice supplied during design

The supplied post recommended professional fonts, simple headings, relevant keywords, one column, clear contact information, action verbs, metrics, relevant skills, spelling review and job-specific customization.

Accepted:

- readable professional typography;
- standard headings and simple structure;
- truthful use of job-description language;
- relevant skills and experience;
- clear contact information;
- action-oriented accomplishment writing;
- spelling and grammar review;
- customization for each application;
- removal of unnecessary sensitive personal information.

Corrected or contextualized:

- PDF is not always the correct submission format;
- one page is not a universal requirement;
- metrics are used only when known and verified;
- photographs and personal details depend on the market and explicit instructions;
- an ATS simulator cannot reliably predict every employer system;
- keywords cannot be added when the candidate lacks supporting evidence.

## What the evidence does not prove

The sources do not prove that:

- one template works for every employer;
- one page is always superior;
- a file will receive a particular ATS ranking;
- keywords cause interviews by themselves;
- a recruiter will read sections in one fixed order;
- a resume alone caused a hire;
- this repository can guarantee an interview or job.

The controlling evidence remains the candidate's verified history, the target job, the job market, and the application instructions.
