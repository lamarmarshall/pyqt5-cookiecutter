import sys
from PyQt5 import QtWidgets
from ui.Test_Window import Ui_MainWindow

class {{cookiecutter.project_name}}():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow =QtWidgets.QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.setWindowTitle('First Test')
        
        self.update_widgets()
        self.widget_actions()
    
        self.MainWindow.show()
        sys.exit( app.exec_())

    def widget_actions(self):
        #toolbar action
        self.ui.actionExit.setStatusTip("exit program")
        self.ui.actionExit.triggered.connect(self.close_GUI)
        self.ui.actionExit.setShortcut('Ctrl+Q')
        self.ui.btn2.clicked.connect(self.set_label )
        self.ui.btn3.clicked.connect(self.print_it)

    def print_it(self):
        print("got it")

    def set_label(self):
        self.ui.label.setText("did it")


    def close_GUI(self):
        self.MainWindow.close()

    def update_widgets(self):
        self.ui.pushButton.setText("First Button")
        self.ui.btn2.setText("Second Button")



if __name__ == '__main__':
    {{cookiecutter.project_name}}()

