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
  --strip-bg:  #f7f6f2;
  --strip-fg:  #1a1917;
  --strip-sub: #3d3b38;
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
   SECTION HEADING BASE (old - replaced by enhanced)
══════════════════════════════════════════════ */
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
   TYPOGRAPHY
══════════════════════════════════════════════ */
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

.stat-row { display: flex; gap: 1rem; flex-wrap: wrap; margin: 2.2rem 0; }

.tag-row { display: flex; flex-wrap: wrap; gap: 0.45rem; margin: 1.2rem 0; }

.tag.outline {
  background: transparent;
  color: var(--muted);
  border-color: var(--border);
}

.tag.dark {
  background: var(--ink);
  color: var(--bg);
  border-color: var(--ink);
}

/* ══════════════════════════════════════════════
   SKILL GROUPS — clean wrap, no overflow
══════════════════════════════════════════════ */
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
  transition: all 0.25s ease;
  white-space: nowrap;
}
.tool-badge:hover { 
  border-color: var(--accent); 
  color: var(--accent);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(200, 82, 42, 0.1);
}

/* ══════════════════════════════════════════════
   CONTACT LABEL & VALUE
══════════════════════════════════════════════ */
.contact-label {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.13em;
  color: var(--muted);
  font-weight: 650;
}
.contact-value {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.98rem;
  font-weight: 600;
  color: var(--ink);
  margin-top: 0.15rem;
}
}

.card::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 4px; height: 100%;
  background: linear-gradient(180deg, var(--accent), var(--accent2));
  border-radius: 4px 0 0 4px;
  transition: width 0.3s ease;
}

.card:hover::before {
  width: 6px;
}

/* ══════════════════════════════════════════════
   ENHANCED STAT CARDS - Data-Focused Design
══════════════════════════════════════════════ */
.stat-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 1.5rem 1.6rem;
  flex: 1;
  min-width: 120px;
  position: relative;
  overflow: hidden;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  animation: fadeInUp 0.6s ease-out forwards;
}

.stat-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  animation: slideInLeft 0.6s ease-out;
}

.stat-card:hover {
  transform: translateY(-6px);
  border-color: var(--accent);
  box-shadow: 0 16px 40px rgba(200, 82, 42, 0.15);
}

.stat-card:hover::after {
  opacity: 1;
  transform: scale(1.1);
}

.stat-card::after {
  content: '';
  position: absolute;
  top: -50%; right: -50%;
  width: 100px; height: 100px;
  background: radial-gradient(circle, var(--accent2) 0%, transparent 70%);
  border-radius: 50%;
  opacity: 0;
  transition: all 0.3s ease;
}

.stat-num {
  font-family: 'Nunito', sans-serif;
  font-size: 2.2rem;
  font-weight: 900;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--muted);
  font-weight: 600;
}

/* ══════════════════════════════════════════════
   ENHANCED BUTTONS & LINKS
══════════════════════════════════════════════ */
button[data-testid="stFormSubmitButton"] {
  background: linear-gradient(135deg, var(--accent), var(--accent2)) !important;
  color: #fff !important;
  font-weight: 700 !important;
  border: none !important;
  border-radius: 10px !important;
  transition: all 0.3s ease !important;
  position: relative !important;
  overflow: hidden !important;
}

button[data-testid="stFormSubmitButton"]:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 12px 24px rgba(200, 82, 42, 0.25) !important;
  background: linear-gradient(135deg, var(--accent2), var(--accent)) !important;
}

.stLinkButton button {
  background: linear-gradient(135deg, var(--surface2), var(--surface)) !important;
  border: 1.5px solid var(--border) !important;
  color: var(--ink) !important;
  font-weight: 600 !important;
  transition: all 0.25s ease !important;
  border-radius: 10px !important;
}

.stLinkButton button:hover {
  border-color: var(--accent) !important;
  background: var(--surface) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 20px rgba(200, 82, 42, 0.1) !important;
}

/* ══════════════════════════════════════════════
   ENHANCED FORM ELEMENTS
══════════════════════════════════════════════ */
.stTextInput input, .stTextArea textarea {
  border: 1.5px solid var(--border) !important;
  border-radius: 10px !important;
  transition: all 0.25s ease !important;
  background: var(--surface) !important;
  font-size: 0.95rem !important;
  padding: 0.65rem 1rem !important;
}

.stTextInput input:focus, .stTextArea textarea:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px rgba(200, 82, 42, 0.1) !important;
}

div[data-baseweb="select"] > div {
  border-radius: 10px !important;
  border: 1.5px solid var(--border) !important;
  transition: all 0.25s ease !important;
}

