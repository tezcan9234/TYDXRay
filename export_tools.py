import os
from zipfile import ZipFile
from fpdf import FPDF
from datetime import datetime

def export_simulation_outputs(folder="output"):
    if not os.path.exists(folder):
        print(f"[!] '{folder}' klasörü bulunamadı.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # PDF oluştur
    pdf = FPDF()
    for file in os.listdir(folder):
        if file.endswith(".png"):
            pdf.add_page()
            pdf.image(os.path.join(folder, file), x=10, y=10, w=180)
    pdf_path = os.path.join(folder, f"simulasyon_{timestamp}.pdf")
    pdf.output(pdf_path)
    print(f"[✓] PDF kaydedildi: {pdf_path}")

    # ZIP oluştur
    zip_path = os.path.join(folder, f"simulasyon_{timestamp}.zip")
    with ZipFile(zip_path, 'w') as zipf:
        for file in os.listdir(folder):
            full_path = os.path.join(folder, file)
            if os.path.isfile(full_path):
                zipf.write(full_path, arcname=file)
    print(f"[✓] ZIP dosyası oluşturuldu: {zip_path}")
