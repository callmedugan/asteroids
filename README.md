# Asteroids

A classic arcade-style **Asteroids** game built with **Python** and **Pygame**.  
Originally developed through the Boot.dev curriculum, this version expands on the core project with additional gameplay systems including **lives, scoring, levels, and multiple power-ups**. The aim was to make something that feels totally ridiculous to play, but also super satisfying.

![demo](https://github.com/user-attachments/assets/333ee2a2-4805-4605-a2e6-35aa559e82d8)

## Tech Stack

- **Python 3**
- **Pygame**

## Features

- **Physics-based movement** with ship rotation and momentum
- **Collision detection** for asteroids, bullets, power-ups, and the player
- **Object-oriented design** with reusable classes, inheritance, and polymorphism
- **Lives system** for extended gameplay (you'll definitely need them)
- **Score tracking** to reward survival and accuracy
- **Level progression** with increasing difficulty and scoring multipliers
- **Power-up system** 5 unique upgrades for the ship that offer a ton of hectic fun

## Installation

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

- Destroy asteroids to earn points
- Larger asteroids split into smaller ones
- Collect power-ups to gain temporary or enhanced abilities
- Progress through levels as the game becomes more challenging
- Lose a life when colliding with an asteroid unless shielded
- The game ends when all lives are lost

### Controls

| Action            | Key(s)                 |
| :---------------- | :--------------------- |
| **Move / Rotate** | `WASD` or `Arrow Keys` |
| **Fire Laser**    | `Spacebar`             |

### Power-Ups

**Shield** - Protects ship from being destroyed during collision
**Fire Rate Up** - Reduces delay between shots
**Speed Up** - Increases ship movement speed
**Multishot** - Fires 3 shots at once
**Bounce** - Shots ricochet instead of disappearing on impact

### Learning Goals

This project helped reinforce:

object-oriented programming
real-time game loop design
collision handling
state management
scaling gameplay systems
extending a base project with original features
my love of turning a basic game project into something ridiculous
