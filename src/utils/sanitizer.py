import re

def sanitize_text(text: str) -> str:
    """Очищает строку от email и телефонов."""
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    phone_pattern = r'(\+7|8)[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}'
    
    text = re.sub(email_pattern, '[EMAIL_HIDDEN]', text)
    text = re.sub(phone_pattern, '[PHONE_HIDDEN]', text)
    return text