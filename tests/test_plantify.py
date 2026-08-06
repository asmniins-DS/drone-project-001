import unittest

from plant_database import PlantDatabase
from classifier import Classifier


class PlantifyTests(unittest.TestCase):
    def test_database_contains_neem(self):
        db = PlantDatabase()
        info = db.get_plant_info("neem")
        self.assertIsNotNone(info)
        self.assertEqual(info["common_name"], "Neem")
        self.assertTrue(info["medicinal"])

    def test_classifier_returns_a_result_for_green_frame(self):
        classifier = Classifier()
        import numpy as np

        frame = np.zeros((120, 160, 3), dtype=np.uint8)
        frame[:, :, 1] = 255
        frame[20:100, 40:120] = [0, 180, 0]

        result = classifier.classify_frame(frame)
        self.assertTrue(result.common_name)
        self.assertGreaterEqual(result.confidence, 0.0)
        self.assertLessEqual(result.confidence, 1.0)


if __name__ == "__main__":
    unittest.main()
