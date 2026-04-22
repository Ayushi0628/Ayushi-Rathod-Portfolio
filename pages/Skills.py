import streamlit as st

st.set_page_config(page_title="Skills | Ayushi Rathod", page_icon="⚙️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');
:root { --ink:#0d0d0d; --paper:#f5f2ec; --accent:#c8522a; --muted:#6b6660; --border:#ddd9d2; --card:#ffffff; }
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; background-color:var(--paper); color:var(--ink); }
#MainMenu, footer, header { visibility:hidden; }
.block-container { padding:2.5rem 3rem 4rem 3rem; max-width:960px; }
section[data-testid="stSidebar"] { background:var(--ink); border-right:3px solid var(--accent); }
section[data-testid="stSidebar"] * { color:#f5f2ec !important; }
.page-title { font-family:'Syne',sans-serif; font-size:2.6rem; font-weight:800; letter-spacing:-0.03em; line-height:1.1; margin-bottom:0.3rem; }
.page-title span { color:var(--accent); }
.page-eyebrow { font-size:.78rem; text-transform:uppercase; letter-spacing:.15em; color:var(--accent); font-weight:600; margin-bottom:.4rem; }
.divider { border:none; border-top:1.5px solid var(--border); margin:2rem 0; }
.section-heading { font-family:'Syne',sans-serif; font-size:1.3rem; font-weight:700; letter-spacing:-0.02em; margin:2rem 0 1rem 0; padding-bottom:.5rem; border-bottom:2px solid var(--border); }
.section-heading span { color:var(--accent); }

/* skill group card */
.skill-group { background:var(--card); border:1.5px solid var(--border); border-radius:10px; padding:1.4rem 1.6rem; margin-bottom:1rem; }
.skill-group-title { font-family:'Syne',sans-serif; font-weight:700; font-size:0.95rem; margin-bottom:0.8rem; display:flex; align-items:center; gap:0.5rem; }
.skill-tags { display:flex; flex-wrap:wrap; gap:0.4rem; }
.tag { display:inline-block; background:var(--ink); color:#f5f2ec; font-size:0.74rem; font-weight:500; padding:0.32rem 0.8rem; border-radius:100px; letter-spacing:0.03em; }
.tag.secondary { background:transparent; color:var(--ink); border:1.5px solid var(--border); }

/* proficiency bar */
.prof-row { margin-bottom:0.9rem; }
.prof-label { display:flex; justify-content:space-between; font-size:0.83rem; font-weight:500; margin-bottom:0.3rem; }
.prof-bar-bg { background:var(--border); border-radius:4px; height:7px; width:100%; }
.prof-bar { height:7px; border-radius:4px; background:var(--accent); }

/* tool badge */
.tool-badge { display:inline-flex; align-items:center; gap:0.4rem; background:var(--card); border:1.5px solid var(--border); border-radius:8px; padding:0.55rem 1rem; font-size:0.82rem; font-weight:500; margin:0.3rem; }
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

st.markdown('<div class="page-eyebrow">Technical Expertise</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">Tools that <span>get results</span>.</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Proficiency bars ──────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">Core <span>Proficiencies</span></div>', unsafe_allow_html=True)

skills_proficiency = [
    ("Python (pandas, scikit-learn, XGBoost)", 90),
    ("SQL (MySQL, PostgreSQL, BigQuery)",       88),
    ("Power BI (DAX, Data Modelling)",          92),
    ("Excel / VBA / Power Query",               85),
    ("Tableau",                                 78),
    ("Machine Learning & SHAP",                 80),
    ("Statistical Analysis",                    82),
    ("ETL Pipelines & Data Engineering",        75),
    ("Azure / AWS / Git",                       68),
]

col_l, col_r = st.columns(2, gap="large")
for i, (name, pct) in enumerate(skills_proficiency):
    target = col_l if i % 2 == 0 else col_r
    with target:
        st.markdown(f"""
        <div class="prof-row">
          <div class="prof-label"><span>{name}</span><span style="color:var(--accent);font-weight:600;">{pct}%</span></div>
          <div class="prof-bar-bg"><div class="prof-bar" style="width:{pct}%;"></div></div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Skill groups ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">Skill <span>Categories</span></div>', unsafe_allow_html=True)

groups = [
    ("📊 Analytics & Reporting", ["Data Processing", "KPI Reporting", "Trend Analysis", "Data Integrity", "Stakeholder Insights", "Ad-hoc Analysis"]),
    ("🗄️ Data Management", ["ETL Pipelines", "Data Cleaning", "SQL (MySQL · PostgreSQL)", "Data Validation", "ERD Design", "BigQuery"]),
    ("📈 Visualization", ["Power BI", "DAX", "Tableau", "Excel Dashboards", "Interactive Reporting", "SHAP Plots"]),
    ("🧮 Statistics & ML", ["Regression", "Hypothesis Testing", "Forecasting", "XGBoost", "Random Forest", "SMOTE", "SHAP"]),
    ("⚙️ Automation & Tools", ["Power Automate", "Power Apps", "Git / GitHub", "Azure", "AWS", "Jupyter Notebooks"]),
    ("💻 Programming", ["Python", "R", "SQL", "VBA", "Power Query M", "pandas", "scikit-learn"]),
]

col1, col2 = st.columns(2, gap="large")
for i, (title, tags) in enumerate(groups):
    target = col1 if i % 2 == 0 else col2
    with target:
        tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
        st.markdown(f"""
        <div class="skill-group">
          <div class="skill-group-title">{title}</div>
          <div class="skill-tags">{tag_html}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Certifications / Tools ────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🛠️ Tools &amp; <span>Platforms</span></div>', unsafe_allow_html=True)

tools = [
    ("📊","Power BI"), ("🐍","Python"), ("🗃️","PostgreSQL"), ("📋","Excel"),
    ("☁️","BigQuery"), ("🔷","Azure"), ("📦","AWS"), ("📉","Tableau"),
    ("🤖","scikit-learn"), ("🌿","Git"), ("⚡","Power Automate"), ("🧪","Jupyter"),
]

tool_html = "".join(
    f'<span class="tool-badge"><span>{ico}</span><span>{name}</span></span>'
    for ico, name in tools
)
st.markdown(f'<div style="display:flex;flex-wrap:wrap;">{tool_html}</div>', unsafe_allow_html=True)