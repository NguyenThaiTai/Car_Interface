# Form implementation generated from reading ui file 'Car_Interface.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 664)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 500))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1100, 500))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main_header.setStyleSheet("QFrame\n"
"{\n"
"    border-bottom: 1px solid #000;\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.main_header.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tittle_bar_container = QtWidgets.QFrame(parent=self.main_header)
        self.tittle_bar_container.setEnabled(True)
        self.tittle_bar_container.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tittle_bar_container.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.tittle_bar_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tittle_bar_container.setObjectName("tittle_bar_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_menu_toggle = QtWidgets.QFrame(parent=self.tittle_bar_container)
        self.left_menu_toggle.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet("QFrame{\n"
"    background-color: #000;\n"
"}\n"
"QPushButton{\n"
"    padding: 5px 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: #000;\n"
"    color: #fff\n"
"}\n"
"QPushButton:Hover\n"
"{\n"
"        background-color: rgb(0, 92, 157);\n"
"}")
        self.left_menu_toggle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.left_menu_toggle)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 92, 157 );\n"
"}\n"
"\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/cil-menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_5.addWidget(self.left_menu_toggle)
        self.tittle_bar = QtWidgets.QFrame(parent=self.tittle_bar_container)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tittle_bar.setFont(font)
        self.tittle_bar.setStyleSheet("QLabel\n"
"{\n"
"    color: #fff;\n"
"}")
        self.tittle_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tittle_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tittle_bar.setObjectName("tittle_bar")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tittle_bar)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.logo = QtWidgets.QFrame(parent=self.tittle_bar)
        self.logo.setMinimumSize(QtCore.QSize(70, 0))
        self.logo.setMaximumSize(QtCore.QSize(70, 150))
        self.logo.setStyleSheet("border-image: url(resources/images/R-removebg-preview.png);\n"
"border: -17px solid rgb(1, 90, 153);")
        self.logo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.logo.setObjectName("logo")
        self.horizontalLayout_6.addWidget(self.logo)
        self.frame_2 = QtWidgets.QFrame(parent=self.tittle_bar)
        self.frame_2.setMinimumSize(QtCore.QSize(40, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_2.setStyleSheet("image: url(:/images/resources/images/VietNam.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6.addWidget(self.frame_2)
        self.label_4 = QtWidgets.QLabel(parent=self.tittle_bar)
        font = QtGui.QFont()
        font.setFamily("UTM NguyenHa 01")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_5.addWidget(self.tittle_bar)
        self.horizontalLayout_2.addWidget(self.tittle_bar_container)
        self.top_right_btns = QtWidgets.QFrame(parent=self.main_header)
        self.top_right_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.top_right_btns.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.top_right_btns.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.top_right_btns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.top_right_btns.setObjectName("top_right_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.restoreButton = QtWidgets.QPushButton(parent=self.top_right_btns)
        self.restoreButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.restoreButton.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 92, 157 );\n"
"}\n"
"\n"
"")
        self.restoreButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/icons/cil-window-restore.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.restoreButton.setIcon(icon1)
        self.restoreButton.setIconSize(QtCore.QSize(24, 24))
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout_3.addWidget(self.restoreButton)
        self.minimizeButton = QtWidgets.QPushButton(parent=self.top_right_btns)
        self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.minimizeButton.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 92, 157 );\n"
"}\n"
"\n"
"")
        self.minimizeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/icons/cil-minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.minimizeButton.setIcon(icon2)
        self.minimizeButton.setIconSize(QtCore.QSize(24, 24))
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout_3.addWidget(self.minimizeButton)
        self.closeButton = QtWidgets.QPushButton(parent=self.top_right_btns)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.closeButton.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 92, 157 );\n"
