import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
from Controller import *
from Tester import *

class NeighborButton(QtGui.QPushButton):

	def __init__(self,name,start_comp,end_comp):
		
		super(NeighborButton,self).__init__(name)
		self.start = start_comp
		self.end = end_comp
		
		self.clicked.connect(self.retrace)
		self.pressed.connect(self.pressedSlot)
		print str(name) + " has " + str(len(self.end.neighbors)) + " neighbors"
		print "with mini button list of length " + str(len(self.end.miniComponentButtonList))+"\n"
		
		#self.setToolTip(self.setMessage())
		#self.setMessage()

	def pressedSlot(self):
		print "pressed!"
		# global listWidget
		# listWidget = QtGui.QListWidget()
		# for neighbor in self.end.neighbors:
		# 	listWidget.addItem(neighbor.title())
		# listWidget.show()

	def setMessage(self):
		string = "connects to...\n"
		self.end.neighbors.sort()
		for neighbor in self.end.neighbors:
			string += str(neighbor.title())+"\n"
		self.setToolTip(string)


	def retrace(self):

		self.end.button.showComponent(self.end.parentWidget())
		self.end.parentWidget().button.showRoom(self.end.parentWidget().parentWidget())
		self.end.parentWidget().parentWidget().button.showFloor(self.end.parentWidget().parentWidget().parentWidget())