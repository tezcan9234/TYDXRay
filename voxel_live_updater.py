import pyvista as pv
from ai.interpreter import interpret_value

def update_voxel_scene(plotter, mesh, data_points):
    for x, y, z, value in data_points:
        cube = pv.Cube(center=(x + 0.5, y + 0.5, z + 0.5), x_length=1, y_length=1, z_length=1)
        color = interpret_value(value)
        plotter.add_mesh(cube, color=color, show_edges=False)
    plotter.render()
