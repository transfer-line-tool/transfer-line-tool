#Plant
import sys
from PyQt4 import QtGui, QtCore
from RoomButton import *
from ComponentButton import *
from Components import *


class Room(QtGui.QGroupBox):
	
	def __init__(self, name, parent, tracker):

		super(Room, self).__init__(name, parent)
		
		self.componentButtonList = []
		self.componentObjectList = []
		self.tracker = tracker
		self.button = None
   		
   		self.initUI(name, parent, tracker)

	def initUI(self, name, parent, tracker):
        #parsePlantXML(name)
		#FOR TESTING PURPOSES ONLY!!!!!
		lastDigit = name[-1]
		componentList = ["M-"+lastDigit+"-1","M-"+lastDigit+"-2","M-"+lastDigit+"-3",
						"T-"+lastDigit+"-1","T-"+lastDigit+"-2","T-"+lastDigit+"-3", 
						"M-"+lastDigit+"-4","M-"+lastDigit+"-5","M-"+lastDigit+"-6"]

		grid = QtGui.QGridLayout()
		upperPartLayout = QtGui.QHBoxLayout()
		grid.setSpacing(10)
		grid.setVerticalSpacing(20)
		
        #floorList is returned by xml parser --> ["Floor 1","Floor 2",...]
        #create instances of FloorButton (extends AbstractButton) from floorList
		for i in range(len(componentList)):
			
			theComponent = Components(componentList[i],self,self.tracker) #should be Component
			theComponentButton = ComponentButton(componentList[i],self,theComponent)
			theComponent.addButton(theComponentButton)

			self.componentButtonList.append(theComponentButton) #was GtGui.QPushButton
			#uncomment when ComponentButton is written!!!!!!!!!!!!!!!!!!!!!!1
			#self.roomButtonList.append(RoomButton(roomList[i], self, theRoom)) #abstract button --> FloorButton

			self.componentObjectList.append(theComponent)

			theComponent.addToFinalComponentList()

		for k in range(len(self.componentButtonList)):
			upperPartLayout.addWidget(self.componentButtonList[k])
			grid.addLayout(upperPartLayout, 0,0,1,2)
			grid.addWidget(self.componentObjectList[k], 1, 0)
			
			test = QtGui.QGroupBox('test',self)
			test.setStyleSheet("""QGroupBox { border: 2px solid rgb(0, 34, 102); background-color: rgb(0, 34, 102); 
			border-radius: 6px; padding-top: 20px; }""")
			grid.addWidget(test,1,1)
		# for k in range(len(self.floorObjectList)):
		# 	grid.addWidget(self.floorObjectList[k], 1, 0, 1, len(self.floorButtonList))
		self.setLayout(grid)
		self.setStyleSheet(""".Room { background-color: rgb(255, 255, 255); font-size: 10px; border-radius: 6px; } 
			.Room::title { color: transparent; background-color: transparent; padding-top: 5px; padding-left: 5px;}""")
		# self.setGeometry(300, 300, 350, 300)
		# self.show()  

	def addButton(self, newButton):
		self.button = newButton