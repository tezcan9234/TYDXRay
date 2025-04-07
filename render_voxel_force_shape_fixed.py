import numpy as np
import pyvista as pv

# 📏 Manuel grid boyutu
X, Y, Z = 64, 64, 32
VOXEL_COUNT = X * Y * Z

with open("altin.v3d", "rb") as f:
    raw = f.read()

# ⛔ İlk 64 byte başlık → veri oradan başlıyor
data_bytes = raw[64:]

# 🧪 Alternatif çözüm: önce uint8 ile deneyelim
try:
    voxels = np.frombuffer(data_bytes, dtype=np.uint8)
    print(f"[INFO] uint8 ile okundu. Toplam: {voxels.size}")
except:
    raise RuntimeError("uint8 çözümlemesi başarısız.")

if voxels.size != VOXEL_COUNT:
    print(f"❌ Beklenen: {VOXEL_COUNT}, Okunan: {voxels.size}")
    exit()

# 🎯 Şekillendir
voxels = voxels.reshape((X, Y, Z))

# 🔲 PyVista Grid
grid = pv.UniformGrid()
grid.dimensions = np.array(voxels.shape) + 1
grid.origin = (0, 0, 0)
grid.spacing = (1, 1, 1)
grid.cell_data["values"] = voxels.flatten(order="F")

# 🎨 Görselleştir
plotter = pv.Plotter()
plotter.add_volume(grid, scalars="values", cmap="viridis", opacity="sigmoid")
plotter.show()
