import struct
import numpy as np
import pyvista as pv

def oku_ve_gorsellestir(v3d_dosya_yolu):
    # Veriyi oku ve float32 dizisine çevir
    with open(v3d_dosya_yolu, "rb") as f:
        data = f.read()

    manyetik_degerler = []
    for i in range(0, len(data), 4):
        try:
            val = struct.unpack("<f", data[i:i+4])[0]
            manyetik_degerler.append(val)
        except:
            continue

    manyetik_degerler = np.array(manyetik_degerler)

    # Şekil belirleme (otomatik grid şekli denemesi)
    for x in range(10, 100):
        for y in range(10, 100):
            if len(manyetik_degerler) % (x * y) == 0:
                z = len(manyetik_degerler) // (x * y)
                volume = manyetik_degerler.reshape((x, y, z))
                break

    # PyVista ile görselleştir
    grid = pv.UniformGrid()
    grid.dimensions = np.array(volume.shape) + 1
    grid.spacing = (1, 1, 1)
    grid.origin = (0, 0, 0)
    grid.cell_data["manyetik"] = volume.flatten(order="F")

    plotter = pv.Plotter()
    opacity = [0, 0.1, 0.2, 0.4, 0.6, 1.0]
    plotter.add_volume(grid, cmap="coolwarm", opacity=opacity)
    plotter.show()

# Kullanım örneği:
oku_ve_gorsellestir("kaya içi kazan.v3d")
