#Plant
import sys
from PyQt4 import QtGui, QtCore
from RoomButton import *
from Room import *


class Floor(QtGui.QGroupBox):
	
	def __init__(self, name, parent, tracker):

		super(Floor, self).__init__(name, parent)
		
		self.roomButtonList = []
		self.roomObjectList = []
		self.tracker = tracker
		self.button = None
   		
   		self.initUI(name, parent, tracker)

	def initUI(self,name, parent, tracker):
        #parsePlantXML(name)
		#FOR TESTING PURPOSES ONLY!!!!!
		roomList = []
		if (name == "Floor 1"):
			roomList = ["Room 1","Room 2","Room 3"]
		elif (name == "Floor 2"):
			roomList = ["Room 4","Room 5","Room 6"]
		else:
			roomList = ["Room 7","Room 8","Room 9"]

		grid = QtGui.QGridLayout()
		grid.setSpacing(10)
		grid.setVerticalSpacing(20)
		
        #floorList is returned by xml parser --> ["Floor 1","Floor 2",...]
        #create instances of FloorButton (extends AbstractButton) from floorList
		for i in range(len(roomList)):
			
			theRoom = Room(roomList[i],self,self.tracker)#QtGui.QGroupBox(roomList[i]) #should be Room()
			theRoomButton = RoomButton(roomList[i], self, theRoom)
			theRoom.addButton(theRoomButton)

			self.roomButtonList.append(theRoomButton) #abstract button --> FloorButton
			self.roomObjectList.append(theRoom)
			
		for k in range(len(self.roomButtonList)):
			grid.addWidget(self.roomButtonList[k], 0, k)
		#Comment after testing!!!!!
		for k in range(len(self.roomObjectList)):
			grid.addWidget(self.roomObjectList[k], 1, 0, 1, len(self.roomButtonList))
		self.setLayout(grid)
		# self.setGeometry(300, 300, 350, 300)
		# self.show()  
		self.setStyleSheet(""".Floor { background-color: white; font-size: 10px; border-radius: 6px} 
			.Floor::title { color: transparent; background-color: transparent; padding-top: 5px; padding-left: 5px; }""")

	def addButton(self, newButton):
		self.button = newButton

