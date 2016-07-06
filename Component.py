#Component.py

import sys
from PyQt4 import QtGui,QtCore


class Component(QtGui.QLabel):
    
    def __init__(self, name, tuple_pos):
        super(Component, self).__init__()
        self.position = tuple_pos
        self.initUI(name)
        
    def initUI(self, name):
        
        self.setText(name)
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameShadow(QtGui.QFrame.Plain)
        self.setFixedSize(150,30)