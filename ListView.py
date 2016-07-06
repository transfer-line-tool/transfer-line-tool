#ListView 
from PyQt4 import QtGui, QtCore

class ListView(QtGui.QTreeWidget):
	
	def __init__(self,tracker):
		
		super(ListView ,self).__init__()
		self.tracker = tracker
		#self.setStyleSheet("QTreeView: { selection-background-color: transparent; }")
		self.setFocusPolicy(QtCore.Qt.NoFocus)

		header = QtGui.QTreeWidgetItem()
		header.setText(0,"COMPONENTS")
		self.setHeaderItem(header)

		#self.append("<b><u>COMPONENT LIST<u><b>")
		manifoldItem = QtGui.QTreeWidgetItem()
		manifoldItem.setText(0,"MANIFOLDS")
		tankItem = QtGui.QTreeWidgetItem()
		tankItem.setText(0,"TANKS")
		self.addTopLevelItem(manifoldItem)
		self.addTopLevelItem(tankItem)
		
		for component in self.tracker.finalComponentList:
		
			if str(component.title())[0] == "M":
				# header = QtGui.QTreeWidgetItem()
				# header.setText(0,"MANIFOLDS")
				# self.setHeaderItem(header)

				item = QtGui.QTreeWidgetItem()
				item.setText(0,component.title())

				childItem = QtGui.QTreeWidgetItem()
				childString = self.generateComponentDescription(component)
				childItem.setText(0,childString)

				item.addChild(childItem)
				manifoldItem.addChild(item)

			if str(component.title())[0] == "T":
				# header = QtGui.QTreeWidgetItem()
				# header.setText(0,"TANKS")
				# self.setHeaderItem(header)

				item = QtGui.QTreeWidgetItem()
				item.setText(0,component.title())

				childItem = QtGui.QTreeWidgetItem()
				childString = self.generateComponentDescription(component)
				childItem.setText(0,childString)

				item.addChild(childItem)
				tankItem.addChild(item)


	def generateComponentDescription(self, component):
		string = "Location: " 
		string += component.parentWidget().title() + ", " #room
		string += component.parentWidget().parentWidget().title() + ", " #floor
		string += component.parentWidget().parentWidget().parentWidget().title() #plant
		string += "\n"
		string += "Connected to: "
		for neighbor in component.neighbors:
			string += neighbor.title() + ", "
		string += "\n"
		return string
