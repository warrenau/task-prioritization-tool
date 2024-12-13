# task-prioritization-tool/database.py

"""This module provides a database connection."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def createConnection(databaseName):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Tasks",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _createTasksTable()
    return True

def _createTasksTable():
    """Create the tasks table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )