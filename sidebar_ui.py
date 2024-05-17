# Form implementation generated from reading ui file 'sidebar.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(parent=self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap(":/icon/logo.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 5, -1, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.side_line_1 = QtWidgets.QFrame(parent=self.icon_only_widget)
        self.side_line_1.setStyleSheet("background-color: rgb(204, 202, 201)")
        self.side_line_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.side_line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.side_line_1.setObjectName("side_line_1")
        self.verticalLayout.addWidget(self.side_line_1)
        self.home_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.home_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/task.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.home_btn_1.setIcon(icon)
        self.home_btn_1.setIconSize(QtCore.QSize(25, 25))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout.addWidget(self.home_btn_1)
        self.favorites_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.favorites_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/star.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.favorites_btn_1.setIcon(icon1)
        self.favorites_btn_1.setIconSize(QtCore.QSize(25, 25))
        self.favorites_btn_1.setCheckable(True)
        self.favorites_btn_1.setAutoExclusive(True)
        self.favorites_btn_1.setObjectName("favorites_btn_1")
        self.verticalLayout.addWidget(self.favorites_btn_1)
        self.calendar_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.calendar_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/calendar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.calendar_btn_1.setIcon(icon2)
        self.calendar_btn_1.setIconSize(QtCore.QSize(25, 25))
        self.calendar_btn_1.setCheckable(True)
        self.calendar_btn_1.setAutoExclusive(True)
        self.calendar_btn_1.setObjectName("calendar_btn_1")
        self.verticalLayout.addWidget(self.calendar_btn_1)
        self.history_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.history_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/history.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.history_btn_1.setIcon(icon3)
        self.history_btn_1.setIconSize(QtCore.QSize(25, 25))
        self.history_btn_1.setCheckable(True)
        self.history_btn_1.setAutoExclusive(True)
        self.history_btn_1.setObjectName("history_btn_1")
        self.verticalLayout.addWidget(self.history_btn_1)
        self.side_line_2 = QtWidgets.QFrame(parent=self.icon_only_widget)
        self.side_line_2.setMinimumSize(QtCore.QSize(1, 2))
        self.side_line_2.setStyleSheet("background-color: rgb(204, 202, 201)")
        self.side_line_2.setLineWidth(1)
        self.side_line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.side_line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.side_line_2.setObjectName("side_line_2")
        self.verticalLayout.addWidget(self.side_line_2)
        self.options_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.options_btn_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.options_btn_1.setIcon(icon4)
        self.options_btn_1.setIconSize(QtCore.QSize(25, 25))
        self.options_btn_1.setCheckable(True)
        self.options_btn_1.setAutoExclusive(True)
        self.options_btn_1.setObjectName("options_btn_1")
        self.verticalLayout.addWidget(self.options_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.exit_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QtCore.QSize(25, 25))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(parent=self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(":/icon/logo.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.full_menu_line = QtWidgets.QFrame(parent=self.full_menu_widget)
        self.full_menu_line.setStyleSheet("background-color: rgb(204, 202, 201);\n"
"margin-top: 0px;")
        self.full_menu_line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.full_menu_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.full_menu_line.setObjectName("full_menu_line")
        self.verticalLayout_2.addWidget(self.full_menu_line)
        self.home_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.home_btn_2.setFont(font)
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.favorites_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.favorites_btn_2.setFont(font)
        self.favorites_btn_2.setIcon(icon1)
        self.favorites_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.favorites_btn_2.setCheckable(True)
        self.favorites_btn_2.setAutoExclusive(True)
        self.favorites_btn_2.setObjectName("favorites_btn_2")
        self.verticalLayout_2.addWidget(self.favorites_btn_2)
        self.calendar_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calendar_btn_2.setFont(font)
        self.calendar_btn_2.setIcon(icon2)
        self.calendar_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.calendar_btn_2.setCheckable(True)
        self.calendar_btn_2.setAutoExclusive(True)
        self.calendar_btn_2.setObjectName("calendar_btn_2")
        self.verticalLayout_2.addWidget(self.calendar_btn_2)
        self.history_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.history_btn_2.setFont(font)
        self.history_btn_2.setIcon(icon3)
        self.history_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.history_btn_2.setCheckable(True)
        self.history_btn_2.setAutoExclusive(True)
        self.history_btn_2.setObjectName("history_btn_2")
        self.verticalLayout_2.addWidget(self.history_btn_2)
        self.line_2 = QtWidgets.QFrame(parent=self.full_menu_widget)
        self.line_2.setStyleSheet("background-color: rgb(204, 202, 201);")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.options_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.options_btn_2.setFont(font)
        self.options_btn_2.setIcon(icon4)
        self.options_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.options_btn_2.setCheckable(True)
        self.options_btn_2.setAutoExclusive(True)
        self.options_btn_2.setObjectName("options_btn_2")
        self.verticalLayout_2.addWidget(self.options_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit_btn_2.setFont(font)
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(parent=self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(parent=self.widget)
        self.change_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.change_btn.setIcon(icon6)
        self.change_btn.setIconSize(QtCore.QSize(20, 20))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 7, -1, -1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_input = QtWidgets.QLineEdit(parent=self.widget)
        self.search_input.setStyleSheet("")
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(parent=self.widget)
        self.search_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_btn.setIcon(icon7)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.user_btn = QtWidgets.QPushButton(parent=self.widget)
        self.user_btn.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.user_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/user1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.user_btn.setIcon(icon8)
        self.user_btn.setIconSize(QtCore.QSize(20, 20))
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_4.addWidget(self.user_btn)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.page)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_4.setMinimumSize(QtCore.QSize(151, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #fff;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_current_day = QtWidgets.QLabel(parent=self.frame_5)
        self.label_current_day.setMinimumSize(QtCore.QSize(151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_current_day.setFont(font)
        self.label_current_day.setStyleSheet("color: #fff;")
        self.label_current_day.setObjectName("label_current_day")
        self.horizontalLayout_5.addWidget(self.label_current_day)
        spacerItem4 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.btn_only_today = QtWidgets.QPushButton(parent=self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setKerning(True)
        self.btn_only_today.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/today.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_only_today.setIcon(icon9)
        self.btn_only_today.setIconSize(QtCore.QSize(30, 30))
        self.btn_only_today.setObjectName("btn_only_today")
        self.horizontalLayout_5.addWidget(self.btn_only_today)
        self.btn_more = QtWidgets.QPushButton(parent=self.frame_5)
        self.btn_more.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/more.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_more.setIcon(icon10)
        self.btn_more.setIconSize(QtCore.QSize(30, 30))
        self.btn_more.setObjectName("btn_more")
        self.horizontalLayout_5.addWidget(self.btn_more)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=self.page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(50, 25, 0, 5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.add_btn_task = QtWidgets.QPushButton(parent=self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        self.add_btn_task.setFont(font)
        self.add_btn_task.setStyleSheet("")
        self.add_btn_task.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_btn_task.setIcon(icon11)
        self.add_btn_task.setIconSize(QtCore.QSize(30, 30))
        self.add_btn_task.setObjectName("add_btn_task")
        self.horizontalLayout_7.addWidget(self.add_btn_task)
        self.add_task = QtWidgets.QLineEdit(parent=self.frame_4)
        self.add_task.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.add_task.setFont(font)
        self.add_task.setStyleSheet("")
        self.add_task.setObjectName("add_task")
        self.horizontalLayout_7.addWidget(self.add_task)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.listView_2 = QtWidgets.QListView(parent=self.frame_2)
        self.listView_2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.listView_2.setStyleSheet("")
        self.listView_2.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_2.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragOnly)
        self.listView_2.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.listView_2.setMovement(QtWidgets.QListView.Movement.Free)
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout_7.addWidget(self.listView_2)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(parent=self.page)
        self.frame.setMinimumSize(QtCore.QSize(0, 1))
        self.frame.setStyleSheet("border: none;\n"
"background-color: transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.page_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.page_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=self.page_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(parent=self.page_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(parent=self.page_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.favorites_btn_1.toggled['bool'].connect(self.favorites_btn_2.setChecked) # type: ignore
        self.calendar_btn_1.toggled['bool'].connect(self.calendar_btn_2.setChecked) # type: ignore
        self.history_btn_1.toggled['bool'].connect(self.history_btn_2.setChecked) # type: ignore
        self.options_btn_1.toggled['bool'].connect(self.options_btn_2.setChecked) # type: ignore
        self.favorites_btn_2.toggled['bool'].connect(self.favorites_btn_1.setChecked) # type: ignore
        self.calendar_btn_2.toggled['bool'].connect(self.calendar_btn_1.setChecked) # type: ignore
        self.history_btn_2.toggled['bool'].connect(self.history_btn_1.setChecked) # type: ignore
        self.options_btn_2.toggled['bool'].connect(self.options_btn_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo_label_3.setText(_translate("MainWindow", "Plan My Day"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.favorites_btn_2.setText(_translate("MainWindow", "Favorites"))
        self.calendar_btn_2.setText(_translate("MainWindow", "Calendar"))
        self.history_btn_2.setText(_translate("MainWindow", "History"))
        self.options_btn_2.setText(_translate("MainWindow", "Options"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.label_4.setText(_translate("MainWindow", "My Day"))
        self.label_current_day.setText(_translate("MainWindow", "Monday, April 1"))
        self.btn_only_today.setText(_translate("MainWindow", "Only Today"))
        self.add_btn_task.setProperty("class", _translate("MainWindow", "add"))
        self.add_task.setPlaceholderText(_translate("MainWindow", "Add your task"))
        self.label_5.setText(_translate("MainWindow", "Favorites Page"))
        self.label_6.setText(_translate("MainWindow", "Calendar Page"))
        self.label_7.setText(_translate("MainWindow", "History Page"))
        self.label_8.setText(_translate("MainWindow", "Options Page"))
        self.label_9.setText(_translate("MainWindow", "Search Page"))
        self.label_10.setText(_translate("MainWindow", "User Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())