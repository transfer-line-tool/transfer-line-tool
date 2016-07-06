import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
from Controller import *
from Tester import *

class ComponentButton(QtGui.QPushButton):

	def __init__(self,name,parent,component):
		
		super(ComponentButton,self).__init__(name, parent)
		self.myComponent = component
		self.myComponent.hide()

		#WILL NEED THIS LATER
		#self.tracker = self.myRoom.tracker

		#self.installEventFilter(self)
		# self.setMask(QtGui.QRegion(QtCore.QRect(self.x(),self.y()+50,200,100),QtGui.QRegion.Ellipse))
		# self.resize(200,200)
		self.clicked.connect(lambda: self.showComponent(parent))
		

		self.pressed.connect(self.pressedSlot)
		

		#self.clicked.connect(self.rightClick)
		#self.clicked.connect(clicked_slot)

	def pressedSlot(self):
		print "pressed!"

	def showComponent(self,parent):
		# newWindow = QtGui.QMainWindow()
		# newWindow.setCentralWidget(QtGui.QLabel("View of component"))
		# newWindow.show()
		self.setStyleSheet('QPushButton {color: Red; font-weight: bold;}')
		for button in parent.componentButtonList:
			if (button != self):
				button.setStyleSheet('QPushButton {color: rgb(0, 34, 102);}')
		#Controller().switchState(States.COMPONENT)
		
		for component in parent.componentObjectList:
			if (component != self.myComponent):
				component.hide()
			else:
				component.show()

	# def eventFilter(self, object, event):
	# 	if (event.type() == QtCore.QEvent.HoverMove):
	# 		print "you hovered!"
	# 		return True
	# 	else:
	# 		return False



