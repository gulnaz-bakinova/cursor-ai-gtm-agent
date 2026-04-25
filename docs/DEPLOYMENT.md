# Deployment Guide

This project is designed as a modular, containerized AI agent system.

## 1. Prerequisites
- **Python 3.12+**
- **Docker Desktop**
- **API Keys:** Groq (for LLM), Airtable (for CRM), Notion (for Knowledge).

## 2. Environment Setup
Create a `.env` file in the root directory using [.env.example](/.env.example) as a template:

```bash
DATABASE_URL=postgresql://postgres:password123@localhost:5432/ai_gtm
GROQ_API_KEY=your_key_here
LANGFUSE_SECRET_KEY=your_key_here
LANGFUSE_PUBLIC_KEY=your_key_here
AIRTABLE_API_KEY=your_key_here
AIRTABLE_BASE_ID=your_id_here
AIRTABLE_TABLE_NAME=Leads
NOTION_TOKEN=your_token_here
SLACK_WEBHOOK_URL=your_webhook_url
SLACK_BOT_TOKEN=your_xoxb_token
```
## 3. Infrastructure (PostgreSQL)

We use Docker for containerized database management with pgvector support.

```bash
docker-compose up -d
```

## 4. Application Setup

1. **Virtual Environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Initialize Database & RAG:**

```bash
python3 data/init_db.py
python3 data/populate_embeddings.py
```

## 5. Running the Application

### Option A: Cloud-based LLM (Recommended for Production)

The system is configured to work with Groq (Llama-3.3-70B) for high performance:

```bash
./.venv/bin/python3 -m uvicorn src.main:app
```

### Option B: Local LLM (Development/Offline)

You can run models locally using LM Studio.

1. Launch LM Studio and start the "Local Server" on `http://127.0.0.1:1234/v1`.
2. Ensure a model (e.g., Llama-3) is loaded.
3. Update `src/orchestrator/nodes.py` to point to the local API endpoint.
