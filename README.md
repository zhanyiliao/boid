# Boids Simulation

A Python implementation of **Craig Reynolds’ Boids algorithm**, demonstrating emergent flocking behavior through three simple rules: **separation**, **alignment**, and **cohesion**.  
This simulation uses **Pygame** for real-time visualization and supports parameter tuning via command-line arguments.

---

## Overview

This project simulates a group of autonomous agents (“boids”) moving in a two-dimensional space.  
Each boid independently updates its velocity and position based on local interactions with nearby boids, resulting in complex, lifelike collective motion.

The algorithm models **flocking behavior** without any centralized control — global coordination emerges solely from local rules.

---

## Core Principles

Each boid follows three behavioral rules:

| Rule | Description | Visual Indicator |
|------|--------------|------------------|
| **Separation** | Avoid crowding nearby boids to prevent collisions. | Red circle / vector |
| **Alignment** | Match velocity with nearby boids. | Green circle / vector |
| **Cohesion** | Move toward the center of nearby boids. | Blue circle / vector |

The combined effect of these forces determines the boid’s acceleration, which updates its velocity and position.

---

## Features

- ✅ Real-time 2D visualization using **Pygame**  
- ✅ Parameterized radii and behavior strengths  
- ✅ Optional **smooth decay** for continuous influence fields  
- ✅ Soft boundary control (prevents boids from escaping the window)  
- ✅ Reproducible experiments via random seed  
- ✅ Visual debugging: radii and force vectors drawn for the first boid  

---

## Algorithm Workflow

1. **Initialize** boids with random positions and velocities.  
2. **Compute local interactions** for each boid:  
   - Separation force  
   - Alignment force  
   - Cohesion force  
3. **Combine forces** (weighted sum) into an acceleration vector.  
4. **Update motion** using acceleration and velocity limits.  
5. **Render** the boids and their behavior radii each frame.

---

## Requirements

- Python ≥ 3.8  
- [NumPy](https://numpy.org/)  
- [SciPy](https://scipy.org/)  
- [Pygame](https://www.pygame.org/)  

Install dependencies via:

```bash
pip install numpy scipy pygame
