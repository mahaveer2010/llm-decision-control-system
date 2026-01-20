from typing import Tuple


def violates_policy(user_query: str) -> Tuple[bool, str]:
    """
    Returns (True, reason) if the query violates a hard policy constraint.
    """

    lowered = user_query.lower()

    # Example: illegal or harmful intent
    banned_keywords = ["illegal", "harm", "exploit", "bypass"]

    for word in banned_keywords:
        if word in lowered:
            return True, f"Policy violation detected: '{word}'"

    return False, "No policy violations detected."
