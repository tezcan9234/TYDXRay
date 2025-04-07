# visualization/voxel_renderer_sim.py

import numpy as np
import pyvista as pv

class VoxelRendererSim:
    def __init__(self):
        self.plotter = pv.Plotter(window_size=(800, 600), off_screen=False)
        self.grid_size = (10, 10, 10)
        self.grid = np.zeros(self.grid_size)
        self.x, self.y, self.z = 0, 0, 0
        self.plotter.add_axes()
        self.plotter.set_background("black")

    def add_data(self, value):
        print(f"Gelen veri: {value}")
        try:
            anomaly = value > 180
            color = "red" if anomaly else "blue"
            opacity = 0.9 if anomaly else 0.3

            center = (self.x, self.y, self.z)
            cube = pv.Cube(center=center, x_length=1, y_length=1, z_length=1)
            self.plotter.add_mesh(cube, color=color, opacity=opacity)

            self.z += 1
            if self.z >= self.grid_size[2]:
                self.z = 0
                self.y += 1
                if self.y >= self.grid_size[1]:
                    self.y = 0
                    self.x += 1

            self.plotter.render()  # ✅ Kritik: sahne güncelle
        except Exception as e:
            print(f"[HATA] Voxel eklenemedi: {e}")

    def show(self):
        try:
            self.plotter.show(auto_close=False)
        except Exception as e:
            print(f"[HATA] PyVista gösterim hatası: {e}")
