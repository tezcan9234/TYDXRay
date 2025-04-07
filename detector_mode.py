import numpy as np
import time
import pyvista as pv
import os
import platform

# Windows ise winsound kullan
if platform.system() == "Windows":
    import winsound
    def play_beep(frequency=800, duration=200):
        winsound.Beep(frequency, duration)
else:
    def play_beep(frequency=800, duration=200):
        print("🔔 Beep (Simulated)")  # Windows dışı sistemlerde basit çıktı

def detector_mode(grid, threshold=0.7, delay=0.1):
    shape = grid.shape
    if len(shape) == 2:
        shape = (shape[0], shape[1], 1)
        grid = grid.reshape(shape)

    grid = np.nan_to_num(grid, nan=0.0, posinf=0.0, neginf=0.0)
    gmin, gmax = np.min(grid), np.max(grid)
    if gmax - gmin == 0:
        gmax += 1e-6
    grid = (grid - gmin) / (gmax - gmin)
    grid = grid.astype(np.float32)

    x, y, z = shape
    plotter = pv.Plotter()
    plotter.show(auto_close=False, interactive_update=True)

    for current_z in range(z):
        slice_data = grid[:, :, current_z]

        anomaly_mask = slice_data > threshold
        anomaly_count = np.sum(anomaly_mask)

        # Sesli uyarı (yoğunluk arttıkça daha fazla frekans)
        if anomaly_count > 0:
            freq = 800 + anomaly_count * 10
            duration = 200
            play_beep(frequency=freq, duration=duration)

        # PyVista sahnesini güncelle
        ug = pv.UniformGrid()
        ug.dimensions = (x + 1, y + 1, 2)
        ug.origin = (0, 0, 0)
        ug.spacing = (1, 1, 1)
        slice_for_render = slice_data[:, :, np.newaxis]
        ug["values"] = slice_for_render.flatten(order="F")

        plotter.clear()
        plotter.add_volume(ug,
                           scalars="values",
                           cmap="coolwarm",
                           opacity="sigmoid",
                           opacity_unit_distance=2.5,
                           shade=True)
        plotter.update()
        time.sleep(delay)

    print("\n✅ Dedektör modu tamamlandı.")
    plotter.show()

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    from dedektor_modu import DedektorModuUI
    window = DedektorModuUI()
    window.show()
    sys.exit(app.exec())
