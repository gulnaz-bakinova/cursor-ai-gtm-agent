import psycopg2
import os
from dotenv import load_dotenv
from src.utils.embedder import get_embedding
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

# Инициализируем те же эмбеддинги, что использовались при создании базы
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def query_rag_base(query: str) -> list[str]:
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()
    
    query_vector = get_embedding(query)
    
    # 0.7 - вес вектора, 0.3 - вес текстового поиска
    sql = """
        SELECT content 
        FROM knowledge_base 
        ORDER BY (embedding <=> %s::vector) * 0.7 + (1.0 / (1.0 + ts_rank(to_tsvector('russian', content), plainto_tsquery('russian', %s)))) * 0.3
        LIMIT 5;
    """
    
    cursor.execute(sql, (query_vector, query))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [row[0] for row in rows]