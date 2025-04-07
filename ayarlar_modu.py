from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class AyarlarModulu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("⚙️ Ayarlar")
        self.setGeometry(300, 300, 300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Ayarlar paneli aktif.\n(Seçenekler eklenecek.)")
        layout.addWidget(self.label)

        self.setLayout(layout)
