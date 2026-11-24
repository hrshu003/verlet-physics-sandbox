import pygame

from src.particle import Particle
from src.constraint import Constraint

from src.config import (
    Window_width,
    Window_height,
    max_particles,
    constraint_iterations,
)

class PhysicsWorld:

    def __init__(self):

        self.particles = []
        self.constraints = []

        self.wind = 0.0

    def add_particle(self, x, y):
        if len(self.particles) >= max_particles:
            return None

        particle = Particle(x, y)

        self.particles.append(particle)
        return particle

    def connect(self, particle_a, particle_b):

        constraint = Constraint(particle_a, particle_b)

        self.constraints.append(constraint)

        return constraint

    def add_rope(self, x, y, count=15, spacing=10):

        rope = []

        for i in range(count):
            particle = self.add_particle( x + i * spacing, y)

            if particle is None:
                return

            rope.append(particle)

            if i==0:
                particle.pin()

            else:
                self.connect(rope[i-1], particle)

    def add_cloth(self, x, y, rows=10, columns=15, spacing=10):

        grid = []

        for row in range(rows):

            current_row = []

            for col in range(columns):
                particle = self.add_particle(x + col * spacing, y + row * spacing)

                if particle is None:
                    return

                # Fix the upper edge
                if row == 0:
                    particle.pin()

                current_row.append(particle)

                # Horizoantal constraints
                if col > 0:
                    self.connect(current_row[col - 1], particle)

                # vertical constraints
                if row > 0:
                    self.connect(grid[row - 1][col], particle)

            grid.append(current_row)


    def apply_boundaries(self):

        for particle in self.particles:

            if particle.pinned:
                continue

            radius = particle.radius

            # left boundary
            particle.x = max(radius, particle.x)

            # right boundary
            particle.x = min(Window_width - radius, particle.x)

            # top boundary
            particle.y = max(radius, particle.y)

            # bottom boundary
            particle.y = min(Window_height - radius, particle.y)

            # Prevent continued movement into the boudnary
            if particle.x <= radius or particle.x >= Window_width - radius:
                particle.old_x = particle.x

            if particle.y <= radius or particle.y >= Window_height - radius:
                particle.old_y = particle.y

    def solve_collisions(self):

        # Simple particle-particle collision detection
        for i in range(len(self.particles)):
            a = self.particles[i]

            for j in range(i + 1, len(self.particles)):
                b = self.particles[j]

                dx = b.x - a.x
                dy = b.y - a.y 

                distance = (dx * dx + dy * dy) ** 0.5

                min_distance = a.radius + b.radius

                if distance == 0 or distance >= min_distance:
                    continue

                overlap = min_distance - distance

                nx = dx / distance
                ny = dy / distance

                if a.pinned and b.pinned:
                    continue

                elif a.pinned:
                    b.x += nx * overlap
                    b.y += ny * overlap

                elif b.pinned:
                    a.x -= nx * overlap
                    a.y -= ny * overlap

                else:
                    a.x -= nx * overlap * 0.5
                    a.y -= ny * overlap * 0.5

                    b.x += nx * overlap * 0.5
                    b.y += ny * overlap * 0.5

    def update(self, dt):
        # Move particles
        for particle in self.particles:

            if not particle.pinned:

                velocity_x = particle.x - particle.old_x

                particle.x += self.wind * dt * dt

            particle.update(dt)

        # Solve physical constraints repeatedly
        for _ in range (constraint_iterations):

            for constraints in self.constraints:
                constraints.solve()

            self.solve_collisions()
            self.apply_boundaries()





