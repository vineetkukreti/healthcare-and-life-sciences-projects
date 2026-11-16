# Orby — Digital Brain for Neurological Rehabilitation

## Overview
Orby is combining **AI** and **neurotechnology**, applying:
- Complex mathematical models
- **Google Cloud's IT resources**
- **Gemini**

…to create a **"digital brain"** that supports patients' rehabilitation, helping them **recover lost motor skills** and **reduce pain**.

## Core Idea
A neurotech + AI platform that models the patient's nervous system and uses that model to drive personalized stimulation, biofeedback, and rehabilitation protocols — for stroke survivors, spinal cord injury, chronic pain.

## Tech Stack
- **Google Cloud** (compute for large biological simulations)
- **Gemini** (clinician copilot + multimodal patient interaction)
- **Mathematical neural models** (computational neuroscience, possibly biophysically realistic neuron / network simulations)
- Wearable / clinic hardware for stimulation and biosignal capture (EMG, EEG)
- Mobile app for patient adherence

## Key Features
1. **Patient "digital brain"** — a personalized computational model of relevant motor / pain circuits.
2. **Adaptive rehab protocols** — model predicts which stimulation pattern or exercise will maximize recovery for *this* patient.
3. **Real-time biofeedback** — wearable EMG/EEG signals feed into the model; protocol adjusts within session.
4. **Clinician copilot** — Gemini explains the model's recommendation, lets PT/neurologist adjust parameters.
5. **Outcomes tracking** — quantified motor function recovery, pain VAS, return-to-function metrics.

## Target Users
- Stroke survivors in rehabilitation
- Spinal cord injury patients
- Chronic pain patients (especially neuropathic)
- Rehabilitation hospitals and clinics
- Physiotherapists and neurologists

## Project Plan (if rebuilt)
1. **Computational neuro model** — published motor cortex / spinal circuit models adapted to a patient's lesion / condition; runs on GCE/GKE.
2. **Hardware integration** — Bluetooth EMG sensors, TENS / FES stimulators, optional EEG headset.
3. **Personalization loop** — assimilate patient signals into the model parameters (Bayesian / ML-based).
4. **Protocol engine** — model-based optimization → suggested stimulation + exercise plan.
5. **Patient app** — guided sessions, gamified exercises, adherence tracking.
6. **Clinician dashboard** — model state, recommendations, override controls, outcomes.

## Business Value
- True precision rehab vs one-size-fits-all PT
- Reduces clinician time per patient (better targeting)
- Differentiated in a market that has been mostly hardware-only
- Strong scientific moat (computational models + clinical validation)
- Reimbursement pathway via rehabilitation CPT codes + outcomes-based contracts
