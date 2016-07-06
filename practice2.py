import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()

    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()      
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        btn1 = QtGui.QPushButton('MANIFOLD 1', self)
        btn1.setToolTip('This is a <b>manifold</b>')
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 50) 

        btn2 = QtGui.QPushButton('QUIT', self)
        btn2.setToolTip('This terminates application')
        btn2.resize(btn2.sizeHint())
        btn2.move(200, 50) 
        btn2.clicked.connect(self.closeEvent(QtGui.QCloseEvent))#QtCore.QCoreApplication.instance().quit)         
        
        self.setGeometry(300, 300, 450, 150)
        self.setWindowTitle('Example Layout')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()