# CitiusTech — Healthcare AI Search & Workflow Automation

## Overview
CitiusTech, a global healthcare technology services firm, uses **Google Cloud** to improve patient experience, reduce administrative burden on clinical staff, and save costs for healthcare systems. The flagship product is an **AI search solution built on Vertex AI** that efficiently connects patients with the right specialists and automates critical clinical workflows.

## Core Idea
An enterprise healthcare AI platform that combines:
- Intelligent search across clinical and provider data
- Workflow automation for admin-heavy tasks
- Patient-provider matching using semantic understanding

## Tech Stack
- **Google Cloud Platform** (foundational)
- **Vertex AI** (search + agent orchestration)
- **Vertex AI Search** (enterprise semantic search)
- BigQuery for clinical data
- Cloud Healthcare API for FHIR/HL7 ingestion

## Key Features
1. **Provider matching search** — patient describes symptoms/needs in natural language, system returns ranked specialists (geography, insurance, specialty, availability).
2. **Clinical workflow automation** — agentic AI handles prior auth, referral routing, appointment scheduling.
3. **Knowledge retrieval** — clinicians query patient charts, guidelines, and policies in natural language.
4. **Cost analytics** — surface savings from automated workflows.

## Target Users
- Hospitals and health systems
- Payers and integrated delivery networks
- Healthcare BPOs

## Project Plan (if rebuilt)
1. **FHIR data layer** — ingest provider directory, patient data via Cloud Healthcare API.
2. **Vector index** — embed provider profiles, specialties, conditions in Vertex AI Search.
3. **Query understanding** — Gemini parses patient intent → structured search filters.
4. **Workflow agents** — LangGraph/Vertex Agents for referral, prior-auth automation.
5. **Audit + compliance** — HIPAA logging, role-based access.

## Business Value
- Faster patient → specialist matching
- 30-50% reduction in admin staff time
- Better patient satisfaction (NPS)
