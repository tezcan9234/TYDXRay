
import pyvista as pv
import numpy as np
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication
import sys

os.environ["PYVISTA_USE_MESA"] = "1"
os.environ["PYVISTA_OFF_SCREEN"] = "false"

plotter = pv.Plotter()
plotter.set_background("black")

# Global variable for Z-slice
z = 0

def add_voxel_layer():
    global z
    x, y = np.meshgrid(np.arange(5), np.arange(5))
    points = np.c_[x.ravel(), y.ravel(), np.full_like(x, z).ravel()].astype(np.float32)
    values = np.random.rand(points.shape[0])
    grid = pv.PolyData(points)
    grid["magnetik"] = values

    plotter.add_points(
        grid,
        scalars="magnetik",
        point_size=20,
        render_points_as_spheres=True,
        cmap="turbo"
    )
    plotter.update()
    z += 1

def start_4d_visualization():
    # Start the interactive plot
    plotter.show(auto_close=False, interactive_update=True)

    # Timer to update the visualization every second
    timer = QTimer()
    timer.timeout.connect(update_voxel_layer)
    timer.start(1000)  # Update every 1000 ms (1 second)

def update_voxel_layer():
    # Updates the voxel visualization with new layers
    add_voxel_layer()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_4d_visualization()
    sys.exit(app.exec())
