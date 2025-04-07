import pyvista as pv
import numpy as np

def baslat_voxel_demo():
    grid = pv.UniformGrid()
    grid.dimensions = (20, 20, 20)
    grid.spacing = (1, 1, 1)
    grid.origin = (0, 0, 0)

    # Rastgele demo yoğunluk verisi
    data = np.random.rand(20 * 20 * 20)
    grid.cell_data["yoğunluk"] = data  # Cell verisi olarak ekle

    # Hücre verisini nokta verisine çevir (bu adım kritik!)
    grid = grid.cell_data_to_point_data()

    # 3D sahneyi oluştur
    plotter = pv.Plotter()
    plotter.add_volume(grid, scalars="yoğunluk", cmap="plasma", opacity="sigmoid")
    plotter.show(title="TYDX 4D Demo", auto_close=False)

if __name__ == "__main__":
    baslat_voxel_demo()
