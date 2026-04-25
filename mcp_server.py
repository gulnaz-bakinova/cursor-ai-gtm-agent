from mcp.server.fastmcp import FastMCP
from src.tools.notion_tool import search_notion # Берем твою готовую функцию поиска

# Создаем MCP сервер
mcp = FastMCP("Notion-Agent-Server")

# Регистрируем инструмент, чтобы агент его "видел"
@mcp.tool()
async def search_notion_tool(query: str) -> str:
    """Ищет информацию в Notion по запросу пользователя."""
    return search_notion(query)

if __name__ == "__main__":
    # Запуск сервера
    mcp.run()

print("MCP server is running and tool 'notion_search' is registered")