import numpy as np
from matplotlib import cm

def apply_anomaly_colormap(normalized_data, colormap_name='jet'):
    """
    Normalize edilmiş voxel verisine renk haritası uygular (RGB olarak döner).
    """
    cmap = cm.get_cmap(colormap_name)
    colored_data = cmap(normalized_data)  # RGBA (4 kanal)
    return (colored_data[:, :, :3] * 255).astype(np.uint8)  # RGB dönüştür
