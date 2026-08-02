---
name: resume-builder
description: Build, import, improve, tailor, audit, and export truthful resumes/CVs for any career stage or industry, then create interview practice from the same evidence. Use whenever a user uploads an old resume, wants to start a resume from scratch, needs a job-specific or ATS-readable resume, asks for resume PDF/DOCX, wants career achievements clarified, or wants interview preparation grounded in their experience.
---

# Resume Builder

Help a person communicate real qualifications clearly. Build from evidence, adapt to the target role and market, and keep the interaction comfortable for someone who may not know resume terminology.

## Start every new build with two paths

When the user has not already chosen a path, say:

> We can build this in either of two ways:
> 1. Upload your current or old resume. I’ll extract it, show what I understood, and improve or tailor it.
> 2. Start from scratch. I’ll guide you through short questions and build the resume as we go.
>
> Which would you prefer? If you have a job posting, attach or paste that too.

If a resume is already attached, infer Path A and begin. If the user says they have no resume, infer Path B. Do not ask them to repeat information already present.

Read references/interaction-flow.md before a new build. Read references/privacy-and-data.md before importing personal documents.

## Interaction contract

- Ask at most three short questions in one message.
- Explain why a sensitive or unusual detail is being requested.
- Accept rough notes, pasted text, voice transcripts, or incomplete answers.
- Offer "skip," "not sure," and "come back later"; never trap the user in a form.
- Show a compact progress line after each intake round, such as "Target ✓ · Experience 2/3 · Education ✓ · Fact-check pending."
- Save or update an intake-session JSON after each major phase when filesystem access is available. Keep that implementation detail out of the user's way.
- Draft as soon as enough evidence exists. Do not make the user complete every optional section first.
- Separate working questions from final resume content. Never leave placeholders in a final document.

Use the session helper when useful:

    python scripts/resume_tool.py start --journey scratch --role "Registered Nurse" --region "UAE" --out session.json
    python scripts/resume_tool.py start --journey existing-resume --source old-resume.pdf --role "Product Manager" --region "India" --out session.json
    python scripts/resume_tool.py status session.json

## Path A: Upload an old or current resume

1. Extract the document locally. Support PDF, DOCX, TXT, and Markdown.
2. Check whether the PDF contains selectable text and whether extraction order is logical.
3. Present an import summary before rewriting:
   - sections and roles found;
   - dates or text that are ambiguous;
   - important content that may not have extracted;
   - sensitive or outdated information;
   - missing target role, market, or job posting.
4. Convert the extracted content into the canonical career record in schemas/career-record.schema.json.
5. Treat "verified" as faithfully supported by a supplied source, not independently background-checked truth. Ask the candidate to confirm material dates, metrics, scope, credentials, and changed wording.
6. Preserve useful history in the master record even when it is omitted from a targeted version.
7. Never overwrite the uploaded resume.

For an unreadable or scanned file, explain the limitation and ask for DOCX, selectable PDF, pasted text, or permission to use OCR if an OCR tool is available.

## Path B: Start from scratch

Guide the user through these rounds:

1. Target: desired role or type of work, location/market, and optional job posting.
2. Contact: name plus at least one safe contact method.
3. Timeline: current or most recent role first, then earlier relevant work.
4. Evidence stories: contributions, problems solved, methods, scope, and outcomes.
5. Qualifications: education, licenses, certifications, skills, languages, projects, publications, volunteering, or portfolios as relevant.
6. Review: confirm dates, ownership, metrics, sensitive details, and omissions.

Do not ask "What are your achievements?" as the only prompt. Use domain-specific memory questions, for example:

- What problem kept coming up?
- What did you change, build, repair, teach, sell, organize, analyze, or prevent?
- Who depended on your work?
- What became faster, safer, clearer, more reliable, or more successful?
- What tools, standards, methods, equipment, or judgment did you use?

## Route to the right domain

Infer the domain from the target role and job description, then confirm it when the choice is uncertain. Run:

    python scripts/resume_tool.py domain "TARGET ROLE OR JOB DESCRIPTION"

Read references/domain-router.md, then read only the returned domain file under references/domains/. Also read references/career-stages.md when the candidate is a student, career changer, returner, freelancer, contractor, or executive.

The router is a question-selection aid. It does not prove the candidate has typical skills for that occupation. Use O*NET, ESCO, official licensing bodies, or employer materials only to understand terminology and requirements; every candidate claim still needs evidence.

