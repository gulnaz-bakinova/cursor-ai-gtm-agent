from __future__ import annotations
import re
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from src.orchestrator.state import OrchestratorState
from src.tools.airtable_tool import search_leads
from src.tools.knowledge_tool import search_knowledge_base
from src.tools.notion_tool import search_notion 
from src.tools.rag_tool import query_rag_base 
from src.utils.sanitizer import sanitize_text
from tenacity import retry, stop_after_attempt, wait_exponential
from src.utils.reranker import rerank_results # Импортируй


load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

_EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

def _extract_email_from_query(query: str) -> str:
    m = _EMAIL_RE.search(query)
    return m.group(0).strip().lower() if m else "anna@gmail.com"

def classify_node(state: OrchestratorState) -> dict:
    query = state.get("input_query", "")
    prompt = (
        'Ты — классификатор запросов. Определи категорию. '
        'Если вопрос про покупку, цены, клиентов — верни "sales". '
        'Если вопрос про инструкции, тикеты — верни "knowledge". '
        f"Запрос: {query}. Верни только одно слово."
    )
    response = llm.invoke([{"role": "user", "content": prompt}])
    text = response.content.lower()
    return {"classification": "sales" if "sales" in text else "knowledge"}

def sales_node(state: OrchestratorState) -> dict:
    query = state.get("input_query", "") or ""
    email = _extract_email_from_query(query)
    result = search_leads(email)

    if result.get("success") is True and result.get("record"):
        record = result["record"]
        fields = record.get("fields") or {}
        name = fields.get("Name") or "—"
        status = fields.get("Status") or "—"
        # Безопасно получаем бюджет (пытаемся превратить в число)
        raw_budget = fields.get("Budget") or fields.get("budget") or 0
        try:
            budget = float(raw_budget)
        except ValueError:
            budget = 0
            
        # Логика скоринга
        if budget >= 500000:
            score = "🔥 ГОРЯЧИЙ"
        elif budget >= 100000:
            score = "📈 ТЕПЛЫЙ"
        else:
            score = "❄️ ХОЛОДНЫЙ"
            
        final_answer = (
            f"Нашел лида: {name}.\n"
            f"Статус: {status}.\n"
            f"Бюджет: {budget}.\n"
            f"Скоринг: {score}"
        )
    else:
        final_answer = "К сожалению, в CRM нет лида с таким email"

    return {"final_answer": sanitize_text(final_answer)}

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
def knowledge_node(state: OrchestratorState) -> dict:
    query = state.get("input_query", "")
    
    # 1. Получаем 5 кандидатов через Hybrid Search
    candidates = query_rag_base(query)
    
    # 2. Переранжируем (выбираем лучший)
    ranked = rerank_results(query, candidates)
    best_doc = ranked[0] if ranked else "К сожалению, у меня нет информации."
    
    # 3. Отправляем в LLM
    system_prompt = f"Ты — ассистент. Используй этот контекст: {best_doc}"

    # Здесь теперь есть "умные повторы"
    response = llm.invoke(
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ]
    )

    return {"final_answer": sanitize_text(response.content.strip())}