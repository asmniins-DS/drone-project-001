import cv2
import numpy as np

from classifier import Classifier, ClassificationResult


class PlantDetector:
    def __init__(self, classifier: Classifier | None = None) -> None:
        self.classifier = classifier or Classifier()

    def detect(self, frame: np.ndarray) -> tuple[ClassificationResult, np.ndarray]:
        if frame is None:
            raise ValueError("Frame cannot be None")

        display_frame = frame.copy()
        result = self.classifier.classify_frame(frame)

        cv2.putText(
            display_frame,
            f"{result.common_name} ({result.confidence:.2f})",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )
        return result, display_frame
