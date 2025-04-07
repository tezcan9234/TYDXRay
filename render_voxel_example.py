import sys
sys.path.append(r'C:\Users\Monster\Desktop\TYDX\visualization')  # visualizasyon dizinini ekle

import pyvista as pv
import numpy as np
from render_voxel import render_voxel  # doğru yolu kullanarak import et

# Voxel verisi için mesh oluştur
x, y, z = np.mgrid[-5:5:1, -5:5:1, -5:5:1]
values = np.random.random(x.shape)

# Grid oluştur
grid = pv.StructuredGrid(x, y, z)
grid.point_data['values'] = values.flatten()

# Plotter oluştur
plotter = pv.Plotter()

# Voxel render fonksiyonunu çağır
render_voxel(grid, plotter)
