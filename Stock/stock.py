import os
from PyQt5 import QtGui, uic, QtWidgets,QtCore
from functools import partial
import pymysql
from Stock.adv_search import adv_searchWindow
from Stock.stock_add import stock_addWindow
from Stock.stock_delete import stock_deleteWindow


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/stock.ui')
Form, Base = uic.loadUiType(main_path)

class stockWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        # -------------------------------------------
        self.pushButton_4.setFocus()
        self.pushButton.clicked.connect(self.regular_search)
        self.pushButton_2.clicked.connect(self.delete_item)
        self.pushButton_3.clicked.connect(self.add_item)
        self.initial_stock()
        self.pushButton_4.clicked.connect(self.advance_search)
        self.pushButton_5.clicked.connect(self.refresh_table)
        self.pushButton_6.clicked.connect(self.update_quantity)
        self.display_msg = QtWidgets.QMessageBox()
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)

        self.tableWidget.setCurrentCell(0, 0)

        # -------------------------------------------
        
    def regular_search(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        tel = self.lineEdit.text()
        cursor.execute("SELECT * FROM available_stock where item_name = %s or supp_name = %s or brand_name = %s or category_name = %s or item_id = %s",(tel,tel,tel,tel,tel))
        data = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row_number = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()
        self.tableWidget.setCurrentCell(0, 0)

    def advance_search(self):
        # Dialog = QtWidgets.QDialog()
        self.ui = adv_searchWindow()
        # ui.setupUi(Dialog)
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

    def update_quantity(self):
        selected_col = 1
        selected_row = self.tableWidget.currentItem().row()
        selected_item_id = self.tableWidget.item(selected_row,selected_col).text()
        updated_quantity = self.lineEdit_2.text()

        if(self.lineEdit_2.text() == "" or not updated_quantity.isdigit() or selected_item_id == 'None'):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Please Enter valid Quantity')
            self.display_msg.show()
        else:
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("UPDATE stock SET stock_quantity = %s where stock_item_id=%s",(updated_quantity,selected_item_id))
            db.commit()
            db.close()

            self.display_msg.setWindowTitle('Information')
            self.display_msg.setText('Quantity Updated')
            self.display_msg.show()

            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM available_stock where item_id = %s",selected_item_id)
            data = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_number = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            db.close()
        self.tableWidget.setCurrentCell(0, 0)

    def add_item(self):
        # Dialog = QtWidgets.QDialog()
        self.ui = stock_addWindow()
        # ui.setupUi(Dialog)
        # Dialog.show()
        self.ui.exec_()
        req_tupple = self.ui.returning
        #print(req_tupple)
        if(req_tupple[0] == 2):
            #error
            if(req_tupple[1] == 1):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Select Supplier Name')
                self.display_msg.show()
            elif(req_tupple[1]==2):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Select Category or Enter New if not Exists')
                self.display_msg.show()
            elif(req_tupple[1]==3):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Select EITHER Existing Category or New Category')
                self.display_msg.show()
            elif(req_tupple[1]==4):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Select Brand or Enter New if not Exists')
                self.display_msg.show()
            elif(req_tupple[1]==5):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Select EITHER Existing Brand or New Brand')
                self.display_msg.show()
            elif(req_tupple[1]==6):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Enter valid Item Name')
                self.display_msg.show()
            elif(req_tupple[1]==7):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Enter valid Price')
                self.display_msg.show()
            elif(req_tupple[1]==8):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Please Enter valid Quantity')
                self.display_msg.show()
            elif(req_tupple[1]==9):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Category name already Exists')
                self.display_msg.show()
            elif(req_tupple[1]==10):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Brand name already Exists')
                self.display_msg.show()
            elif(req_tupple[1]==11):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText('Item already Exist')
                self.display_msg.show()
                  
        if(req_tupple[0] == 1):
            #item added
            req_item = str(req_tupple[2])
            req_category = str(req_tupple[3])
            req_brand = str(req_tupple[4])
            req_item_desc = str(req_tupple[5])
            req_price = int(req_tupple[6])
            req_quantity = int(req_tupple[7])
            req_supplier= str(req_tupple[8])
            if(req_tupple[1] == 1):
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into category (category_name) values (%s)",req_category)
                db.commit()
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into brand (brand_name) values (%s)",req_brand)
                db.commit()
                db.close()


                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select category_id from category where category_name = %s",req_category)
                data = cursor.fetchone()
                req_category_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select brand_id from brand where brand_name = %s",req_brand)
                data = cursor.fetchone()
                req_brand_id =  data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select supp_id from supplier where supp_name = %s ",req_supplier)
                data = cursor.fetchone()
                req_supp_id = data[0]
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into items (item_category_id,item_brand_id,item_name,item_desc,item_price) values (%s, %s, %s ,%s,%s)",(req_category_id,req_brand_id,req_item,req_item_desc,req_price))        
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select item_id from items where item_name = %s ",req_item)
                data = cursor.fetchone()
                req_item_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into stock (stock_item_id,stock_quantity,stock_sup_id) values (%s, %s, %s)",(req_item_id,req_quantity,req_supp_id))
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select * from available_stock where item_id = %s",req_item_id)
                data=cursor.fetchall()
                self.tableWidget.setRowCount(0)
                for row_data in data:
                    row_no = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_no)
                    for column_no,data in enumerate(row_data):
                        self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
                db.close()
                self.display_msg.setWindowTitle('Information')
                self.display_msg.setText('Item Added Successfully')
                self.display_msg.show()

            elif(req_tupple[1] == 2):
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into category (category_name) values (%s)",req_category)
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select category_id from category where category_name = %s",req_category)
                data = cursor.fetchone()
                req_category_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select brand_id from brand where brand_name = %s",req_brand)
                data = cursor.fetchone()
                req_brand_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select supp_id from supplier where supp_name = %s ",req_supplier)
                data = cursor.fetchone()
                req_supp_id = data[0]
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into items (item_category_id,item_brand_id,item_name,item_desc,item_price) values (%s, %s, %s ,%s,%s)",(req_category_id,req_brand_id,req_item,req_item_desc,req_price))        
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select item_id from items where item_name = %s ",req_item)
                data = cursor.fetchone()
                req_item_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into stock (stock_item_id,stock_quantity,stock_sup_id) values (%s, %s, %s)",(req_item_id,req_quantity,req_supp_id))
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select * from available_stock where item_id = %s",req_item_id)
                data=cursor.fetchall()
                self.tableWidget.setRowCount(0)
                for row_data in data:
                    row_no = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_no)
                    for column_no,data in enumerate(row_data):
                        self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
                db.close()
                self.display_msg.setWindowTitle('Information')
                self.display_msg.setText('Item Added Successfully')
                self.display_msg.show()
                
                
            elif(req_tupple[1] == 3):
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into brand (brand_name) values (%s)",req_brand)
                db.commit()
                db.close()


                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select category_id from category where category_name = %s",req_category)
                data = cursor.fetchone()
                req_category_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select brand_id from brand where brand_name = %s",req_brand)
                data = cursor.fetchone()
                req_brand_id =  data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select supp_id from supplier where supp_name = %s ",req_supplier)
                data = cursor.fetchone()
                req_supp_id = data[0]
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into items (item_category_id,item_brand_id,item_name,item_desc,item_price) values (%s, %s, %s ,%s,%s)",(req_category_id,req_brand_id,req_item,req_item_desc,req_price))        
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select item_id from items where item_name = %s ",req_item)
                data = cursor.fetchone()
                req_item_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into stock (stock_item_id,stock_quantity,stock_sup_id) values (%s, %s, %s)",(req_item_id,req_quantity,req_supp_id))
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select * from available_stock where item_id = %s",req_item_id)
                data=cursor.fetchall()
                self.tableWidget.setRowCount(0)
                for row_data in data:
                    row_no = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_no)
                    for column_no,data in enumerate(row_data):
                        self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
                db.close()
                self.display_msg.setWindowTitle('Information')
                self.display_msg.setText('Item Added Successfully')
                self.display_msg.show()

            elif(req_tupple[1] == 4):
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select category_id from category where category_name = %s",req_category)
                data = cursor.fetchone()
                req_category_id = data[0]
                #print(req_category_id)
                #print(type(req_category_id))
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select brand_id from brand where brand_name = %s",req_brand)
                data = cursor.fetchone()
                req_brand_id =  data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select supp_id from supplier where supp_name = %s ",req_supplier)
                data = cursor.fetchone()
                req_supp_id = data[0]
                db.close()
                
                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into items (item_category_id,item_brand_id,item_name,item_desc,item_price) values (%s, %s, %s ,%s,%s)",(req_category_id,req_brand_id,req_item,req_item_desc,req_price))        
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select item_id from items where item_name = %s ",req_item)
                data = cursor.fetchone()
                req_item_id = data[0]
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("insert into stock (stock_item_id,stock_quantity,stock_sup_id) values (%s, %s, %s)",(req_item_id,req_quantity,req_supp_id))
                db.commit()
                db.close()

                db = pymysql.connect("localhost","root","","ims" )
                cursor = db.cursor()
                cursor.execute("select * from available_stock where item_id = %s",req_item_id)
                data=cursor.fetchall()
                self.tableWidget.setRowCount(0)
                for row_data in data:
                    row_no = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_no)
                    for column_no,data in enumerate(row_data):
                        self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
                db.close()
                self.display_msg.setWindowTitle('Information')
                self.display_msg.setText('Item Added Successfully')
                self.display_msg.show()
        self.tableWidget.setCurrentCell(0, 0)
                

    def delete_item(self):
        selected_col = 1
        selected_row = self.tableWidget.currentItem().row()
        selected_item_id = self.tableWidget.item(selected_row,selected_col).text()
        # Dialog = QtWidgets.QDialog()
        self.ui = stock_deleteWindow()
        # ui.setupUi(Dialog)
        # Dialog.show()
        self.ui.exec_()
        got_status = self.ui.set_status
        if(got_status==1):
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("delete from stock where stock_item_id = %s",selected_item_id)
            db.commit()
            db.close()
            
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("delete from items where item_id = %s",selected_item_id)
            db.commit()
            db.close()
            self.display_msg.setWindowTitle('Information')
            self.display_msg.setText('Delete Successfull')
            self.display_msg.show()
            self.initial_stock()
        elif(got_status==-1):
            self.display_msg.setWindowTitle('Error')
            self.display_msg.setText('Please Select Category and Brand')
            self.display_msg.show()
        self.tableWidget.setCurrentCell(0, 0)

    def refresh_table(self):
        self.initial_stock()
        self.lineEdit.clear()
        self.lineEdit.clear()
        self.tableWidget.setCurrentCell(0, 0)

    def initial_stock(self):
        db=pymysql.connect("localhost","root","","ims")
        cursor=db.cursor()
        query = "SELECT * from available_stock"
        try:
            cursor.execute(query)
            data=cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_no =self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_no)
                for column_no,data in enumerate(row_data):
                    self.tableWidget.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))

            db.commit()
        except:
            db.rollback()
        db.close()
        self.tableWidget.setCurrentCell(0, 0)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = stockWindow()
    w.show()
    sys.exit(app.exec_())
    