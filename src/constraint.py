import math

class Constraint:

    def __init__(self, particle_a, particle_b, rest_length=None):

        self.a = particle_a
        self.b = particle_b

        if rest_length is None:

            dx = particle_b.x - particle_a.x
            dy = particle_b.y - particle_a.y

            rest_length = math.sqrt(dx * dx + dy * dy)

        self.rest_length = rest_length

    def solve(self):
        dx = self.b.x - self.a.x
        dy = self.b.y - self.a.y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance == 0:
            return

        # difference between actual and desired distance
        difference = (distance - self.rest_length)

        # Normalize correction
        correction_x = (dx / distance) * difference
        correction_y = (dy / distance) * difference

        # Determine how much correction is distributed
        if self.a.pinned and self.b.pinned:
            return # Both particles are pinned, no correction needed

        elif self.a.pinned:
            self.b.x -= correction_x
            self.b.y -= correction_y

        elif self.b.pinned:
            self.a.x += correction_x
            self.a.y += correction_y

        else:
            self.a.x += correction_x * 0.5
            self.a.y += correction_y * 0.5
            self.b.x -= correction_x * 0.5
            self.b.y -= correction_y * 0.5


            