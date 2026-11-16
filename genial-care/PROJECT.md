# Genial Care — AI for Autism Spectrum Care Records

## Overview
Genial Care, a Latin American healthcare network, is a reference in **innovative care for children with Autism Spectrum Disorder (ASD)** and their families. By investing in **Vertex AI**, the company has improved the quality of records of therapy sessions involving atypical children and their families, allowing caregivers to fully monitor the work being carried out.

## Core Idea
An AI-augmented care platform for pediatric autism therapy (ABA, speech, occupational) that:
- Captures rich session notes from audio/video without burdening therapists
- Provides parents transparent visibility into progress
- Coordinates multi-disciplinary care teams

## Tech Stack
- **Vertex AI** (foundation models for transcription, summarization, structured note generation)
- **Gemini** (likely, for multimodal session understanding)
- Speech-to-text + speaker diarization
- Web/mobile portal for therapists, parents, supervisors
- Secure session recording infrastructure

## Key Features
1. **Automatic session documentation** — therapy session audio → structured SOAP-style note + skill progress.
2. **Behavioral tracking** — auto-detect target behaviors (e.g., "pointed to object", "made eye contact") to track progress over weeks.
3. **Parent portal** — parents see session summaries, home practice suggestions, child's progress trajectory.
4. **Care team coordination** — speech, ABA, OT therapists share aligned records.
5. **Supervisor QA** — clinical leads review AI-generated notes; flag for retraining.

## Target Users
- Children with ASD and their families (LATAM)
- ABA therapists, speech-language pathologists, OTs
- Clinical supervisors / BCBAs
- Insurance/payer audit teams (Brazilian health plans require detailed session logs)

## Project Plan (if rebuilt)
1. **Recording capture** — secure in-clinic and tele-therapy session recording (HIPAA + LGPD compliant).
2. **STT + diarization** — separate therapist / child / parent speakers.
3. **Behavior extraction** — Gemini analyzes transcript + clinician's target-behavior list; outputs counts and qualitative notes.
4. **SOAP note generation** — structured note for billing + clinical record.
5. **Parent-facing summary** — plain-language progress note + activities for home practice.
6. **Compliance audit log** — full traceability of AI suggestions vs final clinician sign-off.

## Business Value
- Reduces therapist documentation burden (a major burnout driver)
- Better parent engagement → better outcomes
- Higher session billable rate (better-documented sessions)
- Differentiated offering in growing LATAM autism care market
