"""
Shared CSS injected on every page.
Call:  from styles import inject_css; inject_css()
"""
import streamlit as st

SIDEBAR_HTML = """
<div class="sb-name">Ayushi Rathod</div>
<div class="sb-role">Data Analyst · BI Associate</div>
"""

def inject_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

/* ══════════════════════════════════════════════
   LIGHT THEME  (default)
══════════════════════════════════════════════ */
:root {
  --bg:        #f5f2ec;
  --surface:   #ffffff;
  --surface2:  #eeebe4;
  --ink:       #0d0d0d;
  --ink2:      #3a3632;
  --muted:     #6b6660;
  --border:    #ddd9d2;
  --accent:    #c8522a;
  --accent2:   #e8743f;
  --sidebar-bg:#0d0d0d;
  --sidebar-fg:#f5f2ec;
  --tag-bg:    #0d0d0d;
  --tag-fg:    #f5f2ec;
  --strip-bg:  #0d0d0d;
  --strip-fg:  #f5f2ec;
  --strip-sub: #c0bbb4;
}

/* ══════════════════════════════════════════════
   DARK THEME
══════════════════════════════════════════════ */
@media (prefers-color-scheme: dark) {
  :root {
    --bg:        #111210;
    --surface:   #1c1b19;
    --surface2:  #252420;
    --ink:       #f0ece4;
    --ink2:      #ccc8c0;
    --muted:     #8a8680;
    --border:    #333028;
    --accent:    #e8743f;
    --accent2:   #f09060;
    --sidebar-bg:#0a0a09;
    --sidebar-fg:#f0ece4;
    --tag-bg:    #2a2824;
    --tag-fg:    #f0ece4;
    --strip-bg:  #1c1b19;
    --strip-fg:  #f0ece4;
    --strip-sub: #8a8680;
  }
}

/* Streamlit also sets data-theme attribute — cover both ways */
[data-theme="dark"] {
  --bg:        #111210;
  --surface:   #1c1b19;
  --surface2:  #252420;
  --ink:       #f0ece4;
  --ink2:      #ccc8c0;
  --muted:     #8a8680;
  --border:    #333028;
  --accent:    #e8743f;
  --accent2:   #f09060;
  --sidebar-bg:#0a0a09;
  --sidebar-fg:#f0ece4;
  --tag-bg:    #2a2824;
  --tag-fg:    #f0ece4;
  --strip-bg:  #1c1b19;
  --strip-fg:  #f0ece4;
  --strip-sub: #8a8680;
}

/* ── Reset & Base ── */
html, body, [class*="css"], .stApp {
  font-family: 'DM Sans', sans-serif !important;
  background-color: var(--bg) !important;
  color: var(--ink) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3rem 5rem 3rem !important; max-width: 980px; }

/* ── Streamlit native elements ── */
.stTextInput input, .stTextArea textarea, .stSelectbox select,
div[data-baseweb="select"] > div {
  background: var(--surface) !important;
  color: var(--ink) !important;
  border-color: var(--border) !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label,
.stMarkdown p, .stMarkdown li { color: var(--ink) !important; }
.stForm { background: transparent !important; border: none !important; }
hr { border-color: var(--border) !important; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
  background: var(--sidebar-bg) !important;
  border-right: 3px solid var(--accent) !important;
}
section[data-testid="stSidebar"] * { color: var(--sidebar-fg) !important; }
section[data-testid="stSidebar"] a:hover { color: var(--accent) !important; }
section[data-testid="stSidebar"] hr { border-color: #2a2824 !important; }
.sb-name {
  font-family: 'Syne', sans-serif;
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  border-bottom: 1px solid #2a2824;
  padding-bottom: 0.75rem;
  margin-bottom: 0.6rem;
}
.sb-role {
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: var(--accent) !important;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

/* ── Typography ── */
.eyebrow {
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--accent);
  font-weight: 600;
  margin-bottom: 0.4rem;
}
.page-title {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2.2rem, 4.5vw, 3.5rem);
  font-weight: 800;
  line-height: 1.06;
  letter-spacing: -0.03em;
  color: var(--ink);
  margin: 0.2rem 0 1rem 0;
}
.page-title span { color: var(--accent); }
.page-title em {
  font-style: normal;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.lead {
  font-size: 1.05rem;
  line-height: 1.75;
  color: var(--muted);
  font-weight: 300;
  max-width: 560px;
  margin-bottom: 1.8rem;
}

/* ── Section heading ── */
.sh {
  font-family: 'Syne', sans-serif;
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--ink);
  margin: 2.2rem 0 1rem 0;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--border);
}
.sh span { color: var(--accent); }

