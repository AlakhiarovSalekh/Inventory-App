import os
from PyQt5 import QtGui, uic, QtWidgets
import pymysql

import math
d1  = -1
d2 = -1


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/contact.ui')
Form, Base = uic.loadUiType(main_path)

class contactWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        # ------------------------------------------------------
        self.intitial_read()
        self.pushButton_3.clicked.connect(self.search_by_mob)
        self.pushButton_2.clicked.connect(self.search_by_bill)
        self.calendarWidget.clicked.connect(self.showDate1)
        self.calendarWidget_2.clicked.connect(self.showDate2)
        self.pushButton.clicked.connect(self.search_by_date)
        self.pushButton_4.clicked.connect(self.refresh)
        # ------------------------------------------------------


        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        # table widget on double clik wont be editable
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.display_msg = QtWidgets.QMessageBox(self)
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)
        self.showDate1()
        self.showDate2()


    def refresh(self):
        self.intitial_read()
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def intitial_read(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        try:
            cursor.execute("SELECT * FROM customer_table LIMIT 100")
            data = cursor.fetchall()
            # print(data)
            self.tableWidget.setRowCount(0)

            for row_data in data:
                row_number = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)
            db.rollback()
        db.close()
        
    def search_by_mob(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        tel = self.lineEdit.text()
        if (tel.isdigit()):
            cursor.execute("SELECT * FROM customer_table where C_contact = %s",tel)
            data = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_number = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Please Enter a Number')
            self.display_msg.show()
        db.close()
        
    def search_by_bill(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        bill = self.lineEdit_2.text()
        if (bill.isdigit()):
            cursor.execute("SELECT * FROM customer_table where billing_id = %s",bill)
            data = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_number = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Please Enter a Number')
            self.display_msg.show()
        db.close()
        
    def search_by_date(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        d1 = self.selected_date1
        d2 = self.selected_date2

        if(d1==-1):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Please Select First Date')
            self.display_msg.show()
        elif(d2==-1):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Please Select Second Date')
            self.display_msg.show()
        else:
            cursor.execute("SELECT * FROM customer_table where billing_date Between %s And %s",(d1,d2))
            data = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_number = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()
        
    def showDate1(self):
        self.selected_date1=self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.label_5.setText(self.selected_date1)

    def showDate2(self):
        self.selected_date2=self.calendarWidget_2.selectedDate().toString("yyyy-MM-dd")
        self.label_6.setText(self.selected_date2)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    w = contactWindow()
    w.show()
    sys.exit(app.exec_())
    