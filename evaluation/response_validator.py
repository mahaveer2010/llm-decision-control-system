from typing import Dict, Tuple
from evaluation.confidence_checks import confidence_ok
from evaluation.consistency_checks import consistency_ok


def validate_response(response: Dict) -> Tuple[bool, str]:
    """
    Validates an LLM response.
    Returns (True, reason) if accepted, (False, reason) if rejected.
    """

    if not isinstance(response, dict):
        return False, "Response is not a structured object."

    required_fields = ["answer", "confidence"]

    for field in required_fields:
        if field not in response:
            return False, f"Missing required field: {field}"

    if not confidence_ok(response["confidence"]):
        return False, "Confidence below acceptable threshold."

    if not consistency_ok(response["answer"]):
        return False, "Response failed consistency checks."

    return True, "Response passed validation."
