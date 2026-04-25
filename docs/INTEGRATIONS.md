# Integrations & API Overview

This project integrates several third-party services to create an autonomous GTM workflow.

## 1. Slack
- **Purpose:** Primary communication channel for agents and daily reporting.
- **Integration Method:** Events API (inbound) and `chat.postMessage` (outbound).
- **Required Scopes:** `channels:history`, `chat:write`, `incoming-webhook`.
- **Security:** Incoming Webhook URL is stored in environment variables.

## 2. Airtable CRM
- **Purpose:** Source of truth for lead data and status tracking.
- **Integration Method:** REST API.
- **Functionality:** Real-time lead lookup by email with automated pagination handling.
- **Security:** Managed via Personal Access Token with specific `data.records:read/write` scope.

## 3. Notion
- **Purpose:** Knowledge base for technical documentation and internal guidelines.
- **Integration Method:** Official Notion SDK (MCP-compatible pattern).
- **Configuration:** Requires an Internal Integration Secret (`ntn_...`) and explicit page access in Notion settings.

## 4. LLM Infrastructure
- **Cloud Provider:** Groq (Llama-3.3-70B-versatile).
- **Local/Development:** LM Studio (compatible with OpenAI-API protocol).
- **Observability:** Langfuse (SDK-based tracing).
