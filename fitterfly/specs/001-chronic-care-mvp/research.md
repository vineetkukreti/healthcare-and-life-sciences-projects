# Research: Chronic Care MVP

## Decision: Build a web MVP before native mobile

**Rationale**: The repository currently contains only `PROJECT.md`. A web app
with backend API gives the fastest path to a runnable product slice while still
testing the core Fitterfly workflows: meal logging, coaching, support triage,
and enterprise reporting.

**Alternatives considered**:
- Native iOS/Android first: closer to the long-term product but too much setup
  before validating the actual workflows.
- Backend-only prototype: simpler, but it would not demonstrate user-facing
  meal review, coaching, or dashboard behavior.

## Decision: Use provider adapters for AI

**Rationale**: The project note mentions Gemini Flash and Vertex AI, but the MVP
should not require live credentials to run. Provider adapters let the app start
with deterministic mock responses and later swap in real AI services.

**Alternatives considered**:
- Direct vendor calls in product code: faster initially but hard to test and
  difficult to run locally.
- No AI layer: misses the core product value.

## Decision: Treat human review as a core workflow

**Rationale**: Healthcare coaching and support automation require review,
override, and escalation paths. Modeling human review from the start prevents
unsafe silent automation.

**Alternatives considered**:
- Add review later: risky because it changes data model and UX assumptions.
- Fully manual coaching: safe but does not test the automation value.

## Decision: Use SQLite for MVP persistence

**Rationale**: SQLite keeps local setup small and makes tests deterministic. The
schema should avoid SQLite-only assumptions so it can move to PostgreSQL or a
managed database later.

**Alternatives considered**:
- BigQuery first: useful for analytics later, but heavy for local MVP
  development.
- In-memory only: quick but loses auditability and outcome history.
