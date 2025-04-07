import pyvista as pv
import numpy as np

def render_voxel(grid):
    np.seterr(all='ignore')  # Tüm uyarı sistemini kapat

    shape = grid.shape
    print(f"Render başlatılıyor... Grid şekli: {shape}")

    if len(shape) == 2:
        shape = (shape[0], shape[1], 1)
        grid = grid.reshape(shape)

    grid = np.nan_to_num(grid, nan=0.0, posinf=0.0, neginf=0.0)

    gmin = np.min(grid)
    gmax = np.max(grid)
    if gmax - gmin == 0:
        gmax += 1e-6

    grid = (grid - gmin) / (gmax - gmin)
    grid = grid.astype(np.float32)

    color_data = np.zeros_like(grid)
    color_data[grid < 0.3] = 0.1
    color_data[(grid >= 0.3) & (grid < 0.6)] = 0.5
    color_data[grid >= 0.6] = 0.9

    grid_pv = pv.UniformGrid()
    grid_pv.dimensions = np.array(shape) + 1
    grid_pv.origin = (0, 0, 0)
    grid_pv.spacing = (1, 1, 1)
    grid_pv["anomaly_values"] = color_data.flatten(order="F")

    plotter = pv.Plotter()
    plotter.add_volume(grid_pv,
                       scalars="anomaly_values",
                       cmap="coolwarm",
                       opacity=[0.0, 0.3, 0.6, 0.9, 1.0],
                       opacity_unit_distance=2.5,
                       shade=True,
                       show_scalar_bar=True)
    plotter.show()
