# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 70, 261, 151))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.radioButton)

        self.radioButton_2 = QRadioButton(self.formLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.formLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.radioButton_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Blablabla", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"blablablabl", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"adsads", None))
    # retranslateUi

