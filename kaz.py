import argparse
import numpy as np
from visualization.render_voxel_with_overlay import render_voxel

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dosya', required=True)
    parser.add_argument('--shape', required=True, type=str)
    parser.add_argument('--render', action='store_true')
    args = parser.parse_args()

    shape = tuple(map(int, args.shape.split(',')))
    expected = shape[0] * shape[1] * shape[2]

    with open(args.dosya, 'rb') as f:
        raw = f.read()
        veri = np.frombuffer(raw, dtype=np.float32)

    print(f"[OK] V3D boyutu: {len(veri)} değer, beklenen: {expected}")

    if len(veri) > expected:
        print(f"[UYARI] Fazla veri tespit edildi: {len(veri) - expected} adet kesiliyor...")
        veri = veri[:expected]
    elif len(veri) < expected:
        print(f"[HATA] V3D okunamadı: V3D boyutu ile shape uyuşmuyor.")
        print(f"[!] Beklenen: {expected}, Gelen: {len(veri)}")
        return

    if args.render:
        render_voxel(veri, shape)

if __name__ == '__main__':
    main()
