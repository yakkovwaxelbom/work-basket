
# Space Invaders Game

## Project Structure

This project is a clone of the classic "Space Invaders" game, developed using Python and Pygame. The code is organized into several modules, with each handling a different part of the game's functionality.

### Screenshot

![Game start](assets/graphics/game_start.png) 
![Game play](assets/graphics/game_play.png) 
![Game vin](assets/graphics/game_vin.png)
![Game over](assets/graphics/game_over.png)  

### Directory Structure

```
project_root/
│
├── README.md               # Project documentation
├── src/                    # Source code for the game
│   ├── main.py             # Entry point for the game
│   ├── alien.py            # Alien class (enemies)
│   ├── aliens_manager.py   # Manages alien groups and movements
│   ├── bullet.py           # Bullet and bullet movement logic
│   ├── bullet_manager.py   # Manages bullets for both player and aliens
│   ├── collision_manager.py# Handles collision detection between bullets, players, and aliens
│   ├── game_manager.py     # Main game logic and state management
│   ├── player.py           # Player class
│   ├── player_manager.py   # Manages player actions and status
│   ├── settings.py         # Stores all game settings and constants
│   ├── state_manager.py    # Manages the different game states (start, playing, game over)
│   └── ui_manager.py       # Handles UI elements such as score and lives
├── assets/                 # Contains all graphical and sound assets
│   ├── graphics/           # Images used in the game (players, aliens, bullets, background)
│   │   ├── game_screenshot.png  # Sample screenshot for README
│   │   ├── alien.png
│   │   ├── player_1.png
│   │   ├── shoot_1.png
│   │   ├── shoot_4.png
│   │   └── new_background.png
│   └── sounds/             # Sound effects used in the game
│       ├── game over.mp3
│       ├── hit.mp3
│       ├── shoot.mp3
│       ├── smash.mpeg
│       └── success.mp3
```

### How to Run the Game

1. Clone the repository to your local machine.
2. Make sure you have Python and Pygame installed. You can install Pygame using:
   ```
   pip install pygame
   ```
3. Navigate to the `src` folder:
   ```
   cd src
   ```
4. Run the game:
   ```
   python main.py
   ```

### Game Features

- **Player and Alien Movements**: Use the arrow keys to move the player left and right, and space to shoot.
- **Alien Shooting**: Aliens will shoot bullets randomly toward the player.
- **Collision Detection**: Bullets collide with aliens and other bullets.
- **Multiple Levels**: Once all aliens are defeated, the player progresses to the next level.
- **Game Over**: The game ends when the player loses all lives or defeats all aliens.

### Assets

All graphical assets (like the player's ship, aliens, and bullets) and sound effects are stored in the `assets/` directory. These include:

- **Graphics**: `assets/graphics/`
- **Sounds**: `assets/sounds/`

Feel free to modify the assets to personalize the game!

### Future Improvements

- Add more levels with increasing difficulty.
- Implement a scoring system with bonuses.
- Add power-ups for the player (e.g., faster bullets, temporary shields).