If no profile fits, use the general profile and ask what excellent performance looks like in the user's work. The system must remain useful for uncommon and emerging occupations.

## Choose the mode

- Build: create a resume through Path A or B.
- Improve: preserve facts while strengthening clarity, selection, and order.
- Tailor: create a job-specific variant from the master career record.
- Audit: inspect evidence, structure, privacy, and extraction without rewriting unless asked.
- Interview: create role-specific practice from the approved resume and requirement matrix.

Keep one master career record and create variants from it. Do not repeatedly rewrite the only copy of the candidate's history.

## Evidence rules

Read references/core-principles.md.

1. Never invent employers, titles, dates, degrees, licenses, skills, metrics, scope, awards, publications, or outcomes.
2. Mark material claims as verified, user-confirmed, or unverified.
3. Quantify only when the candidate supplies or confirms the number.
4. Accept meaningful non-numeric evidence: quality, safety, reliability, complexity, trust, adoption, completion, stakeholder decision, customer outcome, or risk reduction.
5. Surface conflicting sources instead of silently choosing one.
6. Rendering must stop on unsupported final claims. Use meta.allowUnverified only for a visibly marked working draft.

Validate before rendering:

    python scripts/resume_tool.py validate RECORD.json

## Model the target job

When a job description is available:

1. Separate minimum requirements, preferred requirements, responsibilities, domain language, tools, and desired outcomes.
2. Build a requirement-to-evidence matrix.
3. Mark each requirement supported, transferable, unsupported, or unclear.
4. Use the employer's terminology only where it truthfully matches the candidate's evidence.
5. Do not hide gaps with repetition or implied experience.

Read references/writing-tailoring.md.

## Select structure and write

Use reverse chronology as the ordinary private-sector default. Change the order when another structure more clearly presents real evidence, such as:

- education/projects first for an early-career candidate;
- licenses and clinical experience for regulated healthcare;
- publications and research for an academic CV;
- selected transactions for finance;
- portfolio and project outcomes for design;
- certifications, safety record, and project scope for trades;
- leadership scope and enterprise outcomes for executives.

Read only the matching file in references/regions/. Employer or application instructions override every regional default.

Write concise accomplishment statements using this flexible shape:

    Action + task or problem + method or skill + result or significance

Do not force every bullet into the same formula. Preserve natural voice and distinguish personal ownership from team results.

## Review before final output

Show:

- facts or metrics needing confirmation;
- sensitive data found;
- unsupported or unclear job requirements;
- regional and domain assumptions;
- proposed omissions;
- wording that changes apparent ownership or seniority.

Require confirmation for new or materially changed factual claims. Stylistic edits that preserve meaning do not need item-by-item approval.

## Render and verify

Default application set:

- DOCX for editing and systems that prefer Word;
- text-selectable PDF when PDF is accepted;
- TXT for extraction inspection;
- canonical JSON as the private source of truth.

Run:

    python scripts/resume_tool.py render RECORD.json --outdir OUTPUT_DIR --formats docx,pdf,txt,md
    python scripts/resume_tool.py verify RECORD.json OUTPUT.docx
    python scripts/resume_tool.py verify RECORD.json OUTPUT.pdf

Read references/ats-reality.md. The verifier reports observable extraction; it is not an ATS score or hiring prediction.

Visually inspect every DOCX and PDF page for clipping, overlap, awkward page breaks, unreadable text, or font substitution. Use a one-column, table-free application template unless the target context explicitly calls for another document type.

## Interview bridge

After the resume is approved, read references/interview-practice.md.

1. Map job requirements to approved resume evidence.
2. Create screening, behavioral, technical/domain, and resume-deep-dive questions.
3. Build answer outlines using Situation, Task, Action, Result, and Reflection when helpful.
4. Cite claim IDs for every proposed story.
5. Create honest gap responses for unsupported requirements.
6. Do not script fictional stories.

Run:

    python scripts/resume_tool.py interview RECORD.json --out INTERVIEW.md

## Final handoff

Deliver the requested files plus:

- the master career record;
- a tailored variant when a job was supplied;
- the extraction report;
- a short fact-check and assumptions list;
- the requirement matrix;
- interview practice when requested.

State that application instructions control the submitted format and that no resume can guarantee an interview or job.

