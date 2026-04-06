# Asteroids

A classic arcade-style Asteroids game built with Python and Pygame. This project was developed as part of the [Boot.dev](https://www.boot.dev) curriculum to master Object-Oriented Programming and game loop logic.

## Tech Stack

- **Language:** Python 3
- **Library:** Pygame

## Features

- **Physics-based Movement:** Rotational movement and momentum for the player ship.
- **Collision Detection:** Circular hitbox logic for asteroids, bullets, and the player.
- **Object-Oriented Design:** Clean class structures for game objects including inheritance and polymorphism.
- **Dynamic Difficulty:** Randomly spawning asteroids of varying sizes.

## Technical Highlights

- **Game Loop:** Implemented a standard `dt` (delta time) calculation to ensure frame-rate independent movement.
- **Inheritance:** Created a base `CircleShape` class that provides shared logic for all circular game entities.
- **Groups:** Utilized Pygame Groups to efficiently manage and update dozens of game objects simultaneously.

## Installation & Running

1. Clone the repository:
   ```bash
   git clone https://github.com/callmedugan/asteroids.git
   cd asteroids
   ```
2. Install dependencies:
   pip install pygame

3. Run the game:
   python3 main.py

## How to Play

The objective is simple: survive the asteroid field as long as possible!

### Controls

| Action            | Key(s)                 |
| :---------------- | :--------------------- |
| **Move / Rotate** | `WASD` or `Arrow Keys` |
| **Fire Laser**    | `Spacebar`             |

### Rules

- **Asteroids:** Larger asteroids split into smaller ones when shot.
- **Collisions:** If your ship touches an asteroid, it's Game Over!
