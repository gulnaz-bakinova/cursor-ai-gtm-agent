import os
from src.tools.airtable_tool import search_leads
from src.tools.slack_tool import send_slack_message
from dotenv import load_dotenv

load_dotenv()

def send_daily_summary():
    # 1. Получаем всех лидов (используем наш новый инструмент с пагинацией)
    # Передаем пустую строку, чтобы получить всё или используем метод getAll
    # Если в твоем airtable_tool есть метод getAll - используй его
    # Если нет, давай "схитрим" и поищем по пустому значению, если метод позволяет
    
    # Давай создадим прямо в slack_tool или здесь простую функцию для получения всех лидов
    # Для теста сейчас просто вызовем поиск по конкретному email, 
    # чтобы проверить отправку отчета:
    
    result = search_leads("anna@gmail.com") 
    
    if result.get("success") and result.get("record"):
        record = result["record"]
        fields = record.get("fields", {})
        message = (
            "🚀 *Ежедневный отчет по продажам:*\n"
            f"Найден важный лид: {fields.get('Name', 'Без имени')}\n"
            f"Статус: {fields.get('Status', 'Неизвестен')}\n"
            f"Бюджет: {fields.get('Budget', 0)}"
        )
        send_slack_message(message)
        print("Саммари успешно отправлено в Slack!")
    else:
        print("Лидов для отчета не найдено.")

if __name__ == "__main__":
    send_daily_summary()