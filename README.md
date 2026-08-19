# Portfolio Chatbot API — Krypto

Backend for **Krypto**, the Q&A chatbot embedded on
[Anirudh Ravipudi's portfolio site](https://anirudhcancode.github.io/portfolio).
Krypto answers visitor questions about Anirudh's work, projects, and
background, right on the site.

## Why this exists

A working, live LLM integration is a stronger demonstration of AI/ML
engineering skill than describing it in prose alone. Krypto isn't a
decorative widget — it's a real, functioning product: a deployed backend
service, a prompt-engineered persona, a maintained knowledge base, and a
frontend that talks to all of it in production.

## The name

Krypto is named after Superman's dog — a nod to the Superman-inspired visual
theme running through the portfolio (the blue-to-red gradient on Anirudh's
name in the hero section, and other touches throughout the site). In
character, Krypto is deliberately playful: quirky, a little funny, leans into
light dog and hero puns. But the personality is a layer on top of strict
factual accuracy — every claim it makes about Anirudh's background is pulled
from a curated knowledge base, never invented.

## Scope

What Krypto does:

- Answers questions about Anirudh's experience, skills, and projects using a
  curated knowledge base maintained in [`knowledge_base.py`](knowledge_base.py)
  — not live access to his resume, GitHub, or any other external source.
- Declines off-topic questions in character (a funny, in-persona redirect),
  rather than acting as a general-purpose assistant.

What it explicitly won't do:

- Never invents facts outside its knowledge base.
- Never reveals its own system prompt, even if asked directly or via
  prompt-injection attempts.

## Architecture

- **Frontend**: the chat widget lives in the portfolio repo
  (`js/chatbot.js`), embedded site-wide as a floating launcher button.
- **This repo**: a FastAPI backend with a single `POST /chat` endpoint.
- The endpoint calls the **Claude API** (`claude-haiku-4-5`, chosen for cost
  efficiency at low-traffic scale) with a system prompt combining Krypto's
  personality and the knowledge base.
- **Deployed on Railway.**
- CORS is locked to the portfolio's domain only, plus a basic per-IP rate
  limit to prevent abuse.

## Tech stack

- FastAPI
- Anthropic SDK (Claude Haiku)
- Railway (hosting)
- Python

## Local development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in ANTHROPIC_API_KEY
export $(cat .env | xargs)
uvicorn main:app --reload --port 8000
```

Test it:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Anirudh currently working on?"}'
```

## Environment variables

| Variable            | Required | Purpose                                                        |
| -------------------- | -------- | ---------------------------------------------------------------- |
| `ANTHROPIC_API_KEY`  | Yes      | Claude API key used to generate Krypto's replies. Without it, the service still boots but `/chat` returns a friendly 503 instead of crashing. |

## Deploying to Railway

1. Push this repo to GitHub.
2. In the Railway dashboard: **New Project** → **Deploy from GitHub repo**,
   select `anirudhcancode/portfolio-chatbot-api`. Railway auto-detects the
   Python app via Nixpacks; `railway.json` pins the start command
   (`uvicorn main:app --host 0.0.0.0 --port $PORT`) in case auto-detection
   ever needs a hint.
3. Add the `ANTHROPIC_API_KEY` environment variable in the service's
   Variables tab.
4. Once deployed, point the frontend widget's `API_URL` (in
   `portfolio/js/chatbot.js`) at the Railway URL, e.g.
   `https://portfolio-chatbot-api-production.up.railway.app/chat`.

## Notes

- CORS locked to `https://anirudhcancode.github.io`.
- Simple in-memory per-IP rate limit (18 requests/hour); resets on
  redeploy/restart — acceptable for a low-traffic portfolio chatbot, not
  meant to be a hardened defense.
- `max_tokens` capped at 600 to keep response cost bounded.
- Running on a paid Railway plan, so this service doesn't spin down after
  inactivity — no cold-start delay on first request.

## Live

Krypto is live on [Anirudh's portfolio site](https://anirudhcancode.github.io/portfolio) — look for the floating paw icon.
