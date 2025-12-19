from typing import Annotated, TypedDict, List
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, SystemMessage

from app.brain import get_llm
from app.tools import get_tools

# --- 1. Define State ---
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

# --- 2. Build the Graph ---
async def build_graph():
    llm = get_llm()
    tools = await get_tools()
    
    # Bind tools to the LLM
    llm_with_tools = llm.bind_tools(tools)

    # Node: The Brain (Decides what to do)
    def reasoner(state: AgentState):
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

    # Node: The Feedback/Evaluator Loop
    def should_continue(state: AgentState):
        last_message = state["messages"][-1]
        # If the LLM returns tool_calls, go to "tools" node
        if last_message.tool_calls:
            return "tools"
        # Otherwise, stop
        return END

    # Define Graph
    workflow = StateGraph(AgentState)
    
    workflow.add_node("brain", reasoner)
    workflow.add_node("tools", ToolNode(tools)) # Prebuilt node to run tools

    workflow.add_edge(START, "brain")
    workflow.add_conditional_edges("brain", should_continue)
    workflow.add_edge("tools", "brain") # Loop back after action!

    return workflow.compile()
