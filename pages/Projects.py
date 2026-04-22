import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from styles import inject_css, sidebar

st.set_page_config(page_title="Projects | Ayushi Rathod", page_icon="🗂️", layout="wide")
inject_css()
sidebar()

st.markdown('<div class="eyebrow">✦ Selected Work</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">Projects that <span>moved numbers</span>.</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

projects = [
    {
        "num": "01",
        "title": "🧠 Behavioral Health Risk Scoring System",
        "stack": "Python · BigQuery · XGBoost · Random Forest · SHAP",
        "desc": "Built a machine learning pipeline on 400K+ health records to classify patient risk levels and generate a composite 0–100 risk score. The system empowers clinicians to prioritize high-risk patients and deploy targeted interventions at scale.",
        "metrics": [("87%","Model Accuracy"),("400K+","Records"),("25%","Better Risk ID")],
        "bullets": [
            "Engineered a composite 0–100 risk score using feature scaling and normalization for effective risk stratification",
            "Applied SHAP for model interpretability — identified key behavioral drivers influencing high-risk outcomes",
            "Developed scalable BigQuery pipelines for automated preprocessing and efficient data handling",
            "Enabled data-driven interventions improving decision-making efficiency by 25%",
        ],
        "tags": ["XGBoost","Random Forest","SHAP","BigQuery","Feature Engineering","Risk Scoring"],
    },
    {
        "num": "02",
        "title": "📉 Customer Churn Prediction Model",
        "stack": "Python · SQL · Power BI · Logistic Regression · Random Forest · SMOTE",
        "desc": "Developed a full-cycle churn prediction solution — from feature engineering and model training to interactive Power BI dashboards with SHAP visualizations. Enabled the retention team to act on predicted churners with targeted campaigns.",
        "metrics": [("85%","Accuracy"),("Strong","ROC-AUC"),("20%","Better Retention")],
        "bullets": [
            "Engineered behavioral and transactional features to enhance predictive signal and model performance",
            "Handled class imbalance using SMOTE and class weighting to improve recall and model robustness",
            "Evaluated models with precision, recall, F1-score, and ROC-AUC to ensure optimal selection",
            "Delivered actionable insights via Power BI dashboards and SHAP visualizations",
        ],
        "tags": ["Logistic Regression","Random Forest","SMOTE","Power BI","SHAP","ROC-AUC"],
    },
    {
        "num": "03",
        "title": "📊 Operational KPI Dashboard",
        "stack": "Power BI · SQL · Python · DAX · Automated Pipelines",
        "desc": "Designed an end-to-end Power BI dashboard integrating SQL and Python to track operational KPIs in real time. Replaced a manual, error-prone reporting process with an automated pipeline that refreshes on schedule and surfaces trends.",
        "metrics": [("40%","Less Manual Work"),("30%","Faster Decisions"),("25%","More Insights")],
        "bullets": [
            "Built automated data pipelines enabling real-time refresh and improving decision-making speed by 30%",
            "Performed data cleaning and transformation ensuring cross-system data accuracy and consistency",
            "Conducted trend analysis to identify operational inefficiencies and support performance improvements",
            "Improved dashboard usability and stakeholder adoption, increasing insight-driven decisions by 25%",
        ],
        "tags": ["Power BI","DAX","SQL","Python","ETL","Automation"],
    },
]

for p in projects:
    metrics_html = "".join(
        f'<div class="metric"><div class="metric-val">{v}</div><div class="metric-lbl">{l}</div></div>'
        for v, l in p["metrics"]
    )
    bullets_html = "".join(f'<li>{b}</li>' for b in p["bullets"])
    tags_html    = "".join(f'<span class="tag" style="margin:0.18rem;">{t}</span>' for t in p["tags"])

    st.markdown(f"""
    <div class="proj-card">
      <div class="proj-num">{p['num']}</div>
      <div class="proj-title">{p['title']}</div>
      <div class="proj-stack">{p['stack']}</div>
      <p class="proj-desc">{p['desc']}</p>
      <div class="metric-row">{metrics_html}</div>
      <ul class="bullet-list">{bullets_html}</ul>
      <div style="margin-top:1rem;">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)