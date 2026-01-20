from dataclasses import dataclass
from typing import Optional


@dataclass
class DecisionRecord:
    user_query: str
    decision: str
    reason: str
    stage: str
    confidence: Optional[float] = None
