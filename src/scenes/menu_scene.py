import pygame
from src.scenes.scene import Scene
from src.game_state import GameState
from src.core.ui.button import Button
from src.core.ui.text import Text

class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        
        center_x = self.game.screen.get_width() // 2
        center_y = self.game.screen.get_height() // 2
        
        # Create UI elements
        self.title = Text(
            center_x, 
            center_y - 100,
            "Space Shooter",
            self.game.resource_manager.get_font("title"),
            (255, 255, 255)
        )
        self.title.rect.centerx = center_x
        
        self.play_button = Button(
            center_x - 100, center_y,
            200, 50,
            "Play Game",
            self.game.resource_manager.get_font("main"),
            (100, 100, 100),
            (150, 150, 150),
            (255, 255, 255)
        )
        self.play_button.on_click = lambda: self.game.change_state(GameState.PLAYING)
        
        self.quit_button = Button(
            center_x - 100, center_y + 70,
            200, 50,
            "Quit",
            self.game.resource_manager.get_font("main"),
            (100, 100, 100),
            (150, 150, 150),
            (255, 255, 255)
        )
        self.quit_button.on_click = lambda: setattr(self.game, 'is_running', False)
    
    def update(self, dt: float) -> None:
        self.play_button.update(dt)
        self.quit_button.update(dt)
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 40))
        self.title.draw(screen)
        self.play_button.draw(screen)
        self.quit_button.draw(screen)
    
    def handle_event(self, event: pygame.event.Event) -> None:
        self.play_button.handle_event(event)
        self.quit_button.handle_event(event) 