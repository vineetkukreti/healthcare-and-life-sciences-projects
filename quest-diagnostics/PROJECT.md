# Quest Diagnostics — Quest AI Companion (Lab Results Chat)

## Overview
Quest Diagnostics launched **Quest AI Companion**, an AI-powered chat feature integrated into its **secure MyQuest patient portal**, that:
- Analyzes up to **5 years of personal lab data**
- Helps patients **understand their test results**
- Identifies **health trends** over time
- Helps patients **compose informed questions** for their healthcare provider

## Core Idea
Turn cryptic lab reports into a longitudinal, conversational health narrative — patients ask plain-language questions about their own labs and get safe, educational answers grounded in their own historical results.

## Tech Stack
- **MyQuest patient portal** (existing secure infra)
- **LLM-based chat** (likely Gemini / Vertex AI under the hood)
- **Lab data warehouse** (HIPAA-compliant; 5+ year retention)
- **RAG / structured grounding** on patient's longitudinal labs
- Clinical guardrails — never diagnose or prescribe

## Key Features
1. **Plain-language explanation** — "Your LDL is 145 — what does that mean?" → contextualized educational answer.
2. **Trend analysis** — "Has my HbA1c been going up?" → multi-year chart + narrative.
3. **Question prep for doctor visits** — generate a personalized list of questions to ask the PCP.
4. **Out-of-range alerts** — surfaces values that deserve clinician attention.
5. **Strict safety** — refuses to diagnose or recommend treatment; routes those questions to the user's clinician.

## Target Users
- Patients receiving Quest lab tests (massive US footprint)
- Patients with chronic conditions (diabetes, cardiovascular, thyroid)
- Health-literate consumers who want more than a PDF
- Caregivers managing parents' / family members' health

## Project Plan (if rebuilt)
1. **Lab data normalization** — LOINC-coded results; canonical reference ranges; longitudinal patient timeline.
2. **Grounded RAG agent** — only answers grounded in: (a) this patient's lab values and (b) Quest-vetted reference content.
3. **Trend computation** — deterministic time-series summaries (no LLM hallucination on numbers).
4. **Safety layer** — classifier to detect "asking for diagnosis / treatment" → safe response + clinician referral.
5. **Question generator** — produces patient-friendly question list before doctor visit.
6. **Audit logging** — every Q/A logged for compliance and clinical safety review.

## Business Value
- Increases MyQuest portal engagement (recurring touchpoint, not just one-off result delivery)
- Differentiator vs LabCorp and hospital portals
- Drives repeat testing / preventive screening conversations
- Foundation for value-added consumer services
- Massive scale: Quest serves ~150M patient encounters/year
