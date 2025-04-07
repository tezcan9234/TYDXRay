import pyvista as pv
import numpy as np

def main():
    # 10x10x10 boyutlu rastgele 0-1 maske
    mask = np.random.randint(0, 2, (10, 10, 10))

    # PyVista UniformGrid oluştur
    grid = pv.UniformGrid()
    grid.dimensions = np.array(mask.shape) + 1
    grid.cell_data["anomaly"] = mask.flatten(order="F")

    # Plotter sahnesi
    plotter = pv.Plotter()
    plotter.add_volume(grid, scalars="anomaly", opacity=[0,1], cmap="viridis")
    plotter.show_axes()

    # Pencereyi kapatma davranışını iptal ediyoruz
    plotter.show(auto_close=False)

    # Terminalde bekletiyoruz
    input("Pencere şu anda açık. Kapatmak için Enter'a basın...")

if __name__ == "__main__":
    main()
