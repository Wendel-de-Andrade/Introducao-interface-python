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

# Import Modules
import sys
import os

# Import QT Core
from qt_core import *

# Import Main Windows
from gui.windows.main_window.ui_main_window import *

# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Software BRABO do Wendel")
        
        #Setup Main Window
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        
        #Exibe a Aplicação
        self.show()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
