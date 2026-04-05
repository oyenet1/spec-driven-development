# Specification-Driven Development — Methodology

## What is SDD?

Specification-Driven Development inverts the traditional relationship between specs and code. Instead of writing specs to guide coding, you write specs that **drive** implementation. The specification is the source of truth. Code is its expression in a particular language.

In traditional development:
```
Idea → Code → (maybe) Documentation
```

In SDD:
```
Idea → Specification → Design → Tasks → Code
```

Specifications don't serve code — code serves specifications. Maintaining software means evolving specifications. Debugging means fixing specifications that generate incorrect code.

---

## Why SDD?

1. **Eliminates the spec-code gap** — when specs generate code, there's no drift between intent and implementation.
2. **Enables rapid pivots** — change a requirement, regenerate affected design and tasks. Minutes, not days.
3. **Forces clarity** — writing testable acceptance criteria exposes ambiguity early, before it becomes a bug.
4. **Creates traceability** — every design decision links to a requirement, every task links to a component. Nothing exists without justification.
5. **Supports AI-assisted development** — well-structured specs are the best possible context for AI code generation.

---

## The Five Phases

### Phase 1: Interview & Capture

Transform the user's vague idea into a clear problem statement. Ask:

- What problem does this solve?
- Who are the users? What are their goals?
- What's the existing context (tech stack, constraints, team)?
- What's explicitly out of scope?
- What does "done" look like?

Mark unknowns with `[NEEDS CLARIFICATION]` — never assume.

### Phase 2: Requirements

Translate the captured intent into formal, testable requirements using:

- **User stories**: As a [role], I want [feature], so that [benefit]
- **Acceptance criteria**: WHEN/SHALL/IF/THEN language
- **Glossary**: Define every domain term
- **Non-functional requirements**: Performance, security, scalability, observability

Every requirement must pass the testability check: "Can I write an automated test that verifies this criterion passes or fails?"

### Phase 3: Design

Transform requirements into architecture:

- Map each requirement to one or more components
- Define component interfaces and responsibilities
- Design data models (tables, relationships, indexes)
- Specify API contracts (endpoints, payloads, error shapes)
- Document security measures and deployment needs
- Use ASCII diagrams for visual clarity

Every design decision MUST reference a requirement number. If a decision doesn't trace to a requirement, either the requirement is missing or the decision is unnecessary.

### Phase 4: Tasks

Break the design into an ordered implementation checklist:

- Order by dependency (what must exist first)
- Make each task concrete enough to implement without ambiguity
- Include testing tasks inline (not as a separate phase)
- Mark parallelizable tasks with `[P]`
- Reference requirement numbers for traceability

### Phase 5: Config & Metadata

Generate the `.config.kiro` file with a unique spec ID, workflow type, and spec type. This enables tooling to track and manage specs.

---

## Quality Checklist

Run this checklist before delivering any spec:

### Requirements Quality
- [ ] Every requirement has a user story
- [ ] Every acceptance criterion uses SHALL/WHEN/IF language
- [ ] Every criterion is testable (you can describe the test)
- [ ] No `[NEEDS CLARIFICATION]` markers remain (or user accepted them)
- [ ] Glossary covers all domain-specific terms
- [ ] Non-functional requirements are included
- [ ] No speculative "might need" features

### Design Quality
- [ ] Every design decision references a requirement number
- [ ] Architecture diagram exists and is readable
- [ ] All component interfaces are defined
- [ ] Data model includes indexes on queried columns
- [ ] API contracts include error responses
- [ ] Security considerations are documented

### Tasks Quality
- [ ] Tasks are ordered by dependency
- [ ] Each subtask is concrete enough to implement directly
- [ ] Testing tasks are included alongside implementation
- [ ] Parallelizable tasks are marked with `[P]`
- [ ] No task exists without a corresponding design component

---

## Refinement Loop

Specs are living documents. After initial generation:

1. **User reviews** — the user reads and provides feedback
2. **Identify gaps** — find missing requirements, unclear criteria, orphan tasks
3. **Update incrementally** — modify specific sections, don't regenerate from scratch
4. **Maintain traceability** — when requirements change, update design and tasks to match

The loop continues until the user is satisfied that the specs fully capture their intent.

---

## When to Use SDD

Use SDD for:
- New features or products (any size)
- Major refactors that change behavior
- Complex integrations with multiple moving parts
- Any work where "what exactly should this do?" isn't immediately obvious

Skip SDD for:
- One-line bug fixes with obvious cause and solution
- Pure dependency updates with no behavior change
- Cosmetic/formatting changes
