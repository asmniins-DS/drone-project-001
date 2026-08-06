class SpeechManager:
    def __init__(self) -> None:
        self.enabled = False

    def speak(self, text: str) -> None:
        if not self.enabled:
            return
        print(f"Voice output: {text}")
