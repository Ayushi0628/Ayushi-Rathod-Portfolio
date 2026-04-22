import streamlit as st

st.set_page_config(
    page_title="Ayushi Rathod | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

:root {
    --ink:     #0d0d0d;
    --paper:   #f5f2ec;
    --accent:  #c8522a;
    --muted:   #6b6660;
    --border:  #ddd9d2;
    --card:    #ffffff;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--paper);
    color: var(--ink);
}

/* hide default streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3rem 4rem 3rem; max-width: 960px; }

/* ── sidebar ── */
section[data-testid="stSidebar"] {
    background: var(--ink);
    border-right: 3px solid var(--accent);
}
section[data-testid="stSidebar"] * { color: #f5f2ec !important; }
section[data-testid="stSidebar"] a:hover { color: var(--accent) !important; }
.sidebar-name {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    border-bottom: 1px solid #333;
    padding-bottom: 0.75rem;
    margin-bottom: 1rem;
}
.sidebar-role {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--accent) !important;
    font-weight: 500;
}

/* ── hero ── */
.hero-eyebrow {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--accent);
    font-weight: 600;
    margin-bottom: 0.5rem;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.6rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    margin: 0 0 1.2rem 0;
}
.hero-title span { color: var(--accent); }
.hero-subtitle {
    font-size: 1.08rem;
    color: var(--muted);
    line-height: 1.7;
    max-width: 520px;
    font-weight: 300;
    margin-bottom: 2rem;
}

/* ── stat cards ── */
.stat-row { display: flex; gap: 1rem; flex-wrap: wrap; margin: 2.5rem 0; }
.stat-card {
    background: var(--card);
    border: 1.5px solid var(--border);
    border-radius: 10px;
    padding: 1.2rem 1.5rem;
    flex: 1;
    min-width: 130px;
    position: relative;
    overflow: hidden;
}
.stat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: var(--accent);
}
.stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: var(--ink);
    line-height: 1;
}
.stat-label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--muted);
    margin-top: 0.3rem;
}

/* ── pill tags ── */
.tag-row { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0; }
.tag {
    background: var(--ink);
    color: #f5f2ec;
    font-size: 0.75rem;
    font-weight: 500;
    padding: 0.35rem 0.85rem;
    border-radius: 100px;
    letter-spacing: 0.04em;
}
.tag.outline {
    background: transparent;
    color: var(--ink);
    border: 1.5px solid var(--border);
}

/* ── section heading ── */
.section-heading {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    margin: 2.5rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--border);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-heading span { color: var(--accent); }

/* ── highlight strip ── */
.highlight-strip {
    background: var(--ink);
    color: #f5f2ec;
    border-radius: 12px;
    padding: 1.8rem 2rem;
    margin: 1.5rem 0;
}
.highlight-strip h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    color: #f5f2ec;
}
.highlight-strip p {
    font-size: 0.92rem;
    line-height: 1.65;
    color: #c0bbb4;
    margin: 0;
}

/* ── cta buttons ── */
.cta-row { display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.5rem; }
.cta-btn {
    display: inline-block;
    padding: 0.7rem 1.6rem;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 600;
    text-decoration: none;
    letter-spacing: 0.04em;
    cursor: pointer;
    transition: opacity 0.2s;
}
.cta-primary { background: var(--accent); color: #fff; }
.cta-secondary { background: transparent; color: var(--ink); border: 1.5px solid var(--ink); }
.cta-btn:hover { opacity: 0.82; }

/* divider */
.divider { border: none; border-top: 1.5px solid var(--border); margin: 2rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-name">Ayushi Rathod</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-role">Data Analyst · BI Associate</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("📍 Toronto, ON, Canada")
    st.markdown("📧 ayushirathod74@gmail.com")
    st.markdown("📞 +1 (519) 573-5949")
    st.markdown("---")
    st.markdown("**Navigate**")
    st.page_link("Home.py",            label="🏠 Home")
    st.page_link("pages/About.py",     label="👤 About")
    st.page_link("pages/Skills.py",    label="⚙️ Skills")
    st.page_link("pages/Projects.py",  label="🗂️ Projects")
    st.page_link("pages/Resume.py",    label="📄 Resume")
    st.page_link("pages/Contact.py",   label="✉️ Contact")
    st.markdown("---")
    st.markdown(
        '[LinkedIn ↗](https://linkedin.com/in/ayushirathod)   '
        '[GitHub ↗](https://github.com/ayushirathod)',
        unsafe_allow_html=False
    )

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-eyebrow">Available for full-time &amp; internship roles</div>', unsafe_allow_html=True)
st.markdown("""
<h1 class="hero-title">
  Turning data<br>into <span>decisions</span>.
</h1>
<p class="hero-subtitle">
  Data Analyst &amp; BI Associate with 1.5+ years of experience building
  dashboards, ML pipelines, and automated reporting systems that drive
  measurable business impact.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tag-row">
  <span class="tag">Python · SQL</span>
  <span class="tag">Power BI · Tableau</span>
  <span class="tag">Machine Learning</span>
  <span class="tag">ETL Pipelines</span>
  <span class="tag outline">Open to Work 🟢</span>
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-row">
  <div class="stat-card">
    <div class="stat-num">1.5+</div>
    <div class="stat-label">Years Experience</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">40%</div>
    <div class="stat-label">Reporting Effort Saved</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">87%</div>
    <div class="stat-label">ML Model Accuracy</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">400K+</div>
    <div class="stat-label">Records Processed</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── What I Do ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">What I <span>Do</span></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="stat-card" style="min-height:140px;">
      <div style="font-size:1.6rem;margin-bottom:0.5rem;">📊</div>
      <strong style="font-family:'Syne',sans-serif;">Analytics & BI</strong>
      <p style="font-size:0.83rem;color:#6b6660;margin-top:0.4rem;line-height:1.55;">
        Power BI dashboards with DAX, KPI tracking, and stakeholder-ready reports.
      </p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="stat-card" style="min-height:140px;">
      <div style="font-size:1.6rem;margin-bottom:0.5rem;">🤖</div>
      <strong style="font-family:'Syne',sans-serif;">Machine Learning</strong>
      <p style="font-size:0.83rem;color:#6b6660;margin-top:0.4rem;line-height:1.55;">
        Classification, regression, and risk-scoring models using scikit-learn, XGBoost & SHAP.
      </p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="stat-card" style="min-height:140px;">
      <div style="font-size:1.6rem;margin-bottom:0.5rem;">⚙️</div>
      <strong style="font-family:'Syne',sans-serif;">Data Engineering</strong>
      <p style="font-size:0.83rem;color:#6b6660;margin-top:0.4rem;line-height:1.55;">
        ETL pipelines, SQL data models, BigQuery, and workflow automation with Python & VBA.
      </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Highlight ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="highlight-strip">
  <h3>🎓 Currently at Northeastern University – Toronto</h3>
  <p>
    Completed a Master of Professional Studies in Analytics (Sep 2024 – Mar 2026),
    with coursework spanning Machine Learning, AI, Statistical Modeling, and Business Intelligence.
    Actively seeking co-op &amp; full-time data roles in the Greater Toronto Area.
  </p>
</div>
""", unsafe_allow_html=True)