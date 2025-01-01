# task-prioritization-tool/model.py

"""This module provides a model to manage the tasks table"""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class TasksModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Create and set up the model"""
        tableModel = QSqlTableModel()
        tableModel.setTable("tasks")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("id","Task", "Due Date", "Est Completion Time", "Progress", "Importance", "Priority")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel
    
    def addTask(self,data):
        """Add a task to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows,column+1), field)
        self.model.setData(self.model.index(rows,6), 0)
        self.model.submitAll()
        self.model.select()

    def deleteTask(self, row):
        """Remove a task from the database."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearTasks(self):
        """Remove all tasks in the database."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
