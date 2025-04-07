import numpy as np
import pyvista as pv

def create_zslice_grid(z_value=10):
    x, y, z = np.mgrid[0.2:20:0.2, 0:20, 0:20]
    values = np.sqrt((x - 10)**2 + (y - 10)**2 + (z - z_value)**2)

    mask = z == z_value
    x_slice = x[mask]
    y_slice = y[mask]
    z_slice = z[mask]
    val_slice = values[mask]

    points = np.vstack((x_slice, y_slice, z_slice)).astype(np.float32).T
    grid = pv.PolyData(points)
    grid["values"] = val_slice

    return grid

def render_zslice_glow():
    grid = create_zslice_grid(z_value=10)

    plotter = pv.Plotter(window_size=(800, 600))
    plotter.set_background("black")

    plotter.add_mesh(
        grid,
        scalars="values",
        cmap="turbo",
        point_size=10.0,
        render_points_as_spheres=True
    )

    plotter.show(auto_close=False)

if __name__ == "__main__":
    render_zslice_glow()
