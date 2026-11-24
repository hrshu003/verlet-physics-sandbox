import pygame

from src.config import (
    Window_width, Window_height, background, particle_color, pinned_particle_color, rope_color, text_color, grid_color
)

def draw_world(screen, world, font, paused):
    screen.fill(background)

    # draw background grid
    for x in range(0, Window_width, 40):

        pygame.draw.line(screen, grid_color, (x, 0), (x, Window_height))

    for y in range(0, Window_height, 40):

        pygame.draw.line(screen, grid_color, (0, y), (Window_width, y))

    # Draw constraints first
    for constraint in world.constraints:

        pygame.draw.line(
            screen,
            rope_color,
            (int(constraint.a.x), int(constraint.a.y)),
            (int(constraint.b.x), int(constraint.b.y)),
            2
        )

    # draw particles
    for particle in world.particles:
        color = pinned_particle_color if particle.pinned else particle_color

        pygame.draw.circle( screen, color, (int(particle.x), int(particle.y)), int(particle.radius))

    # draw application information
    status = "PAUSED" if paused else "RUNNING"

    information = [
        "VERLET PHYSICS SANDBOX SIMULATION",
        f"status : {status}",
        f"Particles : {len(world.particles)}",
        f"Constraints : {len(world.constraints)}",
        f"Wind : {world.wind : .0f}",
        "SPACE : PAUSE | R : ROPE | C : CLOTH | W : WIND",
        "LEFT CLICK : ADD / DRAG PARTICLE | RIGHT CLICK : PIN / UNPIN PARTICLE",
        "DELETE : CLEAR PARTICLES | Esc : QUIT"
    ]

    for index, message in enumerate(information):

        text = font.render(message, True, text_color)

        screen.blit(text, (15, 12 + index * 20))