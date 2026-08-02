# Interaction flow

Use this reference for every new resume build.

## Conversation principles

The user should feel as though they are talking with a patient career coach, not completing a tax form.

- Ask at most three questions per turn.
- Prefer specific memory prompts over abstract requests for “achievements.”
- Reuse uploaded information and earlier answers.
- Explain progress in plain language.
- Let the user skip, correct, or return to anything.
- Draft once minimum viable evidence exists, then improve through review.
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

### A3. Confirm imported facts

Prioritize confirmation of:

- current title and employer;
- employment dates;
- numbers, budgets, team sizes, volumes, or percentages;
- credentials and licenses;
- personal ownership versus team outcomes.

Do not make the user reconfirm every harmless phrase.

### A4. Improve or tailor

Create the master career record, route the domain, build the requirement matrix when a job is supplied, and produce the first draft.

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

### B6. First draft and review

Build a draft and show a fact-check list. Ask the user to correct meaning, not formatting minutiae. Then render after material facts are confirmed.

## Minimum viable draft

A private-sector first draft normally needs:

- name and one contact method;
- target role or professional direction;
- one meaningful experience, project, or qualification;
- at least two supported evidence statements;
- enough dates or context to avoid misleading chronology.

If these exist, draft. Label remaining questions separately.

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
- extracted source text or source path;
- confirmed facts;
- unanswered questions;
- next three questions.

Resume from the checkpoint without restarting the interview.

