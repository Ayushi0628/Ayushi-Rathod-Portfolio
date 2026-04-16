import streamlit as st

st.set_page_config(
    page_title="Ayushi Rathod | Portfolio",
    page_icon="📊",
    layout="wide"
)

st.markdown(
    """
    <style>
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #4F8BF9;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .hero-text {
        font-size: 1rem;
        line-height: 1.8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([2.5, 1])

with col1:
    st.markdown('<div class="hero-title">Ayushi Rathod</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Data Analyst · Master’s in Analytics (Applied Machine Intelligence)</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="hero-text">
        I am a data analyst based in Toronto with a strong foundation in Python, SQL, Power BI, R, Excel, and machine learning.
        I recently completed my Master of Professional Studies in Analytics at Northeastern University, Toronto, and I enjoy
        transforming complex data into actionable insights, dashboards, and business solutions.
        <br><br>
        I am actively seeking full-time roles and internship opportunities in Data Analytics, Business Intelligence,
        Reporting, and Entry-Level Data Science.
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.info(
        "📍 Toronto, Canada\n\n"
        "🎓 Northeastern University\n\n"
        "📊 Applied Machine Intelligence\n\n"
        "💼 Open to Full-Time and Internship Roles"
    )

st.write("")

c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("LinkedIn", "https://www.linkedin.com/")
with c2:
    st.link_button("GitHub", "https://github.com/")
with c3:
    st.link_button("Resume", "https://drive.google.com/")

st.markdown("---")
st.subheader("Quick Overview")
st.write(
    """
    Welcome to my portfolio. Use the sidebar to explore my background, technical skills,
    featured projects, resume, and contact information.
    """
)