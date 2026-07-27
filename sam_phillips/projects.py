import streamlit as st

st.title("Projects")

st.markdown("""
<p style="font-size:1.1rem; color:#c4b5fd; margin-bottom:2rem;">
    A selection of projects showcasing my work across AI, data engineering, and machine learning.
</p>
""", unsafe_allow_html=True)

# ---- Project 1: Fitness RAG Assistant ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🏋️ Exercise & Fitness RAG Assistant")
st.markdown("""
An AI-powered fitness assistant that combines **Retrieval-Augmented Generation (RAG)** with LLMs to help users manage workout schedules, 
learn proper exercise form, and answer fitness-related questions. Built with Langchain and Streamlit, this application 
demonstrates practical RAG implementation for domain-specific knowledge retrieval.

**Key features:**
- Document-based Q&A on exercise techniques and fitness guidelines
- Workout schedule management and planning
- Natural language querying of fitness knowledge base
""")
st.markdown(f"""
<div style="margin-top:1rem;">
    <a href="https://phillips-fitness-assistant.streamlit.app/" target="_blank">
        <span style="background:linear-gradient(90deg, #a78bfa, #60a5fa); color:white; padding:0.4rem 1.2rem; border-radius:8px; font-weight:600;">
            🚀 Launch Live App →
        </span>
    </a>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---- Project 2: Agentic Billing AI ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🤖 Agentic Billing AI (OVO Energy)")
st.markdown("""
Architected and deployed OVO Energy's first **agentic Billing AI application** using Google's **Agent Development Kit (ADK)** 
and the A2A protocol. This system automates billing exception management, reducing issue resolution time by up to 3 hours per case 
and generating an estimated **£1M in business value**.

**Key achievements:**
- Automated complex billing exception workflows
- Integrated with enterprise systems via A2A protocol
- Reduced manual intervention and operational costs
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---- Project 3: LLM Contact Centre Platform ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🎯 LLM-Powered Contact Centre Platform (OVO Energy)")
st.markdown("""
Architected and owned a **production-grade LLM-powered contact centre platform** that reduced customer complaint response times 
by **15%**. The platform delivers scalable, reliable, low-latency AI services in production using **Vertex AI** for model training, 
evaluation, deployment, and monitoring.

**Key achievements:**
- End-to-end LLM workflows on Vertex AI with cost optimisation
- RAG pipelines using Langchain to reduce hallucinations
- Online/offline evaluation frameworks with Langsmith (20% faster improvement cycles)
- Infrastructure as Code with Terraform and CI/CD pipelines
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---- Project 4: Real-Time Manufacturing Data Pipeline ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🏭 Real-Time Manufacturing Data Pipeline (JLR)")
st.markdown("""
Designed and implemented a **real-time data pipeline** at Jaguar Land Rover's Solihull manufacturing site using 
Google **Pub/Sub** and **Bigtable**, ingesting machine and sensor data to enable low-latency monitoring and operational analytics. 
This solution contributed to approximately **£400M in cost savings** within six months.

**Key achievements:**
- Reduced manual manufacturing processes by 30%
- Identified and addressed data-driven bottlenecks in vehicle production
- Real-time ingestion and processing of sensor/machine data
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---- Project 5: CNN-Based Fall Prevention ----
st.markdown('<div class="card-bg">', unsafe_allow_html=True)
st.markdown("### 🧠 CNN-Based Fall Prevention System")
st.markdown("""
Developed a **Convolutional Neural Network (CNN)** model achieving **80% accuracy** in fall prevention using publicly available 
training data. The model was deployed via **FastAPI** and seamlessly integrated into a wearable device, boosting user engagement by 30%.

**Key achievements:**
- End-to-end ML lifecycle: research → development → deployment
- FastAPI-based model serving for real-time inference
- Integration with IoT/wearable hardware
""")
st.markdown('</div>', unsafe_allow_html=True)



