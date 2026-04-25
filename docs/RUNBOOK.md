# Runbook: Troubleshooting & Maintenance

A quick guide to solving common issues with the GTM Agent System.

## 1. Bot not responding in Slack
- **Check Server Status:** Is `uvicorn` running in the terminal? 
- **Check Network:** Is `ngrok` active and the URL copied to Slack Event Subscriptions?
- **Check Logs:** Look at the uvicorn terminal.
  - If you see `500 Internal Server Error`, check for `Connection Error` (LLM API issues).
  - If you see `ModuleNotFoundError`, ensure the virtual environment (`.venv`) is activated.

## 2. Model "Hallucinations" (Generic answers)
- **Problem:** The model ignores the RAG context.
- **Solution:** Adjust the `system_prompt` in `nodes.py` to be more restrictive ("Use ONLY provided context...").
- **Tip:** Ensure the `knowledge_base` table in PostgreSQL is populated with embeddings using `data/populate_embeddings.py`.

## 3. Database Connection Issues
- **Problem:** `Connection refused`.
- **Solution:** Ensure `docker-compose up -d` has been executed. Check container status: `docker-compose ps`.
