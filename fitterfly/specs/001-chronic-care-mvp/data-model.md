# Data Model: Chronic Care MVP

## User

- `id`: Stable identifier
- `name`: Display name
- `email`: Contact address
- `condition_focus`: Diabetes, obesity, PCOS, thyroid, or other supported focus
- `consent_status`: Active, withdrawn, pending
- `created_at`, `updated_at`

## Care Profile

- `id`
- `user_id`
- `goals`: Weight, glucose control, adherence, or lifestyle goals
- `dietary_preferences`: Cuisine, restrictions, allergies, dislikes
- `baseline_weight`
- `latest_hba1c`
- `risk_notes`
- `updated_at`

## Meal Log

- `id`
- `user_id`
- `captured_at`
- `source`: AI photo, manual entry, corrected AI
- `items`: Food names and portions
- `calories`
- `macros`: Carbohydrates, protein, fat, fiber when available
- `ai_confidence`
- `confirmation_status`: Unconfirmed, confirmed, corrected
- `correction_history`

## Coaching Recommendation

- `id`
- `user_id`
- `created_at`
- `category`: Diet, activity, sleep, adherence, education
- `message`
- `rationale`
- `source_signals`
- `confidence`
- `risk_level`: Low, medium, high
- `review_status`: Not required, pending review, approved, rejected, revised

## Support Interaction

- `id`
- `user_id`
- `created_at`
- `question`
- `category`: Product, care process, clinical, billing, technical
- `answer`
- `confidence`
- `resolution_state`: Automated, escalated, resolved by human
- `review_case_id`

## Outcome Measurement

- `id`
- `user_id`
- `measurement_type`: Weight, HbA1c, CGM summary, adherence, engagement
- `value`
- `unit`
- `measured_at`
- `source`

## Enterprise Cohort

- `id`
- `name`
- `sponsor_type`: Insurer, employer, care partner
- `privacy_threshold`
- `member_count`
- `aggregate_metrics`

## Human Review Case

- `id`
- `user_id`
- `source_type`: Coaching recommendation, support interaction, meal log,
  enterprise report
- `source_id`
- `reason`
- `assigned_role`: Coach, dietitian, support operator
- `status`: Open, in review, resolved, dismissed
- `resolution_notes`
- `created_at`, `resolved_at`

## Relationships

- A user has one active care profile.
- A user has many meal logs, recommendations, support interactions, outcome
  measurements, and review cases.
- Coaching recommendations may create review cases.
- Support interactions may create review cases.
- Enterprise cohorts contain aggregate metrics derived from enrolled users, but
  do not expose unrestricted user-level records.
