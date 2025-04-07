import numpy as np
import matplotlib.pyplot as plt

# === [1] Voxel Datasını Yükle ===
print("[INFO] Voxel datası yükleniyor...")
data = np.load("voxel_data.npy")
print(f"[INFO] Voxel datası yüklendi, şekil: {data.shape}")

# === [2] Normalize Et ===
data = data - np.min(data)
if np.max(data) != 0:
    data = data / np.max(data)

# === [3] Ortaya Parıltı Noktası Ekleyelim ===
data[4, 18, 1] = 1.0

# === [4] Z-Slice Seç ===
z_index = data.shape[2] // 2
slice_data = data[:, :, z_index]

# === [5] Matplotlib ile Görselleştir ===
plt.figure(figsize=(8, 6))
plt.imshow(slice_data.T, cmap="plasma", origin="lower")
plt.colorbar(label="Yoğunluk")
plt.title(f"Z-Slice Glow Görselleştirme (Z={z_index})")
plt.axis("off")
plt.tight_layout()
plt.show()
