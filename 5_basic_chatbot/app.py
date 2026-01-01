import streamlit as st
from lang_chat import workflow
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

if "message_history" not in st.session_state:
    st.session_state.setdefault("message_history", [])

for message in st.session_state.get("message_history", []):
    with st.chat_message(message.type):
        st.write(message.content)


user_input = st.chat_input("Type your message here...")


if user_input:
    st.session_state.get("message_history", []).append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    messages: list[BaseMessage] = st.session_state.get("message_history", [])
    response = workflow.invoke({"messages": messages})
    st.session_state.get("message_history", []).append(AIMessage(content=response["ai_reply"]))
    with st.chat_message("ai"):
        st.write(response["ai_reply"])
