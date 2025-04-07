# visualization/material_predictor.py

def predict_material(voxel_values):
    import numpy as np

    if len(voxel_values) == 0:
        return "veri yok"

    mean_val = np.mean(voxel_values)
    max_val = np.max(voxel_values)
    min_val = np.min(voxel_values)

    if mean_val > 150 and max_val > 200:
        return "YOĞUN METAL (örnek: demir, büyük obje)"
    elif 70 < mean_val <= 150:
        return "MUHTEMEL ALTIN veya KÜÇÜK METAL CİSİM"
    elif -20 < mean_val <= 70:
        return "NORMAL TOPRAK veya ZAYIF MADDE"
    elif mean_val <= -20:
        return "BOŞLUK veya TAŞ YAPILI ALAN"
    else:
        return "TANIMSIZ"
