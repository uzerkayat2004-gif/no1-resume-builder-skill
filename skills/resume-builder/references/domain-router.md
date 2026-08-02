# Domain router

Use the router to choose better questions and section priorities. It is not a candidate-scoring system.

## Procedure

1. Combine the target title and job description.
2. Run:

       python scripts/resume_tool.py domain "combined role and job text"

3. If the first result is clearly aligned, use its profile.
4. If the top results are close or confidence is low, ask the user which description fits their work.
5. Read only the selected profile file in references/domains/.
6. Apply the relevant career-stage overlay from references/career-stages.md.
7. Let the posting, regulated requirements, and candidate evidence override profile defaults.

## What profiles control

- memory prompts;
- evidence types;
- common section priorities;
- domain-specific review risks;
- useful terminology sources.

## What profiles never control

- whether the candidate possesses a skill;
- whether a credential is valid;
- fabricated metrics;
- automatic keyword insertion;
- hiring likelihood;
- legal or licensing conclusions.

## Uncommon work

If no profile fits:

1. use the general profile;
2. ask what a strong performer in this work delivers;
3. ask what tools, standards, stakeholders, risks, and outcomes define the work;
4. construct a temporary profile in the session notes;
5. keep all candidate claims evidence-backed.

