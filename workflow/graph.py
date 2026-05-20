from langgraph.graph import (StateGraph,START,END)
from workflow.state import SupportState
from workflow.node import (analyze_sentiment,positive_response,diagnose_issue,auto_reply,escalation_response)
from workflow.router import (check_sentiment,check_urgency)


graph = StateGraph(SupportState)


graph.add_node("analyze_sentiment",analyze_sentiment)
graph.add_node("positive_response",positive_response)
graph.add_node("diagnose_issue",diagnose_issue)
graph.add_node("auto_reply",auto_reply)
graph.add_node("escalation_response",escalation_response)


graph.add_edge(START,"analyze_sentiment")
graph.add_conditional_edges("analyze_sentiment",check_sentiment)
graph.add_conditional_edges("diagnose_issue",check_urgency)
graph.add_edge("positive_response",END)
graph.add_edge("auto_reply",END)
graph.add_edge("escalation_response",END)

workflow = graph.compile()