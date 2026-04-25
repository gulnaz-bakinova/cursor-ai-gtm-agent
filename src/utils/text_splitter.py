from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_text_chunks(text: str) -> list[str]:
    # Нарезаем так, чтобы куски были по 500 символов с нахлестом 50 символов
    # Это позволяет не терять смысл на стыках кусков
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    )
    return splitter.split_text(text)