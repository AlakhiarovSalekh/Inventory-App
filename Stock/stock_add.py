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


main_path = resource_path('ui/stock_add.ui')
Form, Base = uic.loadUiType(main_path)

class stock_addWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        # ----------------------------------------------------------
        self.returning = (0,'hi')
        self.drop_menu()
        self.pushButton_3.clicked.connect(self.reset_all)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.accepted.connect(self.check_input)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.rejected.connect(self.return_false)
        # ----------------------------------------------------------
    
    def drop_menu(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        #supplier list 
        cursor.execute("SELECT supp_name FROM supplier group by supp_name")
        data = cursor.fetchall()
        for supp_name in data:
            self.comboBox.addItem(supp_name[0])
        db.close()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        #category list
        cursor.execute("SELECT category_name FROM category group by category_name")
        data = cursor.fetchall()
        for category_name in data:
            self.comboBox_2.addItem(category_name[0])
        db.close()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        #brand list
        cursor.execute("SELECT brand_name FROM brand group by brand_name")
        data = cursor.fetchall()
        for brand_name in data:
            self.comboBox_3.addItem(brand_name[0])
        db.close()
    def return_false(self):
        self.returning = (0,'hi')
        #close case 2

    def check_input(self):
        sel_supplier = self.comboBox.currentText()
        sel_category = self.comboBox_2.currentText()
        sel_new_category = self.lineEdit_2.text()
        sel_brand = self.comboBox_3.currentText()
        sel_new_brand = self.lineEdit_3.text()
        sel_item = self.lineEdit_5.text()
        sel_item_desc = self.lineEdit_4.text()
        sel_price = self.lineEdit_6.text()
        sel_quantity = self.lineEdit_7.text()

        

        if(sel_supplier == '--Not Selected--'):
            self.returning = (2,1,'hi')
            
        elif(sel_category == '--Not Selected--' and sel_new_category == ""):
            self.returning = (2,2,'hi')
             
        elif(sel_category != '--Not Selected--' and sel_new_category != ""):
            self.returning = (2,3,'hi')
             
        elif(sel_brand == '--Not Selected--' and sel_new_brand == ""):
            self.returning = (2,4,'hi')
             
        elif(sel_brand != '--Not Selected--' and sel_new_brand != ""):
            self.returning = (2,5,'hi')
             
        elif(sel_item == ""):
            self.returning = (2,6,'hi')
             
        elif(sel_price == "" or not sel_price.isdigit()):
            self.returning = (2,7,'hi')
             
        elif(sel_quantity == "" or not sel_quantity.isdigit()):
            self.returning = (2,8,'hi')
             
            
        elif(not sel_new_category == "" and self.check_category()):
            self.returning = (2,9,'hi')
            
        elif(not sel_new_brand == "" and self.check_brand()):
            self.returning = (2,10,'hi')
            
        elif(not sel_item == "" and self.check_item()):
            self.returning = (2,11,'hi')

        else:
            if(sel_category == '--Not Selected--' and sel_brand == '--Not Selected--'):
                self.returning = (1,1,sel_item,sel_new_category,sel_new_brand,sel_item_desc,sel_price,sel_quantity,sel_supplier,'hi')
            elif(sel_category == '--Not Selected--' and not sel_brand == '--Not Selected--'):
                self.returning = (1,2,sel_item,sel_new_category,sel_brand,sel_item_desc,sel_price,sel_quantity,sel_supplier,'hi')
            elif(not sel_category == '--Not Selected--' and sel_brand == '--Not Selected--'):
                self.returning = (1,3,sel_item,sel_category,sel_new_brand,sel_item_desc,sel_price,sel_quantity,sel_supplier,'hi')
            elif(not sel_category == '--Not Selected--' and not sel_brand == '--Not Selected--'):
                self.returning = (1,4,sel_item,sel_category,sel_brand,sel_item_desc,sel_price,sel_quantity,sel_supplier,'hi')
                
    def check_category(self):
        sel_supplier = self.comboBox.currentText()
        sel_category = self.comboBox_2.currentText()
        sel_new_category = self.lineEdit_2.text()
        sel_brand = self.comboBox_3.currentText()
        sel_new_brand = self.lineEdit_3.text()
        sel_item = self.lineEdit_5.text()
        sel_item_desc = self.lineEdit_4.text()
        sel_price = self.lineEdit_6.text()
        sel_quantity = self.lineEdit_7.text()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        data = cursor.execute("select category_name from category where category_name = %s",sel_new_category)
        db.close()
        return(data)
    
    def check_brand(self):
        sel_supplier = self.comboBox.currentText()
        sel_category = self.comboBox_2.currentText()
        sel_new_category = self.lineEdit_2.text()
        sel_brand = self.comboBox_3.currentText()
        sel_new_brand = self.lineEdit_3.text()
        sel_item = self.lineEdit_5.text()
        sel_item_desc = self.lineEdit_4.text()
        sel_price = self.lineEdit_6.text()
        sel_quantity = self.lineEdit_7.text()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        data = cursor.execute("select brand_name from brand where brand_name = %s",sel_new_brand)
        db.close()
        return(data)
    
    def check_item(self):
        sel_supplier = self.comboBox.currentText()
        sel_category = self.comboBox_2.currentText()
        sel_new_category = self.lineEdit_2.text()
        sel_brand = self.comboBox_3.currentText()
        sel_new_brand = self.lineEdit_3.text()
        sel_item = self.lineEdit_5.text()
        sel_item_desc = self.lineEdit_4.text()
        sel_price = self.lineEdit_6.text()
        sel_quantity = self.lineEdit_7.text()
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        data = cursor.execute("select item_name from items where item_name = %s",sel_item)
        db.close()
        return(data)

    def add_item(self):
        sel_supplier = self.comboBox.currentText()
        sel_category = self.comboBox_2.currentText()
        sel_new_category = self.lineEdit_2.text()
        sel_brand = self.comboBox_3.currentText()
        sel_new_brand = self.lineEdit_3.text()
        sel_item = self.lineEdit_5.text()
        sel_item_desc = self.lineEdit_4.text()
        sel_price = self.lineEdit_6.text()
        sel_quantity = self.lineEdit_7.text()
        
        if(sel_category == '--Not Selected--'):
            req_category = sel_new_category
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("insert into category(category_name) values (%s)",self.lineEdit_2.text())
            db.commit()
            db.close()
        else:
            req_category = sel_category
        if(sel_brand == '--Not Selected--'):
            req_brand = sel_new_brand
            db = pymysql.connect("localhost","root","","ims" )
            cursor = db.cursor()
            cursor.execute("insert into brand(brand_name) values (%s)",self.lineEdit_3.text())
            db.commit()
            db.close()
        else:
            req_brand = sel_brand
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("select category_id from category where category_name = %s",req_category)
        data = cursor.fetchone()
        req_category_id = data[0]
        db.close()
        
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("select brand_id from brand where brand_name = '"+req_brand+"'")
        data = cursor.fetchone()
        req_brand_id =  data[0]
        db.close()

        
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("insert into items (item_category_id,item_brand_id,item_name,item_desc,item_price) values (%s, %s, %s ,%s,%s)",(req_category_id,req_brand_id,sel_item,sel_item_desc,sel_price))
        db.commit()
        db.close()
                       
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("select item_id from items where item_name = %s ",sel_item)
        data = cursor.fetchone()
        req_item_id = data[0]
        db.close()

        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("select supp_id from supplier where supp_name = %s ",sel_supplier)
        data = cursor.fetchone()
        req_supp_id = data[0]
        db.close()
        
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("insert into stock (stock_item_id,stock_quantity,stock_sup_id) values (%s, %s, %s)",(req_item_id,sel_quantity,req_supp_id))
        db.commit()
        db.close()
        
    def reset_all(self):
        self.lineEdit_2.setFocus()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = stock_addWindow()
    w.show()
    sys.exit(app.exec_())
    