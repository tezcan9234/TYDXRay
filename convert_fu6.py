import numpy as np

def convert_fu6(input_path, output_path, shape):
    try:
        with open(input_path, 'rb') as f:
            raw_bytes = f.read()

        float_count = shape[0] * shape[1] * shape[2]
        expected_byte_size = float_count * 4  # 4 byte per float
        actual_byte_size = len(raw_bytes)

        print(f"[INFO] Veri boyutu: {actual_byte_size} byte, {actual_byte_size // 4} adet float")

        if actual_byte_size > expected_byte_size:
            print(f"[UYARI] {actual_byte_size - expected_byte_size} byte fazla tespit edildi, kesiliyor...")
            raw_bytes = raw_bytes[:expected_byte_size]
        elif actual_byte_size < expected_byte_size:
            raise ValueError("[HATA] Veri boyutu beklenenden küçük, dosya eksik olabilir!")

        float_data = np.frombuffer(raw_bytes, dtype=np.float32)
        float_data.tofile(output_path)
        print(f"[BAŞARILI] Dönüştürülen dosya: {output_path}")

    except Exception as e:
        print(f"[HATA] FU6 dönüştürmede sorun oluştu: {e}")
