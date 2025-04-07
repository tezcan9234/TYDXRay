import numpy as np
import pyvista as pv

# Sahte veri üret (yerine gerçek veri dosyasını okuyabilirsin)
nx, ny, nz = 30, 30, 30
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
z = np.linspace(0, 1, nz)
grid_data = np.random.rand(nx, ny, nz)

# Z dilimi seç
z_index = 15  # Ortadaki katman
slice_data = grid_data[:, :, z_index]

# StructuredGrid oluştur
grid = pv.StructuredGrid()
xv, yv = np.meshgrid(np.arange(nx), np.arange(ny), indexing='ij')
zv = np.full_like(xv, z_index)

points = np.column_stack((xv.ravel(), yv.ravel(), zv.ravel()))
grid.points = points
grid.dimensions = [nx, ny, 1]

# Yoğunluk verisini ata
grid.point_data["density"] = slice_data.flatten(order="F")

# Plot sahnesi oluştur
plotter = pv.Plotter()
z_slice = grid

# Ana mesh + kontur efektleri
plotter.add_mesh(z_slice, scalars="density", cmap="coolwarm", show_edges=True, opacity=1.0)

# Kontur çizgileri
contours = z_slice.contour(isosurfaces=10)
plotter.add_mesh(contours, color="black", line_width=1)

plotter.add_axes()
plotter.show(title="Z-Slice Contour View")
