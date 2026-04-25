# cursor-ai-gtm-agent

**Cursor-built autonomous GTM agent system with pgvector RAG, Multi-Agent LangGraph orchestration, and Slack integration.**

## 🚀 Overview
This project is an autonomous Go-To-Market (GTM) AI system. It orchestrates specialized agents to handle CRM data (Airtable), technical documentation (RAG), and Slack notifications. Designed for high reliability, it utilizes multi-agent routing with LangGraph and real-time observability with Langfuse.

## 🏗 Architecture
The system uses a hub-and-spoke architecture:
1. **Orchestrator:** Routes incoming requests to specialized agents.
2. **Sales Agent:** Manages CRM interactions, lead scoring, and updates.
3. **Knowledge Agent:** Performs Hybrid RAG (Vector + Text search) over technical documentation.

## 🛠 Tech Stack
- **AI Core:** LangGraph, LangChain, Groq (Llama-3.3-70B), Sentence-Transformers.
- **Data & RAG:** PostgreSQL (pgvector), ChromaDB, Hybrid Semantic Search.
- **Backend:** FastAPI, Python 3.13.
- **Integrations:** Slack, Airtable, Notion (MCP-based).
- **Observability:** Langfuse.
- **Infrastructure:** Docker, ngrok.

## ⚙️ Key Engineering Features
- **Multi-Agent Orchestration:** Dynamic routing using LangGraph.
- **Robust RAG:** Hybrid search combining vector similarity and full-text ranking.
- **Resilience:** Implemented `tenacity` for API retry logic and `BackgroundTasks` for async processing.
- **Security:** Integrated PII-sanitization layer to mask sensitive customer data.
- **Performance:** Streamlined embedding pipeline with `RecursiveCharacterTextSplitter`.

## 🚀 Quick Start
1. Clone the repo: `git clone ...`
2. Set up `.env` using `.env.example`.
3. Start services: `docker-compose up -d`.
4. Run the app: `python3 -m uvicorn src.main:app --reload`.
