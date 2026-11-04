# 🛡️ Enterprise-Grade RAG Evaluation \& Testing Platform

An advanced LLM observability and evaluation platform designed to measure, test, and monitor Retrieval-Augmented Generation (RAG) pipelines using industry-standard metrics (**RAGAS**). Built for high-performance AI engineering teams.

\---

## 🚀 Key Features

1. **Multi-LLM Routing Support:** Seamlessly switch between OpenAI (GPT-4o), Anthropic (Claude 3.5 Sonnet), and Groq (Llama 3) for evaluations.
2. **Visual Hallucination \& Fact Highlighter:** Color-coded text highlighting to instantly distinguish context-supported claims from unverified hallucinations (Green vs. Red).
3. **Batch CSV Evaluation:** Bulk testing capability allowing teams to upload large datasets of queries and ground truths to generate aggregate performance scorecards.
4. **Persistent SQLite Analytics \& History:** Automatically logs every evaluation run with timestamps, providing real-time historical trend analysis charts.
5. **One-Click Report Exporter:** Export detailed batch evaluation metrics instantly into downloadable CSV reports for stakeholder review.

\---

## 📊 Evaluation Metrics Tracked

* **Faithfulness:** Measures if the generated answer is strictly derived from the retrieved context (minimizing hallucinations).
* **Answer Relevance:** Evaluates how directly the answer addresses the user's prompt.
* **Context Precision:** Quantifies the accuracy and precision of the retrieval system.

\---

## 🛠️ Tech Stack

* **Core:** Python, Streamlit
* **Evaluation Framework:** RAGAS, LangChain, Hugging Face Datasets
* **Database \& Storage:** SQLite / DuckDB
* **Containerization:** Docker \& Docker Compose

\---

## ⚙️ Local Installation \& Setup

1. **Clone the Repository:**

```bash
   git clone \[https://github.com/amitkumar97097/enterprise-rag-evaluation-platform.git](https://github.com/amitkumar97097/enterprise-rag-evaluation-platform.git)
   cd enterprise-rag-evaluation-platform

