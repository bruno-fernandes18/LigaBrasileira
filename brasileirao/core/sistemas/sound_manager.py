import os

try:
    import pygame
    pygame.mixer.init()
except Exception:  # pragma: no cover - pygame might not be available
    pygame = None


class SoundManager:
    """Simple sound effect manager using pygame if available."""

    _SOUNDS = {
        "gol": "gol.mp3",
        "apito_final": "apito_final.wav",
        "hino_flamengo": "hino_flamengo.mp3",
    }

    @classmethod
    def play(cls, key: str) -> None:
        if pygame is None:
            return
        filename = cls._SOUNDS.get(key)
        if not filename:
            return
        base_dir = os.path.join(os.path.dirname(__file__), "..", "..", "gui", "assets", "sounds")
        path = os.path.normpath(os.path.join(base_dir, filename))
        if os.path.exists(path):
            pygame.mixer.Sound(path).play()
