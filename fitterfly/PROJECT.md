# Fitterfly — AI-Powered Chronic Disease Management

## Overview
Fitterfly, an India-based mobile health app, helps users manage chronic diseases like **diabetes** and **obesity**. The platform uses:
- **Gemini Flash**
- **Vertex AI**

…to reduce **meal logging times by 80%** and **automate 90% of support queries**. The AI-powered platform delivers precision coaching to **30,000+ users** and enterprise clients including major insurers in India and UAE.

## Core Idea
A digital therapeutics (DTx) platform for chronic metabolic conditions:
- AI-powered food recognition for effortless meal logging
- Personalized precision coaching from human coaches + AI
- Automated triage and support

## Tech Stack
- **Gemini Flash** (fast multimodal — meal photo → food + calories + macros)
- **Vertex AI** (precision coaching recommendations, support agent)
- Mobile app (iOS/Android)
- Wearables integration (CGM, fitness trackers)
- BigQuery for outcomes analytics

## Key Features
1. **Meal photo logging** — snap a photo, Gemini Flash identifies the dish, portion, macros. 80% time reduction vs manual logging.
2. **Precision coaching** — AI generates personalized diet, exercise, sleep advice based on the user's HbA1c trajectory, CGM data, lifestyle.
3. **Support automation** — 90% of queries answered by AI; complex ones routed to human coaches/dietitians.
4. **Outcome tracking** — clinical-grade tracking of HbA1c reduction, weight loss for insurer reporting.
5. **Enterprise dashboard** — for insurers (HDFC ERGO, etc.) and employers tracking population health.

## Target Users
- Type 2 diabetes patients (India primary, UAE expanding)
- People managing obesity, PCOS, thyroid
- Insurers offering chronic care benefits
- Corporate wellness programs

## Project Plan (if rebuilt)
1. **Food vision model** — Gemini Flash fine-tuned / prompted with Indian cuisine taxonomy.
2. **CGM + wearable integration** — Abbott Libre, Apple Health, Google Fit.
3. **Coaching engine** — Vertex AI model trained on outcomes data → personalized next-best-action.
4. **Support agent** — RAG over FAQs, clinical protocols; escalation to human coaches.
5. **Insurer reporting** — anonymized outcome dashboards.

## Business Value
- 80% reduction in friction (meal logging) → higher adherence
- 90% support automation → scalable to millions of users
- Measurable HbA1c reduction → insurer reimbursement
- Enterprise B2B2C distribution model
