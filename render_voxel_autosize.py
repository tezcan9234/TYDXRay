import numpy as np
import pyvista as pv
import math

with open("altin.v3d", "rb") as f:
    raw = f.read()

# 🎯 Başlıktaki ilk 64 byte'ı atla
data_bytes = raw[64:]

# 🧠 Formatı dene: uint8
voxels = np.frombuffer(data_bytes, dtype=np.uint8)

# 🔢 Toplam boyut
total_voxels = voxels.size
print(f"[OK] Okunan toplam voxel: {total_voxels}")

# ⚙️ Otomatik boyut tahmini (küp köküyle)
side = round(total_voxels ** (1 / 3))
print(f"🔁 Tahmini boyut: {side} x {side} x {side}")

# ❗ Küp yapmaya zorla
expected_voxel_count = side ** 3
voxels = voxels[:expected_voxel_count]
voxels = voxels.reshape((side, side, side))

# 📦 Grid hazırla
grid = pv.UniformGrid()
grid.dimensions = np.array(voxels.shape) + 1
grid.origin = (0, 0, 0)
grid.spacing = (1, 1, 1)
grid.cell_data["values"] = voxels.flatten(order="F")

# 🎨 Görselleştir
plotter = pv.Plotter()
plotter.add_volume(grid, scalars="values", cmap="viridis", opacity="sigmoid")
plotter.show()
