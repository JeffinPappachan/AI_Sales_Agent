import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"

SYSTEM_PROMPT = """
You are a professional AI sales assistant.
Be polite, concise, and helpful.
Reply in 1-2 sentences.
Encourage demo or follow-up when relevant.
"""

def generate_reply(context, user_message):
    history = ""
    for role, msg in context:
        history += f"{role}: {msg}\n"

    prompt = f"""{SYSTEM_PROMPT}

Conversation:
{history}
User: {user_message}
Assistant:"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.4
            }
        }
    )

    return response.json()["response"].strip()
