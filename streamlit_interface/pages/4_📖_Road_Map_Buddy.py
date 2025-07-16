import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from roadmap_planner.crew import RoadMapBuddy
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="RoadMapBuddy: Roadmap Generator", layout="wide", page_icon="📖")

# Streamlit UI
st.title("🧑‍🔬 RoadMapBuddy: Roadmap Generator")
st.write("This application will generate a detailed roadmap to learn and master any given topic.")

# Input for the topic
topic = st.text_input("Enter a topic Master:")
number_of_days = st.text_input("Enter the number of days you can dedicate for preparation:")

# Function to run the crew
def run_crew(topic):
    inputs = {
        'topic': topic,
        'number_of_days': number_of_days
    }

    try:
        # Get the crew result
        result = RoadMapBuddy().crew().kickoff(inputs=inputs)

        # Parse JSON and extract the "raw" content
        raw_content = result.tasks_output[2].raw  # Adjust this if needed to get the desired output

        # # Return the clean research content
        return raw_content
    except Exception as e:
        return f"An error occurred while running the crew: {e}"


# Button to run the crew
if st.button("Generate a Detailed Roadmap"):
    if topic:
        result = run_crew(topic)
        st.write("A detailed Road Map is generated.")
        st.write(result)
    else:
        st.error("Please enter a valid topic or number of days.")
