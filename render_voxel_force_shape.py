import numpy as np
import pyvista as pv

# Manuel boyutlar
X, Y, Z = 64, 64, 32
VOXEL_COUNT = X * Y * Z

with open("altin.v3d", "rb") as f:
    raw = f.read()

# Başlık atla (örnek olarak ilk 64 byte atlanıyor)
data_bytes = raw[64:]

# float32 olarak veriyi çözümle
try:
    voxels = np.frombuffer(data_bytes, dtype=np.float32)
except:
    raise RuntimeError("Veri float32 değil. Alternatif çözümleme gerekebilir.")

if voxels.size != VOXEL_COUNT:
    print(f"❌ Hedef boyut: {VOXEL_COUNT}, ama okunan: {voxels.size}")
    exit()

voxels = voxels.reshape((X, Y, Z))

# PyVista grid oluştur
grid = pv.UniformGrid()
grid.dimensions = np.array(voxels.shape) + 1
grid.origin = (0, 0, 0)
grid.spacing = (1, 1, 1)
grid.cell_data["values"] = voxels.flatten(order="F")

# Görselleştir
plotter = pv.Plotter()
plotter.add_volume(grid, scalars="values", cmap="plasma", opacity="linear")
plotter.show()
