# Moody Month — Hormone-Aware Wellness Tracker

## Overview
Moody Month, a daily health and wellness tracker used by **100,000+ women**, built its AI-powered platform on:
- **Cloud Run**
- **Gemini 2.5 Pro**
- **BigQuery**

…delivering **personalized hormone forecasts** while keeping sensitive health data secure. The company famously serves 100,000 users a month for just **£1,000** with its scalable Google Cloud microservices infrastructure.

## Core Idea
A wellness app that maps mood, energy, focus, and physical symptoms to the menstrual / hormonal cycle, and uses AI to forecast each user's daily state — turning hormones from "mystery" into an actionable signal.

## Tech Stack
- **Cloud Run** (stateless microservices, scales to zero)
- **Gemini 2.5 Pro** (personalized daily forecasts and insights)
- **BigQuery** (anonymized longitudinal user data, model training)
- **Firestore / Cloud SQL** (per-user state)
- Mobile app

## Key Features
1. **Daily hormone forecast** — AI predicts mood, energy, productivity given cycle phase + history + recent logs.
2. **Symptom logging** — quick taps for mood, energy, cravings, pain, sleep.
3. **Personalized content** — AI suggests workouts, recipes, breathwork matched to cycle phase.
4. **Cycle prediction** — period and ovulation forecasting tuned per user.
5. **Privacy-first** — sensitive cycle data kept secure (especially important post-Roe).

## Target Users
- Women tracking menstrual cycles
- Women in perimenopause
- Athletes and high-performers cycle-syncing training
- Anyone seeking hormone-aware wellness

## Project Plan (cost-efficient rebuild)
1. **Cloud Run microservices** — separate services for logging, forecast, content, auth. Scale-to-zero is key to the £1,000/mo cost.
2. **Per-user state** — Firestore for current cycle state.
3. **Forecast model** — Gemini 2.5 Pro prompt with user's recent log + cycle phase → daily forecast JSON.
4. **Content engine** — RAG over a curated wellness content library, filtered by phase.
5. **BigQuery analytics** — anonymized cohort training data; cycle pattern research.
6. **Security** — encryption at rest, no third-party tracking on sensitive cycle data.

## Business Value
- Ultra-low infra cost — £0.01 per user/month
- High retention via daily-use loop
- Premium subscription model
- B2B opportunities (employer wellness, women's health insurers)
- Differentiated from Flo / Clue by hormone-state AI forecasting
