from pydantic import BaseModel

class ChatRequest(BaseModel):
    lead_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
    intent: str
    confidence: float
    next_action: str
    lead_score: int
    lead_status: str
