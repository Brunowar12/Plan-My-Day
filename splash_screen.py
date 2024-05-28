from imports import *
from assets.UI.ui_splash_screen import Ui_SplashScreen
from auth_window import AuthWindow
from constans import *

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)

        ## SHOW ==> MAIN WINDOW
        self.auth = AuthWindow()

        ## INITIAL TEXT
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        ## CHANGE DESCRIPTION TEXT
        QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))

        ## SHOW ==> MAIN WINDOW
        QTimer.singleShot(4500, self.show_main_window)

    def show_main_window(self):
        self.auth.show()
        self.close()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        counter += 1
        if counter > 100:
            self.timer.stop()
