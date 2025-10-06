import argparse
import math
import numpy as np
import pygame
import random
from scipy.spatial import distance


# Boid class represents each boid in the simulation
class Boid:
    
    def __init__(self, size, position=None, max_speed=20.0, color=None):
    
        self.size = size
        self.position = np.zeros(2) if position is None else np.array(position, dtype=np.float64)
        self.max_speed = max_speed
        self.velocity = (np.random.rand(2) - 0.5) * self.max_speed
        self.acceleration = np.zeros(2)
        self.color = '#FFFFFF' if color is None else color
        
    def move(self, delta_time, width, height, border=100, out_decay=10):
    
        # Apply acceleration adjustments if boid is near the window border
        if self.position[0] < border:
            self.acceleration[0] += (border - self.position[0]) / out_decay
        elif self.position[0] > width - border:
            self.acceleration[0] += (width - border - self.position[0]) / out_decay
            
        if self.position[1] < border:
            self.acceleration[1] += (border - self.position[1]) / out_decay
        elif self.position[1] > height - border:
            self.acceleration[1] += (height - border - self.position[1]) / out_decay
            
        # Update velocity and apply speed limit
        self.velocity += self.acceleration * delta_time
        speed = abs(math.hypot(*self.velocity))
        if speed > self.max_speed:
            self.velocity *= self.max_speed / speed
            
        # Update position based on velocity
        self.position += self.velocity * delta_time
        
    def distance_to(self, other):
    
        return distance.euclidean(self.position, other.position)

        
# Argument parser setup
parser = argparse.ArgumentParser()
parser.add_argument('--smooth', action='store_true',
                    help='Enable smoothing of boid movements')
parser.add_argument('--boids_num', type=int, default=50,
                    help='Number of boids in the simulation')
parser.add_argument('--boid_size', type=int, default=8,
                    help='Size of each boid')
parser.add_argument('--max_speed', type=float, default=20.0,
                    help='Maximum speed of each boid')
parser.add_argument('--delta_time', type=float, default=0.1666,
                    help='Time step for each simulation update')
parser.add_argument('--sep_radius', type=int, default=22,
                    help='Separation radius for boid separation behavior')
parser.add_argument('--ali_radius', type=int, default=70,
                    help='Alignment radius for boid alignment behavior')
parser.add_argument('--coh_radius', type=int, default=110,
                    help='Cohesion radius for boid cohesion behavior')
parser.add_argument('--sep_scalar', type=float, default=0.44,
                    help='Scalar for the strength of the separation behavior')
parser.add_argument('--ali_scalar', type=float, default=0.08,
                    help='Scalar for the strength of the alignment behavior')
parser.add_argument('--coh_scalar', type=float, default=0.09,
                    help='Scalar for the strength of the cohesion behavior')
parser.add_argument('--seed', type=int, default=603,
                    help='Random seed for reproducibility')
args = parser.parse_args()

# Simulation window dimensions
WIDTH, HEIGHT = 1080, 720

# Set random seeds for reproducibility
random.seed(args.seed)
np.random.seed(args.seed)

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Boid')

# Create boids (first boid is colored differently for visualization)
boids = list()
for i in range(args.boids_num):
    position = [random.random() * (WIDTH - args.boid_size * 2) + args.boid_size,
                random.random() * (HEIGHT - args.boid_size * 2) + args.boid_size]
    boids.append(Boid(args.boid_size, position=position,
                      max_speed=args.max_speed,
                      color='#FF00FF' if i == 0 else '#FFFFFF'))

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill('#000000')
    
    for i, boid in enumerate(boids):
    
        sep_count, ali_count, coh_count = 0, 0, 0
        separation = np.zeros(2)
        alignment = np.zeros(2)
        cohesion = np.zeros(2)
    
        for j, flockmate in enumerate(boids):
        
            if i != j:
                
                dist = boid.distance_to(flockmate)

                # Calculate separation vector
                if dist < args.sep_radius:
                    vec = boid.position - flockmate.position
                    if args.smooth:
                        vec = vec * (1 - dist / args.sep_radius)
                    separation += vec
                    sep_count += 1
                
                # Calculate alignment vector
                if dist < args.ali_radius:
                    vec = flockmate.velocity
                    if args.smooth:
                        vec = vec * (1 - dist / args.ali_radius)
                    alignment += vec
                    ali_count += 1
                    
                # Calculate cohesion vector
                if dist < args.coh_radius:
                    vec = flockmate.position - boid.position
                    if args.smooth:
                        vec = vec * (1 - dist / args.coh_radius)
                    cohesion += vec
                    coh_count += 1
        
        # Normalize and scale the behavior vectors
        if sep_count > 0:
            separation = (separation / sep_count) * args.sep_scalar
        if ali_count > 0:
            alignment = (alignment / ali_count) * args.ali_scalar
        if coh_count > 0:
            cohesion = (cohesion / coh_count) * args.coh_scalar
            
        # Update boid's acceleration
        boid.acceleration = separation + alignment + cohesion
        boid.move(args.delta_time, WIDTH, HEIGHT)
        
        # Draw the first boid's behavior radii and vectors for visualization
        if i == 0:
            pygame.draw.circle(window, '#FF0000',
                               boid.position, args.sep_radius, 1)
            pygame.draw.circle(window, '#00FF00',
                               boid.position, args.ali_radius, 1)
            pygame.draw.circle(window, '#0000FF',
                               boid.position, args.coh_radius, 1)
            pygame.draw.line(window, '#FF0000', boid.position,
                             boid.position + separation * 5, 2)
            pygame.draw.line(window, '#00FF00', boid.position,
                             boid.position + alignment * 5, 2)
            pygame.draw.line(window, '#0000FF', boid.position,
                             boid.position + cohesion * 5, 2)

        # Draw the boid
        pygame.draw.circle(window, boid.color, boid.position, boid.size, 2)
        pygame.draw.line(window, boid.color, boid.position,
                         boid.position + boid.acceleration * 5, 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()