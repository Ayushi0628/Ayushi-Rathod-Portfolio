import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from styles import inject_css, sidebar

st.set_page_config(page_title="Contact | Ayushi Rathod", page_icon="✉️", layout="wide")
inject_css()
sidebar()

def send_email(sender_name, sender_email, subject, message):
    try:
        gmail_user     = st.secrets["GMAIL_ADDRESS"]
        gmail_password = st.secrets["GMAIL_APP_PASSWORD"]
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"[Portfolio] {subject} — from {sender_name}"
        msg["From"]    = gmail_user
        msg["To"]      = gmail_user
        msg["Reply-To"] = sender_email
        html_body = f"""
        <html><body style="font-family:sans-serif;color:#0d0d0d;max-width:600px;">
          <div style="background:linear-gradient(135deg,#c8522a,#e8743f);padding:1rem 1.5rem;border-radius:8px 8px 0 0;">
            <h2 style="color:#fff;margin:0;font-family:sans-serif;">New Portfolio Message</h2>
          </div>
          <div style="background:#f5f2ec;padding:1.5rem;border-radius:0 0 8px 8px;border:1px solid #ddd9d2;">
            <p><strong>Name:</strong> {sender_name}</p>
            <p><strong>Email:</strong> <a href="mailto:{sender_email}">{sender_email}</a></p>
            <p><strong>Subject:</strong> {subject}</p>
            <hr style="border:none;border-top:1px solid #ddd9d2;"/>
            <p><strong>Message:</strong></p>
            <p style="line-height:1.7;">{message.replace(chr(10), '<br/>')}</p>
          </div>
        </body></html>
        """
        msg.attach(MIMEText(html_body, "html"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, gmail_user, msg.as_string())
        return True, None
    except Exception as e:
        return False, str(e)

st.markdown('<div class="eyebrow">✦ Get in Touch</div>', unsafe_allow_html=True)
st.markdown("<h1 class=\"page-title\">Let's work <span>together</span>.</h1>", unsafe_allow_html=True)
st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

col_left, col_right = st.columns([3, 2], gap="large")

with col_left:
    st.markdown('<div class="sh">Send a <span>Message</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:.9rem;color:var(--muted);margin-bottom:1rem;">Fill in the form — I typically respond within 24 hours.</p>', unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        name  = st.text_input("Your Name *")
        email = st.text_input("Your Email *")
        subj  = st.selectbox("Subject *", [
            "Job Opportunity", "Internship / Co-op",
            "Project Collaboration", "Networking", "Other"
        ])
        msg = st.text_area("Message *", height=160,
                           placeholder="Tell me about the opportunity or project...")
        submitted = st.form_submit_button("Send Message →", use_container_width=True)

    if submitted:
        if not name or not email or not msg:
            st.error("Please fill in all required fields.")
        elif "@" not in email or "." not in email:
            st.error("Please enter a valid email address.")
        else:
            with st.spinner("Sending your message..."):
                success, error = send_email(name, email, subj, msg)
            if success:
                st.success(f"✅ Thanks {name}! Message sent — I'll reply to {email} within 24 hours.")
                st.balloons()
            else:
                st.error("⚠️ Could not send. Please email me directly at ayushirathod74@gmail.com")

with col_right:
    st.markdown('<div class="sh">Contact <span>Info</span></div>', unsafe_allow_html=True)
    for icon, label, value in [
        ("📧","Email","ayushirathod74@gmail.com"),
        ("📞","Phone","+1 (519) 573-5949"),
        ("📍","Location","Toronto, ON, Canada"),
    ]:
        st.markdown(f"""
        <div class="contact-card">
          <div class="contact-icon">{icon}</div>
          <div>
            <div class="contact-label">{label}</div>
            <div class="contact-value">{value}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="sh" style="margin-top:1.5rem;">Connect <span>Online</span></div>', unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn Profile", "https://linkedin.com/in/ayushirathod", use_container_width=True)
    st.link_button("🐙 GitHub Profile",   "https://github.com/Ayushi0628",     use_container_width=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

st.markdown("""
<div class="avail-strip">
  <h2>🟢 Available for Opportunities</h2>
  <p>
    Actively seeking full-time roles in Data Analytics, Business Intelligence, and Data Science
    in the Greater Toronto Area. Open to remote positions and co-op opportunities too.
    Let's connect — I'd love to learn about your team.
  </p>
  <span class="badge">✓ Available Immediately</span>
  <span class="badge outline">GTA &amp; Remote</span>
  <span class="badge outline">Full-time · Co-op</span>
</div>
""", unsafe_allow_html=True)