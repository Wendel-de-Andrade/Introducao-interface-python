# ///////////////////////////////////////////////////////////////
#
# BY: WENDEL DE ANDRADE
# COURSE BY: WANDERSON M.PIMENTA | https://www.youtube.com/channel/UCy1fv5dh3wQEem1nFAUBJzw
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# Import QT Core
from qt_core import *

#Main Window
class UI_MainWindow(object):
    def setuo_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
            
        #Set Initial Parameters
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)
        
        #Create Central Widget
        self.central_frame = QFrame()
        
        #Create Main Layout
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        #Left Menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        
        
        #Content
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")
        
        #Add Widgets to APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        #Set Central Widget
        parent.setCentralWidget(self.central_frame)
