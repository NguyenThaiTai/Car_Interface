import sys
import os
from PyQt6 import uic
from PyQt6.QtCore import (Qt, QPropertyAnimation, QPointF, QEvent, QPoint, QTimer)
from PyQt6.QtWidgets import (
    QMainWindow,QApplication,QPushButton,
    QCheckBox, QComboBox, QDateEdit, QFontComboBox,
    QLineEdit, QRadioButton, QSlider,
    QSpinBox, QVBoxLayout, QWidget, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QColor, QInputEvent, QMouseEvent, QPointerEvent, QSinglePointEvent, QFont, QFontDatabase
#Convert qrc resource file to python file to update the icons we added
#os.system("Pyrcc5 nike_app.qrc -o nike_app_rc.py")
from nike_app_rc import * 
from Car_Interface import *

WINDOWN_SIZE = 0;
#resources/icons/cil-window-maximize.png
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #uic.loadUi("Car_Interface.ui", self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Remove window titlle bar
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        
        #Set main background to transparent
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        #Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))

        #Apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())

        #close windown
        self.ui.closeButton.clicked.connect(lambda: self.close())

        #Restore/Maximuze window
        self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())

        self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())

        #Stacked pages (Default)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

        self.ui.home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))

        self.ui.account_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.account_page))

        self.ui.setting_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.setting_page))

        def moveWindow(e):
            e = QMouseEvent
            if self.isMaximized() == False:
                if e.button == Qt.MouseButton.LeftButton:
                    self.move(self.pos() + e.globalPosition() - self.clickPosition)
                    self.clickPosition = e.globalPosition()
                    e.accept()

        #Add click event to the top header to move the window
        self.ui.main_header.mouseMoveEvent = moveWindow

        for x in self.ui.left_side_menu.findChildren(QPushButton):
            x.clicked.connect(self.applyButtonStyle)

        self.show()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition()

    def applyButtonStyle(self):
        for x in self.ui.left_side_menu.findChildren(QPushButton):
            if x.objectName() != self.sender().objectName():
                defaultStyle = x.styleSheet().replace("border-left: 2px solid rgb(0, 136, 255);", "")
                defaultStyle = defaultStyle.replace("border-bottom: 2px solid rgb(0, 136, 255);", "")
                x.setStyleSheet(defaultStyle)

            newStyle = self.sender().styleSheet() + ("border-left: 2px solid rgb(0, 136, 255);\nborder-bottom: 2px solid rgb(0, 136, 255);")
            self.sender().setStyleSheet(newStyle)
    
    def slideLeftMenu(self):
        width = self.ui.left_side_menu.width()
        if width == 50:
            newwidth = 125
        else:
            newwidth = 50
        
        self.animation = QPropertyAnimation(self.ui.left_side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()
        


    def restore_or_maximize_window(self):
        global WINDOWN_SIZE
        win_status = WINDOWN_SIZE
        if win_status == 0:
            WINDOWN_SIZE = 1
            self.showMaximized()
            self.ui.restoreButton.setIcon(QtGui.QIcon("resources/icons/cil-window-restore.png"))
        else:
            WINDOWN_SIZE = 0
            self.showNormal()
            self.ui.restoreButton.setIcon(QtGui.QIcon("resources/icons/cil-window-maximize.png"))    

    
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()

    sys.exit(app.exec())
else:
    print(__name__, "hh")