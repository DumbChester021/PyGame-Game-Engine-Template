from typing import Dict, Tuple

# Window Configuration
WINDOW_SIZE: Tuple[int, int] = (1280, 720)
GAME_TITLE: str = "Game Template"
TARGET_FPS: int = 60

# Colors
COLORS: Dict[str, Tuple[int, int, int]] = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255)
}

# Asset Paths
ASSET_DIR = "assets"
IMAGE_DIR = f"{ASSET_DIR}/images"
SOUND_DIR = f"{ASSET_DIR}/sounds"
FONT_DIR = f"{ASSET_DIR}/fonts" 