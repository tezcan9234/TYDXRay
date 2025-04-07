import pyvista as pv
import numpy as np

pv.set_plot_theme("document")

grid = pv.UniformGrid()
grid.dimensions = (11, 11, 11)
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)

# ÇALIŞAN YÖNTEM 👇
grid.point_data["intensity"] = np.random.rand(grid.n_points)

plotter = pv.Plotter()
plotter.add_volume(
    grid,
    scalars="intensity",
    cmap="plasma",
    opacity="linear",
    shade=True,
    show_scalar_bar=True
)
plotter.show(auto_close=False)
plotter.iren.start()
