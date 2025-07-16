import streamlit as st

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 AI Study Buddy")
st.markdown(
    """
    Welcome to **AI Study Buddy** - your multipurpose, AI-powered assistant for all things Computer Science!
    
    Whether you're tackling a tough research topic or debugging your latest code assignment,
    our smart AI agents have your back.
    """
)
st.markdown("---")
st.header("🧑‍🔬 Research Buddy")
st.markdown(
    """
    **Research Buddy** gives you a guided research experience:
    
    - **Researcher Agent:** Gathers in-depth, up-to-date information on any topic.
    - **Research Article Editor Agent:** Refines and checks for clarity, citations, and structure.
    - **Research Article Writer Agent:** Drafts a detailed research article for you.
    
    👉 _Find this tool in the sidebar/pages!_
    """
)
st.markdown("---")
st.header("👨‍💻 Code Buddy")
st.markdown(
    """
    **Code Buddy** is your coding co-pilot:
    
    - **Code Snippets:** Quickly generate code in Python, JavaScript, and more.
    - **Debugging:** Get step-by-step help fixing errors.
    - **Learning:** Ask questions about algorithms, syntax, or best practices.
    
    👉 _Accessible from the sidebar/pages!_ (Requires your OpenAI API key.)
    """
)

st.markdown("---")
st.markdown(
    """
    ### 🚀 Get Started
    
    - Use the navigation menu on the left to choose a feature.
    - Want more tools? [Suggest ideas or contribute on GitHub!](https://github.com/)
    
    ---
    > _AI Study Buddy is open-source. Built with ❤️ using [Streamlit](https://streamlit.io)._
    """
)