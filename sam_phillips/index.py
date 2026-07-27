import streamlit as st

# ---- GLOBAL STYLING ----
st.set_page_config(
    page_title="Samuel Phillips | Data & AI Engineer",
    page_icon=":material/edit:",
    layout="wide",
    initial_sidebar_state="auto"
)

# Custom CSS for a polished, modern look
st.markdown("""
<style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #1a1a3e 50%, #24243e 100%);
        color: #e0e0e0;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a3e 0%, #0f0c29 100%);
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    section[data-testid="stSidebar"] .st-emotion-cache-1cypcdb {
        color: #ffffff;
    }

    /* Navigation links */
    .st-emotion-cache-1v0mbdj a {
        color: #b0b0ff !important;
        font-weight: 500;
    }
    .st-emotion-cache-1v0mbdj a:hover {
        color: #ffffff !important;
    }

    /* Headers */
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 600;
        letter-spacing: -0.02em;
    }
    h1 {
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* Cards for content sections */
    div[data-testid="stVerticalBlock"] > div:has(> div > div > .card-bg) {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        backdrop-filter: blur(8px);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="stVerticalBlock"] > div:has(> div > div > .card-bg):hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(167,139,250,0.15);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 20px rgba(167,139,250,0.4);
    }

    /* Download button */
    .stDownloadButton > button {
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        color: #ffffff;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .stDownloadButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 20px rgba(167,139,250,0.4);
    }

    /* Markdown text */
    p, li, .stMarkdown {
        color: #d0d0e0;
        line-height: 1.7;
    }

    /* Links */
    a {
        color: #a78bfa !important;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    a:hover {
        color: #c4b5fd !important;
        text-decoration: underline;
    }

    /* Dividers */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(167,139,250,0.3), transparent);
        margin: 2rem 0;
    }

    /* Image border radius */
    img {
        border-radius: 12px;
        border: 2px solid rgba(255,255,255,0.08);
    }

    /* Expander */
    .streamlit-expanderHeader {
        color: #a78bfa !important;
        font-weight: 600;
    }

    /* Metric cards */
    [data-testid="stMetricValue"] {
        color: #a78bfa;
        font-weight: 700;
    }
    [data-testid="stMetricLabel"] {
        color: #b0b0d0;
    }

    /* Code blocks */
    code {
        background: rgba(167,139,250,0.1);
        color: #c4b5fd;
        border-radius: 4px;
        padding: 0.1em 0.3em;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #1a1a3e;
    }
    ::-webkit-scrollbar-thumb {
        background: #a78bfa;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ---- PAGE NAVIGATION ----
home_page = st.Page("home.py", title="Home", icon=":material/home:")
projects_page = st.Page("projects.py", title="Projects", icon=":material/lightbulb:")
skills_and_tools = st.Page("skills_and_tools.py", title="Skills & Tools", icon=":material/build:")
technical_writings = st.Page("technical_writings.py", title="Blogs & Writings", icon=":material/article:")

pg = st.navigation([home_page, skills_and_tools, projects_page, technical_writings])
pg.run()