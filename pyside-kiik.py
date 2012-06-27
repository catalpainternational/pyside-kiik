import sys
import os

from PySide import QtCore, QtGui, QtWebKit, QtNetwork


class Browser(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.web = QtWebKit.QWebView()
        self.web.page().setForwardUnsupportedContent(True)
        self.web.page().unsupportedContent.connect(self.download)

        self.manager = QtNetwork.QNetworkAccessManager()
        self.manager.finished.connect(self.finished)

    def download(self, reply):
        self.request = QtNetwork.QNetworkRequest(reply.url())
        self.reply = self.manager.get(self.request)

    def finished(self):
        path = os.path.expanduser(os.path.join('~', unicode(self.reply.url().path()).split('/')[-1]))
        destination = QtGui.QFileDialog.getSaveFileName(self, "Save", path)
        if destination:
            url = reply.url().toString()
            downloaded_file = urllib.urlretrieve(url)[0]
            os.rename(downloaded_file, destination)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    browser = Browser()
    browser.web.load(QtCore.QUrl('http://127.0.0.1:8000'))
    browser.web.show()

    sys.exit(app.exec_())
