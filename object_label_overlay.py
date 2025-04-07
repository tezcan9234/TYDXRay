import pyvista as pv
import numpy as np
import os
import csv
from datetime import datetime

def add_labels_to_scene(grid, labels, export_csv=True, output_dir="output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plotter = pv.Plotter()
    plotter.add_mesh(grid, show_edges=False, opacity=0.3, scalars='values', cmap="viridis")

    for item in labels:
        pos = item['position']
        label = item['label']
        color = item['color']
        density = item.get('density', 'unknown')
        depth = pos[2]

        cube = pv.Cube(center=pos, x_length=1, y_length=1, z_length=1)
        plotter.add_mesh(cube, color=color, opacity=0.6)

        label_text = f"{label} ({density})"
        plotter.add_point_labels([pos], [label_text], text_color='white', font_size=10, point_size=30)

    # CSV Export (isteğe bağlı)
    if export_csv:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_path = os.path.join(output_dir, f"labels_{timestamp}.csv")
        with open(csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Label', 'X', 'Y', 'Z', 'Density'])
            for item in labels:
                pos = item['position']
                writer.writerow([item['label'], pos[0], pos[1], pos[2], item.get('density', '')])
        print(f"[✔] Label data exported: {csv_path}")

    return plotter
