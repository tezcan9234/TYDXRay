import numpy as np
import os

# 4D veri boyutunu belirle (örnek: 20x20x20 voxel, 5 zaman adımı)
grid_size = (20, 20, 20)
time_steps = 5

# Sahte manyetik veriler üret (gerçek dosya yerine simülasyon)
voxel_4d = np.zeros((grid_size[0], grid_size[1], grid_size[2], time_steps))

for t in range(time_steps):
    # Zaman ilerledikçe ortaya çıkan bir "anomali küp" simülasyonu
    cube_start = 5 + t
    cube_end = 8 + t
    voxel_4d[cube_start:cube_end, cube_start:cube_end, cube_start:cube_end, t] = 100

    # Zamanla genişleyen boşluk (düşük değer)
    voxel_4d[2:5, 2:5, t:3+t, t] = 5

# Veriyi klasöre kaydet
os.makedirs("data_4d", exist_ok=True)
output_path = "data_4d/voxel_4d_data.npy"
np.save(output_path, voxel_4d)
print(f"✅ 4D voxel verisi kaydedildi: {output_path}")
