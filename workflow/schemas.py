from pydantic import BaseModel
from typing import Literal

class SentimentSchema(BaseModel):
    sentiment: Literal["Positive", "Negative"]

class DiagnosisSchema(BaseModel):
    issue_type:Literal['Bug','Payment','Login','Performance','UX','Support','Other']
    urgency:Literal['low','medium','high']
    tone:Literal['angry','frustrated','calm','disappointed']

