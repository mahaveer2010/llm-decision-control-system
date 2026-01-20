from enum import Enum
from typing import Tuple


class Decision(Enum):
    ALLOW = "allow"
    REFUSE = "refuse"
    CLARIFY = "clarify"
    ESCALATE = "escalate"


def decide(user_query: str, context: dict | None = None) -> Tuple[Decision, str]:
    """
    Determines whether the system should proceed with an LLM call.
    Returns a decision and a human-readable reason.
    """

    # 1. Empty or meaningless input
    if not user_query or len(user_query.strip()) < 5:
        return Decision.CLARIFY, "Input too short or unclear."

    # 2. Obvious out-of-scope intent (placeholder)
    if "illegal" in user_query.lower():
        return Decision.REFUSE, "Query violates policy constraints."

    # 3. High ambiguity (placeholder)
    if user_query.endswith("?") and "or" in user_query.lower():
        return Decision.CLARIFY, "Ambiguous intent detected."

    # 4. Default allow
    return Decision.ALLOW, "Intent within acceptable bounds."
