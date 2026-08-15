import os
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import QEvent
import re
import pymysql
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/editSupplier.ui')
Form, Base = uic.loadUiType(main_path)

class editSupplierDialog(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.updateButton.clicked.connect(self.fieldCheck)
        self.cancelButton.clicked.connect(self.close)
        
    def emailCheck(self,email):
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if match is None:
            return False
        return True
    
    def errorMsg(self , title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    
    def prefetchText(self, id_val):
        self.id_val = id_val
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query = '''SELECT * from supplier 
        where supp_id =%s '''%id_val
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            name = data[0][1]
            address = data[0][2]
            phone1 = data[0][3]
            phone2 = data[0][4]
            email = data[0][5]
            
            self.nameInput.setText(name)
            self.addressInput.setText(address)
            self.phoneNumber1Input.setText(str(phone1))
            self.phoneNumber2Input.setText(str(phone2))
            self.emailInput.setText(email)
            
            
            db.commit()
        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)
            db.rollback()
        db.close()
    
    def fieldCheck(self,id_val):
        name = self.nameInput.text()
        address = self.addressInput.text()
        phone1 = self.phoneNumber1Input.text()
        phone2 = self.phoneNumber2Input.text()
        email = self.emailInput.text()
        if(not self.emailCheck(email)):
            self.errorMsg("Warning","Email address is not valid")
            return
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query = '''
        Update supplier 
        set supp_name =%s, supp_address=%s, 
        supp_contact_1 = %s, supp_contact_2 = %s, supp_email = %s
        where supp_id =%s
        '''
        val = (name, address, phone1, phone2, email,self.id_val)
        try:
            cursor.execute(query,val)
            db.commit()
        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)
            db.rollback()
        db.close()
        self.close()
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    window = editSupplierDialog()
    
    # the below two lines will make window to come to front
    window.setWindowState(window.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
    window.activateWindow()
    # 
    
    window.show()
    sys.exit(app.exec_())
