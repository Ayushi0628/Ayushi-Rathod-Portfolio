import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from styles import inject_css, sidebar

st.set_page_config(page_title="About | Ayushi Rathod", page_icon="👤", layout="wide")
inject_css()
sidebar()

st.markdown('<div class="eyebrow">✦ About Me</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">The story <span>behind</span> the data.</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

col_bio, col_quick = st.columns([3, 2], gap="large")

with col_bio:
    st.markdown('<div class="sh">Who I <span>Am</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size:1rem;line-height:1.85;font-weight:300;color:var(--ink2);max-width:580px;">
      I'm a data analyst and BI professional with a strong foundation in mathematics and
      computer applications. I thrive at the intersection of numbers and narrative —
      transforming messy datasets into dashboards and models that help teams make faster,
      smarter decisions.
    </p><br/>
    <p style="font-size:1rem;line-height:1.85;font-weight:300;color:var(--ink2);max-width:580px;">
      After 1.5 years at <strong style="color:var(--ink);">Confidosoft Solutions</strong> in India —
      where I built end-to-end BI workflows, automated reporting pipelines, and delivered
      ML-powered insights — I relocated to Toronto to deepen my analytical toolkit at
      <strong style="color:var(--ink);">Northeastern University</strong>, where I completed an MPS in Analytics.
    </p><br/>
    <p style="font-size:1rem;line-height:1.85;font-weight:300;color:var(--ink2);max-width:580px;">
      I'm actively seeking full-time Data Analyst, BI Developer, or Data Science roles
      in the Greater Toronto Area (open to remote too). I bring not just technical depth
      but genuine curiosity about the business problems behind the data.
    </p>
    """, unsafe_allow_html=True)

with col_quick:
    st.markdown('<div class="sh">Quick <span>Facts</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
      <div style="font-size:0.86rem;line-height:2.1;color:var(--ink2);">
        🎓 &nbsp;<strong style="color:var(--ink);">MPS Analytics</strong> — Northeastern (2026)<br/>
        🎓 &nbsp;<strong style="color:var(--ink);">MCA</strong> — M.S. University (2023)<br/>
        🎓 &nbsp;<strong style="color:var(--ink);">B.Sc. Mathematics</strong> — M.S. University (2021)<br/>
        📍 &nbsp;<strong style="color:var(--ink);">Toronto, ON</strong> — GTA &amp; Remote<br/>
        🗣️ &nbsp;English · Hindi · Gujarati<br/>
        💼 &nbsp;<strong style="color:var(--accent);">Available immediately</strong>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sh" style="margin-top:1.5rem;">Core <span>Values</span></div>', unsafe_allow_html=True)
    for v in ["Data integrity above all", "Insights that drive action", "Continuous learning", "Clear communication"]:
        st.markdown(f'<span class="tag" style="margin:0.2rem 0.2rem 0 0;">✓ &nbsp;{v}</span>', unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)
st.markdown('<div class="sh">🎓 <span>Education</span></div>', unsafe_allow_html=True)

for school, degree, period, detail, highlights in [
    ("Northeastern University – Toronto", "Master of Professional Studies in Analytics",
     "Sep 2024 – Mar 2026 ✓ Completed",
     "Advanced analytics program combining machine learning, data science, and business intelligence. Completed intensive coursework in statistical modeling, predictive analytics, and modern data engineering practices.",
     ["Machine Learning & AI", "Statistical Modeling & Inference", "Data Visualization & Storytelling", "Business Intelligence & Analytics", "Advanced Python & SQL", "Big Data Technologies"]),
    ("The Maharaja Sayajirao University of Baroda", "Master of Computer Applications (MCA)",
     "Jul 2021 – May 2023",
     "Comprehensive graduate program in computer science covering modern software development, database management, and computational theory. Hands-on experience building scalable applications and enterprise systems.",
     ["Advanced Database Systems (Oracle, SQL Server)", "Software Engineering & Design Patterns", "Data Structures & Algorithms", "Full-Stack Web Development", "System Design & Architecture", "Networking & Security"]),
    ("The Maharaja Sayajirao University of Baroda", "Bachelor of Science in Mathematics",
     "Jun 2018 – May 2021",
     "Rigorous foundation in pure and applied mathematics with focus on quantitative reasoning. Developed strong analytical and problem-solving skills applicable to data science and analytics.",
     ["Statistics & Probability Theory", "Calculus & Real Analysis", "Linear Algebra & Matrix Theory", "Differential Equations", "Numerical Methods", "Mathematical Modeling"]),
]:
    st.markdown(f"""
    <div class="card">
      <div class="card-title">{school}</div>
      <div class="card-sub">{degree}</div>
      <div class="card-meta">📅 {period}</div>
      <p>{detail}</p>
      <div style="margin-top:0.8rem;display:flex;flex-wrap:wrap;gap:0.4rem;">
    """, unsafe_allow_html=True)
    for highlight in highlights:
        st.markdown(f'<span class="tag" style="font-size:0.8rem;">📌 {highlight}</span>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)
st.markdown('<div class="sh">💼 Professional <span>Experience</span></div>', unsafe_allow_html=True)
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
  </p>
</div>
""", unsafe_allow_html=True)