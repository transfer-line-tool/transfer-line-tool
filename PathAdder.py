from PyQt4 import QtGui,QtCore
from Dijsktra import *
from TransferLine import TransferLine
import itertools

class PathAdder(QtGui.QWidget):

	paths = []
	blockedTransferLines = []
	temporaryTransferLines = []
	
	def __init__(self, mainWindow, tracker):

		super(PathAdder,self).__init__()
		self.tracker = tracker

		overallLayout = QtGui.QHBoxLayout()
		leftSideLayout = QtGui.QVBoxLayout()
		leftSide = QtGui.QWidget()
		leftSide.setContentsMargins(QtCore.QMargins(0,0,0,0))

		pathAdder = QtGui.QWidget()
		pathAdderLayout = QtGui.QFormLayout()
		pathAdderLayout.setFormAlignment(QtCore.Qt.AlignLeft)
		pathAdder.setStyleSheet(""".QWidget { background-color: rgb(204, 221, 255); 
			border-radius: 6px;}""")
		#pathAdder.setMaximumWidth(200)

		transferLineChanger = QtGui.QWidget()
		transferLineChangerLayout = QtGui.QFormLayout()
		transferLineChangerLayout.setFormAlignment(QtCore.Qt.AlignLeft)
		transferLineChanger.setStyleSheet(""".QWidget { background-color: rgb(204, 221, 255); 
			border-radius: 6px;}""")
		
		self.startPoints = QtGui.QComboBox()
		self.endPoints = QtGui.QComboBox()
		self.transferLineStart = QtGui.QComboBox()
		self.transferLineEnd = QtGui.QComboBox()


		self.usedTransferLines = QtGui.QComboBox()
		self.usedTransferLinesViewer = QtGui.QTextEdit()
		self.usedTransferLinesViewer.setReadOnly(True)
		#self.usedTransferLinesViewer.setMaximumWidth(120)


		for component in self.tracker.finalComponentList:
			self.startPoints.addItem(component.title())
			self.endPoints.addItem(component.title())
			self.transferLineStart.addItem(component.title())
			self.transferLineEnd.addItem(component.title())

		for transferLine in self.tracker.transferLineList:
			self.usedTransferLines.addItem(transferLine.name)

		self.componentListCopy = self.tracker.finalComponentList[:]
		self.transferLineListCopy = self.tracker.transferLineList[:]

		addButton = QtGui.QPushButton("Add")
		clearButton = QtGui.QPushButton("Clear All")
		undoButton = QtGui.QPushButton("Undo")
		pathButton = QtGui.QPushButton("Construct")
		blockButton = QtGui.QPushButton("Add Block")
		newButton = QtGui.QPushButton("Add New")


		pathAdderLayout.addRow("Start:", self.startPoints)
		pathAdderLayout.addRow("End:", self.endPoints)
		pathAdderLayout.addWidget(addButton)
		pathAdderLayout.addWidget(clearButton)
		pathAdderLayout.addWidget(undoButton)
		pathAdderLayout.addWidget(pathButton)
		
		self.temporaryName = QtGui.QLineEdit()
		self.newTransferLineViewer = QtGui.QTextEdit()
		self.newTransferLineViewer.setReadOnly(True)



		transferLineChangerLayout.addRow("Block:", self.usedTransferLines)
		transferLineChangerLayout.addWidget(blockButton)
		transferLineChangerLayout.addWidget(QtGui.QLabel("<b>MANUALLY BLOCKED TRANSFER LINES <b>"))
		transferLineChangerLayout.addWidget(self.usedTransferLinesViewer)
		
		rowLayout = QtGui.QHBoxLayout()
		rowLayout.setAlignment(QtCore.Qt.AlignLeft)
		rowLayout.addWidget(QtGui.QLabel("New:  from "))
		rowLayout.addWidget(self.transferLineStart)
		rowLayout.addWidget(QtGui.QLabel(" to "))
		rowLayout.addWidget(self.transferLineEnd)
		

		transferLineChangerLayout.addRow(rowLayout)
		transferLineChangerLayout.addWidget(newButton)


		# transferLineChangerLayout.addRow("New:", self.temporaryName)
		# transferLineChangerLayout.addRow("1", self.transferLineStart)
		# transferLineChangerLayout.addRow("2", self.transferLineEnd)
		transferLineChangerLayout.addWidget(QtGui.QLabel("<b>TEMPORARY CONNECTIONS <b>"))
		transferLineChangerLayout.addWidget(self.newTransferLineViewer)


		
		pathAdder.setLayout(pathAdderLayout)
		transferLineChanger.setLayout(transferLineChangerLayout)
		leftSideLayout.addWidget(pathAdder)
		leftSideLayout.addWidget(transferLineChanger)
		leftSide.setLayout(leftSideLayout)
		
		self.selectionViewer = QtGui.QTextEdit()
		self.pathViewer = QtGui.QTextEdit()
		self.selectionViewer.setReadOnly(True)
		self.pathViewer.setReadOnly(True)

		textView = QtGui.QWidget()
		textViewLayout = QtGui.QVBoxLayout()
		textView.setStyleSheet(""".QWidget { background-color: rgb(204, 221, 255); 
			border-radius: 6px;}""")
		textViewLayout.setContentsMargins(QtCore.QMargins(40,20,40,20))
		textViewLayout.addWidget(QtGui.QLabel("<b>START/END POINTS<b>"))
		textViewLayout.addWidget(self.selectionViewer)
		textViewLayout.addWidget(QtGui.QLabel("<b>FULL PATHS<b>"))
		textViewLayout.addWidget(self.pathViewer)
		textView.setLayout(textViewLayout)

		overallLayout.addWidget(leftSide)
		overallLayout.addWidget(textView)
		self.setLayout(overallLayout)

		addButton.clicked.connect(self.addSelection)
		clearButton.clicked.connect(self.clearAll)
		undoButton.clicked.connect(lambda: self.selectionViewer.undo())
		pathButton.clicked.connect(self.constructPaths)
		blockButton.clicked.connect(self.blockTransferLines)
		newButton.clicked.connect(self.addTransferLines)

	def addSelection(self):
		start = str(self.startPoints.currentText())
		end = str(self.endPoints.currentText())
		string = start + " --> " + end + "\n"

		self.paths.append([start,end])
		self.selectionViewer.append(string)

	def clearAll(self):
		self.selectionViewer.clear()
		self.pathViewer.clear()
		self.usedTransferLinesViewer.clear()
		self.newTransferLineViewer.clear()
		del self.paths[:]
		del self.blockedTransferLines[:]
		del self.temporaryTransferLines[:]
		self.transferLineListCopy = self.tracker.transferLineList[:]

	def constructPaths(self):
		#reset transfer line list back to original
		for x in itertools.permutations(self.paths):
			print x
		for pair in self.paths:
			myMap = Graph(self.componentListCopy,self.transferLineListCopy)
			path,transferLinePath = myMap.findShortestPath(pair[0],pair[1])
			self.pathViewer.append(str(path)+" via transfer lines "+ str(transferLinePath))
			#Now, remove transfer lines from the transfer line list copy to block off those transfer lines
			self.updateAvailableTransferLines(transferLinePath)

	def updateAvailableTransferLines(self,used_line_list):
		newTransferLineList = []
		for transferLine in self.transferLineListCopy:
			if (transferLine.name in used_line_list):
				print "removed transfer line " + transferLine.name
			else: 
				print "did NOT remove transfer line " + transferLine.name
				newTransferLineList.append(transferLine)
		self.transferLineListCopy = newTransferLineList
		print self.transferLineListCopy
		print self.tracker.transferLineList

	def blockTransferLines(self):
		current_blocked = self.usedTransferLines.currentText()
		self.usedTransferLinesViewer.append(current_blocked)
		newTransferLineList = []
		for transferLine in self.transferLineListCopy:
			if transferLine.name == current_blocked:
				print "manually removed " + transferLine.name
				self.blockedTransferLines.append(transferLine.name)
			else:
				newTransferLineList.append(transferLine)
		self.transferLineListCopy = newTransferLineList

	def addTransferLines(self):
		start = str(self.transferLineStart.currentText())
		end = str(self.transferLineEnd.currentText())
		self.newTransferLineViewer.append(start + " to " + end)
		newTransferLine = TransferLine(self.tracker, "TEMPORARY", start, end)
		self.transferLineListCopy.append(newTransferLine)
		self.temporaryTransferLines.append([start,end])
		print "new temporary connection between " + start + " and " + end

	def restoreSession(self,saveState): #save state is a dictionary containing...
		self.clearAll()
		self.restorePathSelections(saveState['paths'])
		self.restoreBlockedTransferLines(saveState['blocked'])
		self.restoreTemporaryTransferLines(saveState['temporary'])

	def restorePathSelections(self, paths):
		for pair in paths:
			start = pair[0]
			end = pair[1]
			string = start + " --> " + end + "\n"
			self.paths.append(pair)
			self.selectionViewer.append(string)

	def restoreBlockedTransferLines(self, blocked):
		newTransferLineList = []
		for transferLine in self.transferLineListCopy:
			if transferLine.name in blocked:
				print "restored block on " + transferLine.name
				self.blockedTransferLines.append(transferLine.name)
				self.usedTransferLinesViewer.append(transferLine.name)
			else:
				newTransferLineList.append(transferLine)
		self.transferLineListCopy = newTransferLineList

	def restoreTemporaryTransferLines(self, temporary):
		for pair in temporary:
			start = pair[0]
			end = pair[1]
			self.newTransferLineViewer.append(start + " to " + end)
			newTransferLine = TransferLine(self.tracker, "TEMPORARY", start, end)
			self.transferLineListCopy.append(newTransferLine)
			self.temporaryTransferLines.append(pair)
			print "restored temporary connection between " + start + " and " + end




