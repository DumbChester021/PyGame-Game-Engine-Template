import pygame
from typing import Tuple

class Camera:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.offset_x = 0
        self.offset_y = 0
        self.target = None
    
    def set_target(self, target) -> None:
        self.target = target
    
    def update(self) -> None:
        if self.target:
            self.offset_x = self.target.rect.centerx - self.width // 2
            self.offset_y = self.target.rect.centery - self.height // 2
    
    def apply(self, entity) -> pygame.Rect:
        return pygame.Rect(
            entity.rect.x - self.offset_x,
            entity.rect.y - self.offset_y,
            entity.rect.width,
            entity.rect.height
        )
    
    def get_offset(self) -> Tuple[int, int]:
        return (self.offset_x, self.offset_y) 