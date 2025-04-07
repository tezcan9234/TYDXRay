
# final_test_overlay.py

import numpy as np
from visualization.object_shape_mapper import detect_shapes_from_voxels
from visualization.material_predictor import predict_material
from visualization.intelligent_overlay import generate_overlay_text

# 📦 Sahte veriyle 20x20x20 grid oluştur
voxel_grid = np.zeros((20, 20, 20))
voxel_grid[5:10, 5:10, 5:10] = 1  # Küp yerleştir

# Aynı küpün manyetik değerleri
voxel_values = [120, 135, 140, 145, 150, 130, 125, 138, 132, 147]

# 🔎 Şekil tespiti
shapes = detect_shapes_from_voxels(voxel_grid)
if shapes:
    shape_info = shapes[0]  # İlk şekli al

    # 🧲 İçerik tahmini
    material_label = predict_material(voxel_values)

    # ✍️ Final yazısı
    overlay = generate_overlay_text(shape_info, material_label)

    # 📢 Sonucu göster
    print("🧠 TYDX TESPİT SONUCU")
    print(overlay)
else:
    print("❌ Herhangi bir şekil tespit edilemedi.")
