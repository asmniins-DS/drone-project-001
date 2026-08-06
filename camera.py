import cv2
import numpy as np


class CameraSource:
    def __init__(self, source: int | str = 0, use_phone_stream: bool = True) -> None:
        self.source = source
        self.use_phone_stream = use_phone_stream
        self.cap = None

    def start(self) -> None:
        if self.cap is not None:
            return
        self.cap = cv2.VideoCapture(self.source)
        if not self.cap.isOpened():
            raise RuntimeError("Unable to open camera source. Connect your phone camera stream or a local camera.")

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
