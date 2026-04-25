# Security & Privacy

This project implements a multi-layer security approach to protect sensitive user information when interacting with LLMs.

## 1. PII-Sanitization Layer
To prevent accidental leakage of personal identifiable information (PII), we use a dedicated sanitization layer:
- **Automatic Masking:** All outgoing agent responses are processed through `sanitize_text` before reaching Slack.
- **Rules:** The system automatically detects and masks `email` addresses and `phone numbers`.
- **Placeholder:** Detected sensitive data is replaced with `[EMAIL_HIDDEN]` or `[PHONE_HIDDEN]`.

## 2. API Security
- **Credential Management:** All secrets (API Keys, Tokens) are managed via environment variables (`.env`).
- **No-Logging Policy:** We explicitly configured the system to avoid logging raw PII in persistent logs, using masking techniques instead.
