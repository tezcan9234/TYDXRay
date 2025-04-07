import struct

def parse_v3d_file(filepath):
    try:
        with open(filepath, "rb") as file:
            raw_bytes = file.read()

        # Her float 4 byte'tır, kaç tane float olduğunu hesapla
        num_floats = len(raw_bytes) // 4
        floats = struct.unpack(f"{num_floats}f", raw_bytes)

        return list(floats)

    except Exception as e:
        print(f"[HATA] Dosya okunamadı: {e}")
        return []
