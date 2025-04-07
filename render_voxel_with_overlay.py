import pyvista as pv
import numpy as np

def render_voxel(data, shape):
    grid = np.array(data).reshape(shape)
    grid = np.transpose(grid, (2, 1, 0))
    plotter = pv.Plotter()
    plotter.add_volume(grid, cmap="coolwarm", opacity="linear")
    plotter.show()
