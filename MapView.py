import pyqtgraph as pg
import numpy
import random
from PyQt4 import QtCore,QtGui

class MapView(pg.GraphicsLayoutWidget):

	def __init__(self, mainwindow, tracker):
		pg.setConfigOption('background', 'w')
		super(MapView,self).__init__()
		self.tracker = tracker

		self.v = self.addViewBox()
		item = pg.GraphItem()
		self.v.addItem(item)

		pos = self.setPositions()
		adj = self.setConnections()
		symbol = self.setSymbols()
		#path.addText(0,0,QtGui.QFont('Helvetica'),"Node")
		#path.setPen(QPen(QColor(0,0,0)))

		item.setData(pos=pos,
			adj=adj,size=50,symbol=symbol,
			symbolBrush=pg.mkBrush('k'),symbolPen=pg.mkPen('w')) #[[0,0],[10,0],[0,10],[10,10],[5,5],[15,5]]
		#numpy.array([[0,1],[1,3],[3,2],[2,1],[4,5],[3,5]])		
		#item.clicked.connect(self.printMessage)
		#self.data.sigClicked.connect(self.printMessage)
		#self.scene().sigMouseMoved.connect(self.mouseMoved)

	def mouseMoved(self, evt):
		pos = evt
		print 'mouse moved'
		if (self.sceneBoundingRect().contains(pos)):
			print "first if"
			mousePoint = self.vb.mapSceneToView(pos)
			index = int(mousePoint.x())
			label.setText("<span style='font-size: 12pt'>x=%0.1f, <span style='color: red'>y1=%0.1f</span>" % (mousePoint.x(), y[index], data2[index]))

	def setPositions(self):
		numberOfComponents = len(self.tracker.finalComponentList)
		posList = []
		for k in range(0,numberOfComponents):
			pos = [random.randint(0,numberOfComponents**3),random.randint(0,numberOfComponents**3)]
			posList.append(pos)
		return numpy.array(posList)

	def setConnections(self):
		compList = self.tracker.finalComponentList
		connectionList = []
		for k in range(len(compList)):
			compList[k].index = k
		for k in range(len(compList)):
			for j in range(len(compList[k].neighbors)):
				myIndex = compList[k].index
				myNeighborIndex = compList[k].neighbors[j].index
				connectionList.append([myIndex,myNeighborIndex])
		return numpy.array(connectionList)

	def setSymbols(self):
		symbolList = []
		for component in self.tracker.finalComponentList:
			path = QtGui.QPainterPath()
			path.addText(0,0,QtGui.QFont('SansSerif'),str(component.title()))
			br = path.boundingRect()
			scale = min(1. / br.width(), 1. / br.height())
			tr = QtGui.QTransform()
			tr.scale(scale*.9, scale*.9)
			tr.translate(-br.x() - br.width()/2., -br.y() - br.height()/2.)
			path = tr.map(path)
			path.addEllipse(0-.5,0-.5,1,1)
			symbolList.append(path)
		return symbolList

	def printMessage(self):
		print 'data point clicked!'

