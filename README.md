# Cursor-built Autonomous GTM Agent System

> Pet progect: Autonomous Go-To-Market AI assistant orchestrating multi-agent workflows with LangGraph, pgvector RAG, and real-time CRM synchronization.

![LangGraph](https://img.shields.io/badge/LangGraph-MultiAgent-blue?style=flat-square)
![RAG](https://img.shields.io/badge/RAG-Hybrid_Search-green?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-Protocol-purple?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-success?style=flat-square)
![Cursor](https://img.shields.io/badge/Cursor-IDE-black?style=flat-square)
![Observability](https://img.shields.io/badge/Langfuse-Traces-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-MVP-brightgreen?style=flat-square)

## Overview
This project is an autonomous GTM AI system developed in Cursor. It orchestrates specialized agents to automate sales qualification (Airtable CRM) and knowledge management (RAG over Postgres/Notion).

## Key Engineering Features
| Feature | Details |
|----------|-------------|
| **Orchestration** | Multi-agent routing via **LangGraph** (State Machine, intelligent routing, tool calling). |
| **Advanced RAG** | Semantic search with **Recursive Character Chunking**, **Hybrid Search** (Vector + FTS), and **Cross-Encoder Reranking**. |
| **Sales Automation** | Lead qualification, **Lead Scoring** (Hot/Warm/Cold), and automated **Slack Summaries**. |
| **Knowledge Base** | Integration via **MCP (Model Context Protocol)** for Notion & Postgres. |
| **Sales Automation** | Lead qualification, automated **Lead Scoring** (Hot/Warm/Cold), and proactive Slack reporting. |
| **Data Pagination** | Auto-paging logic for Airtable API integration to handle large-scale datasets. |
| **Proactive Reporting** | Automated sales summary pipeline [`src/scripts/send_summary.py`](src/scripts/send_summary.py) for daily CRM insights. |
| **Observability** | Full request tracing and cost tracking using **Langfuse**.  |
| **Security** | Middleware layer for **PII-sanitization** (email/phone masking). |
| **Reliability** | `tenacity` retry logic for API fault tolerance. |
| **DevOps** | CI/CD pipeline via **GitHub Actions** and Dockerized infrastructure. |

## Tech Stack
- **AI Core:** LangGraph, LangChain, Groq (Llama-3.3-70B) for cloud-based inference, and support for local LLMs via LM Studio (Llama-3).
- **Development:** Built with a **Spec-first approach** using Pydantic schemas.
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
*   [📄 ARCHITECTURE.md](docs/ARCHITECTURE.md) — System design, data flow diagrams, and spec-first approach details.
*   [🔌 INTEGRATIONS.md](docs/INTEGRATIONS.md) — API specifications for Airtable, Notion, and Slack.
*   [🔐 SECURITY.md](docs/SECURITY.md) — Privacy layer, PII-sanitization, and credential management.
*   [🧪 TEST_SCENARIOS.md](docs/TEST_SCENARIOS.md) — Functional test cases and evaluation metrics.
*   [📖 RUNBOOK.md](docs/RUNBOOK.md) — Troubleshooting guide and maintenance procedures.
*   [🚀 DEPLOYMENT.md](docs/DEPLOYMENT.md) — Step-by-step setup and infrastructure guide.

## Project Structure
- **[`src/`](src/)**
  - [`orchestrator/`](src/orchestrator/): `graph.py` (workflow), `nodes.py` (agent logic), `state.py` (shared state).
  - [`tools/`](src/tools/): MCP-based tools (`airtable_tool`, `rag_tool`, `notion_tool`, `slack_tool`).
  - [`utils/`](src/utils/): `embedder.py` (vectorization), `reranker.py` (ranking), `sanitizer.py` (PII masking).
- **[`data/`](data/)**: Scripts for database initialization (`init_db.py`) and RAG ingestion (`populate_embeddings.py`).
- **[`docs/`](docs/)**: Technical documentation (Architecture, Deployment, Integrations, Runbook, Security).
- **[`assets/`](assets)**: Screenshots of system performance (Slack responses, Langfuse traces).

---

### 👤 Author

**Gulnaz Bakinova**

*AI Automation & Applied AI Engineer · End-to-end automation for sales / support / ops*

Let's connect!
[LinkedIn](https://www.linkedin.com/in/gulnaz-bakinova/) 

*This repository is provided for portfolio and demonstration purposes only*
