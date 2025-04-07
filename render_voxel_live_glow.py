# visualization/render_voxel_live_glow.py
import pyvista as pv
import numpy as np

def render_voxel_scene(data):
    if data.shape[1] < 3:
        print("❌ Veri 3 sütun (X, Y, Z) içermeli.")
        return

    # Normalize data
    x, y, z = data[:, 0], data[:, 1], data[:, 2]
    values = (z - np.min(z)) / (np.max(z) - np.min(z) + 1e-6)

    # Grid oluştur
    grid = pv.StructuredGrid()
    grid.points = np.column_stack((x, y, z))
    grid["intensity"] = values.astype(np.float32)

    # Plotter
    plotter = pv.Plotter()
    plotter.add_volume(grid.delaunay_3d(), scalars="intensity", cmap="turbo", opacity="sigmoid", shade=True)
    plotter.add_text("TYDX - 3D Glow Sahne", font_size=12)
    plotter.show(window_size=[1024, 768], interactive_update=True, auto_close=False)
