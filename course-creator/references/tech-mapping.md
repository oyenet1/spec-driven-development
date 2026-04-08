<!--
  ---------------------------------------------------------------
  Company Name: Bonifade Technologies
  Developer: Bowofade Oyerinde
  GitHub: oyenet1
  Created Date: 2026-04-08
  Updated Date: 2026-04-08
  ---------------------------------------------------------------
-->

# Tech Mapping Reference

Use this file to avoid missing language/framework dependencies while building a course.

## Track Baselines

### Frontend baseline
- Internet basics
- HTML, CSS, JavaScript/TypeScript fundamentals
- Build tools and package managers
- Framework fundamentals
- Testing basics
- Deployment basics

### Backend baseline
- Internet protocols and API fundamentals
- Server runtime language fundamentals
- Database design and SQL basics
- API design and auth
- Testing and observability basics
- Deployment and ops basics

### Fullstack baseline
- Frontend baseline + backend baseline
- Integration and architecture boundaries
- End-to-end data flow and security

## Framework-to-Language Guidance

- Nuxt.js / Vue ecosystem: JavaScript/TypeScript
- React / Next.js: JavaScript/TypeScript
- Hono.js: JavaScript/TypeScript runtime ecosystem
- Laravel: PHP
- Gin / Fiber: Go
- Axum / Actix: Rust

Always include language essentials when framework requires it.

## Mandatory Backend/Fullstack Early Modules

1. Core internet terms (`HTTP`, `HTTPS`, `DNS`, `domain`, `hosting`)
2. UML fundamentals (use case, DFD, ERD)
3. Data modeling and database design
4. System design fundamentals — problem-first teaching, covers: caching/Redis, CDN, indexing, queues, rate limiting, load balancing, replication, API versioning, monolith vs microservices
5. DSA intro — real-life-first teaching, covers: arrays, hash maps, stacks, queues, binary search, sorting, Big O, search example, practical math

## Why / What / When / Where Rule

Every concept across all modules must be explained with all four dimensions:
- Why: the problem it solves
- What: plain-language definition
- When: the condition that triggers its use
- Where: where it lives in a real codebase or system

## Docs Priority Order

1. roadmap.sh track map
2. Official framework docs
3. Supporting beginner explanations from w3schools.com
4. Local roadmap checklists from `backend.pdf`, `frontend.pdf`, `devops.pdf`

## DevOps Minimum Topics

- Git collaboration flow
- FTP/SFTP overview
- CI/CD concepts
- Docker basics
- Kubernetes intro
- Hosting/deployment options (for example Vercel, managed cloud, VM)
- Package and dependency management

## Project Diversity Pattern

Try to spread projects across:
- CRUD and data management
- Authentication and authorization
- Realtime communication (WebSockets)
- Integrations (payments/email/maps)
- Performance and reliability concerns
