import streamlit as st

st.set_page_config(page_title="Resume | Ayushi Rathod", page_icon="📄", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');
:root { --ink:#0d0d0d; --paper:#f5f2ec; --accent:#c8522a; --muted:#6b6660; --border:#ddd9d2; --card:#ffffff; }
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; background-color:var(--paper); color:var(--ink); }
#MainMenu, footer, header { visibility:hidden; }
.block-container { padding:2.5rem 3rem 4rem 3rem; max-width:960px; }
section[data-testid="stSidebar"] { background:var(--ink); border-right:3px solid var(--accent); }
section[data-testid="stSidebar"] * { color:#f5f2ec !important; }
.page-title { font-family:'Syne',sans-serif; font-size:2.6rem; font-weight:800; letter-spacing:-0.03em; }
.page-title span { color:var(--accent); }
.page-eyebrow { font-size:.78rem; text-transform:uppercase; letter-spacing:.15em; color:var(--accent); font-weight:600; margin-bottom:.4rem; }
.divider { border:none; border-top:1.5px solid var(--border); margin:2rem 0; }
.section-heading { font-family:'Syne',sans-serif; font-size:1.3rem; font-weight:700; letter-spacing:-0.02em; margin:2rem 0 1rem 0; padding-bottom:.5rem; border-bottom:2px solid var(--border); }
.section-heading span { color:var(--accent); }
.res-block { background:var(--card); border:1.5px solid var(--border); border-radius:10px; padding:1.4rem 1.8rem; margin-bottom:1rem; position:relative; overflow:hidden; }
.res-block::before { content:''; position:absolute; top:0; left:0; width:3px; height:100%; background:var(--accent); }
.res-title { font-family:'Syne',sans-serif; font-weight:700; font-size:1rem; }
.res-sub { font-size:0.82rem; color:var(--accent); font-weight:600; margin:.15rem 0; }
.res-date { font-size:0.78rem; color:var(--muted); margin-bottom:.6rem; }
.res-bullets { list-style:none; padding:0; margin:0; }
.res-bullets li { font-size:0.86rem; padding:.2rem 0 .2rem 1.2rem; position:relative; color:#3a3632; line-height:1.6; }
.res-bullets li::before { content:'▸'; position:absolute; left:0; color:var(--accent); }
.tag { display:inline-block; background:var(--ink); color:#f5f2ec; font-size:.72rem; font-weight:500; padding:.28rem .7rem; border-radius:100px; margin:.15rem; }
.download-note { background:var(--ink); color:#f5f2ec; border-radius:10px; padding:1.2rem 1.6rem; margin-bottom:1.5rem; font-size:.9rem; }
.download-note strong { color:var(--accent); }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div style="font-family:Syne,sans-serif;font-size:1.3rem;font-weight:800;border-bottom:1px solid #333;padding-bottom:.75rem;margin-bottom:1rem;">Ayushi Rathod</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:.78rem;text-transform:uppercase;letter-spacing:.12em;color:#c8522a;font-weight:500;">Data Analyst · BI Associate</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.page_link("Home.py",            label="🏠 Home")
    st.page_link("pages/About.py",     label="👤 About")
    st.page_link("pages/Skills.py",    label="⚙️ Skills")
    st.page_link("pages/Projects.py",  label="🗂️ Projects")
    st.page_link("pages/Resume.py",    label="📄 Resume")
    st.page_link("pages/Contact.py",   label="✉️ Contact")

st.markdown('<div class="page-eyebrow">Curriculum Vitae</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">My <span>Resume</span>.</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# # ── Download tip ──────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="download-note">
#   📎 Want a PDF copy? Add your resume file to the project folder and enable a download button
#   below using <strong>st.download_button()</strong>. Recruiters love a one-click download!
# </div>
# """, unsafe_allow_html=True)

# Uncomment this block once you add your PDF to the project:
with open("Ayushi_Rathod_Resume.pdf", "rb") as f:
     st.download_button(
         label="⬇️  Download Resume (PDF)",
         data=f,
         file_name="Ayushi_Rathod__Resume.pdf",
         mime="application/pdf"
     )

# ── Experience ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">💼 Professional <span>Experience</span></div>', unsafe_allow_html=True)

st.markdown("""
<div class="res-block">
  <div class="res-title">Confidosoft Solutions — Vadodara, India</div>
  <div class="res-sub">Data Analyst & Business Intelligence Associate</div>
  <div class="res-date">📅 Jan 2023 – Jul 2024</div>
  <ul class="res-bullets">
    <li>Managed end-to-end data-processing workflows ensuring data accuracy, integrity, and consistency across reports</li>
    <li>Extracted, cleaned, and transformed large datasets using SQL, Python, and Power Query for analysis readiness</li>
    <li>Developed Power BI dashboards with DAX to visualize KPIs, trends, and performance insights for stakeholders</li>
    <li>Automated reporting workflows using VBA, Power Query, and Python — <strong>reducing manual effort by 40%</strong></li>
    <li>Applied statistical analysis to identify patterns, trends, and drivers impacting business performance</li>
    <li>Collaborated with cross-functional teams to gather requirements and align insights with business objectives</li>
    <li>Built reusable SQL queries and data models to standardize reporting and improve data reliability</li>
    <li>Documented data definitions, transformations, and workflows to support governance and auditability</li>
    <li><strong>Improved reporting turnaround time by 25%</strong> through process optimization and automation</li>
  </ul>
</div>
""", unsafe_allow_html=True)

# ── Education ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🎓 <span>Education</span></div>', unsafe_allow_html=True)

edu_items = [
    ("Northeastern University – Toronto, Canada",
     "Master of Professional Studies in Analytics",
     "Sep 2024 – Mar 2026",
     "Machine Learning · AI · Statistical Modeling · Data Visualization · Business Intelligence"),
    ("The Maharaja Sayajirao University of Baroda",
     "Master of Computer Applications (MCA)",
     "Jul 2021 – May 2023",
     "Advanced databases, software engineering, data structures, algorithms, full-stack development."),
    ("The Maharaja Sayajirao University of Baroda",
     "Bachelor of Science in Mathematics",
     "Jun 2018 – May 2021",
     "Statistics, calculus, linear algebra, probability theory, numerical methods."),
]
for school, degree, period, detail in edu_items:
    st.markdown(f"""
    <div class="res-block">
      <div class="res-title">{school}</div>
      <div class="res-sub">{degree}</div>
      <div class="res-date">📅 {period}</div>
      <p style="font-size:.86rem;color:#3a3632;margin:0;">{detail}</p>
    </div>
    """, unsafe_allow_html=True)

# ── Skills ────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">⚙️ Technical <span>Skills</span></div>', unsafe_allow_html=True)

skill_cats = {
    "Programming & Data Analysis": ["Python (pandas)", "R", "SQL", "Excel", "VBA", "Power Query M", "Jupyter Notebooks"],
    "Analytics & Reporting":        ["Data Processing", "KPI Reporting", "Trend Analysis", "Data Integrity", "Stakeholder Insights"],
    "Visualization":                ["Power BI (DAX)", "Tableau", "Excel Dashboards", "Interactive Reporting"],
    "Statistics & ML":              ["Regression", "Hypothesis Testing", "Forecasting", "XGBoost", "Random Forest", "SHAP"],
    "Data Management":              ["ETL Pipelines", "Data Cleaning", "MySQL", "PostgreSQL", "BigQuery", "ERD Design"],
    "Automation & Cloud":           ["Power Automate", "Power Apps", "Git/GitHub", "Azure", "AWS"],
}

col1, col2 = st.columns(2, gap="large")
for i, (cat, tags) in enumerate(skill_cats.items()):
    target = col1 if i % 2 == 0 else col2
    with target:
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
        st.markdown(f"""
        <div style="margin-bottom:1rem;">
          <div style="font-size:.8rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin-bottom:.4rem;">{cat}</div>
          {tags_html}
        </div>
        """, unsafe_allow_html=True)