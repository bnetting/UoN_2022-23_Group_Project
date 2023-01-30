self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget) 
self.webEngineView.load(QtCore.QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'\html\test.html')) 