#MainWidget.py

import sys
from PyQt4 import QtGui, QtCore
from Component import Component
from xmlParse import *


class MainWidget(QtGui.QGroupBox):
    
    def __init__(self,name):
        
        super(MainWidget, self).__init__(name)
        self.initUI(name)
        
    def initUI(self,name):
        
        parseXML(name)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        newCompList = []
        for i in range(len(componentList)):
            newCompList.append(Component(componentList[i][0],componentList[i][1]))
        
        del componentList[:]   
        """for an automated list of components"""
        # for k in range(0,5):
        # 	compList.append(Component("MANIFOLD "+str(k)))

        # for k in range(len(compList)):
        # 	grid.addWidget(compList[k], k, k+1)

        ##########################################

        """for individually added components --> MAKE DATA DRIVEN"""
        # newCompList.append(Component("manifold 1", (0,1)))
        # newCompList.append(Component("manifold 2", (2,1)))
        # newCompList.append(Component("manifold 3", (3,2)))

        for comp in newCompList:
            grid.addWidget(comp, comp.position[0], comp.position[1])

        self.setLayout(grid) 
        self.setGeometry(300, 300, 350, 300)   
        self.show()

