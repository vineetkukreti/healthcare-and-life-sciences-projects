# Freenome — Early Cancer Detection via AI + Blood Tests

## Overview
Freenome is creating **diagnostic tests** that help detect life-threatening diseases like **cancer** in the **earliest, most-treatable stages**. The approach combines:
- Latest in **multiomics science** (cfDNA, methylation, protein biomarkers)
- **AI/ML** for signal extraction
- The **ease of a standard blood draw**

## Core Idea
A multiomics liquid biopsy platform: a single blood test that, paired with deep learning, detects cancer years before symptoms — making early intervention possible.

## Tech Stack
- **Google Cloud Platform** (compute + storage for genomics)
- **Vertex AI** (training large-scale multiomics models)
- **Bioinformatics pipelines** — likely BWA, GATK, custom methylation callers
- **Deep learning** — transformer / CNN models on cfDNA fragment profiles
- BigQuery for clinical trial cohort analysis

## Key Features
1. **Multiomics signal capture** — cfDNA mutations, methylation, fragmentomics, protein biomarkers from a single tube of blood.
2. **AI classifier** — deep learning models distinguish cancer signal from background noise.
3. **Tissue of origin prediction** — identify likely cancer site (colon, lung, breast).
4. **Population screening readiness** — designed for asymptomatic at-risk screening (e.g., colorectal cancer screening).

## Target Users
- Primary care physicians (screening)
- Patients eligible for cancer screening (e.g., age 45+ for CRC)
- Payers (Medicare, commercial insurance for covered screening)

## Project Plan (if rebuilding the ML side)
1. **Sample → sequencing pipeline** — automated wet lab → FASTQ → aligned BAM on GCP.
2. **Feature extraction** — methylation patterns, fragment length distributions, end motifs.
3. **Model training** — multimodal deep learning (Vertex AI Training) across a large case-control cohort.
4. **Clinical validation** — prospective trials (e.g., PREEMPT-CRC for colorectal).
5. **Regulatory** — FDA PMA pathway; CLIA-certified lab operations.
6. **Reporting** — clinician-facing PDF report; EHR integration.

## Business Value
- Detects cancers earlier → much higher survival rates
- Non-invasive, scalable to population screening
- Backed by large clinical trials (10,000+ participants)
- Pipeline targets: CRC, lung, multi-cancer early detection (MCED)
