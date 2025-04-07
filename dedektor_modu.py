from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class DedektorModu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔍 Dedektör Modu")
        self.setGeometry(200, 200, 400, 200)

        self.setStyleSheet("""
            QWidget {
                background-color: #fdfdfd;
                font-family: Segoe UI;
            }
            QLabel {
                color: #222;
                font-size: 16px;
            }
        """)

        layout = QVBoxLayout()

        self.label = QLabel("🔊 Dedektör sistemi aktif.")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Segoe UI", 14, QFont.Bold))

        layout.addWidget(self.label)
        self.setLayout(layout)
