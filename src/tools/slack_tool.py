import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_slack_message(text: str) -> bool:
    # Старый метод через Webhook (оставляем для отчетов)
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    return requests.post(webhook_url, json={"text": text}).status_code == 200

def reply_to_slack(channel_id: str, text: str):
    token = os.getenv("SLACK_BOT_TOKEN")
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"channel": channel_id, "text": text}
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code != 200:
        print(f"DEBUG: Ошибка Slack API: {response.text}") # Мы увидим причину здесь
    else:
        print("DEBUG: Ответ в Slack успешно отправлен!")