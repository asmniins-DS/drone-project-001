import cv2
import numpy as np


class CameraSource:
    def __init__(self, source: int | str = 0) -> None:
        self.source = source
        self.cap = None

    def start(self) -> None:
        if self.cap is not None:
            return
        self.cap = cv2.VideoCapture(self.source, cv2.CAP_ANY)
        if not self.cap.isOpened():
            raise RuntimeError(
                f"Unable to open camera source '{self.source}'. "
                "Use a phone stream URL or a local device index."
            )

    def read_frame(self) -> np.ndarray | None:
        if self.cap is None:
            self.start()
        ok, frame = self.cap.read()
        if not ok:
            return None
        return frame

    def stop(self) -> None:
        if self.cap is not None:
            self.cap.release()
            self.cap = None
