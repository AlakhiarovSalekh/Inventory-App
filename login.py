import os
from PyQt5 import QtGui, uic, QtWidgets
import rec_rc,pymysql
import main

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/login.ui')
Form, Base = uic.loadUiType(main_path)

class loginWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        
        # Setting Focus on username Input
        self.usernameInput.setFocus()

        # Login Button Pressed Event
        self.loginButton.clicked.connect(self.authenticate)
        
        # Enter button press on Line Edit event
        self.passwordInput.returnPressed.connect(self.loginButton.click)
        self.usernameInput.returnPressed.connect(self.loginButton.click)
        
        # Enter Button pressed on Login button
        self.loginButton.setAutoDefault(True)
        
        # Make password invisible
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.display_msg = QtWidgets.QMessageBox()
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)

    def authenticate(self):
        self.username = self.usernameInput.text()
        self.password = self.passwordInput.text()
        usern = self.username
        lis = ()
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        cursor.execute("SELECT user_id  FROM user_info where user_name = %s  and user_pass =%s",(self.username,self.password))
        data = cursor.fetchall()
        if(data == lis):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Incorrect Username or Password')
            self.display_msg.show()
        else:
            self.homepageopen()
            self.homepage.fetchUsername(self.username)


    def homepageopen(self):
        try:
            self.homepage = main.MainWidget()
            self.homepage.show()
            self.close()
        except pymysql.OperationalError:
            self.errorMsg("Warning","You are not connected to the server")

    def errorMsg(self , title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = loginWindow()
    w.show()
    sys.exit(app.exec_())
    