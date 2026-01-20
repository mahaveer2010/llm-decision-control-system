def confidence_ok(confidence: float) -> bool:
    """
    Checks whether the model's confidence is within acceptable bounds.
    """

    if not isinstance(confidence, (int, float)):
        return False

    if confidence < 0.4:
        return False

    if confidence > 0.95:
        # suspicious overconfidence
        return False

    return True
