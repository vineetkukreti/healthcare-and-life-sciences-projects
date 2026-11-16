# Bennie Health — Employee Health Benefits Platform

## Overview
Bennie Health uses **Vertex AI** to power an innovative employee health benefits platform, providing actionable insights and streamlining data management for employees and HR teams.

## Core Idea
An AI-driven benefits administration platform that:
- Delivers personalized benefits insights to employees
- Streamlines benefits data management for HR teams
- Enhances decision-making with actionable analytics

## Tech Stack
- **Google Vertex AI** (core AI/ML platform)
- LLM-based insight generation
- Benefits data warehouse (likely BigQuery)
- Web/mobile front-end for employee + HR access

## Key Features
1. **Personalized recommendations** — surface the right benefits to each employee based on demographics, claims history, life events.
2. **HR dashboard** — aggregated, anonymized analytics on benefits utilization and engagement.
3. **AI assistant** — conversational Q&A: "What's covered for fertility?", "How do I add my spouse?"
4. **Predictive insights** — flag underutilized benefits, predict open-enrollment churn.

## Target Users
- Mid-market and enterprise employers
- Benefits brokers
- HR leaders

## Project Plan (if rebuilt)
1. **Data ingestion** — connect benefits providers, claims data, payroll/HRIS.
2. **Knowledge base** — RAG index over plan documents, SPDs, benefits FAQs.
3. **Recommendation engine** — Vertex AI model for personalized benefits matching.
4. **Conversational UI** — Gemini-powered chat for employees.
5. **HR analytics** — BigQuery + Looker dashboards.

## Business Value
- Reduces HR administrative burden
- Drives employee engagement with benefits
- Improves benefits ROI through better utilization
