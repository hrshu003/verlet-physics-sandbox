import math

from src.config import (
    damping_coefficient,
    particle_radius,
    Gravity,
)


class Particle:

    def __init__(self, x, y, radius = particle_radius, mass = 1.0, pinned = False):

        # Current position
        self.x = float(x)
        self.y = float(y)

        # Previous position
        self.old_x = float(x)
        self.old_y = float(y)


        # Particle properties
        self.radius = float(radius)


        self.mass = float(mass)
        self.pinned = bool(pinned)

        # Initialize velocity and acceleration
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = 0.0

    def update(self, dt):

        if self.pinned:
            return

        # calculate movement from previous position
        velocity_x = (self.x - self.old_x) * (1 - damping_coefficient)
        velocity_y = (self.y - self.old_y) * (1 - damping_coefficient)

        # store the current position
        self.old_x = self.x
        self.old_y = self.y

        # apply Verlet integration
        self.x += velocity_x 
        self.y += velocity_y + Gravity * dt * dt

    def pin(self):
        self.pinned = True

        self.old_x = self.x
        self.old_y = self.y

    def unpin(self):
        self.pinned = False

    def set_position(self, x, y):
        self.x = float(x)
        self.y = float(y)

        self.old_x = float(x)
        self.old_y = float(y)

    def distance_to(self, x, y):
        dx = self.x - x
        dy = self.y - y

        return math.sqrt(dx * dx + dy * dy)