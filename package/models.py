import typing
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt


class PinModel(QAbstractTableModel):
    def __init__(self, pins_list, parent=None):
        super(PinModel, self).__init__(parent)
        self._pins_list = pins_list

    def data(self, index: QModelIndex, role: int = ...):
        if index.isValid():
            if role == Qt.EditRole or role == Qt.DisplayRole:
                return self._pins_list[index.row()].data(index.column())

    def setData(self, index: QModelIndex, value: typing.Any, role: int = ...):
        if index.isValid():
            if role == Qt.EditRole or role == Qt.DisplayRole:
                self._pins_list[index.row()].set_data(index.column(), value)
                return True
        return False

    def columnCount(self, parent=None, *args, **kwargs):
        return 6

    def rowCount(self, parent=None, *args, **kwargs):
        return self._pins_list.__len__()

    def flags(self, index: QModelIndex):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable
