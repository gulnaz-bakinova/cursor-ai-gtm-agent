from sentence_transformers import CrossEncoder

# Загружаем модель переранжирования
model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank_results(query: str, documents: list[str]) -> list[str]:
    """Сортирует документы по их релевантности запросу."""
    if not documents:
        return []
    # Создаем пары (запрос, документ)
    pairs = [(query, doc) for doc in documents]
    # Получаем оценки релевантности
    scores = model.predict(pairs)
    # Сортируем документы по убыванию оценки
    ranked = sorted(zip(scores, documents), key=lambda x: x[0], reverse=True)
    return [doc for score, doc in ranked]