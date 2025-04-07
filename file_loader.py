import struct
import numpy as np

def load_fu6_file(file_path, boyut=10):
    """FU6 dosyasını oku ve 3D manyetik veri kümesine dönüştür."""
    veriler = []
    with open(file_path, "rb") as f:
        raw = f.read()
        for i in range(0, len(raw), 4):
            try:
                deger = struct.unpack("<f", raw[i:i+4])[0]
                veriler.append(deger)
            except:
                continue

    beklenen = boyut * boyut * boyut
    if len(veriler) != beklenen:
        print(f"[UYARI] Beklenen veri: {beklenen}, ama dosyada: {len(veriler)}")
        return None

    return np.array(veriler).reshape((boyut, boyut, boyut))