import numpy as np
import pyvista as pv

with open("altin.v3d", "rb") as f:
    raw = f.read()

# Başlık (ilk 64 byte) atla
data = raw[64:]
voxels = np.frombuffer(data, dtype=np.uint8)
total = len(voxels)
print(f"[OK] Okunan toplam voxel: {total}")

# En büyük küp için boyut bul
side = int(total ** (1/3))
usable_voxels = side ** 3
voxels = voxels[:usable_voxels]
print(f"🔁 Kullanılan boyut: {side} x {side} x {side}")

# Voxel verisini şekillendir
voxels = voxels.reshape((side, side, side))

# Grid oluştur
grid = pv.UniformGrid(
    dimensions=(side + 1, side + 1, side + 1),
    spacing=(1, 1, 1),
    origin=(0, 0, 0),
)
grid.cell_data.set_array(voxels.flatten(order="F"), "values")

# Görselleştir
plotter = pv.Plotter()
plotter.add_volume(grid, scalars="values", cmap="viridis", opacity="linear")
plotter.show()
