# Clivi — Generative AI Patient Monitoring Platform

## Overview
Clivi, a Mexican health startup, has created a **gen AI platform with Google Cloud** that enables **personalized and continuous monitoring** of its patients to offer tailored responses, improve volume and capacity of care, and reduce complications.

## Core Idea
A continuous-care platform for chronic disease patients (diabetes, obesity, hypertension, thyroid) that combines:
- Always-on patient monitoring via WhatsApp/mobile
- AI-driven personalized care plans
- Scalable virtual clinic model

## Tech Stack
- **Google Cloud** (foundational infrastructure)
- **Vertex AI / Gemini** (generative responses to patient messages)
- WhatsApp Business API (primary patient interface)
- Patient data store (likely Firestore + BigQuery)
- Clinician dashboard

## Key Features
1. **Continuous symptom tracking** — patients report glucose readings, weight, symptoms via chat; AI summarizes and flags anomalies.
2. **Personalized AI responses** — tailored coaching messages based on the patient's plan, history, recent metrics.
3. **Clinician escalation** — gen AI handles routine questions; human clinicians intervene for red flags.
4. **Care plan optimization** — AI suggests medication / lifestyle changes for clinician review.

## Target Users
- Patients with chronic conditions in LATAM (initial focus: Mexico)
- Insurers and employers offering chronic disease management

## Project Plan (if rebuilt)
1. **Conversational layer** — WhatsApp integration with Gemini for patient interaction.
2. **Patient memory** — long-term per-patient context (vector store + structured profile).
3. **Triage agent** — classify messages → answer / alert clinician / book appointment.
4. **Care plan engine** — generate personalized weekly plans; track adherence.
5. **Clinician console** — review AI suggestions, override, sign off.

## Business Value
- 10× clinician capacity (one clinician supervises hundreds of patients)
- Lower complication rates → reduced hospitalization costs
- Better adherence through always-on coaching
