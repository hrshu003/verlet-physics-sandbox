# Window dimensions
Window_width = 1200
Window_height = 800

# Physics settings
Gravity = 9.81
damping_coefficient = 0.1

# Physics calculations
fixed_dt = 1.0 / 60.0 # Fixed time step for physics calculations (60 FPS)
constraint_iterations = 10 # Number of iterations for constraint solving

# Particle settings
particle_radius = 5.0
particle_mass = 1.0

# Simulation settings 
max_particles = 1000 # Maximum number of particles in the simulation

# RGB colors
background = (0, 0, 0) # Black background
particle_color = (255, 255, 255) # White particles
pinned_particle_color = (255, 0, 0) # Red pinned particles
rope_color = (0, 255, 0) # Green ropes
text_color = (255, 255, 255) # White text
grid_color = (50, 50, 50) # Dark gray grid lines