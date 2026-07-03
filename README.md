# AI-Agents-Intensive-Vibe-Coding-Capstone-Project

## DocuGuard Enterprise: Autonomous Multi-Agent Data Compliance Pipeline 🛡️

**AI-Agents-Intensive-Vibe-Coding-Capstone-Project**

DocuGuard Enterprise is a highly sophisticated, zero-trust unstructured data firewall built using the **Google GenAI ADK** and the **Model Context Protocol (MCP)**. This project demonstrates a Dual-MCP multi-agent architecture powered by Gemini 2.5 Flash that autonomously analyzes, routes, and redacts restricted Personally Identifiable Information (PII) and internal corporate secrets from enterprise datasets (like the Enron Email Corpus).

---

## 🚀 Key Features

* **Dual-MCP Architecture:** Dynamically fetches live corporate compliance rules (e.g., custom redaction keywords) from an external MCP server before processing documents.
* **Supervisor Routing Agent:** Intelligently analyzes text semantic meaning to route sensitive data to the Compliance Agent while safely passing through benign operational chatter, saving compute costs.
* **Compliance & Redaction Agent:** Acts as the strict security enforcer. Scrubs SSNs, employee emails, and restricted internal code names (like *Project Apollo*).
* **Automatic Rate Limit Handling:** Built-in safeguards that gracefully handle `429 RESOURCE_EXHAUSTED` errors on free-tier Gemini API keys.

---

## 🏗️ System Architecture

1. **Ingestion:** Raw text is fed into the multi-agent graph.
2. **Analysis (Supervisor):** Determines if the text contains potential compliance violations.
3. **Redaction (Compliance):** If flagged, the agent queries the **Corporate Compliance Server (Local MCP)** via SSE on port `8001` to fetch current redaction rules.
4. **Validation (Guardrail):** A final Python guardrail acts as the last line of defense before the data is safely outputted as `[REDACTED BY GUARDRAIL]` or safely masked text.

---

## 🛠️ Setup & Installation

### Prerequisites
* Python 3.10+
* A Google Gemini API Key (`GEMINI_API_KEY`)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/AI-Agents-Intensive-Vibe-Coding-Capstone-Project.git
   cd AI-Agents-Intensive-Vibe-Coding-Capstone-Project
   ```

2. **Install the required libraries:**
   ```bash
   pip install google-genai-adk jupyter
   ```

3. **Set your API Key:**
   Create a `.env` file in the root directory and add:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   *(Note: The notebook also supports Kaggle Secrets and interactive prompts if `.env` is not found).*

---

## 💻 Usage

To execute the entire autonomous pipeline end-to-end:

1. Open the Jupyter Notebook `DocuGuard_AI_Capstone_Enterprise.ipynb`.
2. Run all cells.
3. The agents will process the curated test batch. You can track the progress in the cell output.
4. The final, scrubbed dataset will be automatically exported and printed as `processed_corpus.json`.

---

## 📊 Evaluation & Results

The system was rigorously stress-tested on synthetic edge cases and authentic Enron emails:
- **PII Leakage:** Successfully identified and hard-blocked an email containing a leaked SSN.
- **Corporate Secrets:** Seamlessly identified and masked `"Project Apollo"` and `"Titanium Launch"` while preserving the rest of the text.
- **Benign Passthrough:** Correctly ignored a standard daily operational gas nomination email, proving accurate semantic routing.

---

*This project was submitted as a Capstone for the Kaggle Vibe Coding Agents Competition.*
