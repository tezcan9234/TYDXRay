# ui/raporlama_modu.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class RaporlamaModulu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Raporlama Modülü")
        self.setGeometry(200, 200, 400, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        label = QLabel("📄 Raporlama Paneli Açıldı...")
        label.setFont(QFont("Arial", 14))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)
