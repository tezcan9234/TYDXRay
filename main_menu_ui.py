from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys
import subprocess
import os

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TYDX Ana Menü")
        self.setFixedSize(300, 330)

        layout = QVBoxLayout()

        title = QLabel("🧠 TYDX Ana Menü")
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(title)

        btn_dedektor = QPushButton("🔍 Dedektör Modu")
        btn_dedektor.clicked.connect(self.run_dedektor_modu)
        layout.addWidget(btn_dedektor)

        btn_4d = QPushButton("🌐 4D Görselleştirme")
        btn_4d.clicked.connect(self.run_4d_visualization)
        layout.addWidget(btn_4d)

        btn_raporlama = QPushButton("📊 Raporlama Modülü")
        btn_raporlama.clicked.connect(self.run_raporlama_modulu)
        layout.addWidget(btn_raporlama)

        btn_ayarlar = QPushButton("⚙️ Ayarlar")
        btn_ayarlar.clicked.connect(self.run_ayarlar)
        layout.addWidget(btn_ayarlar)

        btn_exit = QPushButton("⛔ Çıkış")
        btn_exit.clicked.connect(self.close)
        layout.addWidget(btn_exit)

        self.setLayout(layout)

    def run_script(self, filename):
        # Tüm yolları tam klasörle al
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        full_path = os.path.join(base_dir, filename)
        subprocess.Popen(["python", full_path])

    def run_dedektor_modu(self):
        self.run_script("dedektor_modu.py")

    def run_4d_visualization(self):
        self.run_script("four_d_visualization.py")

    def run_raporlama_modulu(self):
        self.run_script("raporlama_modu.py")

    def run_ayarlar(self):
        self.run_script("ayarlar_modu.py")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())
