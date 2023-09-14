import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit


class PygameRunner(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QTextEdit widget for entering Python code
        self.code_editor = QTextEdit(self)
        self.code_editor.setPlaceholderText("Enter Pygame code here...")

        # Create a "Run" button
        self.run_button = QPushButton("Run", self)
        self.run_button.clicked.connect(self.run_pygame_code)

        # Create a Pygame screen to display the graphics
        self.screen = None

        # Set up the layout
        layout = QHBoxLayout()
        layout.addWidget(self.code_editor)
        layout.addWidget(self.run_button)

        self.setLayout(layout)

    def run_pygame_code(self):
        # Get the Python code from the QTextEdit widget
        pygame_code = self.code_editor.toPlainText()

        # Initialize Pygame
        pygame.init()

        # Create a Pygame screen (adjust dimensions as needed)
        self.screen = pygame.display.set_mode((800, 600))

        # Execute the Python code (make sure to handle Pygame events)
        try:
            exec(pygame_code)
        except Exception as e:
            print(f"Error: {e}")

        # Main loop to keep the Pygame window open
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()


class PygameApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pygame Editor")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        pygame_runner = PygameRunner()
        main_layout.addWidget(pygame_runner)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = PygameApp()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
