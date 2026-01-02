import streamlit as st
from lang_chat import workflow, all_checkpoints
from langchain_core.messages import HumanMessage
from utils import get_message_history, generate_new_chat, get_AI_stream_message


if "all_threads" not in st.session_state:
    st.session_state.setdefault("all_threads", all_checkpoints or [])

if "thread_id" not in st.session_state:
    generate_new_chat()

# ---------------------------------------------------
# Sidebar

st.sidebar.title("Chat Wise")


if st.sidebar.button("New Chat", type="primary"):
    generate_new_chat()
    st.session_state["message_history"] = []

st.sidebar.header("Active Chats")

all_threads = st.session_state.get("all_threads", [])
for thread in all_threads:
    if st.sidebar.button(str(thread), key=str(thread)):
        st.session_state["message_history"] = get_message_history(thread)

# --------------------------------------------------------

for message in st.session_state.get("message_history", []):
    with st.chat_message(message.type):
        st.write(message.content)


# User char input
user_input = st.chat_input("Type your message here...")
thread_id = str(st.session_state.get("thread_id"))

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    CONFIG = {"configurable": {"thread_id": thread_id}}
    # stream the ai response to have chat gpt like feature
    message_stream = workflow.stream(
        {"messages": [HumanMessage(content=user_input)]}, config=CONFIG, stream_mode="messages"
    )  # type: ignore

    with st.chat_message("ai"):
        ai_message = st.write_stream(get_AI_stream_message(message_stream))

    workflow_state = workflow.get_state(config=CONFIG)
    # add ai message in message history
    st.session_state.update({"message_history": workflow_state.values["messages"]})
