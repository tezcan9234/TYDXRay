# visualization/render_voxel.py

import pyvista as pv
import numpy as np

def render_voxel(data):
    # Veriyi al, normalize et
    x, y, z = data[:, 0], data[:, 1], data[:, 2]
    values = data[:, 3] if data.shape[1] > 3 else np.ones_like(x)

    grid = pv.StructuredGrid()
    grid.points = np.c_[x, y, z]
    grid["yoğunluk"] = values

    plotter = pv.Plotter()
    plotter.add_mesh(grid, scalars="yoğunluk", point_size=10, render_points_as_spheres=True)
    plotter.add_title("TYDX Voxel Görselleştirme")
    plotter.show()
