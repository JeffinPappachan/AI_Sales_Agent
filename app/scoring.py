def score_lead(message_count, intent):
    score = 30 + message_count * 5

    if intent in ["pricing_inquiry", "demo_request"]:
        score += 30
    elif intent == "feature_inquiry":
        score += 20
    elif intent == "not_interested":
        score -= 40

    score = max(0, min(score, 100))

    status = "hot" if score >= 70 else "warm" if score >= 40 else "cold"
    return score, status
