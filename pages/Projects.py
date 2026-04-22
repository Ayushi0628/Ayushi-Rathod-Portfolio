import streamlit as st

st.set_page_config(page_title="Projects | Ayushi Rathod", page_icon="🗂️", layout="wide")

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

/* project card */
.proj-card { background:var(--card); border:1.5px solid var(--border); border-radius:12px; padding:1.8rem 2rem; margin-bottom:1.5rem; position:relative; overflow:hidden; }
.proj-card::before { content:''; position:absolute; top:0; left:0; width:100%; height:4px; background:var(--accent); }
.proj-num { font-family:'Syne',sans-serif; font-size:3rem; font-weight:800; color:var(--border); position:absolute; top:1rem; right:1.5rem; line-height:1; }
.proj-title { font-family:'Syne',sans-serif; font-size:1.25rem; font-weight:700; margin-bottom:0.4rem; }
.proj-stack { font-size:0.78rem; color:var(--accent); font-weight:600; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:1rem; }
.proj-desc { font-size:0.9rem; line-height:1.7; color:#3a3632; margin-bottom:1.2rem; }
.metric-row { display:flex; gap:1.2rem; flex-wrap:wrap; margin-bottom:1.2rem; }
.metric { background:var(--paper); border-radius:8px; padding:0.6rem 1rem; text-align:center; }
.metric-val { font-family:'Syne',sans-serif; font-size:1.3rem; font-weight:800; color:var(--accent); }
.metric-lbl { font-size:0.7rem; text-transform:uppercase; letter-spacing:0.08em; color:var(--muted); }
.bullet-list { list-style:none; padding:0; margin:0; }
.bullet-list li { font-size:0.86rem; padding:0.25rem 0; padding-left:1.2rem; position:relative; color:#3a3632; line-height:1.6; }
.bullet-list li::before { content:'→'; position:absolute; left:0; color:var(--accent); font-weight:600; }
.tag { display:inline-block; background:var(--ink); color:#f5f2ec; font-size:0.72rem; font-weight:500; padding:0.28rem 0.7rem; border-radius:100px; margin:0.2rem; }
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

st.markdown('<div class="page-eyebrow">Selected Work</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">Projects that <span>moved numbers</span>.</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Project 1 ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="proj-card">
  <div class="proj-num">01</div>
  <div class="proj-title">🧠 Behavioral Health Risk Scoring System</div>
  <div class="proj-stack">Python · BigQuery · XGBoost · Random Forest · SHAP</div>
  <p class="proj-desc">
    Built a machine learning pipeline on 400K+ health records to classify patient risk levels and
    generate a composite 0–100 risk score. The system empowers clinicians to prioritize
    high-risk patients and deploy targeted interventions at scale.
  </p>
  <div class="metric-row">
    <div class="metric"><div class="metric-val">87%</div><div class="metric-lbl">Model Accuracy</div></div>
    <div class="metric"><div class="metric-val">400K+</div><div class="metric-lbl">Records Processed</div></div>
    <div class="metric"><div class="metric-val">25%</div><div class="metric-lbl">Better Risk ID</div></div>
  </div>
  <ul class="bullet-list">
    <li>Engineered a composite 0–100 risk score using feature scaling and normalization for effective risk stratification</li>
    <li>Applied SHAP for model interpretability — identified key behavioral drivers influencing high-risk outcomes</li>
    <li>Developed scalable BigQuery data pipelines for automated preprocessing and efficient data handling</li>
    <li>Enabled data-driven interventions improving decision-making efficiency and risk identification accuracy by 25%</li>
  </ul>
  <div style="margin-top:1rem;">
    <span class="tag">XGBoost</span><span class="tag">Random Forest</span><span class="tag">SHAP</span>
    <span class="tag">BigQuery</span><span class="tag">Feature Engineering</span><span class="tag">Risk Scoring</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Project 2 ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="proj-card">
  <div class="proj-num">02</div>
  <div class="proj-title">📉 Customer Churn Prediction Model</div>
  <div class="proj-stack">Python · SQL · Power BI · Logistic Regression · Random Forest · SMOTE</div>
  <p class="proj-desc">
    Developed a full-cycle churn prediction solution — from feature engineering and model training
    to interactive Power BI dashboards with SHAP visualizations. Enabled the retention team to act
    on predicted churners with targeted campaigns.
  </p>
  <div class="metric-row">
    <div class="metric"><div class="metric-val">85%</div><div class="metric-lbl">Accuracy</div></div>
    <div class="metric"><div class="metric-val">Strong</div><div class="metric-lbl">ROC-AUC</div></div>
    <div class="metric"><div class="metric-val">20%</div><div class="metric-lbl">Better Retention</div></div>
  </div>
  <ul class="bullet-list">
    <li>Engineered behavioral and transactional features to enhance predictive signal and model performance</li>
    <li>Handled class imbalance using SMOTE and class weighting to improve recall and model robustness</li>
    <li>Evaluated with precision, recall, F1-score, and ROC-AUC to ensure optimal model selection</li>
    <li>Delivered actionable insights via Power BI dashboards and SHAP visualizations</li>
  </ul>
  <div style="margin-top:1rem;">
    <span class="tag">Logistic Regression</span><span class="tag">Random Forest</span><span class="tag">SMOTE</span>
    <span class="tag">Power BI</span><span class="tag">SHAP</span><span class="tag">ROC-AUC</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Project 3 ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="proj-card">
  <div class="proj-num">03</div>
  <div class="proj-title">📊 Operational KPI Dashboard</div>
  <div class="proj-stack">Power BI · SQL · Python · DAX · Automated Pipelines</div>
  <p class="proj-desc">
    Designed an end-to-end Power BI dashboard integrating SQL and Python to track operational
    KPIs in real time. Replaced a manual, error-prone reporting process with an automated pipeline
    that refreshes on schedule and surfaces trends for continuous improvement.
  </p>
  <div class="metric-row">
    <div class="metric"><div class="metric-val">40%</div><div class="metric-lbl">Less Manual Work</div></div>
    <div class="metric"><div class="metric-val">30%</div><div class="metric-lbl">Faster Decisions</div></div>
    <div class="metric"><div class="metric-val">25%</div><div class="metric-lbl">More Insights Acted On</div></div>
  </div>
  <ul class="bullet-list">
    <li>Built automated data pipelines enabling real-time refresh and improving decision-making speed by 30%</li>
    <li>Performed data cleaning and transformation ensuring cross-system data accuracy and consistency</li>
    <li>Conducted trend analysis to identify operational inefficiencies and support performance improvements</li>
    <li>Improved dashboard usability and stakeholder adoption, increasing insight-driven decisions by 25%</li>
  </ul>
  <div style="margin-top:1rem;">
    <span class="tag">Power BI</span><span class="tag">DAX</span><span class="tag">SQL</span>
    <span class="tag">Python</span><span class="tag">ETL</span><span class="tag">Automation</span>
  </div>
</div>
""", unsafe_allow_html=True)