# Northwell Health — Agentic AI for Patient Experience & Clinical Workflows

## Overview
Northwell Health, **New York's largest health system**, leverages **agentic AI** built with:
- **Gemini Enterprise**
- **Gemini Models**

…to redefine the **patient experience** and optimize **clinical workflows**. The strategic goal is to bridge the gap between legacy systems (EHR, scheduling, billing) and modern AI-driven care, then **scale AI innovation across the enterprise**.

## Core Idea
Enterprise-grade agentic AI that runs across many legacy hospital systems — pulling data, executing actions, talking to patients and clinicians — without replacing the underlying infrastructure.

## Tech Stack
- **Gemini Enterprise** (governed AI workspace for staff)
- **Gemini Models** (reasoning, function calling, multimodal)
- **Vertex AI Agent Builder** (agent orchestration — implied)
- **Cloud Healthcare API** (FHIR adapter to Epic, Allscripts)
- BigQuery (data warehouse)
- MCP / custom tools for legacy system access

## Key Features
1. **Patient-facing agent** — natural-language scheduling, intake, results explanation, billing Q&A across Northwell's 21+ hospitals and hundreds of outpatient locations.
2. **Clinical workflow assistants** — agents that summarize charts, draft notes, surface relevant guidelines, prep for handoffs.
3. **Legacy system bridge** — agents call APIs to Epic, scheduling systems, payer portals; no rip-and-replace.
4. **Cross-enterprise scale** — central platform, many domain-specific agents (cardiology, oncology, ED, etc.).
5. **Governance** — audit, PHI handling, role-based access.

## Target Users
- 21M+ patients in Northwell's catchment
- ~85,000 employees
- Physicians, nurses, schedulers, call-center staff
- Health system executives tracking AI ROI

## Project Plan (enterprise architecture)
1. **Identity + access** — single sign-on, role-aware agents.
2. **FHIR data plane** — Cloud Healthcare API to unify data from Epic, Allscripts, lab systems.
3. **Core agent platform** — Gemini Enterprise + Agent Builder with shared tool library.
4. **Domain agents** — sequential rollout: scheduling agent → results agent → clinical summarization agent → revenue cycle agent.
5. **Evaluation** — clinical safety reviews, A/B tests vs current workflows.
6. **Governance** — model risk management, PHI logging, opt-out controls.

## Business Value
- Reduce clinician burnout (top operational priority)
- Patient experience differentiation in a competitive NYC market
- Scale without proportionally scaling labor costs
- Faster appointment access → revenue retention
- Reference architecture other US health systems will follow
