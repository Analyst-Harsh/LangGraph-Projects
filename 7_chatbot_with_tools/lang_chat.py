from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

# load env vars
load_dotenv()


# define all tools
@tool
def addition_tool(a: int, b: int):
    """
    Tool which can perform addition of two numbers
    """
    return a + b


model = ChatOpenAI(model="gpt-5-nano")
tools = [addition_tool]
model_with_tools = model.bind_tools(tools)


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def get_chat_output(state: ChatState):
    out = model_with_tools.invoke(state["messages"])
    return {"messages": out}


checkpoint = InMemorySaver()
graph = StateGraph(ChatState)
graph.add_node("get_chat_output", get_chat_output)
graph.add_node("tool_node", ToolNode(tools=tools))


graph.add_edge(START, "get_chat_output")
graph.add_conditional_edges(
    "get_chat_output", tools_condition, {"tools": "tool_node", "__end__": END}
)
graph.add_edge("tool_node", "get_chat_output")


workflow = graph.compile(checkpointer=checkpoint)


all_checkpoints = list(checkpoint.list(None))
