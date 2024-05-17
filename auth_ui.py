# Form implementation generated from reading ui file 'auth.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1470, 808)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.52451, y1:1, x2:0.514706, y2:0, stop:0 rgba(204, 203, 200, 255), stop:1 rgba(233, 231, 229, 255));\n"
"border-radius: 15px;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(parent=self.centralwidget)
        self.header.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.header.setStyleSheet("background-color: none;")
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_title = QtWidgets.QFrame(parent=self.header)
        self.header_title.setMinimumSize(QtCore.QSize(0, 130))
        self.header_title.setMaximumSize(QtCore.QSize(450, 16777215))
        self.header_title.setStyleSheet("background-color: none;")
        self.header_title.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header_title.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header_title.setObjectName("header_title")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_title)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_header_img = QtWidgets.QLabel(parent=self.header_title)
        self.label_header_img.setMinimumSize(QtCore.QSize(91, 101))
        self.label_header_img.setStyleSheet("background-color:none;")
        self.label_header_img.setText("")
        self.label_header_img.setPixmap(QtGui.QPixmap(":/icon/logo.png"))
        self.label_header_img.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_header_img.setObjectName("label_header_img")
        self.horizontalLayout_4.addWidget(self.label_header_img)
        self.label_header_text = QtWidgets.QLabel(parent=self.header_title)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.label_header_text.setFont(font)
        self.label_header_text.setStyleSheet("background-color: none;\n"
"color: black;")
        self.label_header_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_header_text.setObjectName("label_header_text")
        self.horizontalLayout_4.addWidget(self.label_header_text)
        self.horizontalLayout.addWidget(self.header_title)
        self.verticalLayout.addWidget(self.header)
        self.body = QtWidgets.QFrame(parent=self.centralwidget)
        self.body.setStyleSheet("background-color: none;")
        self.body.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_3.setContentsMargins(25, -1, 25, -1)
        self.horizontalLayout_3.setSpacing(125)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_auth = QtWidgets.QFrame(parent=self.body)
        self.frame_auth.setMinimumSize(QtCore.QSize(0, 550))
        self.frame_auth.setMaximumSize(QtCore.QSize(325, 600))
        self.frame_auth.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_auth.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_auth.setObjectName("frame_auth")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_auth)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.auth = QtWidgets.QFrame(parent=self.frame_auth)
        self.auth.setMinimumSize(QtCore.QSize(300, 400))
        self.auth.setMaximumSize(QtCore.QSize(300, 390))
        self.auth.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.495098, y1:0, x2:0.514706, y2:1, stop:0 rgba(130, 66, 151, 255), stop:1 rgba(64, 27, 91, 255));\n"
"border-radius: 30px;\n"
"max-width: 300px;\n"
"")
        self.auth.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.auth.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.auth.setObjectName("auth")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.auth)
        self.verticalLayout_7.setContentsMargins(40, 0, 40, 20)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_auth_title = QtWidgets.QLabel(parent=self.auth)
        self.label_auth_title.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.label_auth_title.setFont(font)
        self.label_auth_title.setStyleSheet("QLabel {\n"
"    \n"
"    background-color: none;\n"
"    color: rgb(255, 255, 255);\n"
"    margin-bottom: 15px 0px 0px 0px;\n"
"}")
        self.label_auth_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_auth_title.setObjectName("label_auth_title")
        self.verticalLayout_7.addWidget(self.label_auth_title)
        self.label_auth_subtitle = QtWidgets.QLabel(parent=self.auth)
        self.label_auth_subtitle.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_auth_subtitle.setFont(font)
        self.label_auth_subtitle.setStyleSheet("QLabel {\n"
"    \n"
"    background-color: none;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_auth_subtitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_auth_subtitle.setObjectName("label_auth_subtitle")
        self.verticalLayout_7.addWidget(self.label_auth_subtitle)
        self.auth_login = QtWidgets.QLabel(parent=self.auth)
        self.auth_login.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.auth_login.setFont(font)
        self.auth_login.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.505682, stop:0 rgba(80, 36, 100, 255), stop:1 rgba(80, 36, 98, 255));\n"
"    border-radius: 15px;\n"
"}")
        self.auth_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.auth_login.setObjectName("auth_login")
        self.verticalLayout_7.addWidget(self.auth_login)
        self.auth_login_button = QtWidgets.QPushButton(parent=self.auth)
        self.auth_login_button.setMinimumSize(QtCore.QSize(0, 40))
        self.auth_login_button.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.auth_login_button.setFont(font)
        self.auth_login_button.setStyleSheet("    color: white;\n"
"    background-color: rgb(115, 44, 133);\n"
"    border-radius: 15px;\n"
"")
        self.auth_login_button.setObjectName("auth_login_button")
        self.verticalLayout_7.addWidget(self.auth_login_button)
        self.auth_change_button = QtWidgets.QPushButton(parent=self.auth)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auth_change_button.sizePolicy().hasHeightForWidth())
        self.auth_change_button.setSizePolicy(sizePolicy)
        self.auth_change_button.setMinimumSize(QtCore.QSize(0, 40))
        self.auth_change_button.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.auth_change_button.setFont(font)
        self.auth_change_button.setStyleSheet("    color: black;\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"")
        self.auth_change_button.setObjectName("auth_change_button")
        self.verticalLayout_7.addWidget(self.auth_change_button)
        self.verticalLayout_6.addWidget(self.auth)
        self.offline_button = QtWidgets.QPushButton(parent=self.frame_auth)
        self.offline_button.setMinimumSize(QtCore.QSize(280, 59))
        self.offline_button.setMaximumSize(QtCore.QSize(300, 59))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.offline_button.setFont(font)
        self.offline_button.setStyleSheet("    color: white;\n"
"    background-color: rgb(68, 25, 97);\n"
"    border-radius: 10px;\n"
"")
        self.offline_button.setObjectName("offline_button")
        self.verticalLayout_6.addWidget(self.offline_button)
        self.horizontalLayout_3.addWidget(self.frame_auth)
        self.frame_registration = QtWidgets.QFrame(parent=self.body)
        self.frame_registration.setMinimumSize(QtCore.QSize(620, 0))
        self.frame_registration.setMaximumSize(QtCore.QSize(650, 600))
        self.frame_registration.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_registration.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_registration.setObjectName("frame_registration")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_registration)
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 10)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_registrarion_title = QtWidgets.QLabel(parent=self.frame_registration)
        self.frame_registrarion_title.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.frame_registrarion_title.setFont(font)
        self.frame_registrarion_title.setStyleSheet("background-color: none;\n"
"color: rgb(139, 139, 139)")
        self.frame_registrarion_title.setObjectName("frame_registrarion_title")
        self.verticalLayout_2.addWidget(self.frame_registrarion_title)
        self.frame_email = QtWidgets.QFrame(parent=self.frame_registration)
        self.frame_email.setMinimumSize(QtCore.QSize(460, 0))
        self.frame_email.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_email.setStyleSheet("background-color: white;\n"
"    border-radius: 15px;")
        self.frame_email.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_email.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_email.setObjectName("frame_email")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_email)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.email_title = QtWidgets.QLabel(parent=self.frame_email)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.email_title.setFont(font)
        self.email_title.setStyleSheet("color: black;\n"
"background-color: none;")
        self.email_title.setObjectName("email_title")
        self.verticalLayout_3.addWidget(self.email_title)
        self.input_email = QtWidgets.QLineEdit(parent=self.frame_email)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.input_email.setFont(font)
        self.input_email.setStyleSheet("color: rgb(139, 139, 139);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.input_email.setObjectName("input_email")
        self.verticalLayout_3.addWidget(self.input_email)
        self.email_line = QtWidgets.QFrame(parent=self.frame_email)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.email_line.setFont(font)
        self.email_line.setStyleSheet("background-color: rgb(198, 197, 194);\n"
"")
        self.email_line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.email_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.email_line.setObjectName("email_line")
        self.verticalLayout_3.addWidget(self.email_line)
        self.verticalLayout_2.addWidget(self.frame_email)
        self.frame_registrarion_line = QtWidgets.QFrame(parent=self.frame_registration)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.frame_registrarion_line.setFont(font)
        self.frame_registrarion_line.setStyleSheet("background-color: rgb(198, 197, 194)")
        self.frame_registrarion_line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.frame_registrarion_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame_registrarion_line.setObjectName("frame_registrarion_line")
        self.verticalLayout_2.addWidget(self.frame_registrarion_line)
        self.frame_password = QtWidgets.QFrame(parent=self.frame_registration)
        self.frame_password.setMinimumSize(QtCore.QSize(457, 0))
        self.frame_password.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_password.setStyleSheet("background-color: white;\n"
"    border-radius: 15px;")
        self.frame_password.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_password.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_password.setObjectName("frame_password")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_password)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.password_title = QtWidgets.QLabel(parent=self.frame_password)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.password_title.setFont(font)
        self.password_title.setStyleSheet("color: black;\n"
"background-color: none;")
        self.password_title.setObjectName("password_title")
        self.verticalLayout_4.addWidget(self.password_title)
        self.input_password = QtWidgets.QLineEdit(parent=self.frame_password)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet("color: rgb(139, 139, 139);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.input_password.setObjectName("input_password")
        self.verticalLayout_4.addWidget(self.input_password)
        self.password_line = QtWidgets.QFrame(parent=self.frame_password)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password_line.setFont(font)
        self.password_line.setStyleSheet("background-color: rgb(198, 197, 194);\n"
"")
        self.password_line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.password_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.password_line.setObjectName("password_line")
        self.verticalLayout_4.addWidget(self.password_line)
        self.verticalLayout_2.addWidget(self.frame_password)
        self.frame_confpassword = QtWidgets.QFrame(parent=self.frame_registration)
        self.frame_confpassword.setMinimumSize(QtCore.QSize(457, 0))
        self.frame_confpassword.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_confpassword.setStyleSheet("background-color: white;\n"
"    border-radius: 15px;")
        self.frame_confpassword.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_confpassword.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_confpassword.setObjectName("frame_confpassword")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_confpassword)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.confpassword_title = QtWidgets.QLabel(parent=self.frame_confpassword)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.confpassword_title.setFont(font)
        self.confpassword_title.setStyleSheet("color: black;\n"
"background-color: none;")
        self.confpassword_title.setObjectName("confpassword_title")
        self.verticalLayout_5.addWidget(self.confpassword_title)
        self.confpassword_input = QtWidgets.QLineEdit(parent=self.frame_confpassword)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.confpassword_input.setFont(font)
        self.confpassword_input.setStyleSheet("color: rgb(139, 139, 139);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.confpassword_input.setObjectName("confpassword_input")
        self.verticalLayout_5.addWidget(self.confpassword_input)
        self.confpassword_line = QtWidgets.QFrame(parent=self.frame_confpassword)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confpassword_line.setFont(font)
        self.confpassword_line.setStyleSheet("background-color: rgb(198, 197, 194);\n"
"")
        self.confpassword_line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.confpassword_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.confpassword_line.setObjectName("confpassword_line")
        self.verticalLayout_5.addWidget(self.confpassword_line)
        self.verticalLayout_2.addWidget(self.frame_confpassword)
        self.frame_registrarion_endline = QtWidgets.QFrame(parent=self.frame_registration)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.frame_registrarion_endline.setFont(font)
        self.frame_registrarion_endline.setStyleSheet("background-color: rgb(198, 197, 194)")
        self.frame_registrarion_endline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.frame_registrarion_endline.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame_registrarion_endline.setObjectName("frame_registrarion_endline")
        self.verticalLayout_2.addWidget(self.frame_registrarion_endline)
        self.button_create = QtWidgets.QPushButton(parent=self.frame_registration)
        self.button_create.setMinimumSize(QtCore.QSize(280, 59))
        self.button_create.setMaximumSize(QtCore.QSize(280, 59))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.button_create.setFont(font)
        self.button_create.setStyleSheet("    color: white;\n"
"    background-color: rgb(68, 25, 97);\n"
"    border-radius: 10px;\n"
"")
        self.button_create.setObjectName("button_create")
        self.verticalLayout_2.addWidget(self.button_create)
        self.horizontalLayout_3.addWidget(self.frame_registration)
        self.verticalLayout.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_header_text.setText(_translate("MainWindow", "PLAN MY DAY"))
        self.label_auth_title.setText(_translate("MainWindow", "PLAN MY DAY"))
        self.label_auth_subtitle.setText(_translate("MainWindow", "Authorization"))
        self.auth_login.setText(_translate("MainWindow", "Unknown"))
        self.auth_login_button.setText(_translate("MainWindow", "LOGIN "))
        self.auth_change_button.setText(_translate("MainWindow", "Change account"))
        self.offline_button.setText(_translate("MainWindow", "Offline mode"))
        self.frame_registrarion_title.setText(_translate("MainWindow", "New User Registration"))
        self.email_title.setText(_translate("MainWindow", "Email"))
        self.input_email.setPlaceholderText(_translate("MainWindow", "Enter  your email addres..."))
        self.password_title.setText(_translate("MainWindow", "Password"))
        self.input_password.setPlaceholderText(_translate("MainWindow", "Create and enter your password..."))
        self.confpassword_title.setText(_translate("MainWindow", "Confirm Password"))
        self.confpassword_input.setPlaceholderText(_translate("MainWindow", "Enter created password..."))
        self.button_create.setText(_translate("MainWindow", "Create account"))