# 🛡️ Enterprise-Grade RAG Evaluation & Observability Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%252B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Streamlit-App-red.svg" alt="Streamlit">
  <img src="https://img.shields.io/badge/Framework-RAGAS%20%7C%20LangChain-orange.svg" alt="RAGAS">
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey.svg" alt="SQLite">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

An advanced LLM observability and evaluation platform designed to measure, test, and monitor Retrieval-Augmented Generation (RAG) pipelines using industry-standard metrics (**RAGAS**). Built for high-performance AI engineering teams.

---

## 🚀 Key Features

1. **Multi-LLM Routing Support:** Seamlessly switch between OpenAI, Anthropic Claude, and Groq LLMs for evaluations.
2. **Visual Hallucination & Fact Highlighter:** Color-coded text highlighting to instantly distinguish context-supported claims from unverified hallucinations (Green vs. Red).
3. **Batch CSV Evaluation:** Bulk testing capability allowing teams to upload large datasets of queries and ground truths to generate aggregate performance scorecards.
4. **Persistent SQLite Analytics & History:** Automatically logs every evaluation run with timestamps, providing real-time historical trend analysis charts.
5. **One-Click Report Exporter:** Export detailed batch evaluation metrics instantly into downloadable CSV reports for stakeholder review.

---

## 📊 Evaluation Metrics Tracked

* **Faithfulness:** Measures if the generated answer is strictly derived from the retrieved context (minimizing hallucinations).
* **Answer Relevance:** Evaluates how directly the answer addresses the user's prompt.
* **Context Precision:** Quantifies the accuracy and precision of the retrieval system.

---

## 🏗️ Project Architecture & Directory Structure

```text
rag_evaluation_system/
│
├── app.py                  # Main Streamlit dashboard interface
├── evaluate_rag.py         # Core RAGAS evaluation engine & LLM routing
├── requirements.txt        # Python dependencies
├── docker-compose.yml      # Containerization configuration
├── .gitignore              # Git ignore rules for virtualenvs & caches
└── rag_eval_history.db     # Local persistent SQLite analytics database
