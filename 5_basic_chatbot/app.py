import streamlit as st
from lang_chat import workflow
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

if "message_history" not in st.session_state:
    st.session_state.setdefault("message_history", [])

for message in st.session_state.get("message_history", []):
    with st.chat_message(message.type):
        st.write(message.content)


# User char input
user_input = st.chat_input("Type your message here...")


if user_input:
    st.session_state.get("message_history", []).append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    messages: list[BaseMessage] = st.session_state.get("message_history", [])
    # stream the ai response to have chat gpt like feature
    message_stream = workflow.stream({"messages": messages}, stream_mode="messages")  # type: ignore

    with st.chat_message("ai"):
        ai_message = st.write_stream(message_chunk.content for message_chunk, _ in message_stream)  # type: ignore

    # add ai message in message history
    st.session_state.get("message_history", []).append(AIMessage(content=ai_message))
