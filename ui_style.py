from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QStyleFactory

def apply_styles(app, window):
    """Uygulamanın genel stillerini uygula."""
    app.setStyle(QStyleFactory.create("Fusion"))

    # Arayüz tasarımı görseller ...
    palette = app.palette()
    palette.setColor(app.palette().Window, Qt.white)
    palette.setColor(app.palette().WindowText, Qt.black)
    palette.setColor(app.palette().Base, Qt.lightGray)
    palette.setColor(app.palette().AlternateBase, Qt.gray)
    palette.setColor(app.palette().ToolTipBase, Qt.white)
    palette.setColor(app.palette().ToolTipText, Qt.black)
    palette.setColor(app.palette().Text, Qt.black)
    palette.setColor(app.palette().Button, Qt.darkGray)
    palette.setColor(app.palette().ButtonText, Qt.white)
    app.setPalette(palette)


    app.setFont(QFont("Arial", 10))

    # Widget stilleri
    window.setStyleSheet("""
        QMainWindow {
            background-color: yellow;
        }
        QLabel {
            font-size: 12px;
            font-weight: bold;
            color: black;
        }
        QComboBox, QLineEdit, QPushButton {
            padding: 5px;
            font-size: 12px;
            border: 1px solid yellow;
            border-radius: 3px;
        }
        QPushButton {
            background-color: black;
            color: yellow;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: blue;
        }
        QTableWidget {
            gridline-color: black;
            font-size: 12px;
        }
        QTableWidget QHeaderView::section {
            background-color: black;
            font-weight: bold;
            font-size: 12px;
        }
    """)