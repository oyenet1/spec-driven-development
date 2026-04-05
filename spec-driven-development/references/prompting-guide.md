# SDD Prompting Guide

How to prompt the LLM to get the best specification output.

---

## The Golden Rule

**Give context, not commands.** The more the LLM understands about your world, the better the specs it produces. A 3-sentence description with context beats a 1-paragraph vague request every time.

---

## Prompt Structure

The ideal prompt follows this pattern:

```
[What you're building] + [Who it's for] + [Key constraints] + [What exists already]
```

### Example — Great Prompt

> Spec this: A real-time notification system for our SaaS project management tool.
> Users are team leads and developers. We're using Hono + Vue 3 + PostgreSQL + Redis.
> Notifications should support in-app, email, and push channels.
> We already have an auth module with JWT tokens and a users table.
> MVP scope — no SMS, no scheduled digests yet.

Why this works:
- States **what** clearly (notification system)
- States **who** (team leads, developers)
- States **tech stack** (Hono, Vue, Postgres, Redis)
- States **scope boundaries** (no SMS, no digests)
- States **existing context** (auth module, users table)

### Example — Weak Prompt

> I need notifications for my app

Why this fails:
- What kind of notifications? (in-app? email? push?)
- What app? What stack?
- Who are the users?
- What already exists?
- The LLM will guess everything — and likely guess wrong

---

## Prompt Templates

Copy and fill in these templates for consistently good results.

### Template 1: New Feature

```
Spec this: [feature name]

Context:
- Product: [what your product does, in one sentence]
- Tech stack: [languages, frameworks, database, infra]
- Users: [who will use this feature and their role]

Requirements:
- [must-have 1]
- [must-have 2]
- [must-have 3]

Out of scope:
- [thing to explicitly exclude]

Existing context:
- [what already exists that this feature touches]
```

### Template 2: Refine Existing Idea

```
I have a rough idea for [feature]. Here's what I know so far:

[paste your notes, bullet points, or brain dump]

Help me turn this into a proper spec. My stack is [stack].
Focus on [area of concern — e.g., "the data model" or "API design"].
```

### Template 3: Break Down a Large System

```
SDD: [system name]

This system needs to:
1. [capability 1]
2. [capability 2]
3. [capability 3]

Users: [personas]
Stack: [tech choices]
Scale: [expected usage — e.g., "~1000 users", "high-throughput"]

Break this into separate specs per module if needed.
```

### Template 4: Generate Only One Artifact

```
Generate requirements for: [feature description]
Stack: [tech stack]
Focus on: [specific area — e.g., "security requirements" or "API contracts"]
```

```
Generate tasks for: [feature description]
Design doc is at: .fade/specs/[name]/design.md
```

---

## Power Tips

### 1. State What You DON'T Want

Exclusions sharpen scope dramatically:

> Out of scope: admin panel, bulk operations, CSV export, multi-tenancy

### 2. Mention Your Patterns

If your project follows specific patterns, say so:

> We use modular monolith architecture. Each module has its own routes,
> controller, service, DTO, and schema files. API responses follow
> { success, message, data } format. All tables have soft deletes.

The LLM will match your patterns in the generated specs.

### 3. Reference Existing Specs

If you already have specs for other features, point to them:

> Follow the same format as .fade/specs/auth/requirements.md

This gives the LLM a concrete example of your preferred style.

### 4. Be Specific About Scale

"Handle lots of users" means nothing. Instead:

> Expected: 10K concurrent WebSocket connections, 500 messages/second,
> message history retained for 90 days.

Numbers become testable non-functional requirements.

### 5. Name Your Entities

Instead of "the thing that stores user data", say:

> The `accounts` table stores user profiles. The `auth_sessions` table
> tracks active JWT sessions.

Domain language in your prompt flows directly into the glossary and data model.

### 6. Describe the Happy Path

Walk through the ideal user flow:

> User clicks "New Project" → fills in name and description → selects
> team members → project is created with a default board → team members
> get email notification → they see the project in their dashboard.

This becomes the foundation for user stories and acceptance criteria.

### 7. Iterate, Don't Start Over

After the first spec generation:

> Refine spec .fade/specs/notifications/: Add rate limiting to prevent
> notification spam — max 10 per user per minute. Also add a "mute"
> feature per channel.

Incremental refinement produces better results than regenerating from scratch.

---

## What to Avoid

| Don't | Do Instead |
|---|---|
| "Make it scalable" | "Support 10K concurrent users with <200ms p95 latency" |
| "Handle errors properly" | "Return HTTP 422 with field-level error messages for validation failures" |
| "Add authentication" | "JWT access tokens (15-min) + HTTP-only refresh cookies (7-day)" |
| "Make it secure" | "Rate limit login to 5 attempts/min, hash passwords with bcrypt, sanitize all inputs" |
| "Build a dashboard" | "Admin dashboard showing: user count, active sessions, revenue chart (last 30 days), recent signups table with pagination" |
| Multi-feature mega-prompts | One spec per feature, reference shared modules |

---

## The Iteration Loop

The best specs come from iteration, not a single prompt:

```
1. Give rough idea + context     → Get first draft specs
2. Review requirements           → "Add requirement for X, remove Y"
3. Review design                 → "Use Redis instead of in-memory for cache"
4. Review tasks                  → "Split task 3 into smaller subtasks"
5. Final review                  → "Run the quality checklist"
```

Each round sharpens the specs. Three rounds typically produces production-ready specifications.
