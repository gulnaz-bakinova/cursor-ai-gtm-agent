from __future__ import annotations

import os
import re

import psycopg2
from dotenv import load_dotenv
from src.utils.embedder import get_embedding # Добавили импорт

def _connect():
    load_dotenv()
    database_url = os.getenv("DATABASE_URL")
    conn_kwargs = {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "5432")),
        "dbname": os.getenv("DB_NAME", "ai_gtm"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "password123"),
    }
    if database_url:
        return psycopg2.connect(database_url)
    return psycopg2.connect(**conn_kwargs)

def search_knowledge_base(query: str) -> list[str]:
    # 1. Получаем вектор запроса
    query_vector = get_embedding(query)
    
    # 2. Инициализируем подключение и курсор
    conn = _connect()
    cursor = conn.cursor()
    
    # 3. Выполняем поиск
    cursor.execute(
        "SELECT content FROM knowledge_base ORDER BY embedding <=> %s::vector LIMIT 5;", 
        (query_vector,)
    )
    rows = cursor.fetchall()
    
    # 4. Закрываем подключение
    cursor.close()
    conn.close()
    
    return [row[0] for row in rows]