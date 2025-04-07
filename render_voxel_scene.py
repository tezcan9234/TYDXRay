# -----------------------------
# 📁 File: parser/manyetik_parser.py
# Görev: CSV, FU, 3VD verilerini 3D matris yapısına dönüştür
# -----------------------------
import numpy as np
import os


def parse_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    if ext == '.csv':
        return parse_csv(filepath)
    elif ext == '.fu':
        return parse_fu(filepath)
    elif ext == '.3vd':
        return parse_3vd(filepath)
    else:
        raise ValueError("Desteklenmeyen dosya formatı: " + ext)


def parse_csv(filepath):
    data = np.loadtxt(filepath, delimiter=',')
    return data.reshape((-1, 10, 10))  # Örnek grid boyutu


def parse_fu(filepath):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            row = [float(val) for val in line.strip().split()]
            data.append(row)
    return np.array(data).reshape((-1, 10, 10))


def parse_3vd(filepath):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            x, y, z, val = line.strip().split(',')
            data.append((int(x), int(y), int(z), float(val)))

    max_x = max([d[0] for d in data]) + 1
    max_y = max([d[1] for d in data]) + 1
    max_z = max([d[2] for d in data]) + 1

    volume = np.zeros((max_z, max_y, max_x))
    for x, y, z, val in data:
        volume[z, y, x] = val
    return volume


# Örnek kullanım:
if __name__ == "__main__":
    volume_data = parse_file("../data/sample.csv")
    print("Veri boyutu:", volume_data.shape)


# -----------------------------
# 📁 File: visualization/voxel_auto_shaper.py
# Görev: 3D matris verisinden küp, kürek, tünel gibi yapıları algılamak
# -----------------------------
import numpy as np

def detect_shapes(volume):
    shapes = []
    threshold = np.mean(volume) + np.std(volume)

    z_dim, y_dim, x_dim = volume.shape
    for z in range(1, z_dim - 1):
        for y in range(1, y_dim - 1):
            for x in range(1, x_dim - 1):
                val = volume[z, y, x]
                if val > threshold:
                    shapes.append({
                        'type': guess_shape(volume, x, y, z),
                        'pos': (x, y, z),
                        'intensity': val
                    })
    return shapes


def guess_shape(volume, x, y, z):
    """
    Basit bir şekil tahmin sistemi:
    - Yüzeyde ince uzun: "shovel"
    - Derin büyük blok: "metal_block"
    - Derin yarı boşluk: "void/tunnel"
    """
    region = volume[z-1:z+2, y-1:y+2, x-1:x+2]
    mean_val = np.mean(region)

    if mean_val > np.mean(volume) * 1.5:
        if region.shape[0] == 3 and region.shape[1] == 3 and region.shape[2] >= 2:
            return "shovel"
        return "metal_block"
    elif mean_val < np.mean(volume) * 0.5:
        return "void/tunnel"
    else:
        return "unknown"


# Örnek test:
if __name__ == "__main__":
    test_volume = np.random.rand(20, 20, 20)
    test_volume[10:13, 10:13, 10:15] += 3.5  # Metal blok
    shapes = detect_shapes(test_volume)
    for s in shapes:
        print(s)


# -----------------------------
# 📁 File: visualization/render_voxel_scene.py
# Görev: Tespit edilen şekilleri sahnede çiz, glow + pulse + renk ile
# -----------------------------
import pyvista as pv
from visualization.voxel_auto_shaper import detect_shapes
import numpy as np


def render_voxel_scene(volume):
    plotter = pv.Plotter()
    plotter.set_background("black")

    # Ana voxel grid (renklendirme: yoğunluk)
    grid = pv.wrap(volume)
    plotter.add_volume(grid, cmap="plasma", opacity="sigmoid")

    # Tespit edilen şekiller
    shapes = detect_shapes(volume)
    for shape in shapes:
        x, y, z = shape['pos']
        mesh = pv.Cube(center=(x, y, z), x_length=1, y_length=1, z_length=1)

        color = {
            "metal_block": "red",
            "shovel": "yellow",
            "void/tunnel": "blue",
            "unknown": "white"
        }.get(shape['type'], "white")

        plotter.add_mesh(mesh, color=color, opacity=0.8, show_edges=False)

    plotter.show()


# Örnek test:
if __name__ == "__main__":
    volume = np.random.rand(20, 20, 20)
    volume[12:15, 10:13, 10:12] += 4.0  # Sahte metal yapı
    render_voxel_scene(volume)