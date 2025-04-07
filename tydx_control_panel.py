import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from pyvistaqt import QtInteractor

app = QApplication(sys.argv)

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TYDX Panel")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.plotter = QtInteractor(self)
        layout.addWidget(self.plotter)

        # Grid oluştur
        import pyvista as pv
        import numpy as np

        self.grid = pv.UniformGrid()
        self.grid.dimensions = (32, 32, 32)
        self.grid.spacing = (1, 1, 1)
        self.grid.origin = (0, 0, 0)
        values = np.random.rand(self.grid.n_cells)
        self.grid.cell_data["density"] = values

        self.plotter.add_mesh(self.grid, scalars="density", cmap="coolwarm")
        self.plotter.show()

if __name__ == "__main__":
    panel = ControlPanel()
    panel.show()
    sys.exit(app.exec())
