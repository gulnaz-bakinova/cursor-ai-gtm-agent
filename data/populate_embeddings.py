import psycopg2
import os
from dotenv import load_dotenv
from src.utils.embedder import get_embedding
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()

def populate_embeddings():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()
    
    # Берем все записи, где embedding пустой
    cursor.execute("SELECT id, content FROM knowledge_base WHERE embedding IS NULL;")
    rows = cursor.fetchall()
    
    for row in rows:
        id, content = row
        print(f"Обработка записи {id}...")
        
        # Генерируем вектор
        vector = get_embedding(content)
        
        # Обновляем запись в базе
        cursor.execute(
            "UPDATE knowledge_base SET embedding = %s WHERE id = %s;",
            (vector, id)
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Готово! Обработано записей: {len(rows)}")

if __name__ == "__main__":
    populate_embeddings()

def ingest_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Создаем "умный" нарезатель
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )
    
    chunks = text_splitter.split_text(text)
    
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()
    
    for chunk in chunks:
        vector = get_embedding(chunk)
        cursor.execute(
            "INSERT INTO knowledge_base (content, embedding) VALUES (%s, %s);",
            (chunk, vector)
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Готово! Загружено {len(chunks)} умных чанков.")