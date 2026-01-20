def consistency_ok(answer: str) -> bool:
    """
    Performs basic consistency checks on the answer text.
    """

    if not isinstance(answer, str):
        return False

    if len(answer.strip()) < 20:
        return False

    # Placeholder for deeper checks
    banned_phrases = ["as an ai model", "i cannot"]

    for phrase in banned_phrases:
        if phrase in answer.lower():
            return False

    return True
