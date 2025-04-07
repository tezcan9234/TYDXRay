import pyvista as pv
from pyvistaqt import QtInteractor
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.plotter = QtInteractor(self)
        self.setCentralWidget(self.plotter)
        self.setWindowTitle("TezX-Ray Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Grid oluştur
        grid = pv.UniformGrid()
        grid.dimensions = (11, 11, 11)
        grid.spacing = (1, 1, 1)
        grid.origin = (0, 0, 0)
        grid.point_data["intensity"] = np.random.rand(grid.n_points)

        # Sahneye ekle
        self.plotter.add_volume(
            grid,
            scalars="intensity",
            cmap="plasma",
            opacity="linear",
            shade=True,
            show_scalar_bar=True
        )

        self.plotter.reset_camera()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
