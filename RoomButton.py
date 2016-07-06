import sys
from PyQt4 import QtGui, QtCore
from Controller import *
from Tester import *

class RoomButton(QtGui.QPushButton):

	def __init__(self,name,parent,room):
		
		super(RoomButton,self).__init__(name, parent)
		self.myRoom = room
		self.myRoom.hide()

		#WILL NEED THIS LATER
		#self.tracker = self.myRoom.tracker


		# self.setMask(QtGui.QRegion(QtCore.QRect(self.x(),self.y()+50,200,100),QtGui.QRegion.Ellipse))
		# self.resize(200,200)
		self.clicked.connect(lambda: self.showRoom(parent))
		#self.clicked.connect(clicked_slot)

	def showRoom(self,parent):
		self.setStyleSheet('QPushButton {color: Red; font-weight: bold;}')
		for button in parent.roomButtonList:
			if (button != self):
				button.setStyleSheet('QPushButton {color: rgb(0, 34, 102);}')
		#Controller().switchState(States.ROOM)
		for room in parent.roomObjectList:
			if (room != self.myRoom):
				room.hide()
			else:
				room.show()	 	
