from PyQt4 import QtCore

class TransferLine(QtCore.QObject):

	transferLineList = []

	def __init__(self, tracker, trans_name, comp1_name, comp2_name):

		self.tracker = tracker
		self.name = trans_name

		self.comp1 = self.findComponent(comp1_name)
		self.comp2 = self.findComponent(comp2_name)

		self.connections = [self.comp1,self.comp2]
		#self.addLinks()

	def findComponent(self, comp_name):
		for component in self.tracker.finalComponentList: 
			if (str(component.title()) == comp_name):
				return component
			else:
				pass

	# def addLinks(self):
	# 	self.comp1.addNeighbor(self.comp2)
	# 	self.comp2.addNeighbor(self.comp1)
		# self.connections[0].addNeighbor(self.connections[1])
		# self.connections[1].addNeighbor(self.connections[0])
