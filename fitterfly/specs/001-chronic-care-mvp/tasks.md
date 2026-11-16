# Tasks: Chronic Care MVP

**Input**: Design documents from `specs/001-chronic-care-mvp/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/openapi.yaml`, `quickstart.md`

**Tests**: Included because the constitution requires focused tests for health data, AI recommendations, escalation behavior, and reporting boundaries.

**Organization**: Tasks are grouped by independently testable user story.

## Phase 1: Setup

**Purpose**: Create the runnable backend/frontend project skeleton.

- [x] T001 Create backend project structure in `backend/app/` and `backend/tests/`
- [x] T002 Create frontend project structure in `frontend/src/` and `frontend/tests/`
- [x] T003 Configure backend dependency metadata in `backend/pyproject.toml`
- [x] T004 Configure frontend package metadata in `frontend/package.json`
- [x] T005 [P] Add backend application entrypoint in `backend/app/main.py`
- [x] T006 [P] Add frontend application entrypoint in `frontend/src/main.tsx`
- [x] T007 [P] Add environment examples in `backend/.env.example` and `frontend/.env.example`

---

## Phase 2: Foundational

**Purpose**: Shared models, persistence, provider boundaries, and safety infrastructure required by every story.

- [x] T008 Create database/session setup in `backend/app/core/database.py`
- [x] T009 Create shared API error handling in `backend/app/core/errors.py`
- [x] T010 Create provider interface base classes in `backend/app/services/providers.py`
- [x] T011 Create deterministic mock AI provider in `backend/app/services/mock_ai_provider.py`
- [x] T012 Create audit logging service in `backend/app/services/audit_service.py`
- [x] T013 Create human review case model and schemas in `backend/app/models/review_case.py` and `backend/app/schemas/review_case.py`
- [x] T014 Create human review service in `backend/app/services/review_service.py`
- [x] T015 Create shared frontend API client in `frontend/src/services/api.ts`
- [x] T016 Add backend health endpoint in `backend/app/api/health.py`
- [x] T017 Add baseline backend tests for health and database setup in `backend/tests/test_health.py`

**Checkpoint**: Backend and frontend skeletons exist, health check works, and shared review/audit infrastructure is available.

---

## Phase 3: User Story 1 - Log Meals From Photos (Priority: P1) MVP

**Goal**: User can analyze a meal photo, correct the estimate, and save a confirmed meal log.

**Independent Test**: Submit a sample meal image, edit the returned estimate, save it, and confirm the corrected log appears in the daily meal list.

### Tests

- [x] T018 [P] [US1] Add meal analysis service tests in `backend/tests/test_meal_analysis.py`
- [x] T019 [P] [US1] Add meal log API tests in `backend/tests/test_meal_logs.py`
- [x] T020 [P] [US1] Add meal logging UI behavior tests in `frontend/tests/meal-logging.test.tsx`

### Implementation

- [x] T021 [P] [US1] Create meal log model in `backend/app/models/meal_log.py`
- [x] T022 [P] [US1] Create meal log schemas in `backend/app/schemas/meal_log.py`
- [x] T023 [US1] Implement meal analysis service in `backend/app/services/meal_analysis_service.py`
- [x] T024 [US1] Implement meal log service in `backend/app/services/meal_log_service.py`
- [x] T025 [US1] Implement meal endpoints in `backend/app/api/meal_logs.py`
- [x] T026 [US1] Wire meal endpoints into `backend/app/main.py`
- [x] T027 [US1] Create meal logging page in `frontend/src/pages/MealLoggingPage.tsx`
- [x] T028 [US1] Create editable meal estimate component in `frontend/src/components/MealEstimateEditor.tsx`
- [x] T029 [US1] Add meal API functions in `frontend/src/services/meals.ts`

**Checkpoint**: User Story 1 is fully demoable as the MVP.

---

## Phase 4: User Story 2 - Receive Precision Coaching (Priority: P2)

**Goal**: User receives personalized, bounded guidance with escalation for risky or low-confidence cases.

**Independent Test**: Create a user profile with recent logs, request coaching, and verify normal guidance returns while risky cases create review cases.

### Tests

- [ ] T030 [P] [US2] Add coaching safety tests in `backend/tests/test_coaching_safety.py`
- [ ] T031 [P] [US2] Add coaching API tests in `backend/tests/test_coaching.py`
- [ ] T032 [P] [US2] Add coaching UI tests in `frontend/tests/coaching.test.tsx`

### Implementation

- [ ] T033 [P] [US2] Create user and care profile models in `backend/app/models/user.py`
- [ ] T034 [P] [US2] Create coaching recommendation model in `backend/app/models/coaching.py`
- [ ] T035 [P] [US2] Create user, care profile, and coaching schemas in `backend/app/schemas/`
- [ ] T036 [US2] Implement care profile service in `backend/app/services/care_profile_service.py`
- [ ] T037 [US2] Implement coaching service with safety escalation in `backend/app/services/coaching_service.py`
- [ ] T038 [US2] Implement coaching endpoints in `backend/app/api/coaching.py`
- [ ] T039 [US2] Create coaching page in `frontend/src/pages/CoachingPage.tsx`
- [ ] T040 [US2] Create recommendation card component in `frontend/src/components/RecommendationCard.tsx`
- [ ] T041 [US2] Add coaching API functions in `frontend/src/services/coaching.ts`

