from typing import Optional

from classifier import ClassificationResult


class ReportGenerator:
    def __init__(self) -> None:
        self.last_report: Optional[ClassificationResult] = None

    def generate(self, result: ClassificationResult) -> str:
        self.last_report = result
        return (
            f"Detected Plant: {result.common_name}\n"
            f"Scientific Name: {result.scientific_name}\n"
            f"Confidence: {result.confidence:.2f}\n"
            f"Description: {result.description}\n"
            f"Uses: {result.uses}\n"
            f"Medicinal: {'Yes' if result.medicinal else 'No'}"
        )
