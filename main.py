from imports import *
from splash_screen import SplashScreen

if __name__ == "__main__":
    import new_icon.resources

    app = QApplication(sys.argv)
    with open("./static/style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = SplashScreen()
    window.show()
    sys.exit(app.exec())
