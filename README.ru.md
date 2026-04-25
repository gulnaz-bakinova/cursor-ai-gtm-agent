# Автономная система агентов GTM

*🇺🇸 [English Version](README.md)*

> Пет-проект: Автономный AI-ассистент для GTM-процессов, объединяющий мультиагентные рабочие процессы с использованием LangGraph, RAG на базе pgvector и синхронизацию CRM в реальном времени.

![LangGraph](https://img.shields.io/badge/LangGraph-MultiAgent-blue?style=flat-square)
![RAG](https://img.shields.io/badge/RAG-Hybrid_Search-green?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-Protocol-purple?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-success?style=flat-square)
![Cursor](https://img.shields.io/badge/Cursor-IDE-black?style=flat-square)
![Observability](https://img.shields.io/badge/Langfuse-Traces-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-MVP-brightgreen?style=flat-square)

## Обзор
Этот проект представляет собой автономную AI-систему для автоматизации GTM-процессов, разработанную в Cursor. Она управляет специализированными агентами для автоматизации квалификации продаж (Airtable CRM) и управления знаниями (RAG через Postgres/Notion).

## Ключевые инженерные особенности
| Функция | Описание |
|----------|-------------|
| **Оркестрация** | Маршрутизация между мультиагентами через **LangGraph** (конечный автомат, умная маршрутизация, вызов инструментов). |
| **Продвинутый RAG** | Семантический поиск с использованием **Recursive Character Chunking**, **Гибридного поиска** (Вектор + FTS) и **Cross-Encoder Reranking**. |
| **Автоматизация продаж** | Квалификация лидов, **Скоринг лидов** (Hot/Warm/Cold) и автоматизированные **Slack-отчеты**. |
| **База знаний** | Интеграция через **MCP (Model Context Protocol)** для Notion и Postgres. |
| **Автоматизация данных** | Логика автоматического разбиения на страницы (Pagination) для API Airtable для работы с большими данными. |
| **Проактивная отчетность** | Конвейер автоматизированных отчетов [`src/scripts/send_summary.py`](src/scripts/send_summary.py) для ежедневной CRM-аналитики. |
| **Мониторинг** | Полная трассировка запросов и отслеживание затрат с помощью **Langfuse**. |
| **Безопасность** | Middleware-слой для **PII-санитайзера** (маскировка email/телефонов). |
| **Надежность** | Логика повторных попыток (Retry logic) через `tenacity` для обеспечения отказоустойчивости API. |
| **DevOps** | CI/CD пайплайн через **GitHub Actions** и инфраструктура в Docker. |

## Технологический стек
- **AI Core:** LangGraph, LangChain, Groq (Llama-3.3-70B) для облачных вычислений, поддержка локальных LLM через LM Studio (Llama-3/Phi-3).
- **Разработка:** Подход **Spec-first** с использованием Pydantic-схем.
- **RAG:** PostgreSQL, pgvector, ChromaDB, RecursiveCharacterTextSplitter.
- **Backend:** FastAPI, Python 3.13.
- **Интеграции:** Slack, Airtable, Notion (MCP).
- **DevOps:** Docker, GitHub Actions CI/CD.

## Демонстрация системы
Визуальное подтверждение работы системы:

- **Slack Interaction:** Интерфейс для общения в реальном времени.
- **Monitoring:** Трассировка в реальном времени и трекинг затрат в Langfuse.

![Slack Demo](assets/slack_demo.png)
![Langfuse Traces](assets/langfuse_trace.png)

## Документация
Подробная техническая документация доступна в папке [`/docs`](/docs):
*   [📄 ARCHITECTURE.md](docs/ARCHITECTURE.md) — Проектирование системы, схемы потоков данных и спецификации.
*   [🔌 INTEGRATIONS.md](docs/INTEGRATIONS.md) — Спецификации API для Airtable, Notion и Slack.
*   [🔐 SECURITY.md](docs/SECURITY.md) — Слой защиты данных, PII-санитайзер и управление секретами.
*   [🧪 TEST_SCENARIOS.md](docs/TEST_SCENARIOS.md) — Сценарии функционального тестирования и метрики оценки.
*   [📖 RUNBOOK.md](docs/RUNBOOK.md) — Руководство по устранению неполадок и обслуживанию.
*   [🚀 DEPLOYMENT.md](docs/DEPLOYMENT.md) — Пошаговое руководство по настройке инфраструктуры.

## Структура проекта
- **[`src/`](src/)**
  - [`orchestrator/`](src/orchestrator/): рабочие процессы, логика агентов, состояние системы.
  - [`tools/`](src/tools/): MCP-инструменты (Airtable, Notion, RAG, Slack).
  - [`utils/`](src/utils/): вспомогательные функции (эмбеддинги, ранжирование, санитайзер).
- **[`data/`](data/)**: Скрипты инициализации БД и загрузки знаний.
- **[`docs/`](docs/)**: Техническая документация.
- **[`assets/`](assets)**: Демонстрационные материалы.

---

### 👤 Автор

**Гульназ Бакинова**

*AI Automation & Applied AI Engineer · Сквозная автоматизация продаж, поддержки и операционных процессов*

Давайте общаться!
[LinkedIn](https://www.linkedin.com/in/gulnaz-bakinova/) 

*Этот репозиторий предоставлен исключительно в целях демонстрации портфолио.*
