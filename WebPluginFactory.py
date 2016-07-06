import Tester
from PyQt4 import QtWebKit

class WebPluginFactory(QtWebKit.QWebPluginFactory):

    def __init__(self, parent = None):
        QtWebKit.QWebPluginFactory.__init__(self, parent)
    
    def create(self, mimeType, url, names, values):
        if mimeType == "x-pyqt/widget":
            return Tester.Tester()
    
    def plugins(self):
        plugin = QtWebKit.QWebPluginFactory.Plugin()
        plugin.name = "PyQt Widget"
        plugin.description = "An example Web plugin written with PyQt."
        mimeType = QtWebKit.QWebPluginFactory.MimeType()
        mimeType.name = "x-pyqt/widget"
        mimeType.description = "PyQt widget"
        mimeType.fileExtensions = []
        plugin.mimeTypes = [mimeType]
        print "plugins"
        return [plugin]