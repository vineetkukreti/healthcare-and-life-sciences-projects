# Manipal Hospitals — AI-Powered ePharmacy App

## Overview
Manipal Hospitals, one of India's largest healthcare providers serving **7M+ patients annually**, uses **Vertex AI** and **Gemini models** to power its **ePharmacy app**. The app lets patients:
- View prescriptions
- Order medications
- Arrange home delivery after consultations

The AI platform reduces average **order time from 15 minutes → < 5 minutes** while achieving **99% accuracy**.

## Core Idea
A post-discharge / post-consultation medication fulfillment workflow that turns a paper or e-prescription into a fulfilled order through computer vision + LLM understanding, with delivery logistics built-in.

## Tech Stack
- **Vertex AI** (orchestration, vision)
- **Gemini models** (multimodal — prescription image → structured medication list)
- Pharmacy inventory & ordering system
- Mobile app (patient-facing)
- Delivery logistics integration

## Key Features
1. **Prescription scan** — patient uploads prescription image; Gemini extracts drug name, dose, frequency, duration.
2. **Drug matching** — fuzzy-match handwritten/typed drug names to Manipal pharmacy SKUs (99% accuracy).
3. **Auto-order** — pre-fills cart; patient confirms; payment + delivery scheduled.
4. **Refill prediction** — AI predicts when chronic meds need refilling; sends timely reminders.
5. **Drug interaction checks** — cross-check with patient's existing meds.

## Target Users
- 7M+ Manipal patients annually
- Post-OPD consultation patients
- Chronic medication patients (refills)
- Caregivers ordering for elderly relatives

## Project Plan (if rebuilt)
1. **Prescription OCR + parsing** — Gemini multimodal: image → JSON of structured drugs.
2. **Catalog match** — vector search over Manipal pharmacy SKU catalog with brand/generic mapping.
3. **Clinical safety** — drug-drug interaction module (RxNorm / Indian formulary).
4. **Order workflow** — cart → payment → pharmacy fulfillment → delivery partner API.
5. **Patient app** — order tracking, refill reminders, dose reminders.

## Business Value
- 3× faster order placement (15 min → < 5 min)
- 99% accuracy reduces dispensing errors
- Captures pharmacy revenue (otherwise lost to outside chemists)
- Better medication adherence → better clinical outcomes for chronic patients
- Differentiator vs PharmEasy, Tata 1mg, NetMeds
