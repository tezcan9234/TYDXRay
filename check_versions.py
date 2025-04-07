import pyvista as pv
import vtk

# PyVista ve VTK sürüm bilgilerini yazdır
print(f"PyVista version: {pv.__version__}")
print(f"VTK version: {vtk.VTK_MAJOR_VERSION}.{vtk.VTK_MINOR_VERSION}.{vtk.VTK_BUILD_VERSION}")
