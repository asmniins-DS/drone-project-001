from dataclasses import dataclass
from typing import Optional

import numpy as np

from plant_database import PlantDatabase


@dataclass
class ClassificationResult:
    common_name: str
    scientific_name: str
    confidence: float
    description: str
    uses: str
    medicinal: bool
    raw_label: str


class Classifier:
    def __init__(self, database: Optional[PlantDatabase] = None) -> None:
        self.database = database or PlantDatabase()

    def classify_frame(self, frame: np.ndarray) -> ClassificationResult:
        if frame is None:
            raise ValueError("Frame cannot be None")

        green_intensity = float(np.mean(frame[:, :, 1]))
        if green_intensity > 120:
            label = "neem"
            confidence = 0.91
        else:
            label = "mango"
            confidence = 0.78

        info = self.database.get_plant_info(label)
        if info is None:
            label = "basil"
            info = self.database.get_plant_info(label)

        return ClassificationResult(
            common_name=info.common_name,
            scientific_name=info.scientific_name,
            confidence=float(confidence),
            description=info.description,
            uses=info.uses,
            medicinal=info.medicinal,
            raw_label=label,
        )
