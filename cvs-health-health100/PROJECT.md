# CVS Health — Health100: AI-Native Consumer Engagement Platform

## Overview
CVS Health, a leading health solutions company, is building a world of health around every consumer. Through **Health100**, a new health technology services subsidiary, CVS Health is launching an **AI-native consumer engagement platform** powered by:
- Google Cloud's **Gemini models**
- **Cloud Healthcare API**
- **BigQuery**

The goal: deliver a real-time, omni-channel, agentic AI experience that gives consumers an **always-on personal health care partner**.

## Core Idea
A unified, agentic AI front-door for every CVS consumer interaction — pharmacy, MinuteClinic, Aetna insurance, Caremark — that proactively engages, anticipates needs, and orchestrates care.

## Tech Stack
- **Gemini models** (reasoning, conversational AI)
- **Cloud Healthcare API** (FHIR-compliant clinical data layer)
- **BigQuery** (consumer + claims data warehouse)
- **Vertex AI Agent Builder** (likely, for agentic orchestration)
- Omni-channel: mobile app, web, voice, in-store kiosks, SMS

## Key Features
1. **Personal health partner** — always-on agent that knows your meds, claims, conditions, upcoming appointments.
2. **Proactive nudges** — "Refill your statin, eligible for $0 copay"; "MinuteClinic has 3pm slots for your sinus issue."
3. **Cross-business orchestration** — single agent spans pharmacy + clinic + insurance + PBM.
4. **Real-time omni-channel** — same conversation state across app, voice, in-store.
5. **Agentic workflows** — books appointments, switches meds, submits prior auth on behalf of the consumer.

## Target Users
- ~100M+ CVS Health consumers (largest US health touchpoint)
- Pharmacy customers, Aetna members, MinuteClinic patients

## Project Plan (if rebuilt at scale)
1. **Unified consumer graph** — fuse pharmacy, claims, clinical, demographic data in BigQuery via Cloud Healthcare API.
2. **Identity + auth** — single consumer identity across all CVS touchpoints.
3. **Core agent** — Gemini-powered planner with tools: refill, schedule, claim status, eligibility.
4. **Channel adapters** — mobile, voice (IVR), web, SMS, in-store kiosk — shared session state.
5. **Safety + compliance** — HIPAA logging, clinical guardrails, escalation to pharmacists/clinicians.
6. **Personalization** — long-term memory per consumer; preference learning.

## Business Value
- Differentiated consumer experience (vs Amazon Pharmacy, Walgreens, Walmart Health)
- Higher member retention for Aetna
- Increased pharmacy adherence
- Reduced cost of service (deflect calls, automate routine tasks)
- Cross-sell across CVS lines of business
