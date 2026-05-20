from typing import TypedDict,Literal
class SupportState(TypedDict):
    review:str
    sentiment:Literal["Positive","Negative"]
    diagnosis:str
    response:str
    