# visualization/voxel_renderer_matplotlib.py

import matplotlib.pyplot as plt
import numpy as np
import datetime  # ⏰ Otomatik tarih eklendi

def render_voxel_scene(data_3d):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    filled = data_3d > 0

    colors = np.empty(filled.shape, dtype=object)
    colors[data_3d == 1] = 'red'
    colors[data_3d == 2] = 'blue'
    colors[data_3d == 3] = 'yellow'
    colors[data_3d == 4] = 'green'

    ax.voxels(filled, facecolors=colors, edgecolor='k')
    ax.set_title("3D Voxel Görselleştirme (Matplotlib)", fontsize=12)

    # 💾 Otomatik zaman damgalı PNG kaydı
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"exports/png_snapshots/voxel_output_{timestamp}.png"
    plt.savefig(filename)

    # 📊 Sahneyi göster
    plt.show()
