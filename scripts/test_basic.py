import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QPlainTextEdit
from PyQt5.QtGui import QSyntaxHighlighter, QTextCursor, QTextCharFormat
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PythonCodeEditor(QsciScintilla):
    def __init__(self):
        super().__init__()

        # Create a lexer for Python
        lexer = QsciLexerPython(self)
        self.setLexer(lexer)

        # Set up tab and indentation settings
        self.setTabWidth(4)
        self.setIndentationsUseTabs(False)
        self.setIndentationGuides(True)
        self.setAutoIndent(True)

        # Create a syntax highlighter
        self.highlighter = PythonSyntaxHighlighter(self)

    def setPlainText(self, text):
        super().setPlainText(text)
        self.setCursorPosition(0, 0)


class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.highlighting_rules = []

        # Create rules for highlighting different elements
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.blue)
        keyword_format.setFontWeight(QFont.Bold)
        keywords = ["if", "else", "while", "for", "def", "import", "as", "print"]  # Add more as needed
        for keyword in keywords:
            rule = (r'\b' + keyword + r'\b', keyword_format)
            self.highlighting_rules.append(rule)

        # Create a rule for strings (in double or single quotes)
        string_format = QTextCharFormat()
        string_format.setForeground(Qt.darkGreen)
        self.highlighting_rules.append((r'\".*\"', string_format))
        self.highlighting_rules.append((r'\'.*\'', string_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)


class PygameRunner(QWidget):
    def __init__(self):
        super().__init__()

        # Create a Python code editor widget
        self.code_editor = PythonCodeEditor()

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
        # Clear the Pygame screen if it's already open
        if self.screen:
            pygame.quit()

        # Get the Python code from the code editor
        pygame_code = self.code_editor.text()

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
