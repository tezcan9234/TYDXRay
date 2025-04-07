import numpy as np
import pyvista as pv
from scipy.ndimage import label

def highlight_clusters(grid, threshold=0.7):
    # Segment yoğunluk eşik değerine göre binary maske
    binary_mask = grid["intensity"] > threshold

    # Yüzey kümelerini etiketle
    structure = np.ones((3, 3, 3), dtype=int)
    dims = (grid.dimensions[0] - 1, grid.dimensions[1] - 1, grid.dimensions[2] - 1)
    labeled, num_features = label(binary_mask.reshape(dims, order='F'), structure=structure)


    # Küme ID'lerini intensity array'ine taşı
    labeled_flat = labeled.flatten(order='F')
    cluster_grid = grid.copy()
    cluster_grid["clusters"] = labeled_flat

    # Plot sahnesi
    p = pv.Plotter(window_size=[800, 600])
    p.set_background("black")

    # Orijinal voxel verisi (hafif saydam)
    p.add_volume(cluster_grid, scalars="intensity", opacity=0.1, cmap="gray")

    # Kümeleri renklendir
    p.add_volume(cluster_grid, scalars="clusters", opacity=0.7, cmap="hot", show_scalar_bar=True)

    p.camera_position = "iso"
    p.show()
