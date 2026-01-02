from uuid import uuid4
from lang_chat import workflow
import streamlit as st
from langchain.messages import AIMessage, ToolMessage


def generate_thread_id():
    return uuid4()


def generate_new_chat():
    new_thread_id = generate_thread_id()
    st.session_state["thread_id"] = new_thread_id
    st.session_state["all_threads"].append(new_thread_id)


def get_message_history(thread_id: str):
    workflow_state = workflow.get_state({"configurable": {"thread_id": thread_id}}).values

    messages = workflow_state.get("messages", [])
    return list(
        filter(
            lambda message: not (isinstance(message, ToolMessage) or message.content == ""),
            messages,
        )
    )


def get_AI_stream_message(message_stream):
    for message_chunk, _ in message_stream:
        if isinstance(message_chunk, AIMessage):
            yield message_chunk.content
