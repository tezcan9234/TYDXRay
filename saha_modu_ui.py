# ui/saha_modu_ui.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class SahaModuUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Saha Modu")
        self.setFixedSize(400, 350)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("📡 Saha Modu Aktif")
        title.setFont(QFont("Arial", 18))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bt_status = QLabel("Bluetooth: Bağlı ✅")
        self.battery = QLabel("Pil Durumu: %95 🔋")
        self.clock = QLabel("Saat: 14:38 🕒")

        for label in [self.bt_status, self.battery, self.clock]:
            label.setFont(QFont("Arial", 14))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.back_btn = QPushButton("🔙 Ana Menüye Dön")
        self.back_btn.setFixedHeight(40)

        layout.addWidget(title)
        layout.addWidget(self.bt_status)
        layout.addWidget(self.battery)
        layout.addWidget(self.clock)
        layout.addWidget(self.back_btn)

        self.setLayout(layout)
