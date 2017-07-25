from PIL import Image
import numpy as np

min_x = -2500
max_x = 1000
min_y = -1000
max_y = 1000
increments = 1
factor = 1000.0
iterations = 50

max_y += 1
max_x += 1

complex_grid_reference = []
complex_grid_iterate = []
iteration_grid = []
pixel_data = []

for y in range(min_y, max_y, increments):
    argand_plane_line = []
    for x in range(min_x, max_x, increments):
        argand_plane_line.append(complex(x/factor,y/factor))
    complex_grid_reference.append(argand_plane_line)

for y in range(min_y, max_y, increments):
    argand_plane_line = []
    for x in range(min_x, max_x, increments):
        argand_plane_line.append(complex(x/factor,y/factor))
    complex_grid_iterate.append(argand_plane_line)

for y in range(min_y, max_y, increments):
    current_line = []
    for x in range(min_x, max_x, increments):
        current_line.append(iterations)
    iteration_grid.append(current_line)

for i in range(iterations):
    for i in range(len(complex_grid_iterate)):
        for z in range(len(complex_grid_iterate[1])):
            if abs(complex_grid_iterate[i][z]) > 2:
                iteration_grid[i][z] -= 1
            else:
                complex_grid_iterate[i][z] = complex_grid_iterate[i][z]**2 + complex_grid_reference[i][z]

converted = np.array(iteration_grid)

converted = (255.0 / converted.max() * (converted - converted.min())).astype(np.uint8) # thank God for Stackoverflow

image = Image.fromarray(converted)
image.save('mandelbrot_250.png')
