# visualization/gold_map.py

import pyvista as pv
import numpy as np

def render_gold_map(grid):
    p = pv.Plotter(window_size=(800, 600))
    p.set_background("black")

    # Yüksek değerleri vurgulayan gold renk paleti
    volume = p.add_volume(
        grid,
        scalars="intensity",
        cmap="cividis",  # altın sarısı tonlar
        opacity="linear",
        scalar_bar_args={"title": "Altın Yoğunluğu"}
    )

    p.camera_position = 'iso'
    p.show(auto_close=False)
