import pyvista as pv
import numpy as np

# Basit 10x10x10 voxel küp sahnesi
grid = pv.UniformGrid()
grid.dimensions = (10, 10, 10)
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)

# Rastgele renk verisi
grid.point_data["values"] = np.random.rand(grid.n_points)

plotter = pv.Plotter()
plotter.add_volume(grid, cmap="coolwarm", opacity="linear")
plotter.show(auto_close=False, interactive_update=True)
