import pygame
import random
from src.scenes.scene import Scene
from src.core.sprite import Player, Enemy, Bullet
from src.game_state import GameState
from src.core.ui.text import Text

class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        
        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        
        # Load resources
        self.player_img = self.game.resource_manager.get_image("player")
        self.enemy_img = self.game.resource_manager.get_image("enemy")
        self.bullet_img = self.game.resource_manager.get_image("bullet")
        
        # Create player
        self.player = Player(
            self.game.screen.get_width() // 2,
            self.game.screen.get_height() - 100,
            self.player_img
        )
        self.all_sprites.add(self.player)
        
        # Game state
        self.score = 0
        self.enemy_spawn_timer = 0
        self.enemy_spawn_delay = 1.0
        
        # UI
        self.score_text = Text(
            10, 10, "", 
            self.game.resource_manager.get_font("main"),
            (255, 255, 255)
        )
        
    def spawn_enemy(self):
        x = random.randint(0, self.game.screen.get_width() - self.enemy_img.get_width())
        enemy = Enemy(x, -50, self.enemy_img)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)
    
    def update(self, dt: float) -> None:
        # Update all sprites with input manager
        for sprite in self.all_sprites:
            if isinstance(sprite, Player):
                bullet_pos = sprite.update(dt, input_manager=self.game.input_manager)
                if bullet_pos:
                    bullet = Bullet(bullet_pos[0], bullet_pos[1], self.bullet_img)
                    self.all_sprites.add(bullet)
                    self.bullets.add(bullet)
            else:
                sprite.update(dt)
        
        # Spawn enemies
        self.enemy_spawn_timer -= dt
        if self.enemy_spawn_timer <= 0:
            self.spawn_enemy()
            self.enemy_spawn_timer = self.enemy_spawn_delay
        
        # Check collisions
        for bullet in self.bullets:
            hits = pygame.sprite.spritecollide(bullet, self.enemies, True)
            if hits:
                bullet.kill()
                self.score += 100
        
        # Check for game over
        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            self.game.change_state(GameState.MENU)
        
        # Update score text
        self.score_text.set_text(f"Score: {self.score}")
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 40))  # Dark blue background
        self.all_sprites.draw(screen)
        self.score_text.draw(screen)
    
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.change_state(GameState.MENU) 