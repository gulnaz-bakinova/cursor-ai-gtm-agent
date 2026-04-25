from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from src.orchestrator.nodes import classify_node, knowledge_node, sales_node
from src.orchestrator.state import OrchestratorState


def route_by_classification(state: OrchestratorState) -> str:
    classification = state["classification"]

    if classification not in {"sales", "knowledge"}:
        raise ValueError(
            f"Unexpected classification in state: {classification!r}. "
            "Expected 'sales' or 'knowledge'."
        )

    return classification


def build_graph():
    graph = StateGraph(OrchestratorState)

    graph.add_node("classify", classify_node)
    graph.add_node("sales", sales_node)
    graph.add_node("knowledge", knowledge_node)

    graph.add_edge(START, "classify")
    graph.add_conditional_edges(
        "classify",
        route_by_classification,
        {
            "sales": "sales",
            "knowledge": "knowledge",
        },
    )
    graph.add_edge("sales", END)
    graph.add_edge("knowledge", END)

    return graph.compile()