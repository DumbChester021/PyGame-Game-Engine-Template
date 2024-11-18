import pygame
import os
from typing import Dict
from src.config import IMAGE_DIR, SOUND_DIR, FONT_DIR

class ResourceManager:
    def __init__(self):
        self.images: Dict[str, pygame.Surface] = {}
        self.sounds: Dict[str, pygame.mixer.Sound] = {}
        self.fonts: Dict[str, pygame.font.Font] = {}
    
    def load_image(self, name: str, filename: str) -> None:
        path = os.path.join(IMAGE_DIR, filename)
        self.images[name] = pygame.image.load(path).convert_alpha()
    
    def load_sound(self, name: str, filename: str) -> None:
        path = os.path.join(SOUND_DIR, filename)
        self.sounds[name] = pygame.mixer.Sound(path)
    
    def load_font(self, name: str, filename: str, size: int) -> None:
        path = os.path.join(FONT_DIR, filename)
        self.fonts[name] = pygame.font.Font(path, size)
    
    def get_image(self, name: str) -> pygame.Surface:
        return self.images[name]
    
    def get_sound(self, name: str) -> pygame.mixer.Sound:
        return self.sounds[name]
    
    def get_font(self, name: str) -> pygame.font.Font:
        return self.fonts[name] 