import psycopg2
import os
from dotenv import load_dotenv
from src.utils.embedder import get_embedding

load_dotenv()

def ingest_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Очень простой "чанкинг" (нарезка по 500 символов)
    # Для портфолио можно сказать, что это "Fixed-size chunking"
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()
    
    for chunk in chunks:
        if len(chunk.strip()) < 50: continue # Пропускаем совсем мелкий мусор
        
        vector = get_embedding(chunk)
        cursor.execute(
            "INSERT INTO knowledge_base (content, embedding) VALUES (%s, %s);",
            (chunk, vector)
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Успешно загружено {len(chunks)} чанков.")

if __name__ == "__main__":
    ingest_file("knowledge_source.txt")