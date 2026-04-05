---
name: spec-driven-development
description: "Specification-Driven Development (SDD) workflow — takes any vague requirement or feature idea and transforms it into structured, implementation-ready specs. Use when the user says 'spec this', 'create requirements', 'write a spec', 'plan this feature', 'SDD', 'spec driven', 'specification', 'requirements doc', 'design doc', 'task list', 'break this down', 'plan this', 'refine this idea', 'turn this into tasks', or when they describe a feature they want to build. Also use when working with .kiro/specs directories or any specification workflow. Even if the user just says 'I want to build X' — use this skill to capture and structure their intent before coding."
---

# Spec-Driven Development (SDD)

Specifications are the source of truth. Code serves specifications — not the other way around.

This skill transforms vague ideas into structured, implementation-ready specification documents. It produces three artifacts in every run:

1. **requirements.md** — What to build (user stories + acceptance criteria)
2. **design.md** — How to build it (architecture + interfaces + data model)
3. **tasks.md** — What to do first (ordered, dependency-aware implementation checklist)

**CRITICAL: All specs MUST be written to actual files on disk — never just printed as chat output.** Create the directory `.kiro/specs/<feature-name>/` and write each artifact as a real file inside it. The user should be able to open and read these files in their editor after generation. If you only output specs as text in the conversation without creating files, you have failed the task.

---

## Workflow Overview

```
Idea → Interview → Requirements → Design → Tasks
         ▲                                    │
         └──── Refinement loop ◄──────────────┘
```

There are five phases. Execute them in order. Never skip Phase 1.

---

## Phase 1: Capture & Refine (Interview)

When the user provides a feature idea, do NOT immediately generate specs. First, understand what they actually need.

Ask 3–5 focused clarifying questions covering:

- **Scope**: What is in and what is out?
- **Users**: Who are the primary users / personas?
- **Tech context**: What's the existing stack? Any constraints?
- **Edge cases**: What happens when things go wrong?
- **Priority**: What's the MVP vs nice-to-have?

Mark anything still unclear with `[NEEDS CLARIFICATION: specific question]` — never guess.

Keep the interview conversational and concise. Don't interrogate — synthesize what you can from context and only ask what you truly need answered.

If the user says "just do it" or "skip questions", generate specs with `[NEEDS CLARIFICATION]` markers for ambiguities instead of blocking.

---

## Phase 2: Generate Requirements (`requirements.md`)

Read `references/writing-guide.md` for the full template and examples.

Structure:

```markdown
# Requirements Document

## Introduction
Brief description of what is being built and why.

## Glossary
- **Term**: Definition relevant to this spec.

## Requirements

### Requirement 1: Title
**User Story:** As a [role], I want [feature], so that [benefit].

#### Acceptance Criteria
1. WHEN [condition], THE [component] SHALL [behavior].
2. IF [condition], THEN THE [component] SHALL [behavior].

---
```

Rules:
- Every requirement MUST have a user story and numbered acceptance criteria
- Use SHALL for mandatory behavior, SHOULD for recommended, MAY for optional
- Every criterion must be testable — if you can't write a test for it, rewrite it
- Number requirements sequentially across the entire document
- Add `---` separator after each requirement
- Include both functional and non-functional requirements
- Group related requirements logically

Good acceptance criterion:
> WHEN the user submits a login form with valid credentials, THE auth service SHALL return a JWT access token with a 15-minute expiry and an HTTP-only refresh token cookie with a 7-day expiry.

Bad acceptance criterion:
> The login should work properly and be secure.

---

## Phase 3: Generate Design (`design.md`)

Read `references/writing-guide.md` for the full template.

Structure:

```markdown
# Design Document: [Feature Name]

## Overview
What this system does in 2-3 sentences.

## Architecture
High-level structure with ASCII diagrams.

## Components and Interfaces
Each component's responsibilities, interfaces, key behaviors.

## Data Model
Tables, relationships, indexes (if applicable).

## API Contracts
Endpoints, methods, request/response shapes (if applicable).

## Security Considerations

## Deployment & Infrastructure
```

Rules:
- Every architectural decision MUST reference a requirement number (e.g., "Per Req 3, ...")
- Use ASCII art for diagrams — they work everywhere
- List component responsibilities as bullet points
- Define TypeScript interfaces for all data shapes
- Include error states and edge cases in API contracts

---

## Phase 4: Generate Tasks (`tasks.md`)

Structure:

```markdown
# Implementation Tasks

## Task List

- [ ] 1. Top-level task
  - [ ] 1.1 Concrete subtask with enough detail to implement
  - [ ] 1.2 Another subtask

- [ ] 2. Next top-level task
  - [ ] 2.1 Subtask
```

Rules:
- Order tasks by dependency — things that must exist first come first
- Mark parallelizable tasks with `[P]` at the start of the description
- Each subtask must be concrete enough to implement without referring back to other docs
- Include test tasks alongside their implementation tasks (not in a separate section)
- Group by component or implementation phase
- Reference requirement numbers where helpful (e.g., "Implement X (Req 5)")

---

## Phase 5: Generate Config (`.config.kiro`)

Create a JSON metadata file:

```json
{"specId": "<generated-uuid>", "workflowType": "requirements-first", "specType": "feature"}
```

Generate the UUID using `crypto.randomUUID()` or equivalent.

---

## Output Directory — MANDATORY File Creation

**You MUST create real files on disk. Do NOT just output spec content as chat text.**

Follow this exact procedure for every SDD run:

1. Derive `<feature-name>` as a kebab-case slug from the feature description (e.g., "user notifications" → `user-notifications`)
2. Create the directory: `mkdir -p .kiro/specs/<feature-name>/`
3. Write each artifact as a file using the file creation tool:
   - `.kiro/specs/<feature-name>/.config.kiro`
   - `.kiro/specs/<feature-name>/requirements.md`
   - `.kiro/specs/<feature-name>/design.md`
   - `.kiro/specs/<feature-name>/tasks.md`
4. After creating files, confirm to the user with the full path to the spec directory

```
.kiro/specs/<feature-name>/
├── .config.kiro        ← metadata (UUID, workflow type)
├── requirements.md     ← user stories + acceptance criteria
├── design.md           ← architecture + components + data model
└── tasks.md            ← ordered implementation checklist
```

- If the project already has `.kiro/specs/`, use it; otherwise create it
- If a spec with the same name exists, ask before overwriting
- For partial workflows (only one artifact requested), still create the directory and write the file(s) to disk

---

## Partial Workflows

The user may request only one artifact:

| User says | Action |
|---|---|
| `spec this: [desc]` or `sdd [desc]` | Full workflow (all phases) |
| `generate requirements for [desc]` | Phase 1 → Phase 2 only |
| `generate design for [desc]` | Phase 1 → Phase 3 only (read existing requirements.md if available) |
| `generate tasks for [desc]` | Phase 1 → Phase 4 only (read existing design.md if available) |
| `refine spec [path]` | Read existing spec, identify gaps, improve it |
| `review spec [path]` | Audit spec for completeness without modifying |

---

## Refinement & Review

When reviewing or refining existing specs, check for:

- [ ] No `[NEEDS CLARIFICATION]` markers remain
- [ ] All requirements have acceptance criteria in SHALL/WHEN/IF form
- [ ] All acceptance criteria are testable
- [ ] Glossary covers all domain-specific terms
- [ ] Design references requirement numbers
- [ ] Tasks are ordered by dependency
- [ ] No speculative "might need" features
- [ ] Non-functional requirements are included (performance, security, scalability)
- [ ] Error handling / edge cases are covered

Report findings as a numbered list with severity (Critical / Warning / Info).

---

## Key Principles

1. **Specs first, code second** — never generate code from a vague idea. Capture intent in specs first.
2. **No guessing** — mark ambiguities with `[NEEDS CLARIFICATION]` rather than assuming.
3. **Testable criteria** — if you can't write a test for a requirement, it's not specific enough.
4. **Traceability** — every design decision links to a requirement, every task links to a design component.
5. **Generic** — this workflow works for ANY project, any language, any stack. Don't assume.
6. **Incremental** — specs can be generated incrementally. Start with requirements, add design later, add tasks last.
7. **Living documents** — specs evolve. When requirements change, update design and tasks to match.

---

## References

For detailed templates, examples, and writing guidelines, read:
- `references/writing-guide.md` — exact file templates, good/bad examples, formatting rules
- `references/methodology.md` — SDD philosophy and quality checklists
- `references/prompting-guide.md` — how to prompt for the best spec output (templates, power tips, what to avoid)
