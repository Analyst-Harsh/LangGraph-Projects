from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI

# load env vars
load_dotenv()
model = ChatOpenAI(model="gpt-5-nano")


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def get_chat_output(state: ChatState):
    out = model.invoke(state["messages"])
    return {"messages": out}


checkpoint = InMemorySaver()
graph = StateGraph(ChatState)
graph.add_node("get_chat_output", get_chat_output)


graph.add_edge(START, "get_chat_output")
graph.add_edge("get_chat_output", END)

workflow = graph.compile(checkpointer=checkpoint)


all_checkpoints = list(checkpoint.list(None))
