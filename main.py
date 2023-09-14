import sys
import os
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QPlainTextEdit
from PyQt5 import uic  # Import the uic module
from codeEditor import PythonCodeEditor

class PygameApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('ui/editor.ui', self)
        self.setWindowTitle("PyCon Young Learners Workshop")

        self.codeEditorWidget:QWidget = PythonCodeEditor()
        self.codePanelLayout:QVBoxLayout
        self.codePanelLayout.addWidget(self.codeEditorWidget)



        self.show()


def main():
    app = QApplication(sys.argv)
    ex = PygameApp()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()