/* ── Cards ── */
.card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 12px;
  padding: 1.4rem 1.6rem;
  margin-bottom: 1rem;
  position: relative;
  overflow: hidden;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.card:hover {
  border-color: var(--accent);
  box-shadow: 0 4px 24px rgba(200,82,42,0.08);
}
.card::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 3px; height: 100%;
  background: linear-gradient(180deg, var(--accent), var(--accent2));
}
.card-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 1rem;
  color: var(--ink);
  margin-bottom: 0.15rem;
}
.card-sub {
  font-size: 0.8rem;
  color: var(--accent);
  font-weight: 600;
  letter-spacing: 0.03em;
  margin-bottom: 0.4rem;
}
.card-meta {
  font-size: 0.76rem;
  color: var(--muted);
  margin-bottom: 0.6rem;
}
.card p, .card li {
  font-size: 0.88rem;
  line-height: 1.7;
  color: var(--ink2);
}

/* ── Stat cards ── */
.stat-row { display: flex; gap: 1rem; flex-wrap: wrap; margin: 2rem 0; }
.stat-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 12px;
  padding: 1.2rem 1.4rem;
  flex: 1;
  min-width: 120px;
  position: relative;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}
.stat-card:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(200,82,42,0.1); }
.stat-card::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}
.stat-num {
  font-family: 'Syne', sans-serif;
  font-size: 2rem;
  font-weight: 800;
  color: var(--accent);
  line-height: 1;
  margin-bottom: 0.3rem;
}
.stat-label {
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--muted);
}

/* ── Tags ── */
.tag-row { display: flex; flex-wrap: wrap; gap: 0.45rem; margin: 1.2rem 0; }
.tag {
  background: var(--tag-bg);
  color: var(--tag-fg);
  font-size: 0.74rem;
  font-weight: 500;
  padding: 0.32rem 0.85rem;
  border-radius: 100px;
  letter-spacing: 0.03em;
  border: 1.5px solid transparent;
}
.tag.outline {
  background: transparent;
  color: var(--ink);
  border-color: var(--border);
}
.tag.accent {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}

/* ── Dark strip / highlight block ── */
.strip {
  background: var(--strip-bg);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 1.8rem 2rem;
  margin: 1.5rem 0;
  position: relative;
  overflow: hidden;
}
.strip::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}
.strip h3 {
  font-family: 'Syne', sans-serif;
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--strip-fg) !important;
  margin: 0 0 0.5rem 0;
}
.strip p {
  font-size: 0.9rem;
  line-height: 1.7;
  color: var(--strip-sub) !important;
  margin: 0;
}

/* ── Availability badges ── */
.badge {
  display: inline-block;
  background: var(--accent);
  color: #fff;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.32rem 0.9rem;
  border-radius: 100px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin: 0.25rem 0.15rem;
}
.badge.outline {
  background: transparent;
  color: var(--accent);
  border: 1.5px solid var(--accent);
}

/* ── Skill bar ── */
.prof-row { margin-bottom: 1rem; }
.prof-label {
  display: flex;
  justify-content: space-between;
  font-size: 0.83rem;
  font-weight: 500;
  color: var(--ink);
  margin-bottom: 0.35rem;
}
.prof-pct { color: var(--accent); font-weight: 700; }
.prof-bg {
  background: var(--surface2);
  border-radius: 6px;
  height: 8px;
}
.prof-fill {
  height: 8px;
  border-radius: 6px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}

/* ── Contact card ── */
.contact-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 10px;
  padding: 1.1rem 1.4rem;
  margin-bottom: 0.7rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  transition: border-color 0.2s;
}
.contact-card:hover { border-color: var(--accent); }
.contact-icon { font-size: 1.6rem; }
.contact-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); font-weight: 600; }
.contact-value { font-size: 0.95rem; font-weight: 500; color: var(--ink); margin-top: 0.1rem; }

