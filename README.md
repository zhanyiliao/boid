# Boids Simulation

A Python implementation of **Craig Reynolds’ Boids algorithm**, demonstrating emergent flocking behavior through three simple rules: **Separation**, **Alignment**, and **Cohesion**.  
The simulation uses **Pygame** for real-time visualization and allows parameter tuning via command-line arguments.

## Overview

Each boid moves independently based on local interactions with nearby boids.  
Through three simple behavioral rules, complex and lifelike collective motion emerges **without centralized control**.

| Rule | Description | Color |
|------|--------------|-------|
| **Separation** | Avoid crowding to prevent collisions | Red |
| **Alignment** | Match velocity with nearby boids | Green |
| **Cohesion** | Move toward the local group center | Blue |

## Features

- Real-time 2D visualization using **Pygame**  
- Adjustable behavior radii and strengths  
- Optional **smooth decay** for gradual influence  
- Soft boundary control (prevents boids from leaving the screen)  
- Reproducible results via random seed  
- Visual debugging: colored circles and vectors for the first boid  

## Requirements

- Python ≥ 3.8  
- [NumPy](https://numpy.org/), [SciPy](https://scipy.org/), [Pygame](https://www.pygame.org/)  

Install dependencies:
```bash
pip install numpy scipy pygame
```

## Usage

Run the simulation:
```bash
python boids.py
```

### Key arguments

| Argument       | Default | Description               |
| -------------- | ------- | ------------------------- |
| `--boids_num`  | `50`    | Number of boids           |
| `--boid_size`  | `8`     | Size of each boid         |
| `--max_speed`  | `20.0`  | Maximum velocity          |
| `--sep_radius` | `22`    | Separation radius         |
| `--ali_radius` | `70`    | Alignment radius          |
| `--coh_radius` | `110`   | Cohesion radius           |
| `--sep_scalar` | `0.44`  | Separation strength       |
| `--ali_scalar` | `0.08`  | Alignment strength        |
| `--coh_scalar` | `0.09`  | Cohesion strength         |
| `--smooth`     | —       | Enable smooth force decay |
| `--seed`       | `603`   | Random seed               |

Example:
```bash
python boids.py --smooth --boids_num 100 --sep_scalar 0.5 --ali_scalar 0.1 --coh_scalar 0.08
```

## Visualization

- White circles — boids
- Magenta boid — main reference
- Colored circles — behavioral radii (red, green, blue)
- Colored lines — corresponding force vectors

## Author

Developed as the final project for the **Computer Animation and Special Effects** course, intended for educational and research purposes to illustrate **decentralized swarm intelligence** and **emergent collective motion**.

## 📜 Reference

- [C. W. Reynolds, “Flocks, Herds and Schools: A Distributed Behavioral Model,” *ACM SIGGRAPH Computer Graphics*, vol. 21, no. 4, pp. 25–34, 1987.](https://doi.org/10.1145/37402.37406)
- [Wikipedia – Boids Algorithm](https://en.wikipedia.org/wiki/Boids)
