from fastapi import FastAPI

from app.schemas import ChatRequest
from app.intents import detect_intent
from app.memory import save_message, get_last_messages
from app.llm import generate_reply
from app.scoring import score_lead

app = FastAPI(title="AI Sales Agent")

@app.post("/chat")
def chat(request: ChatRequest):
    intent, confidence = detect_intent(request.message)

    context = get_last_messages(request.lead_id)

    reply = generate_reply(context, request.message)

    save_message(request.lead_id, "user", request.message)
    save_message(request.lead_id, "assistant", reply)

    lead_score, lead_status = score_lead(len(context), intent)

    next_action_map = {
        "pricing_inquiry": "offer_demo",
        "demo_request": "schedule_demo",
        "feature_inquiry": "share_features",
        "follow_up": "assign_sales_rep",
        "not_interested": "close_lead"
    }

    return {
        "reply": reply,
        "intent": intent,
        "confidence": confidence,
        "next_action": next_action_map.get(intent, "nurture"),
        "lead_score": lead_score,
        "lead_status": lead_status
    }
