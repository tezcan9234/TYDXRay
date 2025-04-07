from utils.normalizer import normalize_voxel_data
from visualization.anomaly_colormap import apply_anomaly_colormap
from report.exporter import save_voxel_scene_as_png, generate_pdf_report, compute_statistics

import numpy as np
import os

# Çıkış klasörü oluştur
os.makedirs("outputs", exist_ok=True)

# Örnek veri
data = np.random.rand(50, 50, 1)  # Simülasyon verisi
normalized = normalize_voxel_data(data)
colored = apply_anomaly_colormap(normalized.squeeze())

# Kaydet ve raporla
stats = compute_statistics(normalized)
save_voxel_scene_as_png(colored)
generate_pdf_report(stats=stats)
