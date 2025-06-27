python -m venv .venv
.venv\Scripts\activate

pip install uv
uv tool install crewai

# The below installation of crewai using
# pip is requrired for running with streamlit
pip install crewai

pip install streamlit

# Run below command for setting up a new crewai project only
# crewai create crew <your_project_name>

# Run the below command before running the crew:
crewai install

# running a crew:
crewai run

# Running streamlit app
streamlit run app.py