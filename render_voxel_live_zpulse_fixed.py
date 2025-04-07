import pyvista as pv
import numpy as np

def render_voxel_scene(grid):
    plotter = pv.Plotter()
    plotter.add_mesh(grid, scalars="values", cmap="coolwarm", show_edges=False, opacity='linear')
    plotter.show()

# Örnek veri
x = np.arange(0, 10)
y = np.arange(0, 10)
z = np.arange(0, 10)
x, y, z = np.meshgrid(x, y, z, indexing="ij")
grid = pv.StructuredGrid(x, y, z)

values = np.random.rand(grid.n_points)
grid["values"] = values

render_voxel_scene(grid)
