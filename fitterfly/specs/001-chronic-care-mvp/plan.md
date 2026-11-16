# Implementation Plan: Chronic Care MVP

**Branch**: `001-chronic-care-mvp` | **Date**: 2026-05-14 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/001-chronic-care-mvp/spec.md`

## Summary

Build a runnable MVP for Fitterfly-style chronic care management focused on
four independently testable flows: AI-assisted meal photo logging, personalized
coaching, support triage, and outcome reporting. The first implementation will
be a web application with a backend API and provider adapters that can start
with deterministic mock AI responses, then later connect to Gemini/Vertex-style
services.

## Technical Context

**Language/Version**: Python 3.13 backend, TypeScript frontend

**Primary Dependencies**: FastAPI, Pydantic, SQLAlchemy, SQLite, React, Vite

**Storage**: SQLite for MVP local persistence; schema should be portable to
PostgreSQL later

**Testing**: pytest for backend unit/integration tests; Vitest or Playwright for
frontend behavior when UI is added

**Target Platform**: Local web app MVP, deployable later as API + frontend

**Project Type**: Web application with backend API and frontend client

**Performance Goals**: Meal logging and support responses should return MVP
results in under 2 seconds with mock providers; dashboard pages should load
sample local data in under 1 second

**Constraints**: No real medical diagnosis, medication changes, or emergency
handling by automation; all risky advice and low-confidence outputs escalate
to human review

**Scale/Scope**: MVP supports seeded demo users, local data, mock AI providers,
and aggregate enterprise reporting over sample cohorts

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Patient safety and clinical boundaries**: PASS. Plan limits automated
  coaching, requires escalation for risky or low-confidence situations, and
  keeps medication/emergency advice outside automated scope.
- **Privacy, consent, and data minimization**: PASS. Data model separates user
  care records from aggregate enterprise cohort reporting and requires consent
  state.
- **Measurable health outcomes**: PASS. MVP success criteria include meal
  logging time, support automation, escalation behavior, and aggregate outcome
  privacy.
- **Human-in-the-loop care**: PASS. Human review cases are first-class records
  for coaching, support, and AI override workflows.
- **Simple, testable delivery**: PASS. MVP starts with a local web/API slice and
  deterministic provider adapters before real AI or wearable integrations.

## Project Structure

### Documentation (this feature)

```text
specs/001-chronic-care-mvp/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── openapi.yaml
└── checklists/
    └── requirements.md
```

### Source Code (repository root)

```text
backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   └── services/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── state/
└── tests/
```

**Structure Decision**: Use a web application structure. The product concept is
mobile-first long term, but a web MVP is faster to verify locally from the
current empty repo and keeps AI, safety, privacy, and reporting workflows
testable before native mobile investment.

## Complexity Tracking

No constitution violations identified.
