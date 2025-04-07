import numpy as np
import pyvista as pv
from pyvistaqt import BackgroundPlotter

# === [1] Anomaly Voxel Datasını Yükle ===
print("[INFO] Anomali voxel verisi yükleniyor...")
data = np.load("anomaly_cluster.npy")  # Sadece 0 ve 1 içerir
print(f"[INFO] Veri şekli: {data.shape}")

# === [2] PyVista Grid Oluştur ===
grid = pv.UniformGrid()
grid.dimensions = np.array(data.shape) + 1
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)
grid.cell_data["anomaly"] = data.flatten(order="F")

# === [3] PyVista Qt Sahnesi Aç ===
plotter = BackgroundPlotter(title="Anomali 3D Render", window_size=(800, 600))
plotter.set_background("black")

# === [4] Anomali Verisini Render Et ===
plotter.add_volume(
    grid,
    scalars="anomaly",
    opacity=[0.0, 1.0],     # 0 = görünmez, 1 = tam görünür
    cmap="autumn",         # Sarı-turuncu renk tonları
    show_scalar_bar=False
)

# === [5] Kamera & Görünüm ===
plotter.view_isometric()
plotter.show_axes()

# === [6] Sahne Bilgisi ===
print("[INFO] Anomali sahnesi yüklendi. 3D görünüm hazır.")

# === [7] Sahne açık kalsın ===
plotter.show()
