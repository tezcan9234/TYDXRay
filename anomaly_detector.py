import numpy as np
from scipy.ndimage import label

def tespit_et(voxel_data, threshold=0.9):
    """
    Voxel veri içinden eşik değerin üzerindeki yoğunlukları tespit eder.
    Bağlantılı bölgeleri etiketleyip küme maskesi döner.
    """
    mask = voxel_data > threshold
    labeled, num_clusters = label(mask)
    return labeled, num_clusters

def sadece_anomaliler(voxel_data, threshold=0.9):
    """
    Sadece eşik üstü bölgeleri 0-1 maskesi olarak döner (etiketsiz)
    """
    return (voxel_data > threshold).astype(np.uint8)

if __name__ == "__main__":
    # Test amaçlı çalıştırılabilir
    data = np.random.rand(9, 37, 3)
    labeled, n = tespit_et(data)
    print(f"{n} küme bulundu.")