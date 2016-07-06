import sys
from PyQt4 import QtGui, QtCore
from RoomButton import *
from ComponentButton import *
from NeighborButton import *


class Components(QtGui.QGroupBox):
	
	def __init__(self, name, parent, tracker):

		super(Components, self).__init__(name, parent)
		
		self.miniComponentButtonList = []
		#self.componentObjectList = []
		self.tracker = tracker
		self.button = None
		self.neighbors = []
		self.index = None
   		
   		self.initUI(name, parent, tracker)

	def initUI(self, name, parent, tracker):
        #parsePlantXML(name)
		#FOR TESTING PURPOSES ONLY!!!!!
		lastDigit = name[-1]
		miniComponentList = ["M-"+lastDigit+"-1","M-"+lastDigit+"-2","M-"+lastDigit+"-3"]

		self.grid = QtGui.QVBoxLayout()
		self.grid.setSpacing(0)

		self.setStyleSheet("""QGroupBox { border: 2px solid rgb(0, 34, 102); background-color: rgb(204, 221, 255); 
			border-radius: 6px; padding-top: 20px; }""")
		
        #floorList is returned by xml parser --> ["Floor 1","Floor 2",...]
        #create instances of FloorButton (extends AbstractButton) from floorList

		# for i in range(len(miniComponentList)):
		# 	#theComponent = QtGui.QGroupBox(componentList[i]) #should be Component
			
		# 	self.miniComponentButtonList.append(QtGui.QPushButton(miniComponentList[i])) #was GtGui.QPushButton

		# for k in range(len(self.miniComponentButtonList)):
		# 	grid.addWidget(self.miniComponentButtonList[k], k, 0)
		# for k in range(len(self.miniComponentButtonList),10):
		# 	grid.addWidget(QtGui.QPushButton("empty"))

		self.setLayout(self.grid)
		self.setFixedWidth(200)
		
		label = QtGui.QLabel('expand >>',self)
		label.setStyleSheet("""QLabel { font-size: 8px; color: blue}""")
		label.setGeometry((self.width() - label.sizeHint().width()) / 2 +20 ,
		 (self.height() - label.sizeHint().height()) / 2 -3, label.sizeHint().width(), label.sizeHint().height())
		label.mousePressEvent = self.expand

	def expand(self, event):
		print "link activated!!!!"


	def addToFinalComponentList(self):
		self.tracker.finalComponentList.append(self)
		#print len(self.tracker.finalComponentList)
		#print str(self.title())

	def addButton(self, newButton):
		self.button = newButton

	def addNeighbor(self,neighbor,transfer_line):
		self.neighbors.append(neighbor)
		neighbor.neighbors.append(self)
		
		info_string = " (via " + transfer_line.name + ")"

		neighborButton = NeighborButton("to "+str(neighbor.title())+info_string, self, neighbor) #QtGui.QPushButton(str(neighbor.title()))
		newNeighborButton = NeighborButton("to "+str(self.title())+info_string, neighbor, self)
		
		self.miniComponentButtonList.append(neighborButton)
		neighbor.miniComponentButtonList.append(newNeighborButton)

		self.tracker.neighborButtonList.append(neighborButton)
		self.tracker.neighborButtonList.append(newNeighborButton)
		
		index = 0
		for i in range(self.grid.count()):
			print neighborButton.text() + " vs. " + self.grid.itemAt(i).widget().text()
			if neighborButton.text() <= self.grid.itemAt(i).widget().text():
				print "true"
				break
			index += 1
		self.grid.insertWidget(index, neighborButton)

		_index = 0
		for i in range(neighbor.grid.count()):
			if newNeighborButton.text() <= neighbor.grid.itemAt(i).widget().text():
				break
			_index += 1
		neighbor.grid.insertWidget(_index, newNeighborButton)




		# self.grid.addWidget(neighborButton)
		# neighbor.grid.addWidget(newNeighborButton)

