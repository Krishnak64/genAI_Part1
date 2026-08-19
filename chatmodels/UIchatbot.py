from dotenv import load_dotenv
import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    AIMessage,
    SystemMessage,
    HumanMessage
)

# Load environment variables
load_dotenv()

# Initialize Model
model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9,
    max_tokens=20
)

# Streamlit page configuration
st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Personality Chatbot")

# Choose AI mode
st.sidebar.title("Choose AI Mode")

choice = st.sidebar.radio(
    "Select Response Style",
    [
        "Angry Mode 😡",
        "Funny Mode 😂"
    ]
)

# Set system personality
if choice == "Angry Mode 😡":
    mode = "you are an angry agent. you response aggressively and impatiently"

else:
    mode = "you are a very funny model. you response with humor and jokes"


# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Reset system prompt if user changes mode
if st.session_state.get("current_mode") != mode:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]
    st.session_state.current_mode = mode


# Display previous messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)


# User input
prompt = st.chat_input("Enter your message...")

if prompt:

    # Exit condition
    if prompt == "0":
        st.stop()

    # Show user message
    with st.chat_message("user"):
        st.write(prompt)

    # Add user message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )


    # Get response
    response = model.invoke(
        st.session_state.messages
    )

    # Store AI response
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )


    # Display AI response
    with st.chat_message("assistant"):
        st.write(response.content)