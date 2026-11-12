"""Chiamata all'API OpenAI (Chat Completions) con la sola libreria standard."""
import json
import os
import ssl
import urllib.error
import urllib.request

API_URL = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/") + "/chat/completions"
MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
TIMEOUT = float(os.environ.get("OPENAI_TIMEOUT", "40"))


class LLMUnavailable(Exception):
    """Il servizio AI non risponde, va in errore o non e' configurato."""


def has_key():
    return bool(os.environ.get("OPENAI_API_KEY"))


def chat_json(system, messages, temperature=0.1):
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise LLMUnavailable("OPENAI_API_KEY non impostata")
    body = {
        "model": MODEL,
        "temperature": temperature,
        "response_format": {"type": "json_object"},
        "messages": [{"role": "system", "content": system}] + messages,
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ssl.create_default_context()) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:300]
        raise LLMUnavailable(f"HTTP {e.code}: {detail}") from e
    except Exception as e:  # rete assente, timeout, DNS...
        raise LLMUnavailable(str(e)) from e
    try:
        content = data["choices"][0]["message"]["content"]
        return json.loads(content)
    except Exception as e:
        raise LLMUnavailable(f"Risposta non valida dal modello: {e}") from e
