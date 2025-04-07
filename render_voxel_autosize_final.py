import numpy as np
import pyvista as pv

# Veriyi oku
with open("altin.v3d", "rb") as f:
    f.read(64)  # header'ı atla
    data = f.read()

# uint8 olarak al, float32'ye çevir
voxels = np.frombuffer(data, dtype=np.uint8).astype(np.float32)

# Otomatik küp hesapla
length = len(voxels)
side = int(length ** (1/3))
total_voxels = side ** 3
if length > total_voxels:
    voxels = voxels[:total_voxels]

print(f"[AUTO] Boyut: {side}³ = {total_voxels} voxel")
print(f"[INFO] Okunan veri: {len(voxels)}")

voxels = voxels.reshape((side, side, side))

# Grid oluştur
grid = pv.UniformGrid()
grid.dimensions = np.array(voxels.shape) + 1
grid.origin = (0, 0, 0)
grid.spacing = (1, 1, 1)

# ✅ Doğrudan point_data’ya ata (BU HATAYI ÇÖZER!)
grid.point_data["values"] = voxels.flatten(order="F")

# Göster
plotter = pv.Plotter()
plotter.add_volume(grid, scalars="values", cmap="plasma", opacity="sigmoid")
plotter.show()
