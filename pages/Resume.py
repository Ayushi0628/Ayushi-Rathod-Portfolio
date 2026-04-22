import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from styles import inject_css, sidebar

st.set_page_config(page_title="Resume | Ayushi Rathod", page_icon="📄", layout="wide")
inject_css()
sidebar()

st.markdown('<div class="eyebrow">✦ Curriculum Vitae</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">My <span>Resume</span>.</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

st.markdown("""
<div class="strip">
  <h3>📎 Download a PDF copy</h3>
  <p>
    Add <code style="background:rgba(255,255,255,0.1);padding:0.1rem 0.4rem;border-radius:4px;">Ayushi_Rathod_Resume.pdf</code>
    to the root of your project folder, then uncomment the download button block below in Resume.py.
    Recruiters love a one-click download!
  </p>
</div>
""", unsafe_allow_html=True)

# ── Uncomment once PDF is added to project root:
# with open("Ayushi_Rathod_Resume.pdf", "rb") as f:
#     st.download_button(
#         label="⬇️  Download Resume (PDF)",
#         data=f,
#         file_name="Ayushi_Rathod_Resume.pdf",
#         mime="application/pdf",
#         use_container_width=True,
#     )

st.markdown('<div class="sh">💼 Professional <span>Experience</span></div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
  <div class="card-title">Confidosoft Solutions — Vadodara, India</div>
  <div class="card-sub">Data Analyst &amp; Business Intelligence Associate</div>
  <div class="card-meta">📅 Jan 2023 – Jul 2024</div>
  <ul style="list-style:none;padding:0;margin:0;">
    <li style="font-size:.87rem;padding:.2rem 0 .2rem 1.2rem;position:relative;color:var(--ink2);line-height:1.65;">
      <span style="position:absolute;left:0;color:var(--accent);font-weight:700;">▸</span>
      Managed end-to-end data-processing workflows ensuring accuracy, integrity, and consistency across reports</li>
    <li style="font-size:.87rem;padding:.2rem 0 .2rem 1.2rem;position:relative;color:var(--ink2);line-height:1.65;">
      <span style="position:absolute;left:0;color:var(--accent);font-weight:700;">▸</span>
      Extracted, cleaned, and transformed large datasets using SQL, Python, and Power Query for analysis readiness</li>
    <li style="font-size:.87rem;padding:.2rem 0 .2rem 1.2rem;position:relative;color:var(--ink2);line-height:1.65;">
      <span style="position:absolute;left:0;color:var(--accent);font-weight:700;">▸</span>
      Developed Power BI dashboards with DAX to visualize KPIs, trends, and performance insights for stakeholders</li>
    <li style="font-size:.87rem;padding:.2rem 0 .2rem 1.2rem;position:relative;color:var(--ink2);line-height:1.65;">
      <span style="position:absolute;left:0;color:var(--accent);font-weight:700;">▸</span>
      Automated reporting workflows using VBA, Power Query, and Python — <strong>reducing manual effort by 40%</strong></li>
    <li style="font-size:.87rem;padding:.2rem 0 .2rem 1.2rem;position:relative;color:var(--ink2);line-height:1.65;">
      <span style="position:absolute;left:0;color:var(--accent);font-weight:700;">▸</span>
      Applied statistical analysis to identify patterns, trends, and drivers impacting business performance</li>
    <li style="font-size:.87rem;padding:.2rem 0 .2rem 1.2rem;position:relative;color:var(--ink2);line-height:1.65;">
      <span style="position:absolute;left:0;color:var(--accent);font-weight:700;">▸</span>
      Built reusable SQL queries and data models to standardize reporting and improve data reliability</li>
    <li style="font-size:.87rem;padding:.2rem 0 .2rem 1.2rem;position:relative;color:var(--ink2);line-height:1.65;">
      <span style="position:absolute;left:0;color:var(--accent);font-weight:700;">▸</span>
      <strong>Improved reporting turnaround time by 25%</strong> through process optimization and automation</li>
  </ul>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="sh">🎓 <span>Education</span></div>', unsafe_allow_html=True)
for school, degree, period, detail in [
    ("Northeastern University – Toronto, Canada",
     "Master of Professional Studies in Analytics",
     "Sep 2024 – Mar 2026 ✓ Completed",
     "Machine Learning · AI · Statistical Modeling · Data Visualization · Business Intelligence"),
    ("The Maharaja Sayajirao University of Baroda",
     "Master of Computer Applications (MCA)",
     "Jul 2021 – May 2023",
     "Advanced databases, software engineering, data structures, algorithms, full-stack development."),
    ("The Maharaja Sayajirao University of Baroda",
     "Bachelor of Science in Mathematics",
     "Jun 2018 – May 2021",
     "Statistics, calculus, linear algebra, probability theory, numerical methods."),
]:
    st.markdown(f"""
    <div class="card">
      <div class="card-title">{school}</div>
      <div class="card-sub">{degree}</div>
      <div class="card-meta">📅 {period}</div>
      <p>{detail}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="sh">⚙️ Technical <span>Skills</span></div>', unsafe_allow_html=True)
skill_cats = {
    "Programming & Data Analysis": ["Python (pandas)","R","SQL","Excel","VBA","Power Query M","Jupyter"],
    "Analytics & Reporting":        ["Data Processing","KPI Reporting","Trend Analysis","Data Integrity","Stakeholder Insights"],
    "Visualization":                ["Power BI (DAX)","Tableau","Excel Dashboards","Interactive Reporting"],
    "Statistics & ML":              ["Regression","Hypothesis Testing","XGBoost","Random Forest","SHAP","SMOTE"],
    "Data Management":              ["ETL Pipelines","Data Cleaning","MySQL","PostgreSQL","BigQuery","ERD Design"],
    "Automation & Cloud":           ["Power Automate","Power Apps","Git/GitHub","Azure","AWS"],
}
c1, c2 = st.columns(2, gap="large")
for i, (cat, tags) in enumerate(skill_cats.items()):
    with (c1 if i % 2 == 0 else c2):
        tags_html = "".join(f'<span class="tag" style="margin:.18rem;">{t}</span>' for t in tags)
        st.markdown(f"""
        <div style="margin-bottom:1.2rem;">
          <div style="font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--muted);margin-bottom:.4rem;">{cat}</div>
          {tags_html}
        </div>
        """, unsafe_allow_html=True)