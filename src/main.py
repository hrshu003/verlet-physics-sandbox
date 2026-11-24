import pygame

from src.config import(
    Window_width, Window_height, fixed_dt, max_particles, Gravity
)

from src.world import PhysicsWorld

from src.renderer import draw_world


def find_particle(world, x, y, max_distance=20):

    nearest = None
    nearest_distance = max_distance

    for particle in world.particles:

        distance = particle.distance_to(x, y)

        if distance < nearest_distance:
            nearest = particle
            nearest_distance = distance

    return nearest

def main():

    pygame.init()

    screen = pygame.display.set_mode((Window_width, Window_height))

    pygame.display.set_caption("VERLET PHYSICS SANDBOX SIMULATION")

    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Arial", 18)

    world = PhysicsWorld()

    paused = False

    accumulator = 0.0

    selected_particle = None

    active = True

    while active:

        frame_time = min(clock.tick(60) / 1000.0, 0.25)

        accumulator += frame_time

        # handle application events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                active = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    active = False

                elif event.key == pygame.K_SPACE:
                    paused = not paused

                elif event.key == pygame.K_r:
                    world.add_rope(250, 180)

                elif event.key == pygame.K_c:
                    world.add_cloth(400, 160)

                elif event.key == pygame.K_w:
                    if world.wind == 0.0:
                        world.wind = 200.0
                    else:
                        world.wind = 0.0

                elif event.key == pygame.K_DELETE:
                    world.particles.clear()
                    world.constraints.clear()

                elif event.key == pygame.K_BACKSPACE:
                    world.particles.clear()
                    world.constraints.clear()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                mouse_x, mouse_y = event.pos

                selected_particle = find_particle(world, mouse_x, mouse_y)

                if event.button == 1:

                    if selected_particle is None:

                        if len(world.particles) < max_particles:

                            world.add_particle(mouse_x, mouse_y)

                elif event.button == 3:

                    if selected_particle is not None:

                        if selected_particle.pinned:
                            selected_particle.unpin()

                        else:
                            selected_particle.pin()

            elif event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1:
                    selected_particle = None

        # Drag the selected particle
        if selected_particle is not None:

            if pygame.mouse.get_pressed()[0]:

                mouse_x, mouse_y = pygame.mouse.get_pos()

                selected_particle.set_position(mouse_x, mouse_y)

        # fixed-step physics update
        if not paused:

            while accumulator >= fixed_dt:

                world.update(fixed_dt)

                accumulator -= fixed_dt

        else:
            accumulator = 0.0

        # render the simulation
        draw_world(screen, world, font, paused)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":

    main()
    
    
