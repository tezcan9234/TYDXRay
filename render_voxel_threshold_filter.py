
# render_voxel_threshold_filter.py

import pyvista as pv
import numpy as np

# 📦 Sahte voxel veri (20x20x20)
voxel_grid = np.zeros((20, 20, 20))
voxel_grid[5:10, 5:10, 5:10] = 0.85  # Anomali küp
voxel_grid[12:14, 12:14, 12:14] = 0.5  # Gürültü (filtrelenmesi gerek)

# 🔎 Threshold değeri
threshold_value = 0.7

# 🧹 Filtreleme işlemi
filtered_grid = np.where(voxel_grid >= threshold_value, voxel_grid, 0)

# PyVista grid
grid = pv.UniformGrid()
grid.dimensions = np.array(filtered_grid.shape) + 1
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)
grid.cell_data["values"] = filtered_grid.flatten(order="F")

# 🎥 PyVista sahne
plotter = pv.Plotter()
plotter.add_volume(grid, cmap="plasma", opacity="linear")
plotter.add_text("Threshold: > 0.7", position='upper_left', font_size=12, color='white')
plotter.show()
