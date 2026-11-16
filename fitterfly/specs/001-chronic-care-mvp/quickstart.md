# Quickstart: Chronic Care MVP

## Goal

Run a local MVP that demonstrates:

- AI-assisted meal photo logging with user confirmation
- Personalized coaching with escalation for risky or low-confidence cases
- Support automation with human-review routing
- Personal and enterprise outcome reporting

## Planned Local Setup

```bash
cd /home/vineet/Desktop/projects/healthcare-and-life-sciences-projects/fitterfly

# Backend
cd backend
uv sync
uv run pytest
uv run uvicorn app.main:app --reload

# Frontend, in another terminal
cd ../frontend
npm install
npm run dev
```

## Verification Path

1. Open the frontend.
2. Create or select a demo user.
3. Submit a sample meal photo and correct the returned meal estimate.
4. Save the confirmed meal log.
5. Generate coaching guidance and verify risky situations create review cases.
6. Ask one routine support question and one complex support question.
7. View personal outcome trends and aggregate enterprise outcomes.

## MVP Notes

- AI providers start as deterministic mock adapters.
- Real Gemini/Vertex credentials are not required for the first runnable build.
- Any emergency, medication, diagnosis, or low-confidence advice must escalate.
