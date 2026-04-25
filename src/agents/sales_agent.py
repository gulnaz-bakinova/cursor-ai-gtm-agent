import os
from src.tools.airtable_tool import search_leads
from src.tools.slack_tool import send_slack_message

def process_daily_sales_summary():
    """Функция для формирования отчета по продажам."""
    # Допустим, мы хотим получить отчет по всем лидам
    # Для теста пока используем конкретный email, позже сделаем выборку всех "New"
    lead = search_leads("anna@gmail.com") 
    
    if lead and lead.get("success"):
        record = lead.get("record")
        message = f"📊 *Ежедневный отчет по лидам:*\nЛид: {record.get('fields', {}).get('Name')}\nСтатус: {record.get('fields', {}).get('Status')}"
        send_slack_message(message)
        print("Отчет отправлен в Slack!")
    else:
        print("Лиды не найдены, отчет не отправлен.")