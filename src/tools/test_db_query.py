from src.tools.knowledge_tool import search_knowledge_base

# Проверим прямо SQL-запрос
result = search_knowledge_base("Notion")
print(f"Результат поиска: {result}")