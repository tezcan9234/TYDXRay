import pyvista as pv
import numpy as np

class LiveStreamRenderer:
    def __init__(self, grid_shape=(10, 10, 10)):
        self.grid_shape = grid_shape
        self.grid = pv.UniformGrid()
        self.grid.dimensions = np.array(grid_shape) + 1
        self.grid.spacing = (1, 1, 1)
        self.grid.origin = (0, 0, 0)
        self.grid.cell_data["values"] = np.zeros(np.prod(grid_shape))
        self.plotter = pv.Plotter()
        self.plotter.add_axes()
        self.plotter.set_background("black")

        self.actor = self.plotter.add_volume(
            self.grid,
            cmap="viridis",
            opacity="sigmoid"
        )

        self.plotter.show(auto_close=False, interactive_update=True)

    def update_voxel(self, x, y, z, value):
        idx = x + y * self.grid_shape[0] + z * self.grid_shape[0] * self.grid_shape[1]
        self.grid.cell_data["values"][idx] = value
        self.grid.cell_data["values"].modified()
        self.plotter.update()
