import pygame
from typing import Dict, Set, Tuple

class InputManager:
    def __init__(self):
        self.pressed_keys = {}
        self.previous_keys = {}
        self.mouse_pos: Tuple[int, int] = (0, 0)
        self.mouse_buttons: Dict[int, bool] = {
            1: False,  # Left click
            2: False,  # Middle click
            3: False   # Right click
        }
    
    def update(self) -> None:
        # Store previous key states
        self.previous_keys = self.pressed_keys.copy()
        
        # Update current key states
        keys = pygame.key.get_pressed()
        self.pressed_keys = {
            pygame.K_LEFT: keys[pygame.K_LEFT],
            pygame.K_RIGHT: keys[pygame.K_RIGHT],
            pygame.K_UP: keys[pygame.K_UP],
            pygame.K_DOWN: keys[pygame.K_DOWN],
            pygame.K_SPACE: keys[pygame.K_SPACE],
            pygame.K_ESCAPE: keys[pygame.K_ESCAPE],
            pygame.K_RETURN: keys[pygame.K_RETURN],
            # Add any other keys you need here
        }
        
        # Update mouse state
        self.mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        self.mouse_buttons = {
            1: mouse_buttons[0],
            2: mouse_buttons[1],
            3: mouse_buttons[2]
        }
    
    def is_key_pressed(self, key: int) -> bool:
        return self.pressed_keys.get(key, False)
    
    def is_key_just_pressed(self, key: int) -> bool:
        return self.pressed_keys.get(key, False) and not self.previous_keys.get(key, False)
    
    def is_key_just_released(self, key: int) -> bool:
        return not self.pressed_keys.get(key, False) and self.previous_keys.get(key, False)
    
    def is_mouse_button_pressed(self, button: int) -> bool:
        return self.mouse_buttons.get(button, False)
    
    def get_mouse_position(self) -> Tuple[int, int]:
        return self.mouse_pos