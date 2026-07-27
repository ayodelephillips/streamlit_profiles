import streamlit as st
from utility import ProfileConfig
from pathlib import Path

st.title("About Me")

# Helper function for card-styled sections
def section_card(content_func):
    st.markdown('<div class="card-bg">', unsafe_allow_html=True)
    content_func()
    st.markdown('</div>', unsafe_allow_html=True)

# Profile image and intro
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.image(ProfileConfig().sam_profile_image, width=350)

with col2:
    st.markdown("""
    <div class="card-bg">
        <h2 style="margin-top:0;">👋 Hi, I'm Samuel Phillips</h2>
        <p style="font-size:1.1rem; color:#c4b5fd; font-weight:500;">Senior Data & AI Engineer</p>
        <p>
            I architect production-grade LLM systems, build scalable data pipelines, and deliver 
            AI-powered solutions that drive measurable business impact. With deep expertise in 
            <strong>LLMOps, RAG, agentic AI, and cloud-native infrastructure</strong> on GCP, 
            I combine strong software engineering foundations with hands-on ML engineering to 
            build robust, cost-efficient AI products.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Career Summary
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.header("Career Summary")
st.write("""
Welcome to my page. I'm a Senior Data & AI Engineer with close to 5 years of experience spanning 
software engineering, data engineering, and now AI/ML engineering. I specialise in building 
production-grade LLM applications, scalable data pipelines, and end-to-end ML systems using 
cutting-edge tools like **Langchain**, **Vertex AI**, **BigQuery**, **ADK**, and **Kubeflow Pipelines**.

From architecting agentic billing AI systems that saved £1M in business value, to building RAG 
pipelines that reduced customer complaint response times by 15%, I focus on delivering AI solutions 
that work reliably in production.

Feel free to explore my projects and skills — I'm always pushing the boundaries of what's possible 
with AI and data.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Key Skills
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🛠 Core Competencies")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
    **AI & LLMs**
    - Large Language Models (Gemini, Claude)
    - Langchain / Langsmith / Langgraph
    - Google Agent Development Kit (ADK)
    - RAG & MCP / A2A Protocols
    - Vertex AI (training, eval, deployment, monitoring)

    **MLOps & Infrastructure**
    - Kubeflow Pipelines
    - CI/CD (GitHub Actions)
    - Terraform & Docker
    - Model evaluation & observability
    - Cost optimisation for LLMs
    """)

with col_b:
    st.markdown("""
    **Data & Platforms**
    - BigQuery, Dataform, DBT
    - BigTable, CloudSQL
    - Cloud Pub/Sub, Cloud Composer (Airflow)
    - Real-time data pipelines

    **Engineering & Languages**
    - Python (pandas, numpy, FastAPI)
    - SQL
    - TDD / Pytest
    - RESTful API design
    - Cross-functional collaboration
    """)
st.markdown('</div>', unsafe_allow_html=True)

# Certifications
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 📜 Certifications")
st.markdown(f"""
- 🏆 **GCP Professional Data Engineer** — [View Credential]({ProfileConfig().gcp_certification_url})
- Azure Data Fundamentals (DP900)
""")
st.markdown('</div>', unsafe_allow_html=True)

# Education
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🎓 Education")
st.markdown("""
- **MSc Data Science (Distinction)** — Nottingham Trent University, 2023
- **BSc Computer Science (First Class Honours)** — Redeemers University, 2018
""")
st.markdown('</div>', unsafe_allow_html=True)

# Find Me Online
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🌐 Find Me Online")
st.markdown(f"""
- [GitHub Profile]({ProfileConfig().github_profile})  
- [LinkedIn Profile]({ProfileConfig().linkedin_profile})
""")
st.markdown('</div>', unsafe_allow_html=True)

# Career Evolution
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 📈 Career Evolution")
st.markdown("""
| Period | Role | Focus |
|--------|------|-------|
| Year 1-2 | Software Engineering | Full-stack development, API design |
| Year 2-4 | Data Engineering | Scalable pipelines, BigQuery, Airflow |
| Year 5+ | **Data & AI Engineering** | LLMs, RAG, Agentic AI, MLOps |
""")
st.markdown('</div>', unsafe_allow_html=True)

# Resume download
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 📄 Download My Resume")
with open(ProfileConfig().resume_location, "rb") as file:
    st.download_button(
        label="Download Resume",
        data=file,
        file_name=ProfileConfig().resume_file_name,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
st.markdown('</div>', unsafe_allow_html=True)