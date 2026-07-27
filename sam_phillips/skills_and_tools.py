import streamlit as st
from utility import ProfileConfig

st.title("Skills & Tools")

st.markdown("""
<p style="font-size:1.1rem; color:#c4b5fd; margin-bottom:2rem;">
    A comprehensive overview of the technologies, frameworks, and tools I work with daily.
</p>
""", unsafe_allow_html=True)

# ---- AI & LLM ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🤖 AI & Large Language Models")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - **Langchain** — RAG pipelines, document retrieval, LLM orchestration
    - **Langsmith** — LLM observability, evaluation, tracing, feedback loops
    - **Langgraph** — Building stateful, multi-actor agent workflows
    - **Google ADK (Agent Development Kit)** — Agentic AI applications (e.g., billing AI)
    """)

with col2:
    st.markdown("""
    - **RAG (Retrieval-Augmented Generation)** — Reducing hallucinations, improving factual accuracy
    - **MCP & A2A Protocols** — Model Context Protocol, Agent-to-Agent communication
    - **Vertex AI** — Model training, evaluation, deployment, monitoring, cost optimisation
    - **LLMs** — Gemini, Claude, and other foundation models
    """)
st.markdown('</div>', unsafe_allow_html=True)

# ---- MLOps & Infrastructure ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🏗️ MLOps & Infrastructure")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - **Kubeflow Pipelines** — End-to-end ML workflow orchestration
    - **CI/CD (GitHub Actions)** — Automated testing, deployment, and infrastructure provisioning
    - **Terraform** — Infrastructure as Code for reproducible, auditable environments
    """)

with col2:
    st.markdown("""
    - **Docker** — Containerisation for consistent deployments
    - **Model Evaluation & Observability** — Online/offline evaluation frameworks
    - **Cost Optimisation** — Efficient LLM deployment strategies on GCP
    """)
st.markdown('</div>', unsafe_allow_html=True)

# ---- Data Platforms ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🗄️ Data Platforms & Pipelines")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - **BigQuery** — Serverless data warehouse, analytics at scale
    - **Dataform** — SQL-based data transformation and pipeline management
    - **DBT** — Data build tool for analytics engineering
    - **BigTable** — Low-latency NoSQL database for real-time workloads
    """)

with col2:
    st.markdown("""
    - **CloudSQL** — Managed relational databases (PostgreSQL, MySQL)
    - **Cloud Pub/Sub** — Real-time event ingestion and messaging
    - **Cloud Composer (Airflow)** — Workflow orchestration for complex data pipelines
    - **Real-time Data Pipelines** — Streaming architectures for sensor/machine data
    """)
st.markdown('</div>', unsafe_allow_html=True)

# ---- Engineering & Languages ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 💻 Engineering & Languages")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - **Python** — pandas, numpy, FastAPI, Pytest
    - **SQL** — Complex queries, query optimisation, window functions
    - **FastAPI** — High-performance API development for ML model serving
    """)

with col2:
    st.markdown("""
    - **TDD / Pytest** — Test-driven development, unit/integration testing
    - **GitHub** — Version control, code review, collaboration
    - **RESTful API Design** — Building scalable, well-documented APIs
    - **Cross-functional Collaboration** — Bridging engineering, data science, and business
    """)
st.markdown('</div>', unsafe_allow_html=True)

# ---- Data Science ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 📊 Data Science & ML")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - **Deep Learning** — CNN development for fall prevention (80% accuracy)
    - **TensorFlow / Scikit-learn** — Model development and training
    """)

with col2:
    st.markdown("""
    - **Model Deployment** — FastAPI-based deployment to wearable devices
    - **End-to-End ML Pipelines** — From data ingestion to production inference
    """)
st.markdown('</div>', unsafe_allow_html=True)

# ---- Certifications ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🏆 Certifications")
st.markdown(f"""
<div style="display:flex; align-items:center; gap:1rem; flex-wrap:wrap;">
    <div style="background:rgba(167,139,250,0.1); border:1px solid rgba(167,139,250,0.2); border-radius:12px; padding:1rem 1.5rem; flex:1; min-width:250px;">
        <p style="font-size:1.1rem; font-weight:600; color:#ffffff; margin:0;">GCP Professional Data Engineer</p>
        <p style="margin:0.3rem 0 0 0;">
            <a href="{ProfileConfig().gcp_certification_url}" target="_blank" style="color:#a78bfa !important;">
                🔗 View Credential on Credly →
            </a>
        </p>
    </div>
    <div style="background:rgba(167,139,250,0.1); border:1px solid rgba(167,139,250,0.2); border-radius:12px; padding:1rem 1.5rem; flex:1; min-width:250px;">
        <p style="font-size:1.1rem; font-weight:600; color:#ffffff; margin:0;">Azure Data Fundamentals (DP900)</p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---- Education ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🎓 Education")
st.markdown("""
- **MSc Data Science (Distinction)** — Nottingham Trent University, 2023
- **BSc Computer Science (First Class Honours / Summa Cum Laude)** — Redeemers University, 2018
""")
st.markdown('</div>', unsafe_allow_html=True)