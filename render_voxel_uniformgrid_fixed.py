import pyvista as pv
import numpy as np

# V3D dosyasını oku
with open("altin.v3d", "rb") as f:
    shape_bytes = f.read(12)  # 3 adet int32 = 12 byte
    shape = np.frombuffer(shape_bytes, dtype=np.int32)
    nx, ny, nz = shape
    print(f"[OK] Shape: {nx}x{ny}x{nz}")
    
    data_bytes = f.read()
    data = np.frombuffer(data_bytes, dtype=np.float32)

# Boyut kontrolü
expected_size = nx * ny * nz
if data.size != expected_size:
    raise ValueError(f"[HATA] Veri boyutu uyumsuz: {data.size} != {expected_size}")

# 3D array'e çevir
values = data.reshape((nx, ny, nz))

# Grid oluştur
grid = pv.UniformGrid()
grid.dimensions = np.array(values.shape) + 1
grid.origin = (0, 0, 0)
grid.spacing = (1, 1, 1)
grid.cell_data["values"] = values.flatten(order="F")

# Nokta datasına çevir ve göster
point_grid = grid.cell_data_to_point_data()

plotter = pv.Plotter()
plotter.add_volume(point_grid, scalars="values", cmap="plasma", opacity="linear")
plotter.show()
