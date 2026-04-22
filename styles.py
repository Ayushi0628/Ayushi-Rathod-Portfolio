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
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Source+Sans+3:ital,wght@0,300;0,400;0,600;1,300;1,400&display=swap');

/* ══════════════════════════════════════════════
   LIGHT THEME
══════════════════════════════════════════════ */
:root {
  --bg:        #f7f6f2;
  --surface:   #ffffff;
  --surface2:  #edecea;
  --ink:       #1a1917;
  --ink2:      #3d3b38;
  --muted:     #74706b;
  --border:    #e0ddd7;
  --accent:    #c8522a;
  --accent2:   #e8743f;
  --sidebar-bg:#1a1917;
  --sidebar-fg:#f7f6f2;
  --tag-bg:    #e8f0fe;
  --tag-fg:    #1a56db;
  --tag-border:#c3d3fd;
  --strip-bg:  #1a1917;
  --strip-fg:  #f7f6f2;
  --strip-sub: #b0aca6;
}

/* ══════════════════════════════════════════════
   DARK THEME — media query
══════════════════════════════════════════════ */
@media (prefers-color-scheme: dark) {
  :root {
    --bg:        #13120f;
    --surface:   #1e1d1a;
    --surface2:  #272521;
    --ink:       #f0ece4;
    --ink2:      #cac6be;
    --muted:     #8a8680;
    --border:    #35322c;
    --accent:    #e8743f;
    --accent2:   #f09060;
    --sidebar-bg:#0d0c0a;
    --sidebar-fg:#f0ece4;
    --tag-bg:    #1e2a45;
    --tag-fg:    #93b4fd;
    --tag-border:#2d4070;
    --strip-bg:  #1e1d1a;
    --strip-fg:  #f0ece4;
    --strip-sub: #8a8680;
  }
}

/* ── Streamlit data-theme override ── */
[data-theme="dark"] {
  --bg:        #13120f;
  --surface:   #1e1d1a;
  --surface2:  #272521;
  --ink:       #f0ece4;
  --ink2:      #cac6be;
  --muted:     #8a8680;
  --border:    #35322c;
  --accent:    #e8743f;
  --accent2:   #f09060;
  --sidebar-bg:#0d0c0a;
  --sidebar-fg:#f0ece4;
  --tag-bg:    #1e2a45;
  --tag-fg:    #93b4fd;
  --tag-border:#2d4070;
  --strip-bg:  #1e1d1a;
  --strip-fg:  #f0ece4;
  --strip-sub: #8a8680;
}

/* ══════════════════════════════════════════════
   BASE
══════════════════════════════════════════════ */
html, body, [class*="css"], .stApp {
  font-family: 'Source Sans 3', sans-serif !important;
  background-color: var(--bg) !important;
  color: var(--ink) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3rem 5rem 3rem !important; max-width: 980px; }

/* Hide Streamlit auto-generated sidebar nav */
section[data-testid="stSidebar"] [data-testid="stSidebarNav"],
section[data-testid="stSidebar"] ul[data-testid="stSidebarNavItems"],
div[data-testid="stSidebarNavItems"] { display: none !important; }

/* ── Streamlit form elements ── */
.stTextInput input, .stTextArea textarea,
div[data-baseweb="select"] > div {
  background: var(--surface) !important;
  color: var(--ink) !important;
  border-color: var(--border) !important;
  font-family: 'Source Sans 3', sans-serif !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label,
.stMarkdown p, .stMarkdown li { color: var(--ink) !important; }
.stForm { background: transparent !important; border: none !important; }
hr { border-color: var(--border) !important; }

/* ══════════════════════════════════════════════
   SIDEBAR
══════════════════════════════════════════════ */
section[data-testid="stSidebar"] {
  background: var(--sidebar-bg) !important;
  border-right: 3px solid var(--accent) !important;
}
section[data-testid="stSidebar"] * { color: var(--sidebar-fg) !important; }
section[data-testid="stSidebar"] a:hover { color: var(--accent) !important; }
section[data-testid="stSidebar"] hr { border-color: #2e2c28 !important; }

.sb-name {
  font-family: 'Nunito', sans-serif;
  font-size: 1.3rem;
  font-weight: 900;
  letter-spacing: -0.01em;
  border-bottom: 1px solid #2e2c28;
  padding-bottom: 0.7rem;
  margin-bottom: 0.5rem;
  color: var(--sidebar-fg) !important;
}
.sb-role {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: var(--accent) !important;
  font-weight: 600;
  margin-bottom: 0.4rem;
}

/* ══════════════════════════════════════════════
   TYPOGRAPHY
══════════════════════════════════════════════ */
.eyebrow {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: var(--accent);
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.page-title {
  font-family: 'Nunito', sans-serif;
  font-size: clamp(2.2rem, 4.5vw, 3.4rem);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -0.02em;
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
  font-family: 'Source Sans 3', sans-serif;
  font-size: 1.1rem;
  line-height: 1.8;
  color: var(--muted);
  font-weight: 300;
  max-width: 580px;
  margin-bottom: 1.8rem;
}

/* ── Section heading ── */
.sh {
  font-family: 'Nunito', sans-serif;
  font-size: 1.3rem;
  font-weight: 800;
  letter-spacing: -0.01em;
  color: var(--ink);
  margin: 2.2rem 0 1rem 0;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--border);
}
.sh span { color: var(--accent); }

/* ══════════════════════════════════════════════
   CARDS
══════════════════════════════════════════════ */
.card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 1.4rem 1.6rem 1.4rem 1.9rem;
  margin-bottom: 1rem;
  position: relative;
  overflow: hidden;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.card:hover {
  border-color: var(--accent);
  box-shadow: 0 4px 20px rgba(200,82,42,0.09);
}
.card::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 4px; height: 100%;
  background: linear-gradient(180deg, var(--accent), var(--accent2));
  border-radius: 4px 0 0 4px;
}
.card-title {
  font-family: 'Nunito', sans-serif;
  font-weight: 800;
  font-size: 1rem;
  color: var(--ink);
  margin-bottom: 0.15rem;
}
.card-sub {
  font-size: 0.82rem;
  color: var(--accent);
  font-weight: 600;
  letter-spacing: 0.02em;
  margin-bottom: 0.4rem;
}
.card-meta { font-size: 0.78rem; color: var(--muted); margin-bottom: 0.6rem; }
.card p, .card li { font-size: 0.92rem; line-height: 1.75; color: var(--ink2); }

/* ══════════════════════════════════════════════
   STAT CARDS
══════════════════════════════════════════════ */
.stat-row { display: flex; gap: 1rem; flex-wrap: wrap; margin: 2rem 0; }
.stat-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 1.2rem 1.4rem;
  flex: 1;
  min-width: 120px;
  position: relative;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}
.stat-card:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(200,82,42,0.1); }
.stat-card::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}
.stat-num {
  font-family: 'Nunito', sans-serif;
  font-size: 2rem;
  font-weight: 900;
  color: var(--accent);
  line-height: 1;
  margin-bottom: 0.3rem;
}
.stat-label {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--muted);
}

/* ══════════════════════════════════════════════
   TAGS  — fixed wrapping, new style
══════════════════════════════════════════════ */
.tag-row { display: flex; flex-wrap: wrap; gap: 0.45rem; margin: 1.2rem 0; }

.tag {
  display: inline-block;
  background: var(--tag-bg);
  color: var(--tag-fg);
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.28rem 0.85rem;
  border-radius: 6px;
  border: 1.5px solid var(--tag-border);
  white-space: nowrap;          /* ← stops mid-word breaking */
  letter-spacing: 0.01em;
  line-height: 1.5;
}
.tag.outline {
  background: transparent;
  color: var(--muted);
  border-color: var(--border);
}
.tag.accent {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}
.tag.dark {
  background: var(--ink);
  color: var(--bg);
  border-color: var(--ink);
}

/* ══════════════════════════════════════════════
   SKILL GROUPS — clean wrap, no overflow
══════════════════════════════════════════════ */
.skill-group {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 1.3rem 1.5rem;
  margin-bottom: 1rem;
  transition: border-color 0.2s, box-shadow 0.2s;
  height: 100%;
}
.skill-group:hover {
  border-color: var(--accent);
  box-shadow: 0 4px 16px rgba(200,82,42,0.08);
}
.skill-group-title {
  font-family: 'Nunito', sans-serif;
  font-weight: 800;
  font-size: 0.92rem;
  color: var(--ink);
  margin-bottom: 0.8rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.skill-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

/* ══════════════════════════════════════════════
   SKILL BARS
══════════════════════════════════════════════ */
.prof-row { margin-bottom: 1.1rem; }
.prof-label {
  display: flex;
  justify-content: space-between;
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--ink);
  margin-bottom: 0.38rem;
}
.prof-pct { color: var(--accent); font-weight: 700; }
.prof-bg { background: var(--surface2); border-radius: 6px; height: 8px; }
.prof-fill {
  height: 8px;
  border-radius: 6px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}

/* ══════════════════════════════════════════════
   STRIP / HIGHLIGHT BLOCK
══════════════════════════════════════════════ */
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
  font-family: 'Nunito', sans-serif;
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--strip-fg) !important;
  margin: 0 0 0.5rem 0;
}
.strip p { font-size: 0.92rem; line-height: 1.75; color: var(--strip-sub) !important; margin: 0; }

/* ══════════════════════════════════════════════
   BADGES
══════════════════════════════════════════════ */
.badge {
  display: inline-block;
  background: var(--accent);
  color: #fff;
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.74rem;
  font-weight: 700;
  padding: 0.3rem 0.9rem;
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

/* ══════════════════════════════════════════════
   PROJECT CARDS
══════════════════════════════════════════════ */
.proj-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 16px;
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
  font-family: 'Nunito', sans-serif;
  font-size: 3.5rem;
  font-weight: 900;
  color: var(--border);
  position: absolute;
  top: 0.8rem; right: 1.5rem;
  line-height: 1;
  pointer-events: none;
}
.proj-title {
  font-family: 'Nunito', sans-serif;
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 0.3rem;
}
.proj-stack {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.76rem;
  color: var(--accent);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  margin-bottom: 0.9rem;
}
.proj-desc { font-size: 0.92rem; line-height: 1.75; color: var(--ink2); margin-bottom: 1.1rem; }
.metric-row { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.1rem; }
.metric {
  background: var(--surface2);
  border-radius: 10px;
  padding: 0.65rem 1.1rem;
  text-align: center;
  min-width: 90px;
}
.metric-val { font-family: 'Nunito', sans-serif; font-size: 1.35rem; font-weight: 900; color: var(--accent); }
.metric-lbl { font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); margin-top: 0.1rem; }
.bullet-list { list-style: none; padding: 0; margin: 0; }
.bullet-list li {
  font-size: 0.9rem;
  padding: 0.24rem 0 0.24rem 1.4rem;
  position: relative;
  color: var(--ink2);
  line-height: 1.7;
}
.bullet-list li::before { content: '→'; position: absolute; left: 0; color: var(--accent); font-weight: 700; }

/* ══════════════════════════════════════════════
   TOOL BADGES
══════════════════════════════════════════════ */
.tool-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 8px;
  padding: 0.5rem 0.95rem;
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.84rem;
  font-weight: 600;
  color: var(--ink);
  margin: 0.28rem;
  transition: border-color 0.2s, color 0.2s;
  white-space: nowrap;
}
.tool-badge:hover { border-color: var(--accent); color: var(--accent); }

/* ══════════════════════════════════════════════
   CONTACT CARD
══════════════════════════════════════════════ */
.contact-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 12px;
  padding: 1.1rem 1.4rem;
  margin-bottom: 0.7rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  transition: border-color 0.2s;
}
.contact-card:hover { border-color: var(--accent); }
.contact-icon { font-size: 1.55rem; }
.contact-label {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--muted);
  font-weight: 600;
}
.contact-value {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--ink);
  margin-top: 0.1rem;
}

/* ══════════════════════════════════════════════
   AVAILABILITY STRIP
══════════════════════════════════════════════ */
.avail-strip {
  background: var(--strip-bg);
  border: 1.5px solid var(--border);
  border-radius: 16px;
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
  font-family: 'Nunito', sans-serif;
  font-size: 1.5rem;
  font-weight: 900;
  color: var(--strip-fg) !important;
  margin: 0 0 0.5rem 0;
}
.avail-strip p {
  font-size: 0.93rem;
  color: var(--strip-sub) !important;
  line-height: 1.75;
  margin-bottom: 1rem;
}

/* ── Divider ── */
.divider { border: none; border-top: 1.5px solid var(--border); margin: 2rem 0; }

/* ══════════════════════════════════════════════
   SIDEBAR TOGGLE / HAMBURGER MENU
══════════════════════════════════════════════ */
/* Make Streamlit's hamburger menu button visible and prominent */
header[data-testid="stHeader"] {
  visibility: visible !important;
}

/* Ensure the toolbar with menu button is visible */
div[data-testid="stToolbar"] {
  visibility: visible !important;
  display: flex !important;
}

/* Style the hamburger menu button */
button[data-testid="stSidebarCollapseButton"] {
  background: var(--sidebar-bg) !important;
  border: 2px solid var(--accent) !important;
  color: var(--sidebar-fg) !important;
  padding: 0.5rem 0.7rem !important;
  border-radius: 8px !important;
  font-size: 1.2rem !important;
  cursor: pointer !important;
  transition: all 0.3s ease !important;
  margin-left: 1rem !important;
  visibility: visible !important;
  display: block !important;
}

button[data-testid="stSidebarCollapseButton"]:hover {
  background: var(--accent) !important;
  transform: scale(1.05);
}

/* For smaller screens, ensure the menu button is accessible */
@media (max-width: 768px) {
  button[data-testid="stSidebarCollapseButton"] {
    padding: 0.6rem 0.9rem !important;
    font-size: 1.3rem !important;
  }
}
</style>
""", unsafe_allow_html=True)


def sidebar(active="home"):
    with st.sidebar:
        st.markdown(SIDEBAR_HTML, unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(
            '<div style="font-size:0.76rem;color:#8a8680;line-height:1.8;">'
            '📍 Toronto, ON<br/>📧 ayushirathod74@gmail.com</div>',
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
            '[LinkedIn ↗](https://linkedin.com/in/ayushi-rathod-data-analyst)   [GitHub ↗](https://github.com/Ayushi0628)'
        )