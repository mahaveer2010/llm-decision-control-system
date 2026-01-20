def should_stop(
    attempt_count: int,
    max_attempts: int,
    uncertainty_score: float
) -> bool:
    """
    Determines whether the system should stop further processing.
    """

    if attempt_count >= max_attempts:
        return True

    if uncertainty_score > 0.7:
        return True

    return False
