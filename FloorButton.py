import sys
from Controller import *
from PyQt4 import QtGui, QtCore

class FloorButton(QtGui.QPushButton):

	def __init__(self,name,parent,floor):
		
		super(FloorButton,self).__init__(name, parent)
		self.myFloor = floor
		self.myFloor.hide()

		self.tracker = self.myFloor.tracker

		self.clicked.connect(lambda: self.showFloor(parent))
		self.clicked.connect(lambda: self.tracker.switch())
		self.installEventFilter(self.tracker.main)
		#self.clicked.connect(clicked_slot)

	def showFloor(self,parent):
		self.setStyleSheet('QPushButton {color: Red; font-weight: bold;}')
		for button in parent.floorButtonList:
			if (button != self):
				button.setStyleSheet('QPushButton {color: rgb(0, 34, 102);}')
		for floor in parent.floorObjectList:
			if (floor != self.myFloor):
				floor.hide()
			else:
				floor.show()
		#Controller().switchState(States.FLOOR)

		