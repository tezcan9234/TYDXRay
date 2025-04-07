import pyvista as pv
import numpy as np
import os

os.environ["PYVISTA_USE_MESA"] = "1"

# Grid boyutu ve verisi
x, y, z = np.mgrid[0:10, 0:10, 0:10]
values = np.sqrt((x - 5)**2 + (y - 5)**2 + (z - 5)**2)
values = (values.max() - values) * 10  # Anomaly yoğunluğu

# Anomali tipi tespiti: Metal = kırmızı, Boşluk = mavi, Altın = sarı
anomaly_types = np.select(
    [values < 10, (values >= 10) & (values < 20), values >= 20],
    ['metal', 'void', 'gold'],
    default='unknown'
)

# StructuredGrid oluştur
grid = pv.StructuredGrid(x, y, z)
grid["intensity"] = values.ravel(order="F")
grid["anomaly_type"] = anomaly_types.ravel(order="F")

# Plotter oluştur
plotter = pv.Plotter()
plotter.set_background("black")
plotter.add_volume(
    grid,
    scalars="intensity",
    cmap="plasma",
    opacity="sigmoid",
    clim=[values.min(), values.max()],
    shade=True
)

# Anomali tipi tespiti ve renk kodlaması
plotter.add_mesh(grid, scalars="anomaly_type", show_edges=False, cmap="coolwarm", opacity=0.5)

# Kamera ayarı (isteğe bağlı)
plotter.view_isometric()
plotter.show(title="Anomaly Detection and Glow - TYDX")
