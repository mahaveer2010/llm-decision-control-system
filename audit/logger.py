import json
from audit.decision_record import DecisionRecord


def log_decision(record: DecisionRecord) -> None:
    """
    Logs a decision record in structured form.
    """

    log_entry = {
        "user_query": record.user_query,
        "decision": record.decision,
        "reason": record.reason,
        "stage": record.stage,
        "confidence": record.confidence,
    }

    print(json.dumps(log_entry))
