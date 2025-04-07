# visualization/object_shape_mapper.py

import numpy as np
from scipy.ndimage import label

def detect_shapes_from_voxels(voxel_grid, threshold=1):
    """
    Voxel grid içindeki kümeleri bulur ve basit geometrik şekil sınıflaması yapar.
    """
    binary_grid = (voxel_grid >= threshold).astype(np.int8)

    # Kümeleri etiketle
    labeled_array, num_features = label(binary_grid)

    detected_shapes = []

    for label_id in range(1, num_features + 1):
        # O kümeye ait tüm voxel koordinatlarını al
        coords = np.argwhere(labeled_array == label_id)

        if coords.shape[0] < 10:
            continue  # Çok küçük kümeleri geç

        # Şekil boyutunu bul
        min_vals = coords.min(axis=0)
        max_vals = coords.max(axis=0)
        dims = max_vals - min_vals + 1

        # Sınıflandırma
        if np.all(np.abs(dims - dims[0]) <= 2):
            shape = "küp"
        elif np.max(dims) / np.min(dims) > 2:
            shape = "silindir/blok"
        elif dims[2] < dims[0] and dims[2] < dims[1]:
            shape = "plaka/taş"
        else:
            shape = "belirsiz şekil"

        center = coords.mean(axis=0)
        detected_shapes.append({
            "shape": shape,
            "size": dims.tolist(),
            "center": center.tolist(),
            "voxel_count": coords.shape[0]
        })

    return detected_shapes
