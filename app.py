import streamlit as st
import streamlit.components.v1 as components

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="VEERABABU VEERA | AI SOVEREIGN",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# GLOBAL CSS (Streamlit override + shared theme)
# ─────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Rajdhani:wght@300;400;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet">
<style>
:root {
    --cyan: #00d4ff;
    --gold: #ffd700;
    --crimson: #ff3c5f;
    --bg: #04080f;
    --glass: rgba(0,212,255,0.04);
    --glass-border: rgba(0,212,255,0.15);
    --muted: #5a7a9a;
}

/* App background */
.stApp {
    background: linear-gradient(135deg, #04080f 0%, #070d1a 100%) !important;
}
.stApp::before {
    content: '';
    position: fixed; inset: 0;
    background-image:
        linear-gradient(rgba(0,212,255,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,212,255,0.025) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none; z-index: 0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #040810 0%, #06101f 100%) !important;
    border-right: 1px solid rgba(0,212,255,0.12) !important;
}
section[data-testid="stSidebar"] * { color: #c8d8e8 !important; }

/* Streamlit native elements restyled */
.stSlider > div { padding: 0 !important; }
.stSlider [data-baseweb="slider"] { padding: 0 !important; }
div[data-testid="stNumberInput"] input {
    background: rgba(0,0,0,0.5) !important;
    border: 1px solid rgba(0,212,255,0.2) !important;
    color: #00d4ff !important;
    font-family: 'Share Tech Mono', monospace !important;
    border-radius: 6px !important;
}
div[data-testid="stNumberInput"] input:focus {
    border-color: #00d4ff !important;
    box-shadow: 0 0 0 1px rgba(0,212,255,0.3) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid rgba(0,212,255,0.15) !important;
    gap: 4px;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #5a7a9a !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    border-bottom: 2px solid transparent !important;
}
.stTabs [aria-selected="true"] {
    color: #00d4ff !important;
    border-bottom-color: #00d4ff !important;
}
.stTabs [data-baseweb="tab-panel"] {
    background: transparent !important;
    padding-top: 20px !important;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: rgba(0,212,255,0.04) !important;
    border: 1px solid rgba(0,212,255,0.12) !important;
    border-radius: 8px !important;
    padding: 16px !important;
}
div[data-testid="stMetricLabel"] { color: #5a7a9a !important; font-size: 0.72rem !important; letter-spacing: 2px !important; }
div[data-testid="stMetricValue"] { color: #00d4ff !important; font-family: 'Share Tech Mono', monospace !important; }
div[data-testid="stMetricDelta"] { color: #ffd700 !important; }

/* Progress bar */
div[data-testid="stProgressBar"] > div { background: rgba(0,212,255,0.1) !important; }
div[data-testid="stProgressBar"] > div > div { background: linear-gradient(90deg, #00d4ff, #ffd700) !important; }

/* Section dividers */
hr { border-color: rgba(0,212,255,0.15) !important; }

/* Streamlit info/success boxes */
div[data-testid="stInfo"] {
    background: rgba(0,212,255,0.06) !important;
    border: 1px solid rgba(0,212,255,0.2) !important;
    border-radius: 8px !important;
    color: #c8d8e8 !important;
}
div[data-testid="stSuccess"] {
    background: rgba(255,215,0,0.06) !important;
    border: 1px solid rgba(255,215,0,0.2) !important;
    color: #ffd700 !important;
}

/* Text */
h1, h2, h3, h4, h5 { font-family: 'Cinzel', serif !important; color: white !important; }
p, li, label { font-family: 'Rajdhani', sans-serif !important; color: #c8d8e8 !important; }

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# REUSABLE HTML CARD RENDERER
# ─────────────────────────────────────────────
CARD_CSS = """
<style>
body { margin:0; padding:0; background:transparent; font-family:'Rajdhani',sans-serif; }
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Rajdhani:wght@400;600&family=Share+Tech+Mono&display=swap');
.card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(0,212,255,0.15);
    border-left: 3px solid var(--accent, #00d4ff);
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 14px;
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(0,212,255,0.03), transparent);
    opacity: 0; transition: opacity 0.3s;
}
.card:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(0,212,255,0.12); }
.card:hover::before { opacity: 1; }
.card h4 { font-family:'Cinzel',serif; font-size:0.82rem; color:#fff; letter-spacing:2px; margin-bottom:8px; }
.card p { font-size:0.84rem; color:#5a7a9a; line-height:1.6; margin:0; }
.metric {
    margin-top:10px;
    font-family:'Share Tech Mono',monospace;
    font-size:0.7rem;
    background: rgba(0,212,255,0.06);
    color: var(--accent, #00d4ff);
    padding: 3px 10px;
    border-radius: 4px;
    display: inline-block;
}
</style>
"""

def project_cards(projects, accent="#00d4ff", height=None):
    """Render a list of project dicts as glassmorphism cards."""
    cards_html = CARD_CSS + f'<style>:root{{--accent:{accent}}}</style>'
    for p in projects:
        cards_html += f"""
        <div class="card">
            <h4>{p['name']}</h4>
            <p>{p['desc']}</p>
            <span class="metric">{p['metric']}</span>
        </div>"""
    h = height or (len(projects) * 130)
    components.html(cards_html, height=h, scrolling=False)


# ─────────────────────────────────────────────
# SIDEBAR — Native Streamlit
# ─────────────────────────────────────────────
with st.sidebar:
    # Avatar + name
    components.html("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Share+Tech+Mono&display=swap');
    body { margin:0; background:transparent; text-align:center; }
    .ring-wrap { position:relative; width:120px; height:120px; margin:0 auto 16px; }
    .ring {
        position:absolute; inset:-6px;
        border-radius:50%;
        background: conic-gradient(#00d4ff, #ffd700, #ff3c5f, #00d4ff);
        animation: spin 5s linear infinite;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
    .avatar {
        position:relative; z-index:1;
        width:120px; height:120px;
        border-radius:50%;
        background: linear-gradient(135deg,#0a1628,#1a2a48);
        border: 2px solid rgba(0,212,255,0.3);
        display:flex; align-items:center; justify-content:center;
        font-size:48px;
        box-shadow: 0 0 30px rgba(0,212,255,0.2);
    }
    h1 { font-family:'Cinzel',serif; font-size:1rem; color:#fff; letter-spacing:3px; margin:0; text-shadow:0 0 20px rgba(0,212,255,0.5); }
    .sub { font-family:'Share Tech Mono',monospace; font-size:0.6rem; color:#00d4ff; letter-spacing:2px; margin-top:6px; }
    </style>
    <div class="ring-wrap"><div class="ring"></div><div class="avatar">⚔️</div></div>
    <h1>VEERABABU VEERA</h1>
    <div class="sub">// AI MULTI-DOMAIN CONSULTANT</div>
    """, height=175)

    st.success("◆ Ex-Accenture · Infosys · Tech Mahindra ◆")
    st.divider()

    st.markdown("##### 🔬 2026 Research Lab")
    st.caption("Agentic ROI Orchestration")
    st.progress(0.88, text="Vajra-Sovereign Integration — 88%")
    st.progress(0.92, text="Zero-Leakage Data Sovereignty — 92%")
    st.progress(0.74, text="Kalam-Ramanujan Fusion — 74%")
    st.divider()

    st.markdown("##### 🧩 Core Domains")
    cols = st.columns(2)
    tags = ["GenAI", "LLMOps", "Multi-Agent", "MLOps", "Security AI", "Vision AI", "RAG", "FinOps"]
    for i, tag in enumerate(tags):
        cols[i % 2].markdown(f"`{tag}`")

    st.divider()
    st.caption("📍 Addateegala, Andhra Pradesh")
    st.caption("© 2026 Sovereign Consultancy Protocol")


# ─────────────────────────────────────────────
# MAIN — Hero (HTML component)
# ─────────────────────────────────────────────
components.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Rajdhani:wght@400;600&family=Share+Tech+Mono&display=swap');
body { margin:0; padding:0; background:transparent; }
.hero-tag {
    font-family:'Share Tech Mono',monospace; font-size:0.7rem;
    color:#00d4ff; letter-spacing:4px; margin-bottom:14px;
    display:flex; align-items:center; gap:12px;
}
.hero-tag::before { content:''; display:inline-block; width:30px; height:1px; background:#00d4ff; }
h1 { font-family:'Cinzel',serif; font-size:2.5rem; font-weight:900; color:#fff;
     text-shadow:0 0 60px rgba(0,212,255,0.3); line-height:1.1; margin:0 0 16px; }
.accent { color:#00d4ff; }
.sub { font-family:'Rajdhani',sans-serif; font-size:1.05rem; color:#c8d8e8; line-height:1.7; margin-bottom:22px; max-width:640px; }
.formula {
    display:inline-block;
    background:rgba(0,212,255,0.05); border:1px solid rgba(0,212,255,0.2);
    border-radius:8px; padding:12px 20px;
    font-family:'Share Tech Mono',monospace; font-size:0.82rem; color:#ffd700; letter-spacing:1px;
}
</style>
<div class="hero-tag">SOVEREIGN AI COMMAND CENTER</div>
<h1>Architecting <span class="accent">High-Yield</span><br>Intelligence Systems</h1>
<p class="sub">
    Bridging Legacy Technical Debt and Generative ROI — deploying enterprise-grade AI
    across 27 active projects spanning defense, legal, healthcare, and predictive analytics.
</p>
<div class="formula">Business_Value = Σ ( Astra<sub>Insights</sub> × Vajra<sub>Security</sub> )</div>
""", height=260)

st.divider()

# ─────────────────────────────────────────────
# MAIN — Project Suites (Streamlit tabs + HTML cards)
# ─────────────────────────────────────────────
st.markdown("### 🏹 Project Intelligence Layers")

tab1, tab2, tab3, tab4 = st.tabs(["🛡️ VAJRA SUITE", "🎯 ASTRA SUITE", "🧬 RAMANUJAN-KALAM", "⚖️ LEGAL & HEALTH"])

with tab1:
    st.caption("DEFENSIVE & TACTICAL INFRASTRUCTURE")
    col_a, col_b = st.columns(2)
    with col_a:
        project_cards([
            {"name": "VAJRA SOVEREIGN", "desc": "Flagship governance layer for enterprise LLMs. Zero-leakage data sovereignty.", "metric": "Compliance ≥ 99.9%"},
            {"name": "VAJRA NETRA",     "desc": "Real-time computer vision for industrial security and perimeter monitoring.", "metric": "Latency: <12ms"},
            {"name": "VAJRA KAVACH",    "desc": "Adversarial defense detecting prompt injection, jailbreaks, and model exfiltration.", "metric": "Detection: 98.7%"},
        ], accent="#00d4ff", height=420)
    with col_b:
        project_cards([
            {"name": "VAJRA SENTINEL", "desc": "Autonomous monitoring agent for multi-cloud infrastructure with auto-remediation.", "metric": "MTTR: -67%"},
            {"name": "VAJRA OSINT",    "desc": "Advanced open-source intelligence engine aggregating 400+ data streams.", "metric": "Sources: 400+"},
            {"name": "VAJRA MESH",     "desc": "Federated learning orchestration for privacy-preserving enterprise model training.", "metric": "Privacy: Zero-leak"},
        ], accent="#00d4ff", height=420)

with tab2:
    st.caption("PREDICTIVE & STRATEGIC ORACLE LAYERS")
    col_a, col_b = st.columns(2)
    with col_a:
        project_cards([
            {"name": "ASTRA ORACLE",   "desc": "Multi-agent swarm for predictive logistics and supply chain volatility modeling.", "metric": "ROI: $2.4M saved"},
            {"name": "ASTRA VEDA",     "desc": "Knowledge graph converting unstructured enterprise data into strategic intelligence.", "metric": "Nodes: 18M+"},
            {"name": "ASTRA KETU",     "desc": "Anomaly detection engine for financial fraud and supply chain disruptions.", "metric": "Precision: 99.1%"},
        ], accent="#ffd700", height=420)
    with col_b:
        project_cards([
            {"name": "ASTRA YUDH",    "desc": "Competitive intelligence agent monitoring market signals across 92 markets real-time.", "metric": "Coverage: 92 markets"},
            {"name": "ASTRA MANTHAN", "desc": "Enterprise RAG system with dynamic retrieval across 50+ data lakes and repositories.", "metric": "Retrieval: <200ms"},
        ], accent="#ffd700", height=300)

with tab3:
    st.caption("MATHEMATICAL & SCIENTIFIC EXCELLENCE")
    col_a, col_b = st.columns(2)
    with col_a:
        project_cards([
            {"name": "RAMANUJAN SHIELD", "desc": "Post-quantum cryptographic security using novel number theory for enterprise key management.", "metric": "R = ∫ Enc/Entropy dt"},
            {"name": "BOSE QUANTUM LAYER","desc": "Quantum-inspired optimization for combinatorial scheduling at enterprise scale.", "metric": "Status: Research Phase"},
        ], accent="#ff3c5f", height=300)
    with col_b:
        project_cards([
            {"name": "KALAM RK-V1",      "desc": "Aerospace-grade trajectory optimization adapted for logistical route planning.", "metric": "Efficiency: +41%"},
            {"name": "ARYABHATA NUMERICS","desc": "High-precision financial modeling using Indian mathematical frameworks fused with ML.", "metric": "Accuracy: ±0.003%"},
        ], accent="#ff3c5f", height=300)

with tab4:
    st.caption("HUMANITARIAN & LEGAL AI SYSTEMS")
    col_a, col_b = st.columns(2)
    with col_a:
        project_cards([
            {"name": "RAJARAO LEGAL SUITE", "desc": "Automated legal synthesis, contract analysis, and regulatory compliance for Indian law.", "metric": "10K+ docs/month"},
            {"name": "GRAMEEN AI",           "desc": "Rural AI assistant for agricultural, legal, and healthcare guidance in 8 regional dialects.", "metric": "Languages: 8"},
        ], accent="#a78bfa", height=300)
    with col_b:
        project_cards([
            {"name": "JEEVAKAVACHA",      "desc": "Multimodal AI for early disease intervention and clinical decision support.", "metric": "Accuracy: 94.3%"},
            {"name": "DHARMA COMPLIANCE", "desc": "Automated SEBI, RBI, and GST compliance auditing for SMEs.", "metric": "Time saved: 80%"},
        ], accent="#a78bfa", height=300)

st.divider()

# ─────────────────────────────────────────────
# ROI SIMULATOR — Native Streamlit (interactive)
# ─────────────────────────────────────────────
st.markdown("### 💹 AI Transformation ROI Simulator")

sim_col1, sim_col2 = st.columns([1, 1], gap="large")

with sim_col1:
    opex = st.number_input("Current Annual OpEx (USD $)", min_value=0, value=1_000_000, step=50_000)
    efficiency = st.slider("Target Automation Efficiency", min_value=10, max_value=80, value=35, format="%d%%")
    months = st.number_input("Implementation Timeline (months)", min_value=1, max_value=36, value=6)

with sim_col2:
    savings = opex * (efficiency / 100)
    monthly = savings / 12
    payback = (opex * 0.15) / (monthly) if monthly > 0 else 0  # rough impl cost assumption

    m1, m2 = st.columns(2)
    m1.metric("Annual Savings", f"${savings:,.0f}", f"+{efficiency}% efficiency")
    m2.metric("Monthly Savings", f"${monthly:,.0f}", f"Over {months} months")

    m3, m4 = st.columns(2)
    m3.metric("ROI Rate", f"{efficiency}%", "Automation gain")
    m4.metric("Est. Payback", f"{payback:.1f} mo", "At 15% impl cost")

    st.progress(efficiency / 100, text=f"Efficiency Gain Profile — {efficiency}%")

st.divider()
st.markdown(
    "<center style='font-family:Share Tech Mono,monospace;font-size:0.72rem;color:#5a7a9a;letter-spacing:3px'>"
    "© 2026 VEERABABU VEERA · SOVEREIGN CONSULTANCY PROTOCOL</center>",
    unsafe_allow_html=True
)
