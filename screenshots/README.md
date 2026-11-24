
# Verlet Physics Sandbox

An interactive 2D physics simulation engine built
using Python and Pygame.

## Overview

This project implements a particle-based physics
engine using Verlet Integration.

Particles interact through distance constraints,
gravity, wind, boundaries and basic collision detection.

## Features

- Particle creation
- Gravity simulation
- Verlet Integration
- Distance constraints
- Rope simulation
- Cloth simulation
- Basic particle collision
- Screen boundaries
- Mouse interaction
- Pin and unpin functionality
- Wind simulation
- Adjustable gravity
- Fixed timestep physics

## Technologies

- Python
- Pygame
- Unittest
- Git
- GitHub

## Project Architecture

src/
  config.py
  particle.py
  constraint.py
  world.py
  renderer.py
  main.py

tests/
  test_physics.py

## Installation

Clone the repository:

git clone YOUR_REPOSITORY_URL

Navigate to the project:

cd verlet-physics-sandbox

Create a virtual environment:

python3 -m venv venv

Activate on macOS:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Run

python -m src.main

## Run Tests

python -m unittest discover -s tests -v

## Controls

| Key | Action |
| Space | Pause / Resume |
| R | Create Rope |
| C | Create Cloth |
| W | Toggle Wind |
| Up | Increase Gravity |
| Down | Decrease Gravity |
| Left Click | Create / Drag |
| Right Click | Pin / Unpin |
| Delete | Clear |
| Escape | Exit |

## Physics Concepts

- Position and velocity
- Verlet Integration
- Gravity and acceleration
- Distance constraints
- Collision detection
- Collision resolution
- Numerical simulation

## Future Improvements

- Soft-body simulation
- Friction and restitution
- Spatial hashing
- Simulation recording
- JSON save and load
- Performance optimization

## Author

Harshu Singh
