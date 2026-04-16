import streamlit as st

st.set_page_config(page_title="Resume | Ayushi Rathod", page_icon="📄", layout="wide")

st.title("Resume")

st.write("You can view or download my resume using the button below.")

st.link_button("Download Resume", "https://drive.google.com/")

st.subheader("Profile Summary")
st.write(
    """
    Data Analyst with a Master’s in Analytics (Applied Machine Intelligence) and a strong foundation in Python,
    SQL, Power BI, R, and Excel. Skilled in data analysis, dashboard development, reporting, and translating
    complex datasets into actionable business insights.
    """
)

st.subheader("Target Roles")
st.write("- Data Analyst")
st.write("- Business Intelligence Analyst")
st.write("- Reporting Analyst")
st.write("- Entry-Level Data Scientist")
st.write("- Analytics Intern / Co-op")