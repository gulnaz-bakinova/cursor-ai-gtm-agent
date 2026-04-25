from __future__ import annotations

import operator
from typing import Annotated, Literal, TypedDict

from langchain_core.messages import BaseMessage


class OrchestratorState(TypedDict):
    """Shared state passed between LangGraph nodes."""

    # исходный запрос пользователя
    input_query: str

    # результат классификации оркестратора
    classification: Literal["sales", "knowledge"]

    # итоговый ответ пользователю
    final_answer: str

    # история сообщений (LangGraph будет "склеивать" списки через operator.add)
    messages: Annotated[list[BaseMessage], operator.add]    