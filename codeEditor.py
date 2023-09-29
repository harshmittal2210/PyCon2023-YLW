from PyQt5.QtGui import QTextCursor, QTextCharFormat, QSyntaxHighlighter, QFont
from PyQt5.QtWidgets import QPlainTextEdit, QTextEdit, QWidget, QVBoxLayout, QPushButton, QApplication
from PyQt5.QtCore import Qt, QRegExp

class PythonCodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        # Set up tab and indentation settings
        self.setTabStopWidth(20)
        self.setTabChangesFocus(False)

        # Create a syntax highlighter
        self.highlighter = PythonSyntaxHighlighter(self.document())

        self.zoom_level = 5
    
    def textZoomIn(self):
        self.zoom_level *= 2
        self.zoom_level = min(self.zoom_level, 20)
        self.zoomIn(self.zoom_level)

    def textZoomOut(self):
        self.zoom_level /= 2
        self.zoom_level = max(self.zoom_level, 2)
        self.zoomOut(self.zoom_level)
    
    def text(self):
        return self.toPlainText()

class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        self.highlighting_rules = []

        # Create rules for highlighting different elements
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.blue)
        keyword_format.setFontWeight(QFont.Bold)
        keywords = ["if", "else", "while", "for", "def", 
                    "import", "as", "print", "from", "elif",
                    "len", "not", "is", "and", "else"]  # Add more as needed
        for keyword in keywords:
            rule = (r'\b' + keyword + r'\b', keyword_format)
            self.highlighting_rules.append(rule)

        # Create a rule for strings (in double or single quotes)
        string_format = QTextCharFormat()
        string_format.setForeground(Qt.darkGreen)
        self.highlighting_rules.append((r'\".*\"', string_format))
        self.highlighting_rules.append((r'\'.*\'', string_format))
        self.highlighting_rules.append((r'\#.*\'', string_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

if __name__ == '__main__':
    app = QApplication([])

    editor = PythonCodeEditor()
    editor.show()

    app.exec_()

