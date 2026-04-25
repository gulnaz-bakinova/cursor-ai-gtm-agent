from sentence_transformers import SentenceTransformer

# Загружаем легкую модель для эмбеддингов
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str) -> list[float]:
    """Превращает текст в список чисел (вектор)."""
    # .tolist() нужен, чтобы превратить объект numpy в обычный список Python
    return model.encode(text).tolist()