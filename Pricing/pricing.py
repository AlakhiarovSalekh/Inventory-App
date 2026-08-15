# -*- coding: utf-8 -*-
import os
from PyQt5 import QtGui, uic, QtWidgets
import pymysql
from Pricing.adv_search import adv_searchWindow

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/pricing.ui')
Form, Base = uic.loadUiType(main_path)


class pricingWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        # ------------------------------------------------------
        self.initial_pricing()
        self.lineEdit.setPlaceholderText("Master Search")
        self.pushButton.clicked.connect(self.regular_search)
        self.pushButton_4.clicked.connect(self.advance_search)
        self.pushButton_5.clicked.connect(self.update_price)
        self.lineEdit.setFocus()

        self.display_msg = QtWidgets.QMessageBox()
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)

        
        # -------------------------------------------------------

        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        # table widget on double clik wont be editable
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.tableWidget.setCurrentCell(0, 0)


        
    def initial_pricing(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM update_price")
        data = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row_number = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()
        self.tableWidget.setCurrentCell(0, 0)
    
    def update_price(self):
        selected_col = 1
        selected_row = self.tableWidget.currentItem().row()
        selected_item_id = self.tableWidget.item(selected_row,selected_col).text()
        updated_price = self.lineEdit_2.text()

        if(self.lineEdit_2.text() == "" or not updated_price.isdigit() or selected_item_id == 'None'):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Please Enter valid Price')
            self.display_msg.show()
        else:
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("UPDATE items SET item_price = %s where item_id = %s",(updated_price,selected_item_id))
            db.commit()
            db.close()
            
            self.display_msg.setWindowTitle('Information')
            self.display_msg.setText('Price Updated')
            self.display_msg.show()
            
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM update_price where item_id = %s",selected_item_id)
            data = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_number = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            db.close()
            self.initial_pricing()
        self.tableWidget.setCurrentCell(0, 0)

            
    def advance_search(self):
        #Dialog = QtWidgets.QDialog()
        self.ui = adv_searchWindow()
        #ui.setupUi(Dialog)
        # Dialog.show()
        # Dialog.exec_()
        self.ui.exec_()
        
        req_tupple = self.ui.returning
        #return tupple from search dialog aand pu condition in delete dialog by retuirning some value
        if(req_tupple[0] == 1):
            db=pymysql.connect("localhost","root","","ims")
            cursor=db.cursor()
            cursor.execute("select * from available_stock where category_name = %s and brand_name = %s",(req_tupple[2],req_tupple[3]))
            data=cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_no =self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_no)
                for column_no,data in enumerate(row_data):
                    self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
            db.close()
        elif(req_tupple[0] == 2):
            db=pymysql.connect("localhost","root","","ims")
            cursor=db.cursor()
            cursor.execute("select * from available_stock where item_name = %s and category_name = %s and brand_name = %s",(req_tupple[1],req_tupple[2],req_tupple[3]))
            data=cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_no =self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_no)
                for column_no,data in enumerate(row_data):
                    self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
            db.close()
        elif(req_tupple[0] == 3):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Please selcet a Brand or Category')
            self.display_msg.show()
        self.tableWidget.setCurrentCell(0, 0)
    
    def regular_search(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        tel = self.lineEdit.text()
        cursor.execute("SELECT * FROM update_price where item_name like %s or supp_name like %s or brand_name like %s or category_name like %s or item_id = %s",('%'+str(tel)+'%','%'+str(tel)+'%','%'+str(tel)+'%','%'+str(tel)+'%',tel))
        #print(tel)
        #print(type(tel))
        data = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row_number = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()
        self.tableWidget.setCurrentCell(0, 0)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    w = pricingWindow()
    w.show()
    sys.exit(app.exec_())
    
