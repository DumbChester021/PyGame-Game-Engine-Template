import pygame
from src.core.ui.ui_element import UIElement
from typing import Tuple, Optional

class Button(UIElement):
    def __init__(
        self, 
        x: int, 
        y: int, 
        width: int, 
        height: int, 
        text: str,
        font: pygame.font.Font,
        color: Tuple[int, int, int],
        hover_color: Tuple[int, int, int],
        text_color: Tuple[int, int, int]
    ):
        super().__init__(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False
        
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
    
    def update(self, dt: float) -> None:
        mouse_pos = pygame.mouse.get_pos()
        self.is_hovered = self.contains_point(mouse_pos)
    
    def draw(self, surface: pygame.Surface) -> None:
        if not self.visible:
            return
            
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.text_surface, self.text_rect) 