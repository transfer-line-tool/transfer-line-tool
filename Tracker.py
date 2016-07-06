from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSignal
from TransferLine import *

class Tracker(QtCore.QObject):

	finalComponentList = []
	neighborButtonList = []
	transferLineList = []
	valueUpdated = QtCore.pyqtSignal()
	
	# trackerObjectList = []

	def __init__(self,mainW):
		super(Tracker, self).__init__()
		self.main = mainW


	def switch(self):
		self.valueUpdated.emit()

	def initTransferLines(self):
		listOfTransferLinesAndConnections = self.getXMLTransferLineData() #list in form [[name_str,comp1_str,comp2_str],...]
		for eachTransferLine in listOfTransferLinesAndConnections:
			self.transferLineList.append(TransferLine(self,eachTransferLine[0],eachTransferLine[1],eachTransferLine[2]))
		self.printStuff(self.transferLineList)

	"""FOR TESTING PURPOSES ONLY!!!!!!!!!!"""
	def getXMLTransferLineData(self):
		return [["X1","M-1-1","M-3-1"],["X2","M-2-1","M-3-3"],["X3","M-1-1","M-2-1"],
		["X4","M-3-3","M-1-1"],["X5","M-2-1","M-5-2"],["X6","M-1-1","M-2-1"],["X7","M-3-3","M-1-1"],
		["X8","M-2-1","M-3-3"]]

	def printStuff(self, myList):
		print "TRANSFER LINES"
		print
		for thing in myList:
			print thing.name + " connected to " + str(thing.connections[0]) + " and " + str(thing.connections[1])

	def addLinks(self):
		for transferLine in self.transferLineList:
			(transferLine.comp1).addNeighbor(transferLine.comp2,transferLine)
			#(transferLine.comp2).addNeighbor(transferLine.comp1)

	def addNeighborButtonMessages(self):
		for neighborButton in self.neighborButtonList:
			neighborButton.setMessage()


	#################################################
	
	# def eventFilter(self, object, event):
	# 	if (event.type() == QtCore.QEvent.HoverEnter):
	# 		print "you hovered!"
	# 		return True
	# 	else:
	# 		return False