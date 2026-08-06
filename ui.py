import cv2

from detector import PlantDetector
from camera import CameraSource


class PlantifyUI:
    def __init__(
        self,
        detector: PlantDetector | None = None,
        camera_source: int | str = 0,
        camera: CameraSource | None = None,
    ) -> None:
        self.detector = detector or PlantDetector()
        self.camera = camera or CameraSource(source=camera_source)

    def run(self) -> None:
        self.camera.start()
        print("Plantify AI is ready. Point your phone camera at a plant to begin.")
        while True:
            frame = self.camera.read_frame()
            if frame is None:
                continue

            result, display_frame = self.detector.detect(frame)
            cv2.imshow("Plantify AI - Mobile Camera", display_frame)

            print(f"Detected: {result.common_name} ({result.confidence:.2f})")
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.camera.stop()
        cv2.destroyAllWindows()
