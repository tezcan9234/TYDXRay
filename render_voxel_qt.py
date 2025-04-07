from pyvistaqt import BackgroundPlotter
import pyvista as pv
import numpy as np

pv.set_plot_theme("document")

# Voxel grid
grid = pv.ImageData()
grid.dimensions = (11, 11, 11)
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)
grid.point_data["intensity"] = np.random.rand(grid.n_points)

# Qt destekli plotter
plotter = BackgroundPlotter()
plotter.add_volume(
    grid,
    scalars="intensity",
    cmap="plasma",
    opacity="linear",
    shade=True,
    show_scalar_bar=True
)

# ❌ show() YOK! BackgroundPlotter zaten pencereyi açıyor
# ✅ Bu dosya sadece çalıştırılmalı, pencereyi o açar