/* ── Proj card ── */
.proj-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 1.8rem 2rem 1.6rem 2rem;
  margin-bottom: 1.5rem;
  position: relative;
  overflow: hidden;
  transition: border-color 0.25s, box-shadow 0.25s;
}
.proj-card:hover {
  border-color: var(--accent);
  box-shadow: 0 8px 32px rgba(200,82,42,0.1);
}
.proj-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}
.proj-num {
  font-family: 'Syne', sans-serif;
  font-size: 3.5rem;
  font-weight: 800;
  color: var(--border);
  position: absolute;
  top: 0.8rem; right: 1.5rem;
  line-height: 1;
  pointer-events: none;
}
.proj-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 0.3rem;
}
.proj-stack {
  font-size: 0.75rem;
  color: var(--accent);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 0.9rem;
}
.proj-desc { font-size: 0.9rem; line-height: 1.7; color: var(--ink2); margin-bottom: 1.1rem; }
.metric-row { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.1rem; }
.metric {
  background: var(--surface2);
  border-radius: 8px;
  padding: 0.6rem 1rem;
  text-align: center;
  min-width: 80px;
}
.metric-val { font-family: 'Syne', sans-serif; font-size: 1.3rem; font-weight: 800; color: var(--accent); }
.metric-lbl { font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); }
.bullet-list { list-style: none; padding: 0; margin: 0; }
.bullet-list li {
  font-size: 0.86rem;
  padding: 0.22rem 0 0.22rem 1.3rem;
  position: relative;
  color: var(--ink2);
  line-height: 1.65;
}
.bullet-list li::before { content: '→'; position: absolute; left: 0; color: var(--accent); font-weight: 700; }

/* ── Tool badge ── */
.tool-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 8px;
  padding: 0.5rem 0.9rem;
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--ink);
  margin: 0.25rem;
  transition: border-color 0.2s;
}
.tool-badge:hover { border-color: var(--accent); color: var(--accent); }

/* ── Skill group ── */
.skill-group {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 12px;
  padding: 1.3rem 1.5rem;
  margin-bottom: 1rem;
  transition: border-color 0.2s;
}
.skill-group:hover { border-color: var(--accent); }
.skill-group-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 0.9rem;
  color: var(--ink);
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

/* ── Divider ── */
.divider { border: none; border-top: 1.5px solid var(--border); margin: 2rem 0; }

/* ── Gradient text ── */
.grad { background: linear-gradient(135deg, var(--accent), var(--accent2)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }

/* ── Availability strip ── */
.avail-strip {
  background: var(--strip-bg);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 2rem 2.2rem;
  position: relative;
  overflow: hidden;
}
.avail-strip::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}
.avail-strip h2 {
  font-family: 'Syne', sans-serif;
  font-size: 1.55rem;
  font-weight: 800;
  color: var(--strip-fg) !important;
  margin: 0 0 0.5rem 0;
}
.avail-strip p { font-size: 0.9rem; color: var(--strip-sub) !important; line-height: 1.7; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)


def sidebar(active="home"):
    with st.sidebar:
        st.markdown(SIDEBAR_HTML, unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(
            '<div style="font-size:0.78rem;color:var(--muted);">📍 Toronto, ON &nbsp;·&nbsp; 📧 ayushirathod74@gmail.com</div>',
            unsafe_allow_html=True
        )
        st.markdown("---")
        st.page_link("Home.py",           label="🏠 Home")
        st.page_link("pages/About.py",    label="👤 About")
        st.page_link("pages/Skills.py",   label="⚙️ Skills")
        st.page_link("pages/Projects.py", label="🗂️ Projects")
        st.page_link("pages/Resume.py",   label="📄 Resume")
        st.page_link("pages/Contact.py",  label="✉️ Contact")
        st.markdown("---")
        st.markdown(
            '[LinkedIn ↗](https://linkedin.com/in/ayushirathod)   [GitHub ↗](https://github.com/Ayushi0628)'
        )