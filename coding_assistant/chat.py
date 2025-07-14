from openai import OpenAI
import streamlit as st
import traceback
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="CodeBuddy: Your AI Coding Assistant", page_icon=":robot_face:")

st.title("🤖 CodeBuddy: Your AI Coding Assistant")

client = OpenAI()


# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## 💡 Try these example prompts")
    EXAMPLES = [
        "How do I reverse a list in Python?",
        "What is a lambda function?",
        "Write a for loop to print numbers 1-10.",
        "How do I read a file line by line in Python?",
    ]
    selected_example = st.selectbox("Select an example prompt:", [None] + EXAMPLES)
    st.markdown("---")
    language = st.radio("Programming language for answers", ["Python", "JavaScript", "C++", "Other"], index=0)
    st.markdown("---")
    st.markdown("### 🛠 Paste your error here for debugging help!")
    error_input = st.text_area("Error message (optional)", "")


# --- SYSTEM PROMPT DYNAMICALLY BASED ON SIDEBAR ---
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        f"You are CodeBuddy, a helpful AI coding assistant. "
        f"Answer all questions using {language} (unless user explicitly asks otherwise). "
        "You write concise, clear explanations. "
        "For code, use markdown triple backticks with proper syntax highlighting. "
        "If an error message is given, analyze and help fix it."
    )
}

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4.1"

if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

if "messages" not in st.session_state or st.session_state.get("selected_language") != language:
    # Reset on language switch
    st.session_state.messages = [SYSTEM_PROMPT]
    st.session_state["selected_language"] = language

# --- DISPLAY MESSAGE HISTORY ---
for i, message in enumerate(st.session_state.messages[1:]):  # don't display system
    with st.chat_message(message["role"]):
        # Detect if this message is an assistant code output
        if message["role"] == "assistant" and "```" in message["content"]:
            st.markdown(message["content"])
            # Optionally add 'execute' button for Python only (first code block)
            import re
            lang_match = re.search(r"```(\w+)?", message["content"])
            lang = lang_match.group(1) if lang_match else str()
            if lang.lower() == "python":
                code_blocks = re.findall(r"```python\n(.*?)```", message["content"], re.DOTALL)
                if code_blocks:
                    code = code_blocks[0]
                    # Key guarantees button is unique for each msg
                    exec_btn = st.button("▶️ Execute This Code", key=f"exec_{i}")
                    if exec_btn:
                        st.info("⚠️ Running code may be dangerous. Use for safe, simple snippets only!")
                        try:
                            # Redirect stdout (print) and capture locals
                            import io, contextlib
                            buf = io.StringIO()
                            with contextlib.redirect_stdout(buf):
                                local_vars = {}
                                exec(code, {'__builtins__': {}}, local_vars)  # Only allow limited builtins
                            result = buf.getvalue()
                            st.success(f"Output:\n\n{result if result else 'No output.'}")
                        except Exception as e:
                            st.error(f"Execution Error:\n\n{traceback.format_exc()}")
        else:
            st.markdown(message["content"])

# --- PROMPT HANDLING ---
# Pre-fill chat input with example if chosen


if st.sidebar.button("Send this example ▶️", disabled=not selected_example):
    st.session_state["pending_prompt"] = selected_example

# Always show input box unless servicing pending button click
if "pending_prompt" in st.session_state:
    prompt = st.session_state.pop("pending_prompt")
else:
    prompt = st.chat_input("Ask me a programming question!")

if prompt or error_input:
    # Append user prompt
    user_input = prompt if prompt else ""
    if error_input.strip():
        user_input += f"\n\nHere's the error I'm seeing:\n{error_input}"
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
