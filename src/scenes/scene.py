import pygame
from abc import ABC, abstractmethod

class Scene(ABC):
    def __init__(self, game):
        self.game = game
    
    @abstractmethod
    def update(self, dt: float) -> None:
        pass
    
    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        pass
    
    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        pass 