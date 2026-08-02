# User journey

This document defines how a person experiences Resume Builder. JSON and tooling remain behind the scenes unless the person asks for technical detail.

## Entry

The assistant determines whether the user already chose a path.

| Situation | Behavior |
|---|---|
| Resume attached | Begin Existing Resume path |
| User says they have no resume | Begin Scratch path |
| Neither is clear | Offer the two choices |
| Job posting attached | Capture it without asking again |
| Only asks for an audit | Audit; do not start a full build |

## Existing Resume path

### Step 1 — Import

The assistant:

- preserves the original;
- extracts PDF, DOCX, TXT, or Markdown locally;
- checks for empty/scanned text and extraction order;
- creates a resumable intake checkpoint.

### Step 2 — Understanding report

Before rewriting, the user sees:

- roles and dates found;
- education, skills, projects, and credentials found;
- unreadable or ambiguous content;
- sensitive or outdated details;
- the next confirmation questions.

This prevents a polished rewrite from silently preserving parsing mistakes.

### Step 3 — Confirm

The assistant prioritizes material facts:

- current role;
- dates;
- numbers;
- credentials;
- personal versus team ownership.

### Step 4 — Target

The user can build a reusable base resume or paste a specific job. When a job is supplied, the assistant maps requirements to supported, transferable, unsupported, or unclear evidence.

### Step 5 — Build and render once

After the user confirms the compact fact-and-assumption brief, the assistant writes, approves, renders, and verifies the final resume in one pass. It does not generate a labeled DOCX/PDF draft first unless the user explicitly requests a preview.

## Scratch path

### Round 1 — Target

Ask role/type of work, market, and optional job posting.

### Round 2 — Contact

Ask name and one safe contact method. City/region and professional links are optional or context-dependent.

### Round 3 — Timeline

Collect one role, project, or responsibility at a time, beginning with the most recent or most relevant.

### Round 4 — Evidence stories

Use the selected domain's prompts. Ask about the problem, personal action, method, scope, and result. Accept important non-numeric evidence.

### Round 5 — Qualifications

Ask only for relevant education, licenses, certifications, tools, projects, languages, publications, or portfolio evidence.

### Round 6 — Pre-build fact-check

When minimum viable evidence exists, show the consolidated facts, target assumptions, sensitive details, and proposed omissions. Ask for confirmation before writing or rendering.

### Round 7 — Build and render

After confirmation, write, approve, render, and verify the final resume once. Optional information can be added later without forcing a preliminary document build.

## Question-batch design

Every interaction batch:

1. acknowledges what was learned;
2. shows a compact progress line;
3. asks at most three questions;
4. allows skip/not sure;
5. tells the user what happens next.

Bad:

> Fill out your entire employment history, all education, all certifications, every tool, achievements with metrics, references, and hobbies.

Better:

> Great—I have your target and location. Let’s capture your most recent work:
> 1. What organization or client was it?
> 2. What was your role?
> 3. Roughly when did you start and finish?
>
> You can answer approximately or say “skip” to any item.

## Minimum viable fact set

Ask for pre-build confirmation when the assistant has:

- name and one safe contact;
- target direction;
- one meaningful experience, project, or qualification;
- two supported evidence statements;
- enough chronology to avoid misleading the reader.

## Session recovery

A session checkpoint records:

- selected journey;
- target, region, and domain;
- source path and extracted text when applicable;
- confirmed and unconfirmed answers;
- progress states;
- next three questions.

The checkpoint may contain personal information. It is private working data and must not be committed to the repository.

## Completion

A build is complete when:

- material claims are source-backed or user-confirmed;
- unsupported target requirements are visible;
- regional and domain choices are reviewed;
- requested formats render;
- DOCX/PDF extraction preserves material content;
- final pages pass visual inspection;
- the user receives the fact-check list and any interview kit requested.

