from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="AlgoBuddy: AI Algorithm Visualizer", page_icon="🧮")

st.title("🧮 AlgoBuddy: AI Algorithm Visualizer")

client = OpenAI()


# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## 💡 Try these example prompts")
    EXAMPLES = [
        "Explain bubble sort visually.",
        "Explain selection sort step by step.",
        "Visualize how Dijkstra's algorithm finds the shortest path.",
        "Show how Breadth-First Search explores a graph.",
        "Demonstrate quicksort with an example list.",
    ]
    selected_example = st.selectbox("Select an example prompt:",
                                    [None] + EXAMPLES,
                                    key="example_prompt")

# --- SYSTEM PROMPT DYNAMICALLY BASED ON SIDEBAR ---
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are an AI expert at visually explaining algorithms. "
        "For every question, deliver an intuitive, step-wise explanation with diagrams (using text-art or markdown where suitable), "
        "flowcharts (use text-art, provide the best one possible), or analogies—avoid code snippets unless the user explicitly asks for code. "
        "Whenever possible, walk through at least one complete example or dataset. "
        "Be concise, engaging, and clear; focus on *how* the algorithm does what it does."
    )
}

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4.1"

if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

if "messages" not in st.session_state:
    # Reset on language switch
    st.session_state.messages = [SYSTEM_PROMPT]

# --- DISPLAY MESSAGE HISTORY ---
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=False)

if st.sidebar.button("Send this example ▶️", disabled=not selected_example):
    st.session_state["pending_prompt"] = selected_example

# Always show input box unless servicing pending button click
chat_input_text = st.chat_input("Ask me any algorithm to explain!")

prompt = None
if "pending_prompt" in st.session_state:
    prompt = st.session_state.pop("pending_prompt")
else:
    prompt = chat_input_text

if prompt:
    # Append user prompt
    user_input = prompt if prompt else ""

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=st.session_state.messages,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
