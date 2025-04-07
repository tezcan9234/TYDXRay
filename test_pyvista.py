import pyvista as pv
import numpy as np

# Basit bir örnek veri
grid = pv.ImageData(dimensions=(10, 10, 10))
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)

# Rastgele veri ekleyelim
data = np.random.random((10, 10, 10)) * 100
grid.point_data["intensity"] = data.flatten()

# PyVista Qt ile görselleştirme yapalım
plotter = pv.Plotter(off_screen=False)  # Off-screen yerine normal render
plotter.add_mesh(grid, cmap="viridis", opacity="sigmoid", show_scalar_bar=True)
plotter.show()
