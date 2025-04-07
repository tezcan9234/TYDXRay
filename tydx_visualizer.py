import pyvista as pv
import numpy as np

def create_scene_from_data(data_points):
    grid = np.zeros((30, 10, 10))  # 10 → 30 yap


    for dp in data_points:
        try:
            parts = dp.split(",")
            x, y, z = int(parts[0]), int(parts[1]), int(parts[2])
            value = float(parts[3])

            if value < -20:
                grid[x, y, z] = 2  # Void (blue)
            elif value > 20:
                grid[x, y, z] = 3  # Metal (red)
            else:
                grid[x, y, z] = 1  # Neutral/other

        except Exception as e:
            print("Veri ayrıştırma hatası:", e)

    plotter = pv.Plotter(window_size=(800, 600))
    plotter.set_background("white")

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            for z in range(grid.shape[2]):
                val = grid[x, y, z]
                if val == 0:
                    continue

                color = "gray"
                if val == 1:
                    color = "orange"
                elif val == 2:
                    color = "blue"
                elif val == 3:
                    color = "red"

                cube = pv.Cube(center=(x, y, z), x_length=0.9, y_length=0.9, z_length=0.9)
                plotter.add_mesh(cube, color=color, opacity=0.6)

    plotter.add_text("TYDX – Canlı Cihaz Taraması", font_size=12)
    plotter.show()
