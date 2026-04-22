import streamlit as st

st.set_page_config(page_title="About | Ayushi Rathod", page_icon="👤", layout="wide")

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
.page-eyebrow { font-size:0.78rem; text-transform:uppercase; letter-spacing:0.15em; color:var(--accent); font-weight:600; margin-bottom:0.4rem; }
.divider { border:none; border-top:1.5px solid var(--border); margin:2rem 0; }
.section-heading { font-family:'Syne',sans-serif; font-size:1.3rem; font-weight:700; letter-spacing:-0.02em; margin:2rem 0 1rem 0; padding-bottom:0.5rem; border-bottom:2px solid var(--border); }
.section-heading span { color:var(--accent); }
.card { background:var(--card); border:1.5px solid var(--border); border-radius:10px; padding:1.4rem 1.6rem; margin-bottom:1rem; position:relative; overflow:hidden; }
.card::before { content:''; position:absolute; top:0; left:0; width:3px; height:100%; background:var(--accent); }
.card-title { font-family:'Syne',sans-serif; font-weight:700; font-size:1rem; margin-bottom:0.2rem; }
.card-sub { font-size:0.82rem; color:var(--accent); font-weight:500; margin-bottom:0.5rem; letter-spacing:0.03em; }
.card-meta { font-size:0.78rem; color:var(--muted); margin-bottom:0.6rem; }
.card p { font-size:0.88rem; line-height:1.65; color:#3a3632; margin:0; }
.bio-text { font-size:1.02rem; line-height:1.8; font-weight:300; color:#3a3632; max-width:640px; }
.tag { display:inline-block; background:var(--ink); color:#f5f2ec; font-size:0.73rem; font-weight:500; padding:0.3rem 0.75rem; border-radius:100px; letter-spacing:0.04em; margin:0.2rem; }
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

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="page-eyebrow">About Me</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">The story <span>behind</span> the data.</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Bio ───────────────────────────────────────────────────────────────────────
col_bio, col_quick = st.columns([3, 2], gap="large")

with col_bio:
    st.markdown('<div class="section-heading">Who I <span>Am</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bio-text">
      I'm a data analyst and business intelligence professional with a strong foundation in
      mathematics and computer applications. I thrive at the intersection of numbers and narrative —
      transforming messy, raw datasets into dashboards and models that help teams make faster,
      smarter decisions.
    </p>
    <br/>
    <p class="bio-text">
      After 1.5 years working at <strong>Confidosoft Solutions</strong> in India — where I built
      end-to-end BI workflows, automated reporting pipelines, and delivered ML-powered insights —
      I relocated to Toronto to deepen my analytical toolkit at <strong>Northeastern University</strong>,
      where I'm completing an MPS in Analytics.
    </p>
    <br/>
    <p class="bio-text">
      I'm actively seeking full-time data analyst, BI developer, or data science roles in
      the Greater Toronto Area (and open to remote). I bring not just technical depth but a
      genuine curiosity about the business problems behind the data.
    </p>
    """, unsafe_allow_html=True)

with col_quick:
    st.markdown('<div class="section-heading">Quick <span>Facts</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card" style="margin-bottom:0.75rem;">
      <div style="font-size:0.83rem;line-height:1.9;color:#3a3632;">
        🎓 &nbsp; <strong>MPS Analytics</strong> — Northeastern (2026)<br/>
        🎓 &nbsp; <strong>MCA</strong> — M.S. University (2023)<br/>
        🎓 &nbsp; <strong>B.Sc. Mathematics</strong> — M.S. University (2021)<br/>
        📍 &nbsp; <strong>Toronto, ON</strong> — Open to GTA &amp; Remote<br/>
        🗣️ &nbsp; English, Hindi, Gujarati<br/>
        💼 &nbsp; <strong>Available immediately</strong>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading" style="margin-top:1.5rem;">Core <span>Values</span></div>', unsafe_allow_html=True)
    for v in ["Data integrity above all", "Insights that drive action", "Continuous learning", "Clear communication"]:
        st.markdown(f'<span class="tag">✓ &nbsp;{v}</span>', unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Education ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🎓 Education</div>', unsafe_allow_html=True)

edu = [
    {
        "school": "Northeastern University – Toronto",
        "degree": "Master of Professional Studies in Analytics",
        "period": "Sep 2024 – Mar 2026",
        "detail": "Machine Learning · AI · Statistical Modeling · Data Visualization · Business Intelligence"
    },
    {
        "school": "The Maharaja Sayajirao University of Baroda",
        "degree": "Master of Computer Applications (MCA)",
        "period": "Jul 2021 – May 2023",
        "detail": "Advanced database systems, software engineering, data structures, and full-stack development."
    },
    {
        "school": "The Maharaja Sayajirao University of Baroda",
        "degree": "Bachelor of Science in Mathematics",
        "period": "Jun 2018 – May 2021",
        "detail": "Statistics, calculus, linear algebra, probability theory, and numerical methods."
    },
]

for e in edu:
    st.markdown(f"""
    <div class="card">
      <div class="card-title">{e['school']}</div>
      <div class="card-sub">{e['degree']}</div>
      <div class="card-meta">📅 {e['period']}</div>
      <p>{e['detail']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Experience ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">💼 Professional <span>Experience</span></div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
  <div class="card-title">Confidosoft Solutions — Vadodara, India</div>
  <div class="card-sub">Data Analyst &amp; Business Intelligence Associate</div>
  <div class="card-meta">📅 Jan 2023 – Jul 2024 &nbsp;·&nbsp; 1.5 years</div>
  <p>
    Led end-to-end data processing workflows ensuring accuracy, integrity, and consistency across
    enterprise reports. Built Power BI dashboards with DAX to surface KPIs and performance trends
    for senior stakeholders. Automated reporting workflows using VBA, Power Query, and Python —
    cutting manual effort by <strong>40%</strong> and turnaround time by <strong>25%</strong>.
    Collaborated cross-functionally to align analytical insights with business goals.
  </p>
</div>
""", unsafe_allow_html=True)