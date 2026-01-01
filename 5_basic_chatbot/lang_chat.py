from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage

# load env vars(contains open api key)
load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")


class ChatState(TypedDict):
    messages: list[BaseMessage]
    ai_reply: str


def get_chat_reply(state: ChatState):
    response = model.invoke(state["messages"])
    return {"ai_reply": response.content}


graph = StateGraph(ChatState)
graph.add_node("basic_chatbot", get_chat_reply)

graph.add_edge(START, "basic_chatbot")
graph.add_edge("basic_chatbot", END)

workflow = graph.compile()
