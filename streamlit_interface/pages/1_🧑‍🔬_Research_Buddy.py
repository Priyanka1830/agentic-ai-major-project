import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from research_buddy.crew import ResearchBuddy
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="ResearchBuddy: Research Article Generator", page_icon="🧑‍🔬")

# Streamlit UI
st.title("🧑‍🔬 ResearchBuddy: Research Article Generator")
st.write("This application helps you to write a detailed research article based on a given topic.")

# Input for the topic
topic = st.text_input("Enter a topic for the Research:")


# Function to run the crew
def run_crew(topic):
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }

    try:
        # Get the crew result
        result = ResearchBuddy().crew().kickoff(inputs=inputs)

        # Parse JSON and extract the "raw" content
        raw_content = result.tasks_output[2].raw  # Adjust this if needed to get the desired output

        # Return the clean research content
        return raw_content
    except Exception as e:
        return f"An error occurred while running the crew: {e}"


# Button to run the crew
if st.button("Generate Research Article"):
    if topic:
        result = run_crew(topic)
        st.write("Research Article Result:")
        st.write(result)
    else:
        st.error("Please enter a valid topic.")