div[data-baseweb="select"]:focus-within > div {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px rgba(200, 82, 42, 0.1) !important;
}

/* ══════════════════════════════════════════════
   PAGE TITLE ENHANCEMENTS
══════════════════════════════════════════════ */
.page-title {
  font-family: 'Nunito', sans-serif;
  font-size: clamp(2.2rem, 4.5vw, 3.6rem);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: var(--ink);
  margin: 0.2rem 0 1.2rem 0;
  animation: fadeInUp 0.7s ease-out;
}

.page-title span { 
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.page-title em {
  font-style: normal;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.eyebrow {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.22em;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
  margin-bottom: 0.8rem;
  animation: slideInLeft 0.6s ease-out;
}

.lead {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 1.15rem;
  line-height: 1.85;
  color: var(--ink2);
  font-weight: 300;
  max-width: 600px;
  margin-bottom: 2rem;
  animation: fadeInUp 0.7s ease-out 0.1s both;
}

/* ══════════════════════════════════════════════
   SECTION HEADING POLISH
══════════════════════════════════════════════ */
.sh {
  font-family: 'Nunito', sans-serif;
  font-size: 1.35rem;
  font-weight: 850;
  letter-spacing: -0.01em;
  color: var(--ink);
  margin: 2.5rem 0 1.3rem 0;
  padding-bottom: 0.8rem;
  border-bottom: 2px solid var(--border);
  transition: border-color 0.3s ease;
  animation: slideInLeft 0.5s ease-out;
}

.sh:hover {
  border-bottom-color: var(--accent);
}

.sh span { 
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* ══════════════════════════════════════════════
   STRIP & HIGHLIGHT BLOCKS
══════════════════════════════════════════════ */
.strip {
  background: var(--strip-bg);
  border: 1.5px solid var(--border);
  border-radius: 16px;
  padding: 2rem 2.2rem;
  margin: 2rem 0;
  position: relative;
  overflow: hidden;
  transition: all 0.35s ease;
  animation: fadeInUp 0.7s ease-out;
}

.strip:hover {
  border-color: var(--accent);
  box-shadow: 0 12px 32px rgba(200, 82, 42, 0.08);
}

.strip::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}

.strip h3 {
  font-family: 'Nunito', sans-serif;
  font-size: 1.25rem;
  font-weight: 850;
  color: var(--strip-fg) !important;
  margin: 0 0 0.8rem 0;
}

.strip p { 
  font-size: 0.96rem; 
  line-height: 1.8; 
  color: var(--strip-sub) !important; 
  margin: 0; 
}

.avail-strip {
  background: var(--strip-bg);
  border: 1.5px solid var(--border);
  border-radius: 16px;
  padding: 2.2rem 2.5rem;
  position: relative;
  overflow: hidden;
  transition: all 0.35s ease;
  animation: fadeInUp 0.8s ease-out;
}

.avail-strip:hover {
  border-color: var(--accent);
  box-shadow: 0 16px 40px rgba(200, 82, 42, 0.1);
  transform: translateY(-4px);
}

.avail-strip::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}

.avail-strip h2 {
  font-family: 'Nunito', sans-serif;
  font-size: 1.6rem;
  font-weight: 900;
  color: var(--strip-fg) !important;
  margin: 0 0 0.8rem 0;
}

.avail-strip p {
  font-size: 0.98rem;
  color: var(--strip-sub) !important;
  line-height: 1.8;
  margin-bottom: 1.2rem;
}

/* ══════════════════════════════════════════════
   ENHANCED TAGS & BADGES
══════════════════════════════════════════════ */
.tag {
  display: inline-block;
  background: var(--tag-bg);
  color: var(--tag-fg);
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.8rem;
  font-weight: 650;
  padding: 0.35rem 0.95rem;
  border-radius: 8px;
  border: 1.5px solid var(--tag-border);
  white-space: nowrap;
  letter-spacing: 0.02em;
  line-height: 1.5;
  transition: all 0.25s ease;
  cursor: default;
}

.tag:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(200, 82, 42, 0.12);
}

.tag.accent {
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  color: #fff;
  border-color: var(--accent);
}

.badge {
  display: inline-block;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  color: #fff;
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.78rem;
  font-weight: 700;
  padding: 0.4rem 1.1rem;
  border-radius: 100px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin: 0.3rem 0.2rem;
  transition: all 0.25s ease;
  box-shadow: 0 4px 12px rgba(200, 82, 42, 0.15);
}

.badge:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(200, 82, 42, 0.25);
}

