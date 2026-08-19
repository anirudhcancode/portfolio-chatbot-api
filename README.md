# Portfolio Chatbot API — Krypto

Backend proxy for Krypto, the Q&A chatbot widget embedded on
[anirudhcancode.github.io/portfolio](https://anirudhcancode.github.io/portfolio).
Holds the Anthropic API key server-side so it's never exposed to the browser.

## What it does

A single `POST /chat` endpoint that takes a user message (plus optional short
conversation history), sends it to Claude (`claude-haiku-4-5`) with a system
prompt containing Krypto's persona and a factual knowledge base about
Anirudh's background/skills/projects, and returns the reply.

- CORS locked to `https://anirudhcancode.github.io`
- Simple in-memory per-IP rate limit (18 requests/hour)
- `max_tokens` capped at 600 to keep response cost bounded

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

## Deploying to Railway

1. Push this repo to GitHub.
2. In the Railway dashboard: **New Project** → **Deploy from GitHub repo**,
   select `anirudhcancode/portfolio-chatbot-api`. Railway auto-detects the
   Python app via Nixpacks; `railway.json` pins the start command
   (`uvicorn main:app --host 0.0.0.0 --port $PORT`) in case auto-detection
   ever needs a hint.
3. **Required:** add an environment variable `ANTHROPIC_API_KEY` with your
   Anthropic API key in the service's Variables tab. The service will return
   a friendly 503 on `/chat` until this is set — it never crashes on boot
   without it.
4. Once deployed, update the frontend widget's `API_URL` (in
   `portfolio/js/chatbot.js`) to point at the Railway URL, e.g.
   `https://portfolio-chatbot-api-production.up.railway.app/chat`.

## Notes

- Running on a paid Railway plan, so unlike Render's free tier this service
  doesn't spin down after inactivity — no cold-start delay on first request.
- Rate-limit state is in-memory and resets on redeploy/restart — acceptable
  for this use case (a low-traffic portfolio chatbot), not meant to be a
  hardened defense.
