import streamlit as st
from crew import ProductPriceResearcherCrew
from dotenv import load_dotenv
load_dotenv()

# Function to run the crew
def run_crew(brand, model, my_price):
    inputs = {
        "brand": brand,
        "model": model,
        "my_price": my_price
    }

    try:
        # Get the crew result
        result = ProductPriceResearcherCrew().crew().kickoff(inputs=inputs)

        # Parse JSON and extract the "raw" content
        raw_content = result.tasks_output[2].raw  # Adjust this if needed to get the desired output

        return raw_content

    except Exception as e:
        return f"An error occurred while running the crew: {e}"

# Streamlit UI
st.title("AI Product Price Researcher")
st.write("Given a brand, model and price of an cosumable, it gives suggestions to either lower or higher the price to match with the competitors.")

# Input for the topic
brand = st.text_input("Enter a brand:")
model = st.text_input("Enter a model:")
my_price = st.text_input("Enter your current price:")

# Button to run the crew
if st.button("Suggest best selling price"):
    if brand and model and my_price:
        result = run_crew(brand, model, my_price)
        st.write("Suggestion:")
        st.write(result)
    else:
        st.error("Please enter a valid brand, model and price.")
