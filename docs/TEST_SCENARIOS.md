# Test Scenarios

This document outlines the core functional tests used to verify the AI GTM Agent System.

| Scenario | Input Query | Expected Behavior |
| :--- | :--- | :--- |
| **Sales Query** | "Find lead anna@gmail.com" | Agent routes to `sales_node`, queries Airtable, returns lead details with status/budget. |
| **Knowledge Query** | "How to setup Slack?" | Agent routes to `knowledge_node`, retrieves context from PostgreSQL, answers correctly. |
| **Notion RAG** | "What is AI agent in WhatsApp?" | Agent retrieves data from Notion (MCP tool), LLM generates a response. |
| **PII Protection** | "Data for anna@gmail.com" | Bot identifies email, searches Airtable, returns response with email masked as `[EMAIL_HIDDEN]`. |
| **Error Handling** | "Unknown query" | Agent uses system prompt to respond: "К сожалению, у меня нет информации в базе знаний." |
| **System Resilience** | API timeout / 502 error | `tenacity` retry decorator attempts the Groq/API call up to 3 times before failing gracefully. |

## Evaluation Strategy
We maintain system quality and performance using the following metrics:
- **Performance:** Measured by **Response Latency** via Langfuse Traces (monitoring the time taken from Slack webhook to message delivery).
- **Quality:** Measured by **Context Recall** (manual verification of whether the retrieved RAG context actually contains the answer).
- **Stability:** Monitored via **Error Rate** and system logs in production.

## How to execute tests
1. **Unit tests:** Use `python3 data/test_airtable.py` for CRM verification.
2. **Integration tests:** Send queries via Slack and observe the `DEBUG` logs in the FastAPI terminal.
3. **Observability:** Verify trace generation in the [Langfuse Dashboard](https://cloud.langfuse.com/).
