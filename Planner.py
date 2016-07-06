#provides backbone structure of transfer line planner application 

import sys
from Component import Component
from MainWidget import MainWidget
from PyQt4 import QtGui,Qt


class Planner(QtGui.QMainWindow):
    
    def __init__(self):
        super(Planner, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        mainGrid = QtGui.QGridLayout()
        mainGrid.addWidget(MainWidget("floor1.xml"),0,0)
        mainGrid.addWidget(MainWidget("floor2.xml"),1,0)

        centralWidget = QtGui.QWidget()
        centralWidget.setLayout(mainGrid)

        #textEdit = QtGui.QTextEdit()
        # centralWidget = MainWidget()
        self.setCentralWidget(centralWidget)

        """Menubar actions i.e. add manufacturing floor plan to current window"""
        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        openAction = QtGui.QAction('Add Floor Plan', self)
        openAction.setShortcut('Ctrl+A')

        """Toolbar actions i.e. inspect and create transfer line plan"""
        compAction = QtGui.QAction("Component View", self)
        floorAction = QtGui.QAction("Floor View", self)
        constructAction = QtGui.QAction("Construct Map", self)
        startAction= QtGui.QAction("Add Start Point(s)", self)
        destinationAction= QtGui.QAction("Add End Point(s)", self)
        pathAction = QtGui.QAction("Construct Path", self)

        self.statusBar()

        """Construct menubar and toolbar"""
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(openAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(compAction)
        toolbar.addAction(floorAction)
        toolbar.addAction(constructAction)
        toolbar.addAction(startAction)
        toolbar.addAction(destinationAction)
        toolbar.addAction(pathAction)
        toolbar.setFloatable(True)
        
        """Configure application window"""
        self.setGeometry(200, 200, 900, 562)
        self.setWindowTitle('Transfer Line Planner')    
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Planner()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
