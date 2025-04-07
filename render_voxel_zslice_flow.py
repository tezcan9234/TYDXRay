
import pyvista as pv
import numpy as np
import os

os.environ["PYVISTA_USE_MESA"] = "1"

# Grid boyutu ve verisi
x, y, z = np.mgrid[0:10, 0:10, 0:10]
values = np.sqrt((x - 5)**2 + (y - 5)**2 + (z - 5)**2)
values = (values.max() - values) * 10  # Anomaly yoğunluğu

# StructuredGrid oluştur
grid = pv.StructuredGrid(x, y, z)
grid["intensity"] = values.ravel(order="F")

# Plotter oluştur
plotter = pv.Plotter()
plotter.set_background("black")

# Z-slice efekti
slice_index = 5  # Orta katmanı alıyoruz
slice_grid = grid.slice(normal='z', value=slice_index)

plotter.add_mesh(slice_grid, scalars="intensity", cmap="plasma", opacity=0.5)

# 4D flow: Her yeni veriyle sahnenin güncellenmesi
def update_scene():
    # Yeni veri (Z katmanındaki farklı bir değer alınıyor)
    slice_grid = grid.slice(normal='z', value=slice_index + 1)
    plotter.update()
    plotter.add_mesh(slice_grid, scalars="intensity", cmap="plasma", opacity=0.5)

# Kamera ayarı
plotter.view_isometric()

# Z-slice animasyonu
plotter.add_callback(update_scene, interval=1000)  # Her 1 saniyede bir yeni katman gösterilecek

plotter.show(title="Z-slice and 4D Flow - TYDX")
