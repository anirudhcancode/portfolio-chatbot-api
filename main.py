import os
import time
from collections import defaultdict, deque
from typing import Dict, List, Optional

import anthropic
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from system_prompt import SYSTEM_PROMPT

MODEL = "claude-haiku-4-5"
MAX_TOKENS = 600
MAX_HISTORY_MESSAGES = 10

RATE_LIMIT_MAX_REQUESTS = 18
RATE_LIMIT_WINDOW_SECONDS = 60 * 60

ALLOWED_ORIGINS = [
    "https://anirudhcancode.github.io",
]

app = FastAPI(title="Portfolio Chatbot API (Krypto)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["Content-Type"],
)

_api_key = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=_api_key) if _api_key else None

# Simple in-memory sliding-window rate limiter, keyed by client IP.
# Resets on redeploy/restart -- that's fine for this use case.
_request_log: Dict[str, deque] = defaultdict(deque)


def is_rate_limited(ip: str) -> bool:
    now = time.time()
    q = _request_log[ip]
    while q and now - q[0] > RATE_LIMIT_WINDOW_SECONDS:
        q.popleft()
    if len(q) >= RATE_LIMIT_MAX_REQUESTS:
        return True
    q.append(now)
    return False


def get_client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


class ChatMessage(BaseModel):
    role: str
    content: str = Field(..., max_length=2000)


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)
    history: Optional[List[ChatMessage]] = None


class ChatResponse(BaseModel):
    reply: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, request: Request):
    if client is None:
        raise HTTPException(
            status_code=503,
            detail="Krypto is napping right now (server isn't configured yet). Try again later.",
        )

    client_ip = get_client_ip(request)
    if is_rate_limited(client_ip):
        raise HTTPException(
            status_code=429,
            detail="Whoa, slow down! Krypto needs a water break -- try again in a bit.",
        )

    message = req.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    messages = []
    if req.history:
        for h in req.history[-MAX_HISTORY_MESSAGES:]:
            if h.role in ("user", "assistant") and h.content.strip():
                messages.append({"role": h.role, "content": h.content.strip()})
    messages.append({"role": "user", "content": message})

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=messages,
        )
        reply_text = "".join(
            block.text for block in response.content if block.type == "text"
        ).strip()
    except anthropic.APIStatusError:
        raise HTTPException(
            status_code=502,
            detail="Krypto's leash got tangled talking to the mothership. Try again in a moment.",
        )
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Something spooked Krypto. Try again in a moment.",
        )

    if not reply_text:
        reply_text = "Ruff, I lost my train of thought there. Could you ask that again?"

    return ChatResponse(reply=reply_text)
