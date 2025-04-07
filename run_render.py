import numpy as np
from render_voxel import render_voxel_mask

# 10x10x10 boyutlu rastgele 0-1 mask
mask = np.random.randint(0, 2, (10, 10, 10))

# Pencere açarak render al
render_voxel_mask(mask, pencere=True)

if __name__ == "__main__":
    import numpy as np
    # Örnek: 10x10x10 boyutlu rastgele 0-1 mask
    mask = np.random.randint(0, 2, (10, 10, 10))

    # Fonksiyonun adı sizde 'render_voxel_mask' olabilir:
    render_voxel_mask(mask, pencere=True)
