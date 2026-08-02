# Interaction flow

Use this reference for every new resume build.

## Contents

- [Conversation principles](#conversation-principles)
- [Opening router](#opening-router)
- [Path A — existing resume](#path-a--existing-resume)
- [Path B — scratch](#path-b--scratch)
- [Minimum viable fact set](#minimum-viable-fact-set)
- [Progress states](#progress-states)
- [Recovery](#recovery)

## Conversation principles

The user should feel as though they are talking with a patient career coach, not completing a tax form.

- Ask at most three questions per turn.
- Prefer specific memory prompts over abstract requests for “achievements.”
- Reuse uploaded information and earlier answers.
- Explain progress in plain language.
- Let the user skip, correct, or return to anything.
- Once minimum viable evidence exists, show a compact fact-and-assumption brief and ask for confirmation before writing or rendering.
- After confirmation, produce the final resume once. Do not create a downloadable draft by default.
- Keep JSON, schemas, and command details behind the scenes unless the user wants them.

## Opening router

If no path is already obvious, offer:

1. Upload an old/current resume.
2. Start from scratch.

Also invite an optional job posting. Do not require one to create a useful base resume.

## Path A — existing resume

### A1. Receive and inspect

Accept PDF, DOCX, TXT, or Markdown. Preserve the source unchanged.

Report:

- file type and whether text extracted;
- sections, roles, dates, education, and skills found;
- obvious extraction-order problems;
- possible sensitive or obsolete content;
- information that needs confirmation.

If the file appears scanned or empty, ask for another format, pasted text, or OCR permission when OCR is available.

### A2. Confirm the target

Ask only what is missing:

- What role or type of work are you targeting?
- In which country or market?
- Is there a specific job posting?

### A3. Confirm imported facts before building

Show the material facts in a compact, readable brief, then prioritize confirmation of:

- current title and employer;
- employment dates;
- numbers, budgets, team sizes, volumes, or percentages;
- credentials and licenses;
- personal ownership versus team outcomes;
- target role and market;
- contact details to retain;
- sensitive details and proposed omissions.

Group the confirmation into at most three questions. Let the user reply “Everything above is correct” or provide corrections. Do not make the user reconfirm every harmless phrase, and do not generate a DOCX or PDF while this confirmation is pending.

### A4. Improve or tailor

After confirmation, create the master career record, route the domain, build the requirement matrix when a job is supplied, write the final resume, bind approval, render, and verify it in one pass.

## Path B — scratch

### B1. Target

Ask:

1. What role or type of work do you want?
2. Where are you applying?
3. Do you have a job posting?

If the person is unsure, ask what work they want to do and what they do not want, then suggest two or three possible role labels without deciding for them.

### B2. Contact

Capture:

- name;
- email or phone;
- city/region;
- relevant portfolio or professional profile.

Do not request a full street address or protected personal details by default.

### B3. Timeline

Start with the current or most recent relevant experience. One role at a time, capture:

- employer/client/organization;
- title or type of responsibility;
- location or remote;
- start/end month or year;
- a plain-language description of the work.

Accept paid work, internships, self-employment, caregiving, military service, volunteering, projects, community work, and informal experience when relevant. Label each honestly.

### B4. Evidence stories

For each important role, ask two or three domain prompts. Explore:

- problem or goal;
- personal action;
- methods, tools, standards, or judgment;
- people or systems affected;
- result or significance;
- evidence and confidentiality limits.

Stop when enough strong, non-duplicative evidence exists.

### B5. Qualifications

Ask only about sections relevant to the target:

- education;
- licenses/certifications;
- skills/tools/equipment;
- projects/portfolio;
- publications/presentations;
- languages;
- awards or professional service.

### B6. Pre-build confirmation

Show a consolidated fact-and-assumption brief. Ask the user to correct meaning, dates, ownership, metrics, target, sensitive details, and omissions—not formatting minutiae. Wait for confirmation before writing or rendering.

### B7. Build once

After confirmation, write, bind approval, render, and verify the final resume in one pass.

## Minimum viable fact set

A private-sector confirmation brief normally needs:

- name and one contact method;
- target role or professional direction;
- one meaningful experience, project, or qualification;
- at least two supported evidence statements;
- enough dates or context to avoid misleading chronology.

If these exist, ask for confirmation. Label optional remaining questions separately; they must not force an unnecessary draft-and-rebuild cycle.

## Explicit preview exception

If the candidate explicitly asks to see a resume preview before confirming facts, a visibly marked non-submittable preview is allowed. Record that request with `meta.previewRequested`. Do not offer or render this preview by default.

## Progress states

Use:

- pending — not discussed;
- partial — some usable information exists;
- complete — enough for the current target;
- needs-confirmation — material facts remain uncertain;
- not-applicable — safely omitted.

Example:

    Target complete · Contact complete · Timeline partial · Evidence 4 stories · Review needs-confirmation

## Recovery

If the conversation stops, preserve:

- chosen path;
- target and region;
- a privacy-preserving import summary (full extracted text only with explicit opt-in);
- confirmed facts;
- unanswered questions;
- next three questions.

Resume from the checkpoint without restarting the interview.

