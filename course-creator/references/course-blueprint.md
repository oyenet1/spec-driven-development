<!--
  ---------------------------------------------------------------
  Company Name: Bonifade Technologies
  Developer: Bowofade Oyerinde
  GitHub: oyenet1
  Created Date: 2026-04-08
  Updated Date: 2026-04-08
  ---------------------------------------------------------------
-->

# Course Blueprint Reference

Use this blueprint to build final course outputs.

## 1) Course Metadata

- Course title
- Track type: frontend/backend/fullstack
- Target learner profile
- Selected language(s) and framework(s)
- Total duration (weeks)
- Weekly study hours
- AI-driven mode: yes/no
- Delivery mode: fast/deep

## 2) Chapter Outline

For each chapter, provide:
- Objective
- Prerequisites
- Duration (hours)
- Source references: roadmap.sh URL | official docs URL | w3schools URL (if applicable)
- Dependency note (what must be learned before this chapter)
- Full lesson list — every lesson must be explicitly listed under its chapter, never implied or skipped

Lesson list format under each chapter:
```
Total Lessons: {N}
Lesson N.1: {title}
Lesson N.2: {title}
Lesson N.3: {title}
...
```

Minimum 3 lessons per chapter. The `Total Lessons` count must always match the actual number of lessons listed. No chapter may appear without its lessons listed beneath it.

## 3) Detailed Pages by Chapter

Each lesson must begin with a `Source:` line — the live URL used to write that lesson (roadmap.sh, official docs, or w3schools).

Each lesson should contain page blocks:
- Page 1: concept in plain words — MUST include Why / What / When / Where for every concept introduced
- Page 2: real-life analogy
- Page 3: guided implementation
- Page 4: common mistakes and fixes
- Page 5: mini challenge

### Why / What / When / Where (MANDATORY on every concept)

No concept may be introduced in any lesson without all four dimensions answered. Use this exact format inline:

```
Why: {the problem this solves or the reason it exists}
What: {plain-language definition}
When: {the condition or scenario where you use this}
Where: {where in a real codebase or system this lives}
```

This applies to every term, every system design concept, every DSA concept, every DevOps concept, every database concept, and every API concept.

Every lesson must end with a `References` block:
```
References:
  - Primary: {official docs URL for this specific topic}
  - Tutorial: {w3schools URL, if a relevant page exists}
  - Roadmap: {roadmap.sh URL for this topic, if available}
```

Use simple language and avoid unexplained jargon.

### Concept Illustrations

Include images only where they genuinely aid understanding. Do not illustrate every concept.

Suitable candidates per chapter (max 3 images per chapter, max 1 per lesson page):
- Architecture and system flow diagrams
- Data flow and process flow diagrams
- ERD and UML diagrams
- Visual comparisons (for example sync vs async, stack vs heap)
- Deployment topology diagrams

ALL architectural drawings MUST use Mermaid diagram blocks. This is mandatory — no plain text or ASCII art for architectural content. Every Mermaid block must have a `Caption:` line after the closing fence.

Every image must include:
- `Alt text`: accessible description of the image
- `Caption`: one sentence takeaway for the learner
- `Fallback`: Mermaid diagram block (mandatory for architectural content), ASCII only when no Mermaid type fits

Do not generate images for simple definitions, code examples, or decorative purposes.

## 4) Practice Pack

Per chapter:
- 3+ exercises
- chapter checkpoint quiz/review

Across full course:
- 5+ assignments with grading rubric

## 4b) System Design Chapter (backend and fullstack — MANDATORY)

Must appear after Database Design and before framework implementation chapters.

Every topic in this chapter uses the problem-first pattern:
```
Problem: {realistic scenario — site is slow, server crashes, etc.}
Symptom: {what the user/developer observes}
Root cause: {technical explanation of why}
Solution: {the system design concept}
Why / What / When / Where: {all four dimensions}
Mermaid diagram: {architecture or flow diagram}
```

