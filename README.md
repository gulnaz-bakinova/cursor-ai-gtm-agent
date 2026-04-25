# Cursor-built Autonomous GTM Agent System

Autonomous Go-To-Market AI assistant orchestrating multi-agent workflows with LangGraph, pgvector RAG, and real-time CRM synchronization.

## Overview
This project is an autonomous GTM AI system developed in Cursor. It orchestrates specialized agents to automate sales qualification (Airtable CRM) and knowledge management (RAG over Postgres/Notion).

## Key Engineering Features
- **Orchestration:** Multi-agent routing via **LangGraph** (State Machine, intelligent routing).
- **Advanced RAG:** **Hybrid Search** (Vector + FTS) with **Cross-Encoder Reranking** and **Recursive Chunking**.
- **Sales Automation:** Lead qualification, **Lead Scoring** (Hot/Warm/Cold), and automated **Slack Summaries**.
- **Knowledge Base:** Integration via **MCP (Model Context Protocol)** for Notion & Postgres.
- **Observability:** Full request tracing and cost tracking using **Langfuse**.
- **Security:** Middleware layer for **PII-sanitization** (email/phone masking).
- **Reliability:** `tenacity` retry logic for API fault tolerance.
- **DevOps:** CI/CD pipeline via **GitHub Actions** and Dockerized infrastructure.

## Tech Stack
- **AI Core:** LangGraph, LangChain, Groq (Llama-3.3-70B) for cloud-based inference, and support for local LLMs via LM Studio (Llama-3/Phi-3).
- **RAG:** PostgreSQL, pgvector, ChromaDB, RecursiveCharacterTextSplitter.
- **Backend:** FastAPI, Python 3.13.
- **Integrations:** Slack, Airtable, Notion (MCP).
- **DevOps:** Docker, GitHub Actions CI/CD.

## Proof of Work
*(Здесь вставь свои скриншоты: Slack-ответ, трейсы в Langfuse)*
![Slack Response](assets/slack_demo.png)
![Langfuse Traces](assets/langfuse_trace.png)

## Documentation
Detailed technical documentation is available in the `/docs` folder:
- [Architecture](docs/ARCHITECTURE.md)
- [Security & PII](docs/SECURITY.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## Project Structure
- **`src/`**
  - `orchestrator/`: `graph.py` (workflow), `nodes.py` (agent logic), `state.py` (shared state).
  - `tools/`: MCP-based tools (`airtable_tool`, `rag_tool`, `notion_tool`, `slack_tool`).
  - `utils/`: `embedder.py` (vectorization), `reranker.py` (ranking), `sanitizer.py` (PII masking).
- **`data/`**: Scripts for database initialization (`init_db.py`) and RAG ingestion (`populate_embeddings.py`).
- **`docs/`**: Technical documentation (Architecture, Deployment, Security).
- **`assets/`**: Screenshots of system performance (Slack responses, Langfuse traces).
