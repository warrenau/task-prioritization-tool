# task-prioritization-tool/main.py

"""This module provides task prioritization tool application."""

import sys

from PyQt6.QtWidgets import QApplication

from .database import createConnection
from .views import Window

def main():
    """task-prioritization-tool main function."""
    # Create the application
    app = QApplication(sys.argv)
    # connect to the database before creating any window
    if not createConnection("tasks.sqlite"):
        sys.exit(1)
    # create the main window
    win = Window()
    win.show()
    # run the event loop
    sys.exit(app.exec())