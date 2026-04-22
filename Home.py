import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from styles import inject_css, sidebar

st.set_page_config(
    page_title="Ayushi Rathod | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
inject_css()
sidebar()

# ── Hero
st.markdown('<div class="eyebrow">✦ Open to full-time &amp; co-op roles — Toronto &amp; Remote</div>', unsafe_allow_html=True)
st.markdown("""
<h1 class="page-title">
  Turning data<br>into <em>decisions</em>.
</h1>
<p class="lead">
  Data Analyst &amp; BI Associate with 1.5+ years of experience building
  Power BI dashboards, ML pipelines, and automated reporting systems that
  deliver measurable business impact.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tag-row">
  <span class="tag">Python · SQL</span>
  <span class="tag">Power BI · Tableau</span>
  <span class="tag">Machine Learning</span>
  <span class="tag">ETL Pipelines</span>
  <span class="tag">BigQuery · Azure</span>
  <span class="tag accent">🟢 Open to Work</span>
</div>
""", unsafe_allow_html=True)

# ── Stats
st.markdown("""
<div class="stat-row">
  <div class="stat-card"><div class="stat-num">1.5+</div><div class="stat-label">Years Experience</div></div>
  <div class="stat-card"><div class="stat-num">40%</div><div class="stat-label">Reporting Effort Saved</div></div>
  <div class="stat-card"><div class="stat-num">87%</div><div class="stat-label">ML Model Accuracy</div></div>
  <div class="stat-card"><div class="stat-num">400K+</div><div class="stat-label">Records Processed</div></div>
  <div class="stat-card"><div class="stat-num">25%</div><div class="stat-label">Faster Turnaround</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── What I Do
st.markdown('<div class="sh">What I <span>Do</span></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
services = [
    ("📊", "Analytics & BI", "Power BI dashboards with DAX, KPI tracking, and stakeholder-ready insight reports."),
    ("🤖", "Machine Learning", "Classification, regression, and risk-scoring models using scikit-learn, XGBoost & SHAP."),
    ("⚙️", "Data Engineering", "ETL pipelines, SQL data models, BigQuery, and workflow automation with Python & VBA."),
]
for col, (icon, title, desc) in zip([col1, col2, col3], services):
    with col:
        st.markdown(f"""
        <div class="card" style="min-height:150px;padding-left:1.9rem;">
          <div style="font-size:1.8rem;margin-bottom:0.6rem;">{icon}</div>
          <div class="card-title">{title}</div>
          <p style="font-size:0.84rem;line-height:1.6;color:var(--ink2);margin-top:0.4rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Education
st.markdown("""
<div class="strip">
  <h3>🎓 MPS in Analytics — Northeastern University, Toronto</h3>
  <p>
    Completed a Master of Professional Studies in Analytics (Sep 2024 – Mar 2026),
    with coursework in Machine Learning, AI, Statistical Modeling, Data Visualization,
    and Business Intelligence. Actively seeking full-time data roles in the GTA and beyond.
  </p>
</div>
""", unsafe_allow_html=True)

# ── Quick links
st.markdown('<div class="sh" style="margin-top:2.5rem;">Explore the <span>Portfolio</span></div>', unsafe_allow_html=True)
ql1, ql2, ql3 = st.columns(3)
with ql1:
    st.page_link("pages/Projects.py", label="🗂️ View Projects")
    st.caption("3 end-to-end data & ML projects with metrics")
with ql2:
    st.page_link("pages/Skills.py", label="⚙️ See Skills")
    st.caption("Proficiency bars, tool badges, skill categories")
with ql3:
    st.page_link("pages/Contact.py", label="✉️ Get in Touch")
    st.caption("Available immediately — drop me a message")