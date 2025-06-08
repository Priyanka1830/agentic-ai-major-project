import streamlit as st
from crew import AgenticAiCrew
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# Function to run the crew
def run_crew(topic):
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }

    try:
        # Get the crew result
        result = AgenticAiCrew().crew().kickoff(inputs=inputs)

        # Parse JSON and extract the "raw" content
        raw_content = result.tasks_output[2].raw  # Adjust this if needed to get the desired output

        # Return the clean newsletter content
        return raw_content
    except Exception as e:
        return f"An error occurred while running the crew: {e}"

# Streamlit UI
st.title("AI Crew Newsletter Generator")
st.write("This application allows you to generate a newsletter based on a research topic.")

# Input for the topic
topic = st.text_input("Enter a topic for the newsletter:")

# Button to run the crew
if st.button("Generate Newsletter"):
    if topic:
        result = run_crew(topic)
        st.write("Newsletter Result:")
        st.write(result)
    else:
        st.error("Please enter a valid topic.")
