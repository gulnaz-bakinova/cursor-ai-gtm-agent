import traceback
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, BackgroundTasks
from langfuse import Langfuse
from pydantic import BaseModel
from src.utils.sanitizer import sanitize_text
from src.tools.slack_tool import send_slack_message, reply_to_slack
from src.orchestrator.graph import build_graph
from langchain_groq import ChatGroq


load_dotenv()
langfuse = Langfuse()
app = FastAPI()

class ChatRequest(BaseModel):
    query: str

def process_chat_message(channel_id: str, query: str):
    graph = build_graph()
    result = graph.invoke({"input_query": query})
    final_answer = result.get("final_answer", "Я не знаю ответа.")
    
    # Теперь вызываем правильную функцию sanitize_text
    safe_answer = sanitize_text(final_answer)
    
    if channel_id:
        reply_to_slack(channel_id, safe_answer) 

@app.get("/")
async def root():
    return {"message": "AI GTM Agent System is running"}


@app.post("/chat")
async def chat(payload: dict, background_tasks: BackgroundTasks):
    if payload.get("type") == "url_verification":
        return {"challenge": payload.get("challenge")}

    event = payload.get("event", {})
    query = event.get("text")
    channel_id = event.get("channel")
    
    if not query or event.get("bot_id"):
        return {"status": "ok"}

    background_tasks.add_task(process_chat_message, channel_id, query)
    return {"status": "ok"}
