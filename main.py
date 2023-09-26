import sys
import os
import threading
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFileDialog
from PyQt5.QtWidgets import QAction, QTreeWidget, QPushButton, QTreeWidgetItem, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5 import uic  # Import the uic module
from codeEditor import PythonCodeEditor
import subprocess

class PygameApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pygame_thread = None
        self.screen = None
    
    def initUI(self):
        uic.loadUi('ui/editor.ui', self)
        self.setWindowTitle("PyCon Young Learners Workshop")

        self.codePanelLayout:QVBoxLayout
        self.runButton:QPushButton
        self.terminalButton:QPushButton
        self.fileDirTreeWidget:QTreeWidget

        self.actionOpen:QAction
        self.actionSave:QAction
        self.actionFAQ:QAction
        self.actionAbout:QAction

        self.codeEditorWidget:QWidget = PythonCodeEditor()
        
        self.codePanelLayout.addWidget(self.codeEditorWidget)

        self.terminalButton.setIcon(QIcon("./ui/img/terminal.png"))
        self.runButton.setIcon(QIcon("./ui/img/game.png"))
        self.runButton.clicked.connect(self.runPygameCode)
        self.terminalButton.clicked.connect(self.runTerminalCommand)
        self.fileDirTreeWidget.itemDoubleClicked.connect(self.openTutorialFile)

        ## Actions
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionFAQ.triggered.connect(self.open_faq)
        self.actionAbout.triggered.connect(self.open_about)

        self.actionOpen.setShortcut("Ctrl+O")
        self.actionSave.setShortcut("Ctrl+S")

        self.populateTree("Tutorials", self.fileDirTreeWidget)
        self.fileDirTreeWidget.sortItems(0, 0)

        self.show()
        

    def runPygameCode(self):
        # Clear the Pygame screen if it's already open
        if self.screen:
            pygame.quit()

        pygameCode = self.codeEditorWidget.text()

        # Define a function to run Pygame in a separate thread
        def pygame_thread_function():
            # Initialize Pygame
            # pygame.init()

            # Create a Pygame screen (adjust dimensions as needed)
            # self.screen = pygame.display.set_mode((800, 600))
            running = True
            # Execute the Python code (make sure to handle Pygame events)
            try:
                exec(pygameCode)
            except Exception as e:
                print(f"Error: {e}")
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setWindowTitle("Error")
                error_dialog.setText(f"Error: {e}")
                error_dialog.exec_()

            # Main loop to keep the Pygame window open
            
            # while running:
            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             running = False
            pygame.quit()

            end_dialog = QMessageBox()
            end_dialog.setIcon(QMessageBox.Information)
            end_dialog.setWindowTitle("Information")
            end_dialog.setText(f"Code Execution Completed !!")
            end_dialog.exec_()

        # Start the Pygame thread
        self.pygame_thread = threading.Thread(target=pygame_thread_function, daemon=True)
        self.pygame_thread.start()

    def runTerminalCommand(self):
        
        with open("temp.py", "w") as file:
            file.write(self.codeEditorWidget.text())
        command = f"python temp.py"
        subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"{command}; read -p 'Press Enter to exit...'"])
        print("Done Terminal Code")

    def populateTree(self, path, parent):
        for item in os.listdir(path):
            
            itemPath = os.path.join(path, item)
            itemIsDir = os.path.isdir(itemPath)

            if itemIsDir and type(parent) == QTreeWidget:
                parentItem = QTreeWidgetItem(parent, [item])
                parent.addTopLevelItem(parentItem)
                sys.path.append(itemPath)
                self.populateTree(itemPath, parentItem)
            else:
                QTreeWidgetItem(parent, [item])
                
    
    def openTutorialFile(self, item, column):
        path = []
        while item is not None:
            path.insert(0, item.text(0))
            item = item.parent()

        # Join the path elements and print it
        full_path = os.path.join("./Tutorials", *path)  # Join with "/" as the separator
        # print("Double-clicked:", full_path)
        if full_path.endswith(".py"):
            with open(full_path, 'r') as file:
                # Read the entire file content into a string
                file_content = file.read()
                self.codeEditorWidget.setPlainText(file_content)
    
    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.ExistingFiles

        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Python Files (*.py)")
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setOptions(options)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                with open(file_path, 'r') as file:
                    file_contents = file.read()
                    # Now you can work with the file_contents
                    self.codeEditorWidget.setPlainText(file_contents)
                    return
    
    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.ExistingFiles

        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Python Files (*.py)")
        file_dialog.setOptions(options)

        default_file_name = "TestCode.py"  # Default file name
        file_path, _ = file_dialog.getSaveFileName(self, "Save File", default_file_name, "Python Files (*.py)")

        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.codeEditorWidget.text())
    
    def open_faq(self):
        url = QUrl("https://www.harshmittal.co.in/PyCon2023-YLW")
        QDesktopServices.openUrl(url)

    def open_about(self):
        url = QUrl("https://github.com/harshmittal2210/PyCon2023-YLW/wiki")
        QDesktopServices.openUrl(url)
        



def main():
    app = QApplication(sys.argv)
    ex = PygameApp()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()