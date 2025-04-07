import numpy as np
import os
import pyvista as pv
from pyvistaqt import BackgroundPlotter

# --- AYARLAR ---
data_path = "data_4d/voxel_3d_data.npy"
z_index = 10  # Glow efekti uygulanacak Z dilimi

# --- VERİYİ YÜKLE ---
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Veri bulunamadı: {data_path}")

voxel_data = np.load(data_path)
print(f"[INFO] Voxel datası yüklendi, shape: {voxel_data.shape}")  # (Z, Y, X)

if voxel_data.ndim != 3:
    raise ValueError("3 boyutlu veri bekleniyor (Z, Y, X)!")

Z, Y, X = voxel_data.shape

# --- GRID OLUŞTUR ---
grid = pv.UniformGrid()
grid.dimensions = (X, Y, Z)  # (nx, ny, nz)
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)

# --- GLOW VERİSİ OLUŞTUR ---
glow_volume = np.zeros_like(voxel_data, dtype=np.float32)
if 0 <= z_index < Z:
    glow_volume[z_index, :, :] = voxel_data[z_index, :, :]

glow_flat = glow_volume.flatten(order="F")
if glow_flat.shape[0] != grid.n_points:
    raise ValueError(f"Glow verisi uyumsuz: {glow_flat.shape[0]} vs {grid.n_points}")

grid.point_data["glow"] = glow_flat

# --- SAHNE: Qt destekli pencere ---
plotter = BackgroundPlotter(title="Z-Slice Glow", window_size=(1000, 800))
plotter.add_volume(grid, scalars="glow", cmap="hot", opacity="sigmoid", show_scalar_bar=True)
plotter.add_text(f"Z-Glow Slice: z={z_index}", font_size=14)

# pencereyi aç
plotter.show(auto_close=False)
