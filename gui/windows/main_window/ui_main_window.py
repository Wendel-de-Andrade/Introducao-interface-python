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
    def setup_ui(self, parent):
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
        self.left_menu.setMinimumWidth(50)
        
        
        #Content
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        #Content Layount
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        #Top Bar
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)

        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)

        #Left Label
        self.top_label_left = QLabel("Essa é minha primeira aplicação com PySide6")

        #Top Spacer
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #Right Label
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pb 'segoe UI'")
        
        #Add to Layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)
        

        #Left Label
        self.top_label_left = QLabel("Essa é minha primeira aplicação com PySide6")

        #Top Spacer
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #Right Label
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pb 'segoe UI'")
        
        #Add to Layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)
        
        #Application Pages 
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")

        #Botton Bar
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

        #Add to Content Layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        #Add Widgets to APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        #Set Central Widget
        parent.setCentralWidget(self.central_frame)
