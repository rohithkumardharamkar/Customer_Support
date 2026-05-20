from workflow.state import SupportState
from workflow.schemas import (SentimentSchema,DiagnosisSchema)

from services.llm import llm

sentiment_model = llm.with_structured_output(SentimentSchema)
diagnosis_model = llm.with_structured_output(DiagnosisSchema)


def analyze_sentiment(state: SupportState):
    prompt = f"""
    Analyze the sentiment
    of this customer review.
    Review:
    {state['review']}
    """
    result = sentiment_model.invoke(prompt)
    return {"sentiment": result.sentiment}


def positive_response(state):
    prompt = f"""
    Write a warm thank-you message
    for this positive customer review.
    Review:
    {state['review']}
    Also politely ask the customer
    to leave feedback on our website.
    """
    response = llm.invoke(prompt).content
    return {"response": response}

def diagnose_issue(state: SupportState):
    prompt = f"""
    Diagnose this customer complaint.
    Review:
    {state['review']}
    Detect:
    - issue_type
    - urgency
    - tone
    """
    diagnosis = diagnosis_model.invoke(prompt)
    return {"diagnosis": diagnosis.model_dump()}



def auto_reply(state: SupportState):
    diagnosis = state["diagnosis"]
    prompt = f"""
    You are an AI support assistant.
    Issue Type:
    {diagnosis['issue_type']}
    Urgency:
    {diagnosis['urgency']}
    Tone:
    {diagnosis['tone']}
    Generate a professional
    customer support response.
    """
    response = llm.invoke(prompt).content
    return {"response": response}



def escalation_response(state: SupportState):
    diagnosis = state["diagnosis"]
    prompt = f"""
    This customer issue
    has HIGH urgency.
    Issue Type:
    {diagnosis['issue_type']}
    Generate:
    - apology message
    - escalation message
    - reassurance response
    """
    response = llm.invoke(prompt).content
    return {"response": response}