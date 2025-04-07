import os
import numpy as np
import pyvista as pv
from fpdf import FPDF
from datetime import datetime
import matplotlib.pyplot as plt

def export_scene_and_report(grid, output_name="anomaly_report"):
    # Klasörleri oluştur
    export_dir = "output/exports"
    os.makedirs(export_dir, exist_ok=True)

    # Normalize ve float32
    grid = np.nan_to_num(grid, nan=0.0, posinf=0.0, neginf=0.0)
    gmin = np.min(grid)
    gmax = np.max(grid)
    if gmax - gmin == 0:
        gmax += 1e-6
    grid = (grid - gmin) / (gmax - gmin)
    grid = grid.astype(np.float32)

    # İstatistikler
    max_val = np.max(grid)
    min_val = np.min(grid)
    mean_val = np.mean(grid)
    anomaly_count = np.sum(grid > 0.7)

    # PyVista sahne
    shape = grid.shape
    grid_pv = pv.UniformGrid()
    grid_pv.dimensions = np.array(shape) + 1
    grid_pv.origin = (0, 0, 0)
    grid_pv.spacing = (1, 1, 1)
    grid_pv["values"] = grid.flatten(order="F")

    plotter = pv.Plotter(off_screen=True)
    plotter.add_volume(grid_pv, scalars="values", cmap="coolwarm", opacity="sigmoid")
    screenshot_path = os.path.join(export_dir, f"{output_name}.png")
    plotter.screenshot(screenshot_path)
    plotter.close()

    # Grafik: değer dağılımı
    plt.figure()
    plt.hist(grid.flatten(), bins=50, color='red', alpha=0.7)
    plt.title("Manyetik Anomali Dağılımı")
    plt.xlabel("Değer")
    plt.ylabel("Frekans")
    hist_path = os.path.join(export_dir, f"{output_name}_hist.png")
    plt.savefig(hist_path)
    plt.close()

    # PDF Raporu
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="TYDX Anomali Raporu", ln=True, align='C')
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, txt=f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.cell(200, 10, txt=f"Anomali Sayısı: {anomaly_count}", ln=True)
    pdf.cell(200, 10, txt=f"Max Değer: {max_val:.4f}", ln=True)
    pdf.cell(200, 10, txt=f"Min Değer: {min_val:.4f}", ln=True)
    pdf.cell(200, 10, txt=f"Ortalama: {mean_val:.4f}", ln=True)

    pdf.image(screenshot_path, x=10, y=80, w=180)
    pdf.image(hist_path, x=10, y=160, w=180)

    pdf_path = os.path.join(export_dir, f"{output_name}.pdf")
    pdf.output(pdf_path)

    print(f"\n✅ PNG ve PDF başarıyla oluşturuldu:\n📸 {screenshot_path}\n📄 {pdf_path}")