"}\n"
"\n"
"")
        self.closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/icons/cil-x.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QtCore.QSize(24, 24))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.horizontalLayout_2.addWidget(self.top_right_btns)
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_body.setMaximumSize(QtCore.QSize(16777215, 850))
        self.main_body.setStyleSheet("background-color: #181A2F;")
        self.main_body.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_side_menu = QtWidgets.QFrame(parent=self.main_body)
        self.left_side_menu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_side_menu.setStyleSheet("QFrame{\n"
"    background-color: #000;\n"
"}\n"
"QPushButton{\n"
"    padding: 20px 10px;\n"
"    border: none;\n"
"    border-left: 2px solid transparent;\n"
"    border-bottom: 2px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: #000;\n"
"    color: #fff\n"
"}\n"
"QPushButton:Hover\n"
"{\n"
"        background-color: rgb(0, 92, 157);\n"
"}")
        self.left_side_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.left_side_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_side_menu.setObjectName("left_side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_side_menu)
        self.verticalLayout_2.setContentsMargins(7, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.left_menu_top_buttons = QtWidgets.QFrame(parent=self.left_side_menu)
        self.left_menu_top_buttons.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.left_menu_top_buttons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.account_button = QtWidgets.QPushButton(parent=self.left_menu_top_buttons)
        self.account_button.setMinimumSize(QtCore.QSize(100, 0))
        self.account_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.account_button.setFont(font)
        self.account_button.setStyleSheet("background-image: url(resources/icons/cil-user.png);\n"
"background-repeat: none;\n"
"padding-left: 45px;\n"
"background-position: center left;\n"
"")
        self.account_button.setObjectName("account_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.account_button)
        self.home_button = QtWidgets.QPushButton(parent=self.left_menu_top_buttons)
        self.home_button.setMinimumSize(QtCore.QSize(100, 0))
        self.home_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.home_button.setFont(font)
        self.home_button.setStyleSheet("background-image: url(resources/icons/cil-home.png);\n"
"background-repeat: none;\n"
"padding-left: 40px;\n"
"background-position: center left;\n"
"border-left: 2px solid rgb(0, 136, 255);\n"
"border-bottom: 2px solid rgb(0, 136, 255);")
        self.home_button.setObjectName("home_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.home_button)
        self.verticalLayout_2.addWidget(self.left_menu_top_buttons)
        self.setting_button = QtWidgets.QPushButton(parent=self.left_side_menu)
        self.setting_button.setMinimumSize(QtCore.QSize(100, 0))
        self.setting_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.setting_button.setFont(font)
        self.setting_button.setStyleSheet("background-image: url(resources/icons/cil-settings.png);\n"
"background-repeat: none;\n"
"padding-left: 45px;\n"
"background-position: center left;")
        self.setting_button.setObjectName("setting_button")
        self.verticalLayout_2.addWidget(self.setting_button)
        self.horizontalLayout.addWidget(self.left_side_menu)
        self.center_main_items = QtWidgets.QFrame(parent=self.main_body)
        self.center_main_items.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.center_main_items.setStyleSheet("")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.center_main_items)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.center_main_items)
        self.stackedWidget.setStyleSheet("background-color: #F1917D;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setStyleSheet("background-color: #242E48;")
        self.home_page.setObjectName("home_page")
        self.frame = QtWidgets.QFrame(parent=self.home_page)
        self.frame.setGeometry(QtCore.QRect(254, 21, 500, 500))
        self.frame.setMinimumSize(QtCore.QSize(500, 500))
        self.frame.setMaximumSize(QtCore.QSize(500, 500))
        self.frame.setStyleSheet("border: 3px solid rgb(34, 34, 34);\n"
"border-radius: 20px;\n"
"background-color: rgba(0, 0, 50, 100);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setContentsMargins(-1, 11, 11, 11)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Name = QtWidgets.QLabel(parent=self.frame)
        self.Name.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("UTM Loko")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Name.setFont(font)
        self.Name.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(34,34,34);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(1, 90, 153);\n"
"font: 8pt \"UTM Loko\";")
        self.Name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Name.setObjectName("Name")
        self.verticalLayout_8.addWidget(self.Name)
        self.car = QtWidgets.QFrame(parent=self.frame)
        self.car.setMinimumSize(QtCore.QSize(0, 0))
        self.car.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.car.setStyleSheet("image: url(resources/images/Car.png);\n"
"background-color: rgb(34,34,34);\n"
"border-radius: 20px;\n"
"border: 2px solid rgb(1, 90, 153);")
        self.car.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.car.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.car.setObjectName("car")
        self.top = QtWidgets.QLabel(parent=self.car)
        self.top.setGeometry(QtCore.QRect(185, 5, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.top.setFont(font)
        self.top.setStyleSheet("image: none;\n"
"font: 9pt \"Terminal\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(31,22,66);\n"
"border:3px solid  rgb(45, 45, 45);\n"
"border-radius: 10px;")
        self.top.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.top.setObjectName("top")
        self.bottom = QtWidgets.QLabel(parent=self.car)
        self.bottom.setGeometry(QtCore.QRect(185, 400, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bottom.setFont(font)
        self.bottom.setStyleSheet("image: none;\n"
"font: 9pt \"Terminal\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(31,22,66);\n"
"border:3px solid  rgb(45, 45, 45);\n"
"border-radius: 10px;")
        self.bottom.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bottom.setObjectName("bottom")
        self.left = QtWidgets.QLabel(parent=self.car)
        self.left.setGeometry(QtCore.QRect(5, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.left.setFont(font)
        self.left.setStyleSheet("image: none;\n"
"font: 9pt \"Terminal\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(31,22,66);\n"
"border:3px solid  rgb(45, 45, 45);\n"
"border-radius: 10px;")
        self.left.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.left.setObjectName("left")
        self.right = QtWidgets.QLabel(parent=self.car)
        self.right.setGeometry(QtCore.QRect(355, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.right.setFont(font)
        self.right.setStyleSheet("image: none;\n"
"font: 9pt \"Terminal\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(31,22,66);\n"
"border:3px solid  rgb(45, 45, 45);\n"
"border-radius: 10px;")
        self.right.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.right.setObjectName("right")
        self.signal_top = QtWidgets.QLabel(parent=self.car)
        self.signal_top.setGeometry(QtCore.QRect(215, 40, 55, 61))
        self.signal_top.setStyleSheet("image: url(resources/images/Signal_top.png);\n"
"border-radius: 0px;\n"
"border:0px solid  rgb(45, 45, 45);")
        self.signal_top.setText("")
        self.signal_top.setObjectName("signal_top")
        self.signal_left = QtWidgets.QLabel(parent=self.car)
        self.signal_left.setGeometry(QtCore.QRect(120, 180, 55, 61))
        self.signal_left.setStyleSheet("image: url(resources/images/Signal_left.png);\n"
"border-radius: 0px;\n"
"border:0px solid  rgb(45, 45, 45);")
        self.signal_left.setText("")
        self.signal_left.setObjectName("signal_left")
        self.signal_right = QtWidgets.QLabel(parent=self.car)
        self.signal_right.setGeometry(QtCore.QRect(300, 180, 55, 61))
        self.signal_right.setStyleSheet("border-radius: 0px;\n"
"image: url(resources/images/Signal_right.png);\n"
"border:0px solid  rgb(45, 45, 45);")
        self.signal_right.setText("")
        self.signal_right.setObjectName("signal_right")
        self.signal_bottom = QtWidgets.QLabel(parent=self.car)
        self.signal_bottom.setGeometry(QtCore.QRect(210, 330, 55, 61))
        self.signal_bottom.setStyleSheet("image: url(resources/images/Signal_bottom.png);\n"
"border-radius: 0px;\n"
"border:0px solid  rgb(45, 45, 45);")
        self.signal_bottom.setText("")
        self.signal_bottom.setObjectName("signal_bottom")
        self.verticalLayout_8.addWidget(self.car)
        self.stackedWidget.addWidget(self.home_page)
        self.account_page = QtWidgets.QWidget()
        self.account_page.setStyleSheet("background-color: #242E48;")
        self.account_page.setObjectName("account_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.account_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.login_form_frame = QtWidgets.QFrame(parent=self.account_page)
        self.login_form_frame.setMinimumSize(QtCore.QSize(400, 370))
        self.login_form_frame.setMaximumSize(QtCore.QSize(400, 350))
        self.login_form_frame.setStyleSheet("border: 3px solid rgb(34, 34, 34);\n"
"border-radius: 20px;\n"
"background-color: rgba(0, 0, 50, 100);")
        self.login_form_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.login_form_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.login_form_frame.setObjectName("login_form_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.login_form_frame)
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.input_fileds_frame = QtWidgets.QFrame(parent=self.login_form_frame)
        self.input_fileds_frame.setEnabled(True)
        self.input_fileds_frame.setStyleSheet("QFrame{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(34,34,34);\n"
"    border-radius: 20px;\n"
"    border: 2px solid rgb(1, 90, 153);\n"
"}\n"
"QLineEdit{\n"
"    border: 2px solid rgb(0,93,159);\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"    background-color: rgb(0,69,116);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"    border: 2px solid rgb(206,206,206);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLabel\n"
"{\n"
"    border: 3px solid rgb(45, 45, 45);\n"
"    border-radius: 20px;\n"
"}\n"
"QCheckBox\n"
"{\n"
"    color: rgb(255,255,255);\n"
"    padding: 10px;\n"
"}\n"
"QCheckBox::indicator\n"
"{\n"
"    border: 3px solid rgb(0, 93, 199);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    background: rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:hover\n"
"{\n"
"    border: 3px solid rgb(255,255,255);\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    background: 1px solid rgb(34, 34, 34);\n"
"    background-image: url(resources/icons/cil-check.png);\n"
"}\n"
"")
        self.input_fileds_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.input_fileds_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.input_fileds_frame.setObjectName("input_fileds_frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.input_fileds_frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.input_fileds_frame)
        self.label_2.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(31,22,66);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.input_fileds_frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 50))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit.setStyleSheet("QFrame{\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid  rgb(43, 31, 91);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit{\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"    background-color: rgb(31,22,66);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"    border: 2px solid rgb(206,206,206);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.input_fileds_frame)
        self.label_3.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(31,22,66);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.input_fileds_frame)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 50))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_2.setStyleSheet("QFrame{\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid  rgb(43, 31, 91);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit{\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"    background-color: rgb(31,22,66);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"    border: 2px solid rgb(206,206,206);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.input_fileds_frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QFrame{\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid  rgb(43, 31, 91);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius:15px;\n"
"    padding: 15px;\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"    border: 2px solid rgb(206,206,206);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton_2)
        self.profile_icon_frame = QtWidgets.QFrame(parent=self.input_fileds_frame)
        self.profile_icon_frame.setMinimumSize(QtCore.QSize(110, 80))
        self.profile_icon_frame.setMaximumSize(QtCore.QSize(70, 50))
        font = QtGui.QFont()
        font.setPointSize(57)
        font.setBold(False)
        font.setWeight(50)
        self.profile_icon_frame.setFont(font)
        self.profile_icon_frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.profile_icon_frame.setStyleSheet("border-image: url(resources/images/R-removebg-preview.png);\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 25px;\n"
"border: -20px solid rgb(1, 90, 153);")
        self.profile_icon_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.profile_icon_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.profile_icon_frame.setObjectName("profile_icon_frame")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.profile_icon_frame)
        self.checkBox = QtWidgets.QCheckBox(parent=self.input_fileds_frame)
        self.checkBox.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("")
        self.checkBox.setObjectName("checkBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.checkBox)
        self.verticalLayout_5.addWidget(self.input_fileds_frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_7.addWidget(self.login_form_frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.stackedWidget.addWidget(self.account_page)
        self.setting_page = QtWidgets.QWidget()
        self.setting_page.setStyleSheet("background-color: #242E48;")
        self.setting_page.setObjectName("setting_page")
        self.stackedWidget.addWidget(self.setting_page)
        self.horizontalLayout_7.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.center_main_items)
        self.right_side_menu = QtWidgets.QFrame(parent=self.main_body)
        self.right_side_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.right_side_menu.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.right_side_menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.right_side_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.right_side_menu.setObjectName("right_side_menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.right_side_menu)
        self.verticalLayout_4.setContentsMargins(26, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.right_side_menu)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout.addWidget(self.right_side_menu)
        self.verticalLayout.addWidget(self.main_body)
        self.main_footer = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.main_footer.setStyleSheet("QFrame\n"
"{\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-top-color: solid 1px rgb(0,0,0);\n"
"}\n"
"")
        self.main_footer.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_footer.setObjectName("main_footer")
        self.verticalLayout.addWidget(self.main_footer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Nguyen Thai Tai"))
        self.account_button.setText(_translate("MainWindow", "ACCOUNT"))
        self.home_button.setText(_translate("MainWindow", "HOME"))
        self.setting_button.setText(_translate("MainWindow", "SETTINGS"))
        self.Name.setText(_translate("MainWindow", "Monitoring the collision distance of your automobile\'s four sides"))
        self.top.setText(_translate("MainWindow", "2.12345 m"))
        self.bottom.setText(_translate("MainWindow", "2.12345 m"))
        self.left.setText(_translate("MainWindow", "2.12345 m"))
        self.right.setText(_translate("MainWindow", "2.12345 m"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
        self.checkBox.setText(_translate("MainWindow", "Keep me logged in"))
        self.label.setText(_translate("MainWindow", "right"))
