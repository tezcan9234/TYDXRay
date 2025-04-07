
import pyvista as pv
import numpy as np

# .v3d dosyasını oku
with open("altin.v3d", "rb") as f:
    f.seek(32)  # header'ı atla
    data = np.frombuffer(f.read(), dtype=np.uint8)

# Boyutları belirle (örnek: en uygun küp boyut)
# 43*43*41 = 75989 (yakın ama küçük), en yakın 1: 43x43x42 = 77658 → fazla
# Otomatik olarak en uygun olanı kullanmak için:
def find_best_shape(n):
    for z in range(30, 100):
        for y in range(30, 100):
            for x in range(30, 100):
                if x * y * z == n:
                    return (x, y, z)
    return None

shape = find_best_shape(len(data))
if shape is None:
    # Alternatif olarak en yakın küp boyut: 43x43x41 = 75989 → kalan kısmı kırp
    shape = (43, 43, 41)
    data = data[:43*43*41]

x_len, y_len, z_len = shape
data_reshaped = data.reshape((x_len, y_len, z_len))

# Voxel koordinatlarını oluştur
x, y, z = np.meshgrid(np.arange(x_len), np.arange(y_len), np.arange(z_len), indexing="ij")
grid = pv.StructuredGrid(x, y, z)

# Veriyi ata
grid["values"] = data_reshaped.flatten()

# Görselleştir
plotter = pv.Plotter()
plotter.add_mesh(grid, scalars="values", cmap="plasma", opacity='linear', show_edges=False)
plotter.show()
