# Pear Health Labs — Personalized AI Fitness & Prevention Platform

## Overview
Pear Health Labs is a **health and fitness AI platform** that develops **personalized interventions to prevent chronic conditions**. It powers:
- Recommendations
- Content search
- Dynamic audio coaching

Tech stack:
- **Vertex AI Voice Generation** (dynamic audio coaching)
- **Vector Search in BigQuery** (content recommendation / search)
- The engineering team uses **Gemini Code Assist** for productivity

## Core Idea
A B2B-friendly AI engine that turns generic workout / wellness content into highly personalized, real-time audio coaching experiences — helping insurers, employers, and fitness brands deliver prevention-grade health programs.

## Tech Stack
- **Vertex AI Voice Generation** (text → coaching audio, dynamic mid-workout)
- **Vector Search in BigQuery** (semantic search over content library)
- **Gemini** (program generation, personalization)
- **Gemini Code Assist** (developer productivity)
- Mobile + connected fitness device integrations

## Key Features
1. **Dynamic audio coaching** — the coach's words adapt in real time to the user's pace, heart rate, prior session, goals.
2. **Personalized program generation** — AI builds a multi-week training + recovery plan from user profile.
3. **Content search** — semantic search over thousands of workouts, mindfulness sessions, recipes.
4. **Prevention-focused** — programs designed around metabolic syndrome, MSK risk, cardiovascular risk.
5. **White-label platform** — insurers and fitness brands plug Pear's engine into their app.

## Target Users
- Health insurers offering fitness benefits
- Connected fitness brands needing AI personalization
- Employers with wellness programs
- Consumers seeking adaptive coaching

## Project Plan (if rebuilt)
1. **Content library + tags** — workouts, audio sessions, recipes; structured metadata.
2. **Vector index** — embed content; Vector Search in BigQuery for low-cost serving.
3. **User profile** — fitness level, conditions, goals, recent sessions, biometrics.
4. **Program engine** — Gemini generates weekly plan respecting recovery, progression.
5. **Real-time audio** — Vertex AI Voice Generation produces session audio; mid-workout adaptation based on heart rate / pace.
6. **B2B API** — partner integration: insurers/brands embed via SDK.

## Business Value
- Adaptive coaching → higher adherence vs static workout apps
- Vector Search in BigQuery → cheap, scalable recommendations
- B2B distribution scales without massive consumer marketing
- Prevention positioning fits payer value-based care contracts
