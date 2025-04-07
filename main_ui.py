import sys
from PyQt5.QtWidgets import QApplication
from ui.main_menu_ui import MainMenu

def main():
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
