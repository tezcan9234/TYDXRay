import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Voxel boyutu
nx, ny, nz = 11, 11, 11

# Rastgele yoğunluk
data = np.random.uniform(0, 100, (nx, ny, nz))

# Eşikle glow gösterimi
threshold = 75
voxels = data > threshold

# Renk haritası
colors = np.empty(voxels.shape, dtype=object)
colors[voxels] = 'red'
colors[~voxels] = 'blue'

# Görselleştir
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='k')

ax.set_title("TezXRay - Matplotlib Voxel Viewer")
plt.show()
