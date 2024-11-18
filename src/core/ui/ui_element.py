import pygame
from abc import ABC, abstractmethod
from typing import Tuple, Optional, Callable

class UIElement(ABC):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.rect = pygame.Rect(x, y, width, height)
        self.visible = True
        self.enabled = True
        self.on_click: Optional[Callable[[], None]] = None
    
    def set_position(self, x: int, y: int) -> None:
        self.rect.x = x
        self.rect.y = y
    
    def contains_point(self, point: Tuple[int, int]) -> bool:
        return self.rect.collidepoint(point)
    
    @abstractmethod
    def update(self, dt: float) -> None:
        pass
    
    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        pass
    
    def handle_event(self, event: pygame.event.Event) -> None:
        if not (self.visible and self.enabled):
            return
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.contains_point(event.pos):
                if self.on_click:
                    self.on_click() 