Required topics (all must be covered):
- Scalability — vertical vs horizontal scaling, load balancers
- Caching with Redis — cache hit/miss, TTL, invalidation
- CDN — edge nodes, origin server, cache-control headers
- Database indexing — B-tree, full table scan, query planner
- Message queues and background jobs — producer/consumer, retries
- Rate limiting — token bucket, sliding window
- Load balancing — round-robin, health checks, sticky sessions
- Database replication — primary/replica, read replicas, eventual consistency
- API versioning — URL versioning, backward compatibility, deprecation
- Monolith vs microservices — when to split, service communication

## 4c) DSA Chapter (backend/fullstack required, frontend optional)

Every topic uses the real-life-first pattern:
```
Real-life scenario: {everyday analogy}
Technical concept: {data structure or algorithm}
Why / What / When / Where: {all four dimensions}
Code example: {TypeScript with comments}
Real project use case: {where this appears in actual code}
```

Required topics:
- Arrays and iteration
- Hash maps — O(1) lookup, deduplication, grouping
- Stacks and queues
- Binary search — O(log n) vs O(n) with plain number examples
- Sorting — conceptual bubble sort, practical `.sort()` with comparators
- Big O notation — O(1), O(n), O(n²), O(log n) in plain language
- Search in practice — build a product search, naive vs indexed approach
- Practical math — percentage, average, pagination offset, growth rate as TypeScript utility functions

## 5) Project Portfolio

Track minimums:
- Frontend: 4+
- Backend: 3+
- Fullstack: 7+

Portfolio rules:
- At least one realtime/WebSocket project
- Include beginner, intermediate, and advanced spread
- Include impact-oriented projects useful to society/business

## 5b) Project Prompt Pack

After the Project Portfolio, generate a `Project Prompt Pack` for every project.

Per project, include:
1. One project overview prompt (full context: name, goal, stack, architecture, features list)
2. One feature prompt per feature, ordered by dependency (schema → service → controller → route)

Each feature prompt must be self-contained and include: project name, feature name, stack, context, task, requirements, constraints (TypeScript, bun, Drizzle ORM, modular monolith, snake_case DB, camelCase API response, versioned routes, file header comment), and a validation instruction.

## 6) Tooling and Delivery

Must include practical lessons for:
- Git and collaboration flow
- Deployment targets
- CI/CD basics
- Docker basics
- Kubernetes intro
- Package/dependency management

## 7) Weekly Milestones

For each week:
- Focus topics
- Hours target
- Deliverable
- Checkpoint criteria

## 8) Course Index

The Course Index is always the LAST section of the full course output.

It is an alphabetically sorted reference of every term, concept, technology, tool, pattern, and acronym introduced anywhere in the course.

Per entry:
- Term or concept name (bold)
- One-line plain-language definition
- First occurrence reference: `Ch.N → Lesson N`

Group entries under letter headings (A, B, C, ...). Include all: HTTP verbs, status codes taught, design patterns, ORM methods, CLI commands, architecture terms, framework-specific concepts, and project-specific terms.

## 9) Final Course Validation

- Order follows prerequisites
- Time estimates are realistic
- Theory and practice balanced
- Every concept has Why/What/When/Where answered (no exceptions)
- System design chapter present (backend/fullstack), uses problem-first pattern, covers all 10 required topics
- DSA chapter present (backend/fullstack required), uses real-life-first pattern, covers all 8 required topics
- Every chapter has its lessons explicitly listed and expanded beneath it
- Every lesson has a `Source:` URL and a `References` block (official docs + w3schools + roadmap.sh)
- roadmap.sh fetched for the track before outline was built
- Official docs fetched per topic as lessons were written
- w3schools linked for all applicable foundational topics
- Images placed only where genuinely needed (max 3 per chapter, max 1 per lesson page)
- ALL architectural drawings use Mermaid blocks with captions
- Project Prompt Pack present with overview + feature-by-feature prompts for every project
- Course Index present as last section, alphabetically sorted, with chapter/lesson references
