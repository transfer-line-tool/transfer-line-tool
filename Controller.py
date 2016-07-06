from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSignal
from Tester import *
from PyQt4.QtCore import pyqtSlot

class Controller(QtCore.QObject):

	valueUpdated = QtCore.pyqtSignal()

	def switchState(self, state):
		CENTRAL_WIDGET_STATE = state
		print "The current central widget state is: "+ str(CENTRAL_WIDGET_STATE)

