
import pyvista as pv
import numpy as np

# .v3d dosyasını oku (32 bayt header'dan sonra)
with open("altin.v3d", "rb") as f:
    f.seek(32)
    data = np.frombuffer(f.read(), dtype=np.uint8)

# Voxel şekli (örnek veri için)
shape = (43, 43, 41)
data = data[:np.prod(shape)]
data_reshaped = data.reshape(shape)

# UniformGrid oluştur
grid = pv.UniformGrid()
grid.dimensions = np.array(shape) + 1  # Nokta sayısı = hücre + 1
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)

# Veriyi doğrudan ata (point-data olarak)
grid["values"] = data_reshaped.flatten(order="F")

# Görselleştir
plotter = pv.Plotter()
plotter.add_volume(grid, scalars="values", cmap="plasma", opacity="linear")
plotter.show()
