# main.py
import sys
import traceback
from PyQt6.QtWidgets import QApplication
from ui.main_menu_ui import MainMenu  # Bu import burada kalmalı, çünkü sınıf

def main():
    try:
        app = QApplication(sys.argv)
        window = MainMenu()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print("❌ HATA:", e)
        traceback.print_exc()
        input("🔴 Program kapandı. Devam etmek için Enter'a bas...")

if __name__ == "__main__":
    main()
