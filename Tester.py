import sys
#from Component import Component
from Plant import *
from PyQt4 import QtGui,Qt,QtCore,QtWebKit
from PyQt4.QtCore import pyqtSlot
from Tracker import *
from ListView import *
#from MapView import *
from PathAdder import *
#from pyqtgraph.flowchart import Flowchart
import WebPluginFactory
from Dijsktra import *
from PyQt4.QtWebKit import QWebView, QWebSettings
import pickle
import gc

def enum(**enums):
    return type('Enum',(), enums)

States = enum(FLOOR=1,ROOM=2,COMPONENT=3)
global CENTRAL_WIDGET_STATE

class Tester(QtGui.QMainWindow):
    
    def __init__(self):
        super(Tester, self).__init__()
        self.initUI()
        
    def initUI(self):               
        
        CENTRAL_WIDGET_STATE = 1
        #######################################
        
        self.tracker = Tracker(self)
        self.tracker.valueUpdated.connect(self.changeitup)
        #######################################

        #self.widgetDictionary = {}
        #######################################

        centralWidget1 = Plant("Plant 1", self.tracker)
        
        self.tracker.initTransferLines()
        self.tracker.addLinks()
        self.tracker.addNeighborButtonMessages()

        centralWidget2 = ListView(self.tracker)#QtGui.QLabel("LIST VIEW") #replace with list view object

        #centralWidget3 = MapView(self, self.tracker)

        centralWidget4 = PathAdder(self, self.tracker)
        #centralWidget3 = Flowchart(terminals={'1':{'io': 'in'},'2':{'io': 'out'}, '3':{'io': 'out'}})#MapView(self, self.tracker)

        centralWidget5 = QWebView()
        centralWidget5.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        centralWidget5.show()
        #centralWidget5.load(QtCore.QUrl('http://dafk.net/what/'))

        self.widgetManager = QtGui.QStackedWidget()
        self.widgetManager.addWidget(centralWidget1)
        self.widgetManager.addWidget(centralWidget2)
        #self.widgetManager.addWidget(centralWidget3)
        self.widgetManager.addWidget(centralWidget4)
        self.widgetManager.addWidget(centralWidget5)
        #self.widgetManager.addWidget(centralWidget3.chartGraphicsItem().getViewWidget())

        #self.widgetDictionary["FLOOR"] = centralWidget
        self.setCentralWidget(self.widgetManager)

        #transferLineMap = Graph(self.tracker)
        #transferLineMap.findShortestPath("M-3-1","M-5-2")
        
        """Menubar actions i.e. add manufacturing floor plan to current window"""
        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        openAction = QtGui.QAction('Add Floor Plan', self)
        openAction.setShortcut('Ctrl+A')

        saveAction = QtGui.QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.save)

        restoreSessionAction = QtGui.QAction('Restore Session', self)
        restoreSessionAction.triggered.connect(self.restore)

        """Toolbar actions i.e. inspect and create transfer line plan"""
        listAction = QtGui.QAction("List View", self)
        listAction.setShortcut('Ctrl+L')
        listAction.triggered.connect(lambda: self.switchToView(1))

        floorAction = QtGui.QAction("Floor View", self)
        floorAction.setShortcut('Ctrl+F')
        floorAction.triggered.connect(lambda: self.switchToView(0))

        # mapAction = QtGui.QAction("Map View", self)
        # mapAction.triggered.connect(lambda: self.switchToView(2))

        pathAction= QtGui.QAction("Add Path", self)
        pathAction.triggered.connect(lambda: self.switchToView(2))

        mapAction= QtGui.QAction("Show Map", self)
        mapAction.triggered.connect(lambda: self.switchToView(3))

        #destinationAction= QtGui.QAction("Add End Point(s)", self)
        #pathAction = QtGui.QAction("Construct Path", self)

        self.statusBar()

        """Construct menubar and toolbar"""
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(restoreSessionAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(floorAction)
        toolbar.addAction(listAction)
        toolbar.addAction(mapAction)
        toolbar.addAction(pathAction)
        #toolbar.addAction(destinationAction)
        #toolbar.addAction(pathAction)
        toolbar.setFloatable(True)
        
        """Configure application window"""
        self.setGeometry(100, 0, 1100, 676)
        self.setWindowTitle('Transfer Line Planner')    
        self.show()
        gc.collect()
        print gc.garbage
    
    def changeitup(self):
        #self.setCentralWidget(QtGui.QLabel("It works. Hurray!"))
        print "changed"

    def eventFilter(self, object, event):
        if (event.type() == QtCore.QEvent.MouseButtonDblClick):
            print "you double pressed"
            global newMain
            newMain = QtGui.QMainWindow()
            newMain.setGeometry(250,250,500,300)
            newMain.show()

            return True
        else:
            return False

    def switchToView(self,index):
        self.widgetManager.setCurrentIndex(index)

    def save(self):
        
        inputDialog, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','enter file name: ')
        print str(inputDialog)

        print "we saved, fam"
        with open(inputDialog,'wb') as s:
            saveState = {'paths': self.widgetManager.widget(2).paths, 
            'blocked': self.widgetManager.widget(2).blockedTransferLines, 
            'temporary': self.widgetManager.widget(2).temporaryTransferLines}
            pickle.dump(saveState,s)

    def restore(self):
        
        saveFileName = QtGui.QFileDialog.getOpenFileName(self, 'Open file','/home')
        print "we openin' that, nephew"
        #add file dialog to select appropriate saveState
        with open(saveFileName,'rb') as s:
            saveState = pickle.load(s)
            self.widgetManager.widget(2).restoreSession(saveState)
        
def main():

    app = QtGui.QApplication(sys.argv)
    ex = Tester()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    
