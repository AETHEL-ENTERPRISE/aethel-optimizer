# 🚀 Aethel | Enterprise AI Cost Intelligence Engine

Aethel is a high-fidelity, open-source FinOps telemetry dashboard built in Python to isolate, audit, and mitigate systemic financial leakage in production LLM token streams. 

Every enterprise is deploying generative AI, but most are bleeding margins due to unoptimized context windows, bloated system prompts, and lack of client-side visibility. Aethel ingests production token telemetry logs, flags structural token overhead, and offers immediate actionable mitigation strategies to cut cloud compute bills by up to 80%.

---

## 💎 Core Feature Architecture

*   **Ingestion Pipeline**: Seamlessly drag-and-drop or upload raw `.csv` enterprise telemetry logs.
*   **Cost Intelligence Radar**: Instantly calculates exact financial overhead across multi-model deployments based on modern token pricing matrix guardrails.
*   **Automated System Diagnostics**: An AI-driven heuristics engine that scans token streams to detect massive prompt anomalies (>5,000 baseline tokens).
*   **Production Token Audit Ledger**: An interactive, color-coded tabular interface pinpointing exact operational requests causing margin erosion.

---

## 📊 Expected Schema & Ingestion Protocol

To ensure seamless data serialization, your uploaded CSV logs must contain the following case-sensitive column headers:


| Column Header | Data Type | Description |
| :--- | :--- | :--- |
| `Request` | Integer | Unique identifier for the telemetry stream request. |
| `Model` | String | The LLM model utilized (e.g., `gpt-4o`, `claude-3-5-sonnet`). |
| `Prompt Tokens` | Integer | The quantitative baseline count of input prompt tokens. |
| `Completion Tokens` | Integer | The quantitative baseline count of output completion tokens. |

### Sample Data Format Template:
```text
Request,Model,Prompt Tokens,Completion Tokens
1,gpt-4o,1200,450
2,gpt-4o,14500,200
3,claude-3-5-sonnet,850,600
```

---

## 🛠️ Local Development Installation

If you want to run the infrastructure canvas locally on your machine, clone the codebase and initialize the environment dependencies:

1. Clone the repository architecture:
   ```bash
   git clone https://github.com
   cd aethel-optimizer
   ```

2. Install mandatory runtime frameworks:
   ```bash
   pip install streamlit pandas
   ```

3. Initialize the production canvas local node:
   ```bash
   streamlit run dashboard.py
   ```

---

## 🌐 Live Production Node

The cloud production platform is globally accessible. Ingest your live enterprise logs directly here:
👉 **[https://aethel-optimizer.streamlit.app]**

---

## 🛡️ License & Architecture Rights

Developed under the corporate identity of **Aethel**. Distributed under the MIT License. See `LICENSE` for structural authorization details.
