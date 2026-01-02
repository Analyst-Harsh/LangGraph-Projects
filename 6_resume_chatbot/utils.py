from uuid import uuid4
from lang_chat import workflow
import streamlit as st


def generate_thread_id():
    return uuid4()


def generate_new_chat():
    new_thread_id = generate_thread_id()
    st.session_state["thread_id"] = new_thread_id
    st.session_state["all_threads"].append(new_thread_id)


def get_message_history(thread_id: str):
    return workflow.get_state({"configurable": {"thread_id": thread_id}}).values.get("messages", [])
