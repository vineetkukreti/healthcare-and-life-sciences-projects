# Feature Specification: Chronic Care MVP

**Feature Branch**: `001-chronic-care-mvp`

**Created**: 2026-05-14

**Status**: Draft

**Input**: User description: "Build the initial Fitterfly chronic disease management MVP from PROJECT.md: AI-assisted meal photo logging, precision coaching, support triage, outcome tracking, and enterprise reporting for diabetes and obesity care."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Log Meals From Photos (Priority: P1)

A user managing diabetes or obesity can capture a meal photo, review the
recognized dish and estimated portion, edit the result, and save confirmed
nutrition data to their daily log.

**Why this priority**: Meal logging is the highest-friction daily behavior in
the product concept and directly supports the 80% time-reduction goal.

**Independent Test**: Can be tested by submitting a sample meal image, editing
the recognized result, saving it, and confirming the daily nutrition view
reflects the corrected meal.

**Acceptance Scenarios**:

1. **Given** a user is on the meal logging screen, **When** they upload or take
   a meal photo, **Then** the system presents recognized food items, estimated
   portions, calories, and macros for review.
2. **Given** the recognition result is partially wrong, **When** the user edits
   the dish, portion, or nutrition values, **Then** the corrected values are
   saved instead of the original AI estimate.
3. **Given** the system cannot confidently identify the meal, **When** the
   result is returned, **Then** the user receives a clear prompt to manually
   enter or correct the meal before saving.

---

### User Story 2 - Receive Precision Coaching (Priority: P2)

A user receives personalized daily guidance based on recent meals, health
goals, weight trend, HbA1c context, CGM or wearable signals when available, and
coach-approved chronic care protocols.

**Why this priority**: Coaching turns logged data into behavior change and is
the core digital therapeutics value beyond tracking.

**Independent Test**: Can be tested by creating a user profile with goals and
recent logs, requesting guidance, and verifying the response is personalized,
bounded, and eligible for human review when risk signals appear.

**Acceptance Scenarios**:

1. **Given** a user has profile goals and recent meal logs, **When** they open
   daily coaching, **Then** the system provides diet, exercise, sleep, or habit
   guidance tied to their recent pattern.
2. **Given** user data contains a risky or ambiguous health signal, **When** the
   coaching engine generates guidance, **Then** the item is flagged for coach
   review or routed to an escalation path.

---

### User Story 3 - Automate Support With Escalation (Priority: P3)

A user can ask common product, program, or care-process questions and receive
an immediate support answer, while complex or sensitive questions are routed to
a human coach, dietitian, or support operator.

**Why this priority**: Support automation is required for scalable operations
and supports the target of automating most routine queries.

**Independent Test**: Can be tested by submitting routine and complex support
questions, confirming routine answers resolve automatically and complex items
create a human-review case.

**Acceptance Scenarios**:

1. **Given** a user asks a routine FAQ-style support question, **When** the
   support assistant has a high-confidence answer, **Then** the user receives a
   concise response and the interaction is recorded.
2. **Given** a user asks a medical, billing, safety, or low-confidence question,
   **When** the assistant cannot safely resolve it, **Then** the question is
   escalated with context for a human reviewer.

---

### User Story 4 - Track Outcomes For Users And Enterprises (Priority: P4)

Users can view personal progress over time, and authorized enterprise users can
view aggregate outcomes for enrolled populations without exposing unnecessary
personal health information.

**Why this priority**: Outcome tracking supports user motivation and insurer or
employer reporting, but depends on the earlier logging and coaching flows.

**Independent Test**: Can be tested by loading sample user outcome data,
viewing personal trends, and verifying enterprise views show aggregate metrics
without unnecessary user-identifiable detail.

**Acceptance Scenarios**:

1. **Given** a user has weight, meal, and HbA1c history, **When** they view
   progress, **Then** the system shows trend summaries and milestones.
2. **Given** an enterprise user views a population dashboard, **When** outcomes
   are displayed, **Then** metrics are aggregated by cohort and do not reveal
   individual health records unless explicitly authorized for care operations.

### Edge Cases

- Meal photos may be blurry, contain multiple dishes, show unfamiliar regional
  foods, or have missing portion context.
