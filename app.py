import streamlit as st

st.set_page_config(page_title="Ayushi Rathod Portfolio", layout="wide")

st.title("Ayushi Rathod")
st.subheader("Data Analyst · Master’s in Analytics (Applied Machine Intelligence)")

st.write("""
I am a data analyst focused on turning raw data into actionable insights using Python, SQL, Power BI, R, and machine learning.
I am actively seeking full-time roles and internship opportunities in Data Analytics, BI, Reporting, and Entry-Level Data Science.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("LinkedIn", "www.linkedin.com/in/ayushi-rathod-data-analyst")
with col2:
    st.link_button("GitHub", "https://github.com/Ayushi0628")
with col3:
    st.link_button("Resume", "https://your-resume-link.com")

st.header("Projects")

st.subheader("Customer Churn Analysis")
st.write("Built a predictive analytics workflow using Python and SQL to identify customer churn drivers and support retention strategies.")

st.subheader("Power BI KPI Dashboard")
st.write("Designed an interactive dashboard to track KPIs, automate reporting, and improve decision-making visibility.")

st.subheader("Workforce Planning Model")
st.write("Developed an analytics-based staffing model using Excel, SQL, and BI tools to improve operational planning.")

st.header("Skills")
st.write("Python, SQL, Power BI, R, Excel, Tableau, Machine Learning, Data Cleaning, Data Visualization, Reporting, Statistics")

st.header("Contact")
st.write("Email: your-email@example.com")