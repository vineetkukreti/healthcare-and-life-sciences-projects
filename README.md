# Healthcare & Life Sciences Projects

A working catalog of 14 real-world healthcare/life-sciences AI projects (primarily Google Cloud / Vertex AI / Gemini-powered) that I'm studying as reference architectures. Each subfolder contains a `PROJECT.md` describing what the project does, its tech stack, key features, target users, an implementation plan, and business value.

## Projects

| # | Project | Core focus | Key Google Cloud tech |
|---|---------|-----------|------------------------|
| 1 | [Bennie Health](./bennie-health/PROJECT.md) | Employee benefits insights | Vertex AI |
| 2 | [CitiusTech](./citiustech/PROJECT.md) | Patient-specialist matching & workflow automation | Vertex AI, Vertex AI Search |
| 3 | [Clivi](./clivi/PROJECT.md) | Chronic disease continuous monitoring (LATAM) | Gen AI on Google Cloud |
| 4 | [CVS Health — Health100](./cvs-health-health100/PROJECT.md) | AI-native consumer health partner | Gemini, Cloud Healthcare API, BigQuery |
| 5 | [Family Vision Care of Ponca City](./family-vision-care/PROJECT.md) | Plain-language patient emails | Gemini in Gmail |
| 6 | [Fitterfly](./fitterfly/PROJECT.md) | Diabetes / obesity coaching app | Gemini Flash, Vertex AI |
| 7 | [Freenome](./freenome/PROJECT.md) | Early cancer detection from blood | Google Cloud + AI/ML |
| 8 | [Genial Care](./genial-care/PROJECT.md) | Autism therapy session AI documentation | Vertex AI |
| 9 | [Manipal Hospitals](./manipal-hospitals/PROJECT.md) | AI-powered ePharmacy | Vertex AI, Gemini |
| 10 | [Moody Month](./moody-month/PROJECT.md) | Hormone-aware women's wellness | Cloud Run, Gemini 2.5 Pro, BigQuery |
| 11 | [Northwell Health](./northwell-health/PROJECT.md) | Enterprise agentic AI for hospitals | Gemini Enterprise, Gemini |
| 12 | [Orby](./orby/PROJECT.md) | Digital brain for rehabilitation | Google Cloud + Gemini + math models |
| 13 | [Pear Health Labs](./pear-health-labs/PROJECT.md) | Personalized fitness/prevention coaching | Vertex AI Voice, Vector Search in BigQuery |
| 14 | [Quest Diagnostics](./quest-diagnostics/PROJECT.md) | Lab-results chat assistant | LLM + secure portal |

## How to read each PROJECT.md

Every PROJECT.md follows the same structure:

1. **Overview** — what the project is, verbatim-grounded in the source description.
2. **Core Idea** — the one-paragraph version.
3. **Tech Stack** — Google Cloud / AI services + supporting infra.
4. **Key Features** — what the system actually does for the user.
5. **Target Users** — who it serves.
6. **Project Plan** — a buildable, step-by-step rebuild plan (the part useful for me as a builder).
7. **Business Value** — the "so what" — why this is worth building.

## Themes across these projects

- **Patient-facing conversational AI** is the most common pattern (CVS, Clivi, Quest, Manipal, Northwell).
- **Multimodal Gemini for documentation/extraction** appears repeatedly (Manipal prescriptions, Genial Care sessions, Fitterfly meal photos).
- **Cloud Healthcare API + FHIR** is the standard data-plane substrate for enterprise (CVS, Northwell, CitiusTech).
- **Cost-efficient consumer AI** is shown well by Moody Month — Cloud Run + scale-to-zero is the trick.
- **Prevention / chronic disease** is the dominant disease focus; oncology screening is the moonshot (Freenome).

## Fitterfly MVP prototype

`fitterfly/` also contains a small work-in-progress rebuild prototype (chronic care MVP, spec in `fitterfly/specs/001-chronic-care-mvp`):

- `backend/` – FastAPI + SQLAlchemy (Python >= 3.13, managed with `uv`), pytest tests. Config via `.env` (see `backend/.env.example`: `DATABASE_URL`, `APP_ENV`, `MEAL_VISION_PROVIDER`, `OLLAMA_BASE_URL`, `OLLAMA_MODEL`).
- `frontend/` – React + TypeScript + Vite. Config: `VITE_API_BASE_URL` (see `frontend/.env.example`).

```bash
cd fitterfly/backend && uv sync && uv run uvicorn app.main:app --reload
cd fitterfly/frontend && npm install && npm run dev
```

Dependencies (`node_modules`, `.venv`), build output and the local SQLite database are not committed.