- Users may correct AI results repeatedly; the system must preserve the latest
  user-confirmed value.
- CGM, wearable, weight, or lab data may be missing, delayed, duplicated, or
  contradictory.
- Coaching requests may include medication, emergency, pregnancy, or severe
  symptom context that requires human escalation instead of automated advice.
- Enterprise cohorts may be too small for safe anonymized reporting.
- Support questions may mix product help with clinical or billing concerns.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to create and maintain a chronic care
  profile with condition focus, goals, dietary preferences, and relevant health
  context.
- **FR-002**: System MUST accept meal photos and return editable food item,
  portion, calorie, and macro estimates before saving.
- **FR-003**: Users MUST be able to manually correct or enter meal information
  when recognition is wrong, incomplete, or unavailable.
- **FR-004**: System MUST store user-confirmed meal logs and distinguish them
  from unconfirmed AI estimates.
- **FR-005**: System MUST generate personalized coaching guidance from the
  user's profile, goals, recent logs, and available outcome signals.
- **FR-006**: System MUST flag high-risk, low-confidence, or medical-scope
  coaching situations for human review instead of silently presenting advice.
- **FR-007**: System MUST answer routine support questions using approved
  support knowledge and record whether the interaction was automated or
  escalated.
- **FR-008**: System MUST route complex, sensitive, or low-confidence support
  questions to a human review queue with relevant context.
- **FR-009**: System MUST present personal outcome trends including at least
  meal adherence and weight trend, with HbA1c and CGM summaries when available.
- **FR-010**: System MUST provide authorized enterprise users with aggregate
  population outcome summaries for enrolled cohorts.
- **FR-011**: System MUST prevent enterprise reporting from exposing personal
  health information beyond the user's authorized care or reporting context.
- **FR-012**: System MUST record an audit trail for AI-generated meal results,
  coaching recommendations, support answers, human escalations, and overrides.

### Key Entities *(include if feature involves data)*

- **User**: Person enrolled in chronic care with profile, goals, condition
  focus, preferences, and consent state.
- **Care Profile**: Health and lifestyle context used to personalize coaching,
  including condition focus, goals, measurements, and preferences.
- **Meal Log**: User-confirmed meal entry with food items, portions, calories,
  macros, timestamp, source, and correction history.
- **Coaching Recommendation**: Personalized guidance item with rationale,
  confidence, source data, risk classification, and review status.
- **Support Interaction**: User question, automated answer or escalation state,
  category, confidence, and reviewer notes.
- **Outcome Measurement**: Weight, HbA1c, CGM summary, adherence, or other
  progress signal tied to a user and time period.
- **Enterprise Cohort**: Group of enrolled users visible to an insurer or
  employer for aggregate reporting.
- **Human Review Case**: Escalation record assigned to a coach, dietitian, or
  support operator with status and resolution.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: At least 90% of sample meal logging attempts can be completed by
  a user with AI assistance plus manual correction in under 60 seconds.
- **SC-002**: 100% of saved meal logs are user-confirmed or explicitly marked
  as manually entered; unconfirmed AI estimates are not treated as final data.
- **SC-003**: Coaching output includes a user-specific rationale and safe
  escalation behavior for 100% of flagged high-risk or low-confidence cases.
- **SC-004**: At least 90% of routine support questions in the approved FAQ set
  receive an automated answer without human intervention.
- **SC-005**: 100% of low-confidence, medical-scope, billing-sensitive, or
  unsafe support questions create a human review case.
- **SC-006**: Enterprise dashboards show aggregate outcome metrics without
  exposing individual health records for cohorts below the privacy threshold.
- **SC-007**: A reviewer can trace every AI-generated recommendation or support
  answer back to source inputs, confidence, and review/escalation state.

## Assumptions

- The first build is an MVP prototype, not a regulated medical device release.
- Users have basic mobile or web access and can upload or capture meal photos.
- AI services are treated as replaceable providers behind product workflows;
  the specification does not require a specific vendor.
- Human review roles include at least coach/dietitian and support operator.
- Enterprise users view aggregate insurer/employer outcomes, not unrestricted
  individual records.
- Medication changes, emergency symptoms, and diagnosis are outside automated
  advice scope and require escalation.
