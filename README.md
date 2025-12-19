# AI Sales Agent Backend 🤖📈

An AI-powered Sales Agent backend that interacts with potential customers, understands their intent, maintains conversation context, and assists sales teams by suggesting next best actions and lead scores.

This project was built as part of an **AI Developer Intern Evaluation Task** and demonstrates practical usage of **LLMs, backend APIs, prompt engineering, and business logic design**.

---

## 🚀 Features

- 💬 Chat API for interacting with sales leads
- 🧠 Intent detection (pricing, demo, features, follow-up, not interested)
- 🗂️ Conversation memory per lead (context-aware replies)
- 🤖 AI-generated responses using a **local LLM (Ollama)**
- 📊 Lead scoring (Hot / Warm / Cold)
- 🎯 Next best action suggestion for sales representatives
- 🔒 Privacy-first design (no cloud LLM dependency)

---

## 🧠 System Architecture

Client (Postman / UI)
↓
FastAPI Backend
↓
Intent Detection (Rule-based)
↓
Conversation Memory (SQLite)
↓
LLM Response Generation (Ollama)
↓
Lead Scoring + Next Action
↓
Structured JSON Response


---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **LLM:** Ollama (llama3.2:1b)
- **Database:** SQLite
- **Language:** Python 3.11+
- **API Testing:** Swagger UI / PowerShell

---

## 📂 Project Structure

ai-sales-agent/
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI entry point
│ ├── schemas.py # API request/response models
│ ├── intents.py # Intent detection logic
│ ├── memory.py # Conversation storage (SQLite)
│ ├── llm.py # Ollama LLM integration
│ └── scoring.py # Lead scoring logic
│
├── requirements.txt
└── README.md


---

## 🧩 Intent Detection

The system detects the following intents:

- `pricing_inquiry`
- `demo_request`
- `feature_inquiry`
- `follow_up`
- `not_interested`

### Design Choice
Intent detection is implemented using **rule-based logic** for:
- Reliability
- Speed
- Deterministic behavior

The LLM is used **only for response generation**, not decision-making.

---

## 🧠 LLM Usage & Prompt Design

- Model: `llama3.2:1b` (via Ollama)
- Runs fully **locally**
- Optimized prompt for small models
- Guardrails:
  - Polite
  - Concise
  - Sales-oriented
  - 1–2 sentence replies

### Why Ollama?
- No API cost
- No data leakage
- Offline support
- Demonstrates real-world deployment awareness

---

## 📊 Lead Scoring Logic

Leads are scored from **0–100** based on:
- Number of messages
- Detected intent
- Engagement level

| Score Range | Status |
|-----------|--------|
| 70–100 | Hot |
| 40–69 | Warm |
| 0–39 | Cold |

---

## 🔌 API Specification

### POST `/chat`

#### Request
```json
{
  "lead_id": "123",
  "message": "What is your pricing?"
}

{
  "reply": "Our pricing starts from ₹999 per month. Would you like a demo?",
  "intent": "pricing_inquiry",
  "confidence": 0.9,
  "next_action": "offer_demo",
  "lead_score": 60,
  "lead_status": "warm"
}
```
---
## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone <repo-url>
cd ai-sales-agent
```
### Create Virtual Environment
python -m venv myvenv
myvenv\Scripts\activate   # Windows

### Install Dependencies
```bash
pip install -r requirements.txt
```
### Start Ollama
```bash
ollama run llama3.2:1b
```
Keep this running in the background.

### Start FastAPI Serve
```bash
uvicorn app.main:app --reload
```

### Testing the API
```json
http://127.0.0.1:8000/docs

Invoke-RestMethod -Uri "http://127.0.0.1:8000/chat" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"lead_id":"123","message":"What is your pricing?"}'

```


---
