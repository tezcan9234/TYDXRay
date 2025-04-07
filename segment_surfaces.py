import numpy as np
import pyvista as pv
from scipy.ndimage import label

def segment_surfaces(grid, threshold=0.7):
    # Grid formatını kontrol et
    shape = grid.shape
    if len(shape) == 2:
        shape = (shape[0], shape[1], 1)
        grid = grid.reshape(shape)

    # Temizlik ve normalizasyon
    grid = np.nan_to_num(grid, nan=0.0, posinf=0.0, neginf=0.0)
    gmin, gmax = np.min(grid), np.max(grid)
    if gmax - gmin == 0:
        gmax += 1e-6
    grid = (grid - gmin) / (gmax - gmin)

    # Eşik üstü voxel'lar (anomaliler) → True
    binary_volume = grid > threshold

    # Segmentasyon: bağlantılı bölgeleri etiketle
    labeled, num_features = label(binary_volume)
    print(f"🔍 Tespit edilen segment sayısı: {num_features}")

    # PyVista görselleştirme
    labeled = labeled.astype(np.float32)
    ug = pv.UniformGrid()
    ug.dimensions = np.array(labeled.shape) + 1
    ug.origin = (0, 0, 0)
    ug.spacing = (1, 1, 1)
    ug["segments"] = labeled.flatten(order="F")

    plotter = pv.Plotter()
    plotter.add_volume(ug,
                       scalars="segments",
                       cmap="tab20",  # Her segment için farklı renk
                       opacity="sigmoid",
                       shade=True,
                       show_scalar_bar=True)
    plotter.show()
