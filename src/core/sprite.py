import pygame
from typing import Tuple, Optional

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, image: pygame.Surface):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        
    def update(self, dt: float, **kwargs) -> None:
        self.position += self.velocity * dt
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)

class Player(GameObject):
    def __init__(self, x: float, y: float, image: pygame.Surface):
        super().__init__(x, y, image)
        self.speed = 300
        self.shoot_cooldown = 0.2
        self.shoot_timer = 0
        
    def update(self, dt: float, **kwargs) -> Optional[Tuple[float, float]]:
        input_manager = kwargs.get('input_manager')
        if not input_manager:
            return None
            
        # Movement
        self.velocity.x = 0
        self.velocity.y = 0
        
        if input_manager.is_key_pressed(pygame.K_LEFT):
            self.velocity.x = -self.speed
        if input_manager.is_key_pressed(pygame.K_RIGHT):
            self.velocity.x = self.speed
        if input_manager.is_key_pressed(pygame.K_UP):
            self.velocity.y = -self.speed
        if input_manager.is_key_pressed(pygame.K_DOWN):
            self.velocity.y = self.speed
            
        super().update(dt)
        
        # Shooting
        self.shoot_timer -= dt
        if input_manager.is_key_pressed(pygame.K_SPACE) and self.shoot_timer <= 0:
            self.shoot_timer = self.shoot_cooldown
            return (self.rect.centerx, self.rect.top)
        return None

class Bullet(GameObject):
    def __init__(self, x: float, y: float, image: pygame.Surface):
        super().__init__(x, y, image)
        self.velocity.y = -400

    def update(self, dt: float, **kwargs) -> None:
        super().update(dt)
        if self.rect.bottom < 0:
            self.kill()

class Enemy(GameObject):
    def __init__(self, x: float, y: float, image: pygame.Surface):
        super().__init__(x, y, image)
        self.velocity.y = 150 