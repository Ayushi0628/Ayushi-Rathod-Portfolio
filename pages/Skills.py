import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from styles import inject_css, sidebar

st.set_page_config(page_title="Skills | Ayushi Rathod", page_icon="⚙️", layout="wide")
inject_css()
sidebar()

st.markdown('<div class="eyebrow">✦ Technical Expertise</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">Tools that <span>get results</span>.</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Proficiency bars
st.markdown('<div class="sh">Core <span>Proficiencies</span></div>', unsafe_allow_html=True)

skills = [
    ("Power BI  (DAX, Data Modelling)", 92),
    ("Python  (pandas, scikit-learn)", 90),
    ("SQL  (MySQL, PostgreSQL, BigQuery)", 88),
    ("Statistical Analysis", 84),
    ("Machine Learning & SHAP", 82),
    ("Excel / VBA / Power Query", 85),
    ("Tableau", 78),
    ("ETL Pipelines & Data Engineering", 76),
    ("Azure / AWS / Git", 68),
]

col_l, col_r = st.columns(2, gap="large")
for i, (name, pct) in enumerate(skills):
    with (col_l if i % 2 == 0 else col_r):
        st.markdown(f"""
        <div class="prof-row">
          <div class="prof-label">
            <span>{name}</span>
            <span class="prof-pct">{pct}%</span>
          </div>
          <div class="prof-bg"><div class="prof-fill" style="width:{pct}%;"></div></div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Skill categories
st.markdown('<div class="sh">Skill <span>Categories</span></div>', unsafe_allow_html=True)

groups = [
    ("📊 Analytics & Reporting",  ["Data Processing","KPI Reporting","Trend Analysis","Data Integrity","Stakeholder Insights","Ad-hoc Analysis"]),
    ("🗄️ Data Management",        ["ETL Pipelines","Data Cleaning","SQL (MySQL · PostgreSQL)","BigQuery","Data Validation","ERD Design"]),
    ("📈 Visualization",           ["Power BI","DAX","Tableau","Excel Dashboards","Interactive Reporting","SHAP Plots"]),
    ("🧮 Statistics & ML",         ["Regression","Hypothesis Testing","Forecasting","XGBoost","Random Forest","SMOTE","SHAP"]),
    ("⚙️ Automation & Cloud",      ["Power Automate","Power Apps","Git / GitHub","Azure","AWS","Jupyter Notebooks"]),
    ("💻 Programming",             ["Python","R","SQL","VBA","Power Query M","pandas","scikit-learn"]),
]

c1, c2 = st.columns(2, gap="large")
for i, (title, tags) in enumerate(groups):
    with (c1 if i % 2 == 0 else c2):
        tag_html = "".join(f'<span class="tag" style="margin:0.18rem;">{t}</span>' for t in tags)
        st.markdown(f"""
        <div class="skill-group">
          <div class="skill-group-title">{title}</div>
          <div>{tag_html}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Tools
st.markdown('<div class="sh">🛠️ Tools &amp; <span>Platforms</span></div>', unsafe_allow_html=True)
tools = [
    ("📊","Power BI"),("🐍","Python"),("🗃️","PostgreSQL"),("📋","Excel"),
    ("☁️","BigQuery"),("🔷","Azure"),("📦","AWS"),("📉","Tableau"),
    ("🤖","scikit-learn"),("🌿","Git"),("⚡","Power Automate"),("🧪","Jupyter"),
    ("🔢","R"),("🛢️","MySQL"),("📐","VBA"),
]
html = "".join(f'<span class="tool-badge"><span>{i}</span><span>{n}</span></span>' for i, n in tools)
st.markdown(f'<div style="display:flex;flex-wrap:wrap;">{html}</div>', unsafe_allow_html=True)