from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication


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

        # font = QFont()
        # screen_dpi = QApplication.primaryScreen().logicalDotsPerInch()
        # font_size = int(screen_dpi / 96 * 16)
        # font.setPixelSize(font_size)
        # self.setFont(font)

        self.zoom_level = 5
        self.zoomTo(self.zoom_level)
    
    def textZoomIn(self):
        self.zoom_level *= 2
        self.zoom_level = min(self.zoom_level, 20)
        self.zoomTo(self.zoom_level)
    
    def textZoomOut(self):
        self.zoom_level /= 2
        self.zoom_level = max(self.zoom_level, 2)
        self.zoomTo(self.zoom_level)

    def setPlainText(self, text):
        self.setText(text)
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
