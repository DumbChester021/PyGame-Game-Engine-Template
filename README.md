# PyGame Game Engine Template

A flexible and feature-rich 2D game engine template built with PyGame, featuring a complete scene management system, UI components, resource management, and more.

## 🎮 Features

### Core Systems

- **Scene Management**: Easily switch between different game states (Menu, Playing, Paused, Game Over)
- **Resource Management**: Centralized handling of images, sounds, and fonts
- **Input System**: Streamlined keyboard and mouse input handling
- **Camera System**: Smooth scrolling and viewport management
- **UI Framework**: Ready-to-use UI components including buttons and text elements

### Architecture

- **Component-Based Design**: Modular and extensible architecture
- **Abstract Base Classes**: Well-defined interfaces for scenes and game objects
- **Type Hints**: Comprehensive Python type annotations for better code reliability
- **Event System**: Robust event handling and propagation

### Game Elements

- **Sprite Management**: Base GameObject class with physics properties
- **Collision Detection**: Built-in collision handling system
- **Animation Support**: Framework for sprite animations
- **Particle Systems**: Support for visual effects

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/pygame-template.git
cd pygame-template
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
├── assets/
│   ├── images/
│   ├── sounds/
│   └── fonts/
├── src/
│   ├── core/
│   │   ├── ui/
│   │   │   ├── button.py
│   │   │   ├── text.py
│   │   │   └── ui_element.py
│   │   ├── camera.py
│   │   ├── input_manager.py
│   │   ├── resource_manager.py
│   │   └── sprite.py
│   ├── scenes/
│   │   ├── menu_scene.py
│   │   ├── game_scene.py
│   │   └── scene.py
│   ├── config.py
│   └── game_state.py
└── main.py
```

## 🚀 Getting Started

1. Run the game:

```bash
python main.py
```

2. Create a new scene:

```python
from src.scenes.scene import Scene

class YourScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        # Initialize your scene
  
    def update(self, dt):
        # Update logic
        pass
  
    def draw(self, screen):
        # Drawing logic
        pass
```

## 🎮 Controls

- **ESC**: Return to menu
- **Arrow Keys**: Movement
- **Space**: Action/Shoot
- **P**: Pause game

## 🛠️ Configuration

All game settings can be modified in `src/config.py`:

- Window size and title
- FPS target
- Color definitions
- Asset directory paths

## 🧩 Core Components

### Resource Manager

```python
# Load and manage game assets
resource_manager = ResourceManager()
resource_manager.load_image("player", "player.png")
resource_manager.load_sound("shoot", "shoot.wav")
```

### UI System

```python
# Create UI elements
button = Button(x, y, width, height, "Click Me!", font, color, hover_color, text_color)
text = Text(x, y, "Score: 0", font, color)
```

### Camera System

```python
# Initialize and use camera
camera = Camera(width, height)
camera.set_target(player)
camera.update()
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- PyGame community
- Contributors and testers

## 📞 Contact

- Chester
- Email: breaksoftinc@gmail.com
- GitHub: [@dumbchester021](https://github.com/dumbchester021)
