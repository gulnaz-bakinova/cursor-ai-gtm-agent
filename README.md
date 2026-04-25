# Cursor-built Autonomous GTM Agent System

Autonomous Go-To-Market AI assistant orchestrating multi-agent workflows with LangGraph, pgvector RAG, and real-time CRM synchronization.

## Key Engineering Highlights
- **Multi-Agent Orchestration:** LangGraph-powered routing between Sales and Knowledge agents.
- **Advanced RAG Pipeline:** Hybrid Semantic Search (pgvector + full-text) with Cross-Encoder reranking for 20-30% higher accuracy.
- **Observability:** Full-stack tracing & cost logging via Langfuse SDK.
- **Security:** Automated PII-sanitization (email/phone masking) using regex-based middleware.
- **Resilience:** Built-in automatic retry logic (tenacity) for external API calls (Notion, Airtable, Groq).
- **Standards:** MCP-based tool architecture for modular integration.

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

## 📖 Documentation
Detailed technical documentation is available in the `/docs` folder:
- [Architecture](docs/ARCHITECTURE.md)
- [Security & PII](docs/SECURITY.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
