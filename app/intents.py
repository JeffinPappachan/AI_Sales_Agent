def detect_intent(message: str):
    msg = message.lower()

    if any(word in msg for word in ["price", "pricing", "cost", "plan"]):
        return "pricing_inquiry", 0.9

    if any(word in msg for word in ["demo", "trial", "walkthrough"]):
        return "demo_request", 0.9

    if any(word in msg for word in ["feature", "capability", "do you have"]):
        return "feature_inquiry", 0.85

    if any(word in msg for word in ["call", "contact", "reach me"]):
        return "follow_up", 0.85

    if any(word in msg for word in ["not interested", "no thanks", "stop"]):
        return "not_interested", 0.95

    return "unknown", 0.6
