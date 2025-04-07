# debug_v3d_header.py

def main():
    try:
        with open("altin.v3d", "rb") as f:
            header = f.read(64)
    except FileNotFoundError:
        print("❌ Dosya bulunamadı: altin.v3d")
        return

    print("📦 İlk 64 byte (ham):")
    print(header)

    print("\n🔍 Byte değerleri (hex):")
    print(" ".join(f"{b:02X}" for b in header))

    print("\n🔢 Byte değerleri (decimal):")
    print(" ".join(str(b) for b in header))

    print("\n📊 İlk 12 byte'ı int32 olarak oku:")
    import struct
    try:
        x, y, z = struct.unpack("iii", header[:12])
        print(f"X: {x}, Y: {y}, Z: {z}")
        print(f"Toplam voxel: {x * y * z}")
    except:
        print("⚠️ İlk 12 byte int32 (3x4) olarak çözümlenemedi.")

if __name__ == "__main__":
    main()
