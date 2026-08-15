import os
from PyQt5 import QtGui, uic, QtWidgets
from functools import partial
import pymysql


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/adv_search.ui')
Form, Base = uic.loadUiType(main_path)

class adv_searchWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        
        # ----------------------------------------------------------
        self.sel_category = self.comboBox.currentText()
        self.sel_brand = self.comboBox.currentText()
        self.sel_item = self.lineEdit.text()
        self.returning = (0,self.sel_item,self.sel_category,self.sel_brand)
        self.drop_menu()
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.accepted.connect(self.return_true)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.rejected.connect(self.return_false)
        self.display_msg = QtWidgets.QMessageBox(self)
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)
        # ---------------------------------------------------------
        
        
        
    def return_true(self):
        self.sel_category = self.comboBox.currentText()
        self.sel_brand = self.comboBox_2.currentText()
        self.sel_item = self.lineEdit.text()
        self.returning = (0,self.sel_item,self.sel_category,self.sel_brand)

        if(self.sel_category == '--Not Selected--'):
            self.returning = (3,self.sel_item,self.sel_category,self.sel_brand)
            
        elif(self.sel_brand == '--Not Selected--'):
            self.returning = (3,self.sel_item,self.sel_category,self.sel_brand)
            
        else:
            if(self.sel_item == ""):
                self.returning = (1,self.sel_item,self.sel_category,self.sel_brand)
            else:
                self.returning = (2,self.sel_item,self.sel_category,self.sel_brand)
                
    def return_false(self):
        self.returning = (0,self.sel_item,self.sel_category,self.sel_brand)
        
    def drop_menu(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("SELECT category_name FROM category group by category_name")
        data = cursor.fetchall()
        for category_name in data:
            self.comboBox.addItem(category_name[0])
        cursor.execute("SELECT brand_name FROM brand group by brand_name")
        data = cursor.fetchall()
        for brand_name in data:
            self.comboBox_2.addItem(brand_name[0])
        db.close()
        
        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = adv_searchWindow()
    w.show()
    sys.exit(app.exec_())
    