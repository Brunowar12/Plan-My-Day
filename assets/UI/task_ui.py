# Form implementation generated from reading ui file 'd:\GitHubRepos\Plan-My-Day\assets\UI\task.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(938, 141)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 30, 30)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(parent=Form)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBox_3.setStyleSheet("")
        self.checkBox_3.setText("")
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.check_favorite = QtWidgets.QCheckBox(parent=self.widget_3)
        self.check_favorite.setMaximumSize(QtCore.QSize(50, 16777215))
        self.check_favorite.setStyleSheet("")
        self.check_favorite.setText("")
        self.check_favorite.setChecked(False)
        self.check_favorite.setObjectName("check_favorite")
        self.horizontalLayout.addWidget(self.check_favorite)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\GitHubRepos\\Plan-My-Day\\assets\\UI\\../static/icons/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.widget_3)
        self.sub_widget = QtWidgets.QWidget(parent=Form)
        self.sub_widget.setObjectName("sub_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.sub_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.task_label = QtWidgets.QLabel(parent=self.sub_widget)
        self.task_label.setMaximumSize(QtCore.QSize(40, 20))
        self.task_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.task_label.setObjectName("task_label")
        self.horizontalLayout_2.addWidget(self.task_label)
        self.label_space = QtWidgets.QLabel(parent=self.sub_widget)
        self.label_space.setMaximumSize(QtCore.QSize(5, 20))
        self.label_space.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_space.setObjectName("label_space")
        self.horizontalLayout_2.addWidget(self.label_space)
        self.label_day = QtWidgets.QLabel(parent=self.sub_widget)
        self.label_day.setMaximumSize(QtCore.QSize(80, 20))
        self.label_day.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_day.setObjectName("label_day")
        self.horizontalLayout_2.addWidget(self.label_day)
        self.label_space_3 = QtWidgets.QLabel(parent=self.sub_widget)
        self.label_space_3.setMaximumSize(QtCore.QSize(5, 20))
        self.label_space_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_space_3.setObjectName("label_space_3")
        self.horizontalLayout_2.addWidget(self.label_space_3)
        self.task_label_end = QtWidgets.QLabel(parent=self.sub_widget)
        self.task_label_end.setMaximumSize(QtCore.QSize(150, 20))
        self.task_label_end.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.task_label_end.setObjectName("task_label_end")
        self.horizontalLayout_2.addWidget(self.task_label_end)
        self.label_space_2 = QtWidgets.QLabel(parent=self.sub_widget)
        self.label_space_2.setMaximumSize(QtCore.QSize(25, 20))
        self.label_space_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_space_2.setObjectName("label_space_2")
        self.horizontalLayout_2.addWidget(self.label_space_2)
        self.label_task_status = QtWidgets.QLabel(parent=self.sub_widget)
        self.label_task_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_task_status.setObjectName("label_task_status")
        self.horizontalLayout_2.addWidget(self.label_task_status)
        self.verticalLayout.addWidget(self.sub_widget)
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setStyleSheet("background-color: rgb(198, 197, 194)")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_4.setProperty("class", _translate("Form", "remove"))
        self.task_label.setText(_translate("Form", "Tasks"))
        self.label_space.setText(_translate("Form", "."))
        self.label_day.setText(_translate("Form", "Today"))
        self.label_space_3.setText(_translate("Form", "."))
        self.task_label_end.setText(_translate("Form", "End 18.05.2024"))
        self.label_space_2.setText(_translate("Form", "."))
        self.label_task_status.setText(_translate("Form", "Task: Active"))
