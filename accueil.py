# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets


class accueil(QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
@elif 'QWidget' === 'QMainWindow'
        QtWidgets.QMainWindow.__init__(self)
@elif 'QWidget' === 'QQuickItem'
        QtQuick.QQuickItem.__init__(self)
        pass
