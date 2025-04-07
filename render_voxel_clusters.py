import numpy as np
from sklearn.cluster import DBSCAN
import pyvista as pv
from sklearn.preprocessing import StandardScaler

# 1. thresholded voxellerin koordinatlarını al
points = np.array(thresholded_points)  # (N, 3) boyutlu (x, y, z)

# 2. normalize et (DBSCAN daha iyi çalışsın)
scaler = StandardScaler()
points_scaled = scaler.fit_transform(points)

# 3. DBSCAN ile kümeleme
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(points_scaled)  # her point için küme ID

# 4. VTK için renkli point cloud oluştur
point_cloud = pv.PolyData(points)
point_cloud["cluster_id"] = labels  # her noktaya ID ata

# 5. Küme ID’lerine göre renkli görselleştir
plotter = pv.Plotter()
plotter.add_points(point_cloud, scalars="cluster_id", cmap="tab10", point_size=10)
plotter.show()
