import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

def search_notion(query: str) -> str:
    # Явно указываем версию API, чтобы Notion понял твой новый токен
    notion = Client(auth=os.getenv("NOTION_TOKEN"), notion_version="2022-06-28")
    try:
        results = notion.search(query=query).get("results")
        if not results:
            return "В Notion ничего не найдено."
        
        # Получаем заголовок
        page = results[0]
        # Проверяем структуру свойств (в разных типах страниц она может быть разной)
        title = "Без названия"
        if "properties" in page:
            props = page["properties"]
            # Обычно заголовок лежит в первом попавшемся свойстве типа "title"
            for prop in props.values():
                if prop["type"] == "title":
                    title = prop["title"][0]["plain_text"]
                    break
        return f"Нашел страницу в Notion: {title}"
    except Exception as e:
        return f"Ошибка при поиске в Notion: {str(e)}"