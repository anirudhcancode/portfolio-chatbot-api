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
- `max_tokens` capped at 350 to keep response cost bounded

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

## Deploying to Render

1. Push this repo to GitHub.
2. In the Render dashboard: **New +** → **Blueprint**, point it at this repo
   (it will pick up `render.yaml` automatically). Or **New +** → **Web
   Service** manually with:
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. **Required:** add an environment variable `ANTHROPIC_API_KEY` with your
   Anthropic API key in the Render service's Environment tab. The service
   will return a friendly 503 on `/chat` until this is set — it never
   crashes on boot without it.
4. Once deployed, update the frontend widget's `API_URL` (in
   `portfolio/js/chatbot.js`) to point at the Render URL, e.g.
   `https://portfolio-chatbot-api.onrender.com/chat`.

## Notes

- Render's free tier spins the service down after inactivity; the first
  request after idle may take ~30-50s to wake it up. The frontend widget
  shows a loading state to cover this.
- Rate-limit state is in-memory and resets on redeploy/restart — acceptable
  for this use case (a low-traffic portfolio chatbot), not meant to be a
  hardened defense.
