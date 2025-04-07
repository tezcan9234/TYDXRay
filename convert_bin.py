import struct
import numpy as np

def convert_bin(input_path, output_path, shape):
    try:
        with open(input_path, "rb") as f:
            raw = f.read()
            floats = struct.unpack(f"{len(raw) // 4}f", raw)
            data = np.array(floats).reshape(shape)
            data.astype(np.float32).tofile(output_path)
            print(f"[✓] BIN verisi başarıyla dönüştürüldü: {output_path}")
    except Exception as e:
        print(f"[HATA] BIN dönüştürmede sorun oluştu: {e}")
