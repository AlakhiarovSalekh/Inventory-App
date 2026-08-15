import os
from PyQt5 import QtGui, uic, QtWidgets
from functools import partial
import rec_rc


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASShome
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/homepage.ui')
Form, Base = uic.loadUiType(main_path)
class homepageWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        
        # ----------------------------------------------------------
        # ----------------------------------------------------------

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = homepageWindow()
    w.show()
    sys.exit(app.exec_())
    