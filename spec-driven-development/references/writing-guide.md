# SDD Writing Guide

Detailed templates, examples, and formatting rules for each output file.

---

## Requirements Template

```markdown
# Requirements Document

## Introduction

[2-4 sentences describing what is being built and the problem it solves. Keep it high-level — details go in the requirements themselves.]

---

## Glossary

- **Term_One**: Definition of the first domain term used in this document.
- **Term_Two**: Definition of the second domain term.
[Add every domain-specific or potentially ambiguous term. If in doubt, define it.]

---

## Requirements

### Requirement 1: [Short Descriptive Title]

**User Story:** As a [role], I want [capability/feature], so that [benefit/value].

#### Acceptance Criteria

1. WHEN [trigger/condition], THE [component/system] SHALL [observable behavior].
2. IF [condition], THEN THE [component] SHALL [behavior].
3. WHEN [action], THE [component] SHALL NOT [prohibited behavior].
4. FOR ALL [inputs/entities], [property] SHALL hold.

---

### Requirement 2: [Title]

**User Story:** As a [role], I want [capability], so that [benefit].

#### Acceptance Criteria

1. ...

---
```

### Acceptance Criteria Language

Use these keywords with precise meaning (RFC 2119):

| Keyword | Meaning |
|---|---|
| **SHALL** | Absolute requirement — must be implemented |
| **SHALL NOT** | Absolute prohibition — must never happen |
| **SHOULD** | Recommended — implement unless there's a documented reason not to |
| **SHOULD NOT** | Discouraged — avoid unless there's a documented reason |
| **MAY** | Optional — implement at discretion |

### Good vs Bad Criteria

**Good — specific, testable, unambiguous:**

> WHEN the user submits a registration form with a password shorter than 8 characters, THE API SHALL return HTTP 422 with an errors object containing `{ password: "Password must be at least 8 characters" }`.

> WHEN the system receives more than 100 requests per minute from a single IP on the `/auth/login` endpoint, THE rate limiter SHALL return HTTP 429 with a `Retry-After` header indicating seconds until the limit resets.

> IF the database connection fails during a write operation, THEN THE service SHALL retry up to 3 times with exponential backoff (1s, 2s, 4s) before returning HTTP 503.

**Bad — vague, untestable, ambiguous:**

> The system should handle errors gracefully.

> Authentication needs to be secure.

> The API should be fast.

### Requirement Numbering

- Number sequentially: Requirement 1, 2, 3...
- Within acceptance criteria, number sequentially per requirement: 1, 2, 3...
- When adding requirements to an existing document, continue the sequence
- Never reuse a requirement number, even if an earlier one is deleted

### Non-Functional Requirements

Always include requirements for these categories (when applicable):

- **Performance**: Response times, throughput, resource limits
- **Security**: Authentication, authorization, data protection, input validation
- **Reliability**: Error handling, retry logic, graceful degradation
- **Scalability**: Connection pooling, caching, horizontal scaling
- **Observability**: Logging, monitoring, health checks
- **Deployment**: Container support, environment configuration, CI/CD

---

## Design Template

```markdown
# Design Document: [Feature/System Name]

## Overview

[2-3 sentences: what this system does, who it's for, key constraint or design philosophy.]

---

## Architecture

### High-Level Structure

[ASCII diagram showing the main components and their relationships]

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Frontend   │────▶│   API Layer  │────▶│   Database   │
└──────────────┘     └──────────────┘     └──────────────┘
```

### Component Relationships

[Describe how components interact — data flow direction, protocols, sync vs async]

---

## Components and Interfaces

### [Component Name]

Responsibilities:
- First responsibility
- Second responsibility

Key interfaces:
```typescript
interface ComponentConfig {
  setting: string
  option: boolean
}
```

Key behaviors:
- Describe behavior A
- Describe behavior B (per Req N)

### [Next Component]

...

---

## Data Model

### [Table/Entity Name]

| Column | Type | Constraints | Notes |
|---|---|---|---|
| id | uuid | PK | Auto-generated |
| name | varchar(255) | NOT NULL | Indexed |
| created_at | timestamp | NOT NULL, DEFAULT now() | |
| updated_at | timestamp | NOT NULL, DEFAULT now() | |
| deleted_at | timestamp | NULL | Soft delete |

Indexes:
- `idx_[table]_[column]` on [column] (per Req N)

Relationships:
- Has many [related table] via [foreign key]

---

## API Contracts

### [Endpoint Group]

#### `METHOD /path`

**Description:** What this endpoint does (per Req N).

**Request:**
```json
{
  "field": "type — description"
}
```

**Response (success):**
```json
{
  "success": true,
  "message": "Description",
  "data": {}
}
```

**Response (error):**
```json
{
  "success": false,
  "statusCode": 422,
  "message": "Validation failed",
  "errors": { "field": "Error message" }
}
```

---

## Security Considerations

- [List security measures: auth, rate limiting, input validation, etc.]
- Reference relevant requirement numbers

---

## Deployment & Infrastructure

- [Runtime/platform requirements]
- [Environment variables needed]
- [Container/docker considerations]
```

### ASCII Diagram Conventions

Use box-drawing characters for clean diagrams:

```
Boxes:    ┌──────┐  or  +------+
          │ Name │       | Name |
          └──────┘       +------+

Arrows:   ────▶  (data flow)
          ────   (association)
          - - -▶ (optional/async)

Layers:   Stack vertically for layers
          Place side-by-side for peers
```

Keep diagrams under 80 characters wide for terminal readability.

---

## Tasks Template

```markdown
# Implementation Tasks

## Task List

- [ ] 1. [Phase/Component name]
  - [ ] 1.1 [Concrete subtask — what to create/implement and where]
  - [ ] 1.2 [Another subtask with enough detail to act on]
  - [ ] 1.3 [P] [Parallelizable subtask — can run alongside 1.2]

- [ ] 2. [Next phase/component]
  - [ ] 2.1 [Subtask referencing requirement] (Req 3)
  - [ ] 2.2 Write tests for [component] covering [scenarios]
```

### Task Ordering Rules

1. **Infrastructure first**: Project setup, config, shared utilities
2. **Data layer next**: Database schemas, migrations, ORM setup
3. **Core logic**: Services, business rules, validation
4. **API layer**: Routes, controllers, middleware
5. **Frontend**: Pages, components, composables (if applicable)
6. **Integration**: Cross-cutting concerns, auth, permissions
7. **Testing**: Integration tests, E2E tests (unit tests inline with each component)
8. **Documentation**: API docs, README, deployment guides

### Task Detail Level

Each subtask should answer: **What file(s) to create/modify, what logic to implement, and what behavior to verify.**

**Good task:**
> 2.3 Implement `rateLimiter.ts` middleware with configurable tiers (auth: 5/min, otp: 3/min, api: 100/min), returning HTTP 429 with standard error response and `Retry-After` header on limit exceeded

**Bad task:**
> 2.3 Add rate limiting

### Dependency Markers

- Tasks without markers depend on all previous tasks at the same level
- `[P]` means the task can run in parallel with its siblings
- If a task depends on a specific non-adjacent task, note it: `(after 3.2)`

---

## Config Template

```json
{"specId": "<uuid>", "workflowType": "requirements-first", "specType": "feature"}
```

- `specId`: A unique UUID for this specification (generate fresh each time)
- `workflowType`: Always `"requirements-first"` for SDD
- `specType`: Usually `"feature"`, can be `"bugfix"` or `"refactor"`
