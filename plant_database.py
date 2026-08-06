from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class PlantInfo:
    common_name: str
    scientific_name: str
    description: str
    uses: str
    medicinal: bool
    confidence: float = 0.0

    def __getitem__(self, key: str):
        if key in {"common_name", "scientific_name", "description", "uses", "medicinal", "confidence"}:
            return getattr(self, key)
        raise KeyError(key)


class PlantDatabase:
    def __init__(self) -> None:
        self._plants: Dict[str, PlantInfo] = {
            "neem": PlantInfo(
                common_name="Neem",
                scientific_name="Azadirachta indica",
                description="A fast-growing evergreen tree valued for its medicinal and pesticidal properties.",
                uses="Natural pesticide; skin treatment; soil health",
                medicinal=True,
            ),
            "mango": PlantInfo(
                common_name="Mango",
                scientific_name="Mangifera indica",
                description="A tropical fruit tree with dense foliage and broad leaves.",
                uses="Fruit production; shade; timber",
                medicinal=False,
            ),
            "basil": PlantInfo(
                common_name="Basil",
                scientific_name="Ocimum basilicum",
                description="A fragrant herb commonly used in cooking and traditional medicine.",
                uses="Culinary uses; aromatic herb; teas",
                medicinal=True,
            ),
        }

    def get_plant_info(self, name: str) -> Optional[PlantInfo]:
        return self._plants.get(name.lower())

    def __getitem__(self, name: str) -> PlantInfo:
        info = self.get_plant_info(name)
        if info is None:
            raise KeyError(name)
        return info
