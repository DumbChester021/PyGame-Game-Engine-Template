import pygame
import sys
from typing import Dict, Type
from src.config import WINDOW_SIZE, GAME_TITLE, TARGET_FPS, COLORS
from src.game_state import GameState
from src.scenes.scene import Scene
from src.core.resource_manager import ResourceManager
from src.core.input_manager import InputManager
from src.core.camera import Camera

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(GAME_TITLE)
        
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        # Initialize core systems
        self.resource_manager = ResourceManager()
        self.input_manager = InputManager()
        self.camera = Camera(*WINDOW_SIZE)
        
        # Load resources before creating scenes
        self.load_resources()
        
        self.current_state = GameState.MENU
        
        # Initialize scenes
        self.scenes: Dict[GameState, Scene] = {}
        self.load_scenes()
    
    def load_resources(self) -> None:
        # For testing, we'll use the default system font
        default_font = pygame.font.get_default_font()
        self.resource_manager.fonts["title"] = pygame.font.Font(default_font, 64)
        self.resource_manager.fonts["main"] = pygame.font.Font(default_font, 32)
        
        # Create temporary surfaces for testing
        player_surf = pygame.Surface((32, 32))
        player_surf.fill((0, 255, 0))  # Green player
        self.resource_manager.images["player"] = player_surf
        
        enemy_surf = pygame.Surface((32, 32))
        enemy_surf.fill((255, 0, 0))  # Red enemy
        self.resource_manager.images["enemy"] = enemy_surf
        
        bullet_surf = pygame.Surface((8, 8))
        bullet_surf.fill((255, 255, 0))  # Yellow bullet
        self.resource_manager.images["bullet"] = bullet_surf
        
        # When you have actual assets, use these instead:
        # self.resource_manager.load_image("player", "player.png")
        # self.resource_manager.load_image("enemy", "enemy.png")
        # self.resource_manager.load_image("bullet", "bullet.png")
        # self.resource_manager.load_font("title", "title_font.ttf", 64)
        # self.resource_manager.load_font("main", "main_font.ttf", 32)
        # self.resource_manager.load_sound("shoot", "shoot.wav")
        # self.resource_manager.load_sound("explosion", "explosion.wav")
    
    def load_scenes(self) -> None:
        # Import scenes here to avoid circular imports
        from src.scenes.menu_scene import MenuScene
        from src.scenes.game_scene import GameScene
        
        self.scenes = {
            GameState.MENU: MenuScene(self),
            GameState.PLAYING: GameScene(self)
        }
    
    def change_state(self, new_state: GameState) -> None:
        self.current_state = new_state
    
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            
            self.scenes[self.current_state].handle_event(event)
    
    def update(self, dt: float) -> None:
        self.input_manager.update()
        self.camera.update()
        self.scenes[self.current_state].update(dt)
    
    def draw(self) -> None:
        self.screen.fill(COLORS["BLACK"])
        self.scenes[self.current_state].draw(self.screen)
        pygame.display.flip()
    
    def run(self) -> None:
        while self.is_running:
            dt = self.clock.tick(TARGET_FPS) / 1000.0  # Convert to seconds
            
            self.handle_events()
            self.update(dt)
            self.draw()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run() 