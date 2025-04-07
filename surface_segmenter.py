import numpy as np
from scipy.ndimage import label

def segment_surfaces(grid, threshold=0.7):
    values = grid["intensity"]
    binary_mask = values > threshold

    # Hücre boyutlarını hesapla (n_cells)
    cell_shape = tuple(d - 1 for d in grid.dimensions)

    # 3D olarak yeniden şekillendir
    binary_mask_3d = binary_mask.reshape(cell_shape, order='F')

    # Komşuluk yapısı (6-connectivity)
    structure = np.ones((3, 3, 3))

    # Etiketleme işlemi
    labeled, num_features = label(binary_mask_3d, structure=structure)
    return labeled, num_features