**Checkpoint**: Coaching works with both automated guidance and human-review escalation.

---

## Phase 5: User Story 3 - Automate Support With Escalation (Priority: P3)

**Goal**: Routine support questions are answered automatically; sensitive or low-confidence questions are routed to human review.

**Independent Test**: Submit one routine question and one complex question, then verify the routine answer and review-case creation.

### Tests

- [ ] T042 [P] [US3] Add support triage service tests in `backend/tests/test_support_triage.py`
- [ ] T043 [P] [US3] Add support API tests in `backend/tests/test_support.py`
- [ ] T044 [P] [US3] Add support UI tests in `frontend/tests/support.test.tsx`

### Implementation

- [ ] T045 [P] [US3] Create support interaction model in `backend/app/models/support.py`
- [ ] T046 [P] [US3] Create support schemas in `backend/app/schemas/support.py`
- [ ] T047 [US3] Implement support triage service in `backend/app/services/support_service.py`
- [ ] T048 [US3] Implement support endpoints in `backend/app/api/support.py`
- [ ] T049 [US3] Create support page in `frontend/src/pages/SupportPage.tsx`
- [ ] T050 [US3] Create escalation status component in `frontend/src/components/EscalationStatus.tsx`
- [ ] T051 [US3] Add support API functions in `frontend/src/services/support.ts`

**Checkpoint**: Support automation and escalation are independently demoable.

---

## Phase 6: User Story 4 - Track Outcomes For Users And Enterprises (Priority: P4)

**Goal**: Users see personal progress and enterprise users see privacy-safe aggregate outcomes.

**Independent Test**: Load sample outcome data, view personal trends, and verify aggregate cohort reporting respects the privacy threshold.

### Tests

- [ ] T052 [P] [US4] Add outcome aggregation tests in `backend/tests/test_outcomes.py`
- [ ] T053 [P] [US4] Add enterprise privacy threshold tests in `backend/tests/test_enterprise_privacy.py`
- [ ] T054 [P] [US4] Add dashboard UI tests in `frontend/tests/outcomes.test.tsx`

### Implementation

- [ ] T055 [P] [US4] Create outcome measurement model in `backend/app/models/outcome.py`
- [ ] T056 [P] [US4] Create enterprise cohort model in `backend/app/models/enterprise.py`
- [ ] T057 [P] [US4] Create outcome and enterprise schemas in `backend/app/schemas/`
- [ ] T058 [US4] Implement outcome service in `backend/app/services/outcome_service.py`
- [ ] T059 [US4] Implement enterprise aggregation service in `backend/app/services/enterprise_service.py`
- [ ] T060 [US4] Implement outcome endpoints in `backend/app/api/outcomes.py`
- [ ] T061 [US4] Implement enterprise endpoints in `backend/app/api/enterprise.py`
- [ ] T062 [US4] Create personal outcomes page in `frontend/src/pages/OutcomesPage.tsx`
- [ ] T063 [US4] Create enterprise dashboard page in `frontend/src/pages/EnterpriseDashboardPage.tsx`
- [ ] T064 [US4] Add outcome and enterprise API functions in `frontend/src/services/outcomes.ts`

**Checkpoint**: Personal and enterprise reporting work without exposing unsafe individual details.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, seed data, end-to-end validation, and safety review.

- [ ] T065 [P] Add seeded demo data in `backend/app/core/seed.py`
- [ ] T066 [P] Add README setup instructions in `README.md`
- [ ] T067 Add review-case admin view in `frontend/src/pages/ReviewCasesPage.tsx`
- [ ] T068 Add navigation shell in `frontend/src/App.tsx`
- [ ] T069 Run backend tests and fix failures in `backend/tests/`
- [ ] T070 Run frontend tests and fix failures in `frontend/tests/`
- [ ] T071 Validate quickstart flow from `specs/001-chronic-care-mvp/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- Setup (Phase 1) has no dependencies.
- Foundational (Phase 2) depends on Setup and blocks all stories.
- User Story 1 starts after Foundational and is the MVP.
- User Stories 2, 3, and 4 can start after Foundational, but final demo quality improves if completed in priority order.
- Polish depends on selected user stories being complete.

### User Story Dependencies

- **US1 Meal logging**: No dependency on other stories after foundation.
- **US2 Coaching**: Uses user profile and meal logs when present; can still be tested with seeded data.
- **US3 Support**: No dependency on meal or coaching flows after foundation.
- **US4 Outcomes**: Can be tested with seeded data; richer when US1 and US2 produce records.

## Parallel Opportunities

- T005, T006, and T007 can run in parallel.
- Model/schema tasks within each user story can run in parallel.
- Backend tests and frontend tests for the same story can be written in parallel.
- US2 and US3 can proceed in parallel after Phase 2 because they mainly touch separate services and UI pages.

## Implementation Strategy

### MVP First

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3 only.
3. Validate that meal photo analysis, correction, save, and list behavior work.
4. Then add coaching, support, and reporting in priority order.

### Format Validation

All tasks follow `- [ ] T### [P?] [US?] Description with file path`.
