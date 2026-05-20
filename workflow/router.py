from workflow.state import SupportState
from typing import Literal

def check_sentiment(state: SupportState) -> Literal["positive_response","diagnose_issue"]:
    if state["sentiment"] == "positive":
        return "positive_response"
    return "diagnose_issue"

def check_urgency(state: SupportState) -> Literal["escalation_response","auto_reply"]:
    urgency = state["diagnosis"]["urgency"]
    if urgency == "high":
        return "escalation_response"
    return "auto_reply"