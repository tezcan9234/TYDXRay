import numpy as np
import pyvista as pv
import os

# === PARAMETRELER ===
z_index = 10  # Glow uygulanacak Z slice
veri_yolu = "data_4d/voxel_3d_data.npy"

# === VERIYI YÜKLE ===
if not os.path.exists(veri_yolu):
    raise FileNotFoundError(f"Veri dosyası bulunamadı: {veri_yolu}")

data = np.load(veri_yolu)
print(f"[INFO] Voxel datası yüklendi, şekil: {data.shape}")

Z, Y, X = data.shape

# === SADECE Z-SLICE GÖSTER ===
slice_data = data[z_index, :, :]
grid2d = pv.ImageData(dimensions=(X, Y, 1), spacing=(1, 1, 1))
grid2d.point_data["glow"] = slice_data.flatten(order="F")

# === SAHNE ===
plotter = pv.Plotter()
plotter.add_mesh(grid2d, scalars="glow", cmap="hot", show_scalar_bar=True)
plotter.add_text(f"Z-Slice Glow: z={z_index}", font_size=12)
plotter.show()
