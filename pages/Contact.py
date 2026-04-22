import streamlit as st

st.set_page_config(page_title="Contact | Ayushi Rathod", page_icon="✉️", layout="wide")

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
.contact-card { background:var(--card); border:1.5px solid var(--border); border-radius:10px; padding:1.4rem 1.8rem; margin-bottom:.8rem; display:flex; align-items:center; gap:1.2rem; }
.contact-icon { font-size:1.8rem; }
.contact-label { font-size:.75rem; text-transform:uppercase; letter-spacing:.1em; color:var(--muted); font-weight:600; }
.contact-value { font-size:1rem; font-weight:500; color:var(--ink); margin-top:.1rem; }
.availability-strip { background:var(--ink); color:#f5f2ec; border-radius:12px; padding:2rem 2.2rem; }
.availability-strip h2 { font-family:'Syne',sans-serif; font-size:1.6rem; font-weight:800; margin:0 0 .5rem 0; color:#f5f2ec; }
.availability-strip p { font-size:.92rem; color:#c0bbb4; line-height:1.7; margin:0 0 1.2rem 0; }
.avail-badge { display:inline-block; background:var(--accent); color:#fff; font-size:.78rem; font-weight:600; padding:.35rem 1rem; border-radius:100px; text-transform:uppercase; letter-spacing:.08em; }
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

st.markdown('<div class="page-eyebrow">Get in Touch</div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">Let\'s work <span>together</span>.</h1>', unsafe_allow_html=True)
st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

col_left, col_right = st.columns([3, 2], gap="large")

with col_left:
    st.markdown('<div class="section-heading">Send a <span>Message</span></div>', unsafe_allow_html=True)
    st.markdown("_Fill in the form below — I typically respond within 24 hours._")

    with st.form("contact_form", clear_on_submit=True):
        name  = st.text_input("Your Name *")
        email = st.text_input("Your Email *")
        subj  = st.selectbox("Subject *", [
            "Job Opportunity",
            "Internship / Co-op",
            "Project Collaboration",
            "Networking",
            "Other"
        ])
        msg = st.text_area("Message *", height=160,
                           placeholder="Tell me about the opportunity or project...")
        submitted = st.form_submit_button("Send Message →", use_container_width=True)

    if submitted:
        if name and email and msg:
            st.success(f"✅ Thanks {name}! Your message has been received. I'll be in touch soon.")
            st.balloons()
        else:
            st.error("Please fill in all required fields.")

with col_right:
    st.markdown('<div class="section-heading">Contact <span>Info</span></div>', unsafe_allow_html=True)

    contacts = [
        ("📧", "Email", "ayushirathod74@gmail.com"),
        ("📞", "Phone", "+1 (519) 573-5949"),
        ("📍", "Location", "Toronto, ON, Canada"),
    ]
    for icon, label, value in contacts:
        st.markdown(f"""
        <div class="contact-card">
          <div class="contact-icon">{icon}</div>
          <div>
            <div class="contact-label">{label}</div>
            <div class="contact-value">{value}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading" style="margin-top:1.5rem;">Connect <span>Online</span></div>', unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn Profile", "https://linkedin.com/in/ayushirathod", use_container_width=True)
    st.link_button("🐙 GitHub Profile",   "https://github.com/ayushirathod",     use_container_width=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# ── Availability strip ────────────────────────────────────────────────────────
st.markdown("""
<div class="availability-strip">
  <h2>🟢 Available for Opportunities</h2>
  <p>
    I am actively seeking full-time roles in Data Analytics, Business Intelligence, and
    Data Science in the Greater Toronto Area. I'm also open to remote positions and
    co-op/internship opportunities. Let's connect — I'd love to learn about your team and goals.
  </p>
  <span class="avail-badge">✓ Available Immediately</span>
  &nbsp;
  <span class="avail-badge">GTA & Remote</span>
  &nbsp;
  <span class="avail-badge">Full-time · Co-op</span>
</div>
""", unsafe_allow_html=True)