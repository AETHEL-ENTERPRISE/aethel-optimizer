import streamlit as st
import pandas as pd
import os

# Premium Enterprise Layout Setup
st.set_page_config(page_title="Aethel | AI Cost Intelligence", layout="wide", initial_sidebar_state="collapsed")

# Polished Enterprise Production Design System Style Sheet
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* Global Background and base text colors */
    .main, .stApp { 
        background-color: #060913 !important; 
        color: #e4e7eb !important;
    }
    
    /* Apply premium typography ONLY to custom dashboard content text */
    .brand-title, .brand-subtitle, .section-title, .section-desc, .guide-box, .guide-title, .guide-step, .insight-box {
        font-family: 'Inter', -apple-system, sans-serif !important;
    }
    
    /* BRAND HEADER STYLING */
    .brand-title {
        font-size: 38px !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        letter-spacing: 5px !important;
        margin: 0 !important;
        line-height: 1.1 !important;
    }
    .brand-subtitle {
        font-size: 11px !important;
        color: #00f2fe !important;
        letter-spacing: 2.5px !important;
        font-weight: 600 !important;
        margin: 6px 0 0 0 !important;
    }
    
    .section-title {
        font-size: 20px !important;
        font-weight: 600 !important;
        color: #ffffff !important;
        margin-top: 16px !important;
        margin-bottom: 8px !important;
    }
    .section-desc {
        font-size: 14px !important;
        color: #9ca3af !important;
        margin-bottom: 24px !important;
    }

    /* Fixed Card Layout Containers */
    div[data-testid="metric-container"] {
        background-color: #0d1324 !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        padding: 24px !important;
        border-radius: 14px !important;
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5) !important;
    }
    div[data-testid="stMetricLabel"] > div {
        font-family: 'Inter', -apple-system, sans-serif !important;
        color: #9ca3af !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    div[data-testid="stMetricValue"] > div {
        font-family: 'Inter', -apple-system, sans-serif !important;
        color: #ffffff !important;
        font-size: 32px !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px !important;
    }

    /* Clean File Ingestion Input Box Styling */
    div[data-testid="stFileUploader"] {
        background-color: #0d1324 !important;
        border: 1px dashed rgba(255, 255, 255, 0.1) !important;
        border-radius: 14px !important;
        padding: 16px !important;
    }
    
    /* Guide Panel Custom Layout styling */
    .guide-box {
        background-color: #0d1324;
        border: 1px solid rgba(0, 242, 254, 0.15);
        padding: 24px;
        border-radius: 14px;
        margin-bottom: 24px;
    }
    .guide-title {
        font-size: 16px;
        font-weight: 700;
        color: #00f2fe;
        margin-bottom: 12px;
    }
    .guide-step {
        font-size: 14px;
        color: #e4e7eb;
        margin: 6px 0;
    }

    .insight-box {
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 28px;
        font-size: 14px;
        line-height: 1.5;
    }
    .insight-error {
        background-color: rgba(239, 68, 68, 0.06);
        border: 1px solid rgba(239, 68, 68, 0.15);
        color: #fca5a5;
    }
    .insight-success {
        background-color: rgba(16, 185, 129, 0.06);
        border: 1px solid rgba(16, 185, 129, 0.15);
        color: #a7f3d0;
    }

    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stDecoration"] { display: none !important; }
    footer { visibility: hidden !important; }
    </style>
""", unsafe_allow_html=True)

# Main Navigation Brand Header - Proportional large asset sizing
logo_col, text_col = st.columns([0.12, 0.88])

with logo_col:
    if os.path.exists("aethel_logo.png"):
        st.image("aethel_logo.png", width=130)
    else:
        st.markdown("<h1 style='color: #00f2fe; margin:0; line-height:1; font-size: 60px;'>▲</h1>", unsafe_allow_html=True)

with text_col:
    st.markdown("""
        <div style="margin-top: 24px; padding-left: 15px;">
            <p class="brand-title">AETHEL</p>
            <p class="brand-subtitle">ENTERPRISE AI INTELLECT</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 32px; border-bottom: 1px solid rgba(255, 255, 255, 0.06); padding-bottom: 16px;'></div>", unsafe_allow_html=True)

# Dashboard Title
st.markdown('<p class="section-title">Cost Intelligence Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="section-desc">Ingest and process token consumption matrices to isolate financial telemetry leaks.</p>', unsafe_allow_html=True)

# USER ONBOARDING INTERFACE GUIDE: Displays clear instructions on formatting
st.markdown("""
    <div class="guide-box">
        <div class="guide-title">📋 SYSTEM INGESTION PROTOCOL (HOW TO UPLOAD PROPERLY)</div>
        <div class="guide-step">1. Export your system telemetries as a standard spreadsheet layout or plain text document.</div>
        <div class="guide-step">2. Ensure your headers match the case-sensitive matrix template fields explicitly.</div>
        <div class="guide-step">3. Save or export the finalized data layout exactly as a <strong>.csv</strong> file format extension.</div>
        <div class="guide-step">4. Drop the data file into the tracking target box below to execute your deep financial leak audit.</div>
    </div>
""", unsafe_allow_html=True)

# Interactive Expandable Box for Template Reference
with st.expander("Click to view the mandatory log data format criteria"):
    st.write("Your file structure and column header names must match this pattern perfectly:")
    sample_data = pd.DataFrame({
        "Request": [1, 2],
        "Model": ["gpt-4o", "gpt-4o"],
        "Prompt Tokens": [1200, 9500],
        "Completion Tokens": [450, 150]
    })
    st.dataframe(sample_data)
    st.code("Request,Model,Prompt Tokens,Completion Tokens\n1,gpt-4o,1200,450\n2,gpt-4o,9500,150", language="text")

st.write("")

# File Upload Drop Target
uploaded_file = st.file_uploader("", type="csv")

PRICE_PROMPT = 2.50 / 1_000_000
PRICE_COMPLETION = 10.00 / 1_000_000

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        required_columns = ["Request", "Model", "Prompt Tokens", "Completion Tokens"]
        
        # PROTECTIVE SCHEMA VALIDATION: Catches incorrect formatting before breaking
        if not all(col in df.columns for col in required_columns):
            st.error(f"❌ SCHEMA ERROR: Telemetry structure mismatch. Your file is missing vital structural columns. Please ensure it has exactly these column headers: {required_columns}")
        else:
            df["Cost ($)"] = (df["Prompt Tokens"] * PRICE_PROMPT) + (df["Completion Tokens"] * PRICE_COMPLETION)
            df["Is Waste"] = df["Prompt Tokens"] > 5000

            total_spend = df["Cost ($)"].sum()
            wasted_spend = df[df["Is Waste"]]["Cost ($)"].sum()
            waste_percentage = (wasted_spend / total_spend) * 100 if total_spend > 0 else 0

            st.write("")
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric(label="Gross Compute Allocations", value=f"${total_spend:.4f}")
            with m2:
                st.metric(label="Identified Leakage", value=f"${wasted_spend:.4f}")
            with m3:
                st.metric(label="System Efficiency Score", value=f"{100 - waste_percentage:.1f}%")

            st.markdown('<p class="section-title" style="margin-top: 32px !important;">Automated System Diagnostics</p>', unsafe_allow_html=True)
            flagged_count = df["Is Waste"].sum()
            
            if flagged_count > 0:
                st.markdown(f"""
                    <div class="insight-box insight-error">
                        <strong>CRITICAL ANOMALY DETECTED:</strong> System parameters indicate unoptimized token inflation accounting for 
                        <strong>{waste_percentage:.1f}%</strong> of gross expenditures. Found <strong>{flagged_count} rogue telemetry streams</strong> 
                        exceeding target thresholds. Immediate runtime mitigation recommended via localized context caching layers.
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="insight-box insight-success">
                        <strong>SYSTEM OPTIMAL:</strong> All operational parameters are processing efficiently within calculated infrastructure cost ceilings.
                    </div>
                """, unsafe_allow_html=True)

            st.markdown('<p class="section-title">Production Consumption Ledger</p>', unsafe_allow_html=True)
            
            def style_ledger(row):
                return ['background-color: rgba(239, 68, 68, 0.08)' if row["Is Waste"] else '' for _ in row]

            st.dataframe(df.style.apply(style_ledger, axis=1), use_container_width=True)
            
    except Exception as e:
        st.error(f"❌ FILE PROCESSING ERROR: Unable to compile file array. Details: {e}")
else:
    st.write("")
    st.info("⚡ Ingestion node online. Awaiting CSV file serialization input via drag-and-drop array above.")
