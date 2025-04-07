
import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv

# Generate sample data: let's simulate a grid of values for demonstration
grid = pv.UniformGrid()

# Setting the grid dimensions
grid.dimensions = np.array([10, 10, 10])

# Generate random values for the grid
values = np.random.random(grid.dimensions[0] * grid.dimensions[1] * grid.dimensions[2]).reshape(grid.dimensions)

# Add the data to the grid
grid.point_data["values"] = values.flatten()

# Create the slice: Z-slice (we can choose the slice index or use a dynamic one)
slice_index = 5
slice_grid = grid.slice(normal='z', origin=(0, 0, slice_index))

# Plotting
p = pv.Plotter()
p.add_mesh(slice_grid, scalars="values", cmap="coolwarm", show_edges=False)
p.add_scalar_bar(title="Intensity", vertical=True)
p.show()