.badge.outline {
  background: transparent;
  color: var(--accent);
  border: 1.5px solid var(--accent);
  box-shadow: none;
}

.badge.outline:hover {
  background: var(--accent);
  color: #fff;
  box-shadow: 0 8px 20px rgba(200, 82, 42, 0.2);
}

/* ══════════════════════════════════════════════
   ENHANCED PROJECT CARDS
══════════════════════════════════════════════ */
.proj-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 18px;
  padding: 2rem 2.2rem 1.8rem 2.2rem;
  margin-bottom: 1.8rem;
  position: relative;
  overflow: hidden;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  animation: fadeInUp 0.7s ease-out;
}

.proj-card:hover {
  border-color: var(--accent);
  transform: translateY(-8px);
  box-shadow: 0 20px 48px rgba(200, 82, 42, 0.15);
}

.proj-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 5px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  transition: height 0.3s ease;
}

.proj-card:hover::before {
  height: 6px;
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

.proj-desc { font-size: 0.93rem; line-height: 1.8; color: var(--ink2); margin-bottom: 1.2rem; }

.metric-row { display: flex; gap: 1.2rem; flex-wrap: wrap; margin-bottom: 1.3rem; }

.metric {
  background: var(--surface2);
  border-radius: 12px;
  padding: 0.75rem 1.2rem;
  text-align: center;
  min-width: 100px;
  transition: all 0.25s ease;
}

.metric:hover {
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  box-shadow: 0 4px 12px rgba(200, 82, 42, 0.15);
}

.metric-val { 
  font-family: 'Nunito', sans-serif; 
  font-size: 1.5rem; 
  font-weight: 900; 
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.metric-lbl { 
  font-size: 0.7rem; 
  text-transform: uppercase; 
  letter-spacing: 0.1em; 
  color: var(--muted); 
  margin-top: 0.15rem;
  font-weight: 650;
}

.bullet-list { list-style: none; padding: 0; margin: 0; }

.bullet-list li {
  font-size: 0.92rem;
  padding: 0.3rem 0 0.3rem 1.6rem;
  position: relative;
  color: var(--ink2);
  line-height: 1.75;
  transition: transform 0.2s ease;
}

.bullet-list li:hover {
  transform: translateX(4px);
}

.bullet-list li::before { 
  content: '→'; 
  position: absolute; 
  left: 0; 
  color: var(--accent); 
  font-weight: 800;
}

.proj-title {
  font-family: 'Nunito', sans-serif;
  font-size: 1.3rem;
  font-weight: 850;
  color: var(--ink);
  margin-bottom: 0.4rem;
}

.proj-stack {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.78rem;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 1rem;
}

/* ══════════════════════════════════════════════
   SKILL GROUPS ENHANCEMENT
══════════════════════════════════════════════ */
.skill-group {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 1.4rem 1.6rem;
  margin-bottom: 1.2rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  animation: fadeInUp 0.6s ease-out forwards;
  height: 100%;
}

.skill-group:hover {
  border-color: var(--accent);
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(200, 82, 42, 0.1);
}

/* ══════════════════════════════════════════════
   STAGGER ANIMATIONS
══════════════════════════════════════════════ */
.card:nth-child(1) { animation-delay: 0.05s; }
.card:nth-child(2) { animation-delay: 0.1s; }
.card:nth-child(3) { animation-delay: 0.15s; }
.skill-group:nth-child(1) { animation-delay: 0.05s; }
.skill-group:nth-child(2) { animation-delay: 0.1s; }
.skill-group:nth-child(3) { animation-delay: 0.15s; }

/* ══════════════════════════════════════════════
   CONTACT CARD POLISH
══════════════════════════════════════════════ */
.contact-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 12px;
  padding: 1.2rem 1.5rem;
  margin-bottom: 0.9rem;
  display: flex;
  align-items: center;
  gap: 1.2rem;
  transition: all 0.3s ease;
  animation: fadeInUp 0.6s ease-out forwards;
}

.contact-card:hover {
  border-color: var(--accent);
  transform: translateX(4px);
  box-shadow: 0 8px 20px rgba(200, 82, 42, 0.08);
}

.contact-icon {
  font-size: 1.8rem;
  transition: transform 0.3s ease;
}

.contact-card:hover .contact-icon {
  transform: scale(1.15);
}

/* ══════════════════════════════════════════════
   DIVIDER ENHANCEMENT
══════════════════════════════════════════════ */
.divider { 
  border: none; 
  border-top: 2px solid var(--border); 
  margin: 2.5rem 0;
  transition: border-color 0.3s ease;
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