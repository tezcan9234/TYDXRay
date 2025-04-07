import os
import glob
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("output", exist_ok=True)

def visualize_object(shape="shovel", size=(10, 10, 10)):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(0, 1, size[0])
    y = np.linspace(0, 1, size[1])
    z = np.linspace(0, 1, size[2])
    X, Y, Z = np.meshgrid(x, y, z)

    if shape == "shovel":
        values = np.exp(-((X - 0.5) ** 2 + (Y - 0.5) ** 2 + (Z - 0.2) ** 2) * 20)
    elif shape == "tin":
        values = np.exp(-((X - 0.3) ** 2 + (Y - 0.3) ** 2 + (Z - 0.3) ** 2) * 40)
    elif shape == "void":
        values = 1 - np.exp(-((X - 0.5) ** 2 + (Y - 0.5) ** 2 + (Z - 0.5) ** 2) * 10)
    else:
        values = np.random.rand(*size)

    threshold = 0.5
    filled = values > threshold

    ax.voxels(filled, facecolors='blue', edgecolor='k', alpha=0.7)
    ax.set_title(f"Visualized Shape: {shape}")

    # 🔢 Output dosyası numaralandırma
    existing = glob.glob("output/output*.png")
    next_index = len(existing) + 1
    filename = f"output/output{next_index}.png"

    plt.savefig(filename)
    plt.close()
