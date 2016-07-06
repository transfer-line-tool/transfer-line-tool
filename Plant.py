#Plant
import sys
from PyQt4 import QtGui, QtCore
from FloorButton import *
from Floor import *

class Plant(QtGui.QGroupBox):
	
	def __init__(self, name, tracker):

		super(Plant, self).__init__(name)
		
		self.floorButtonList = []
		self.floorObjectList = []
   		
   		self.initUI(name, tracker)

	def initUI(self,name, tracker):
        #parsePlantXML(name)
		floorList = ["Floor 1","Floor 2","Floor 3"]
		grid = QtGui.QGridLayout()
		grid.setSpacing(10)
		grid.setVerticalSpacing(20)
		
        #floorList is returned by xml parser --> ["Floor 1","Floor 2",...]
        #create instances of FloorButton (extends AbstractButton) from floorList
		for i in range(len(floorList)):
			
			theFloor = Floor(floorList[i], self, tracker) #changed from QtGui.QGroupBox
			theFloorButton = FloorButton(floorList[i], self, theFloor)
			theFloor.addButton(theFloorButton)

			self.floorButtonList.append(theFloorButton) #abstract button --> FloorButton
			self.floorObjectList.append(theFloor)

		for k in range(len(self.floorButtonList)):
			grid.addWidget(self.floorButtonList[k], 0, k)
		for k in range(len(self.floorObjectList)):
			grid.addWidget(self.floorObjectList[k], 1, 0, 1, len(self.floorButtonList))
		
		#self.setStyleSheet(""".Plant { background-color: rgb(0, 34, 102); }""")
		self.setStyleSheet("""QPushButton {color: rgb(0, 34, 102); } .Plant { background-color: white; font-size: 10px; } 
			.Plant::title { color: white; padding-top: 5px; padding-left: 5px; }""")
			#rgb(0, 34, 102)
		self.setLayout(grid)
		self.setGeometry(300, 300, 350, 300)
		self.show()  

def main():
    
	app = QtGui.QApplication(sys.argv)
	ex = Plant("test")
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()    