import os
from PyQt5 import QtGui, uic, QtWidgets, QtCore


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/stock_delete.ui')
Form, Base = uic.loadUiType(main_path)

class stock_deleteWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        
        # ----------------------------------------------------------
        self.set_status = 0
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.accepted.connect(self.return_true)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.rejected.connect(self.return_false)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.buttonBox, self.buttonBox)
        # ----------------------------------------------------------
    def return_true(self):
        self.set_status = 1
    
    def return_false(self):
        self.set_status = 0
        
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = stock_deleteWindow()
    w.show()
    sys.exit(app.exec_())
    