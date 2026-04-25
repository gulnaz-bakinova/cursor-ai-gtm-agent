import os
import requests
from dotenv import load_dotenv

load_dotenv()

def search_leads(email: str) -> dict:
    api_key = os.getenv("AIRTABLE_API_KEY")
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("AIRTABLE_TABLE_NAME")
    
    # Прямой запрос к API без сложных формул
    url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        records = response.json().get("records", [])
        
        # Перебираем все записи и смотрим в поля
        for record in records:
            fields = record.get("fields", {})
            # Ищем во всех значениях полей, вдруг email спрятан в поле с другим именем
            for val in fields.values():
                if str(val).lower() == email.lower():
                    return {"success": True, "message": "Lead found.", "record": record}
        
        return {"success": True, "message": "Lead not found.", "record": None}
        
    except Exception as e:
        return {"success": False, "message": f"Ошибка: {str(e)}"}