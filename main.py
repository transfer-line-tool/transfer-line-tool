from WebPluginFactory import *
from Tester import *

def main():

    html = \
        """<html>
        <head>
        <title>Transfer Line Planner (Web Plugin)</title>
        </head>

        <body>
        <h1>Transfer Line Planner (Web Plugin)</h1>
        <object type="x-pyqt/widget" width="900" height="600"></object>
        <p>bischoj3@gene.com.</p>
        </body>
        </html>
        """

    app = QtGui.QApplication(sys.argv)
    QtWebKit.QWebSettings.globalSettings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
    view = QtWebKit.QWebView()
    ex = WebPluginFactory.WebPluginFactory()
    view.page().setPluginFactory(ex)
    view.setHtml(html)
    view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
