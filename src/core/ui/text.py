import pygame
from src.core.ui.ui_element import UIElement
from typing import Tuple

class Text(UIElement):
    def __init__(
        self,
        x: int,
        y: int,
        text: str,
        font: pygame.font.Font,
        color: Tuple[int, int, int]
    ):
        self.text = text
        self.font = font
        self.color = color
        self.surface = self.font.render(text, True, color)
        super().__init__(x, y, self.surface.get_width(), self.surface.get_height())
    
    def set_text(self, text: str) -> None:
        self.text = text
        self.surface = self.font.render(text, True, self.color)
        self.rect.width = self.surface.get_width()
        self.rect.height = self.surface.get_height()
    
    def update(self, dt: float) -> None:
        pass
    
    def draw(self, surface: pygame.Surface) -> None:
        if self.visible:
            surface.blit(self.surface, self.rect) 