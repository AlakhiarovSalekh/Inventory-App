import os
from PyQt5 import uic, QtWidgets, QtCore
# import rec_rc
import pymysql
import datetime

# current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType("C:\Shubham\demo\demo\Orders\order.ui")


class orderWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
            
        self.populate_table()
        
        self.showAllButton.clicked.connect(self.populate_table)
        
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
        self.generateByIdButton.clicked.connect(self.search_Table)
        
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
            
        self.tableWidget.setSortingEnabled(True)
        
        self.tableWidget.doubleClicked.connect(self.showBillDetails)
        
        
    def search_Table(self):
        searchVal = self.searchByIdInput.text()
        db=pymysql.connect("localhost","root","","ims")
        cursor=db.cursor()
        query = '''SELECT b.billing_datetime, b.billing_id , c.C_name
        
        from billing as b, customer_info as c
        where b.billing_customer_id = c.C_id and
        (c.C_name like"{}%"
        or b.billing_id like"{}" )
        '''  .format(searchVal,searchVal)
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_no = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_no)
                for column_no, data in enumerate(row_data):
                    self.tableWidget.setItem(
                            row_no, column_no, QtWidgets.QTableWidgetItem(
                                    str(data)
                                    )
                            )
            db.commit()
        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)
            db.rollback()
        db.close()

        
    def showBillDetails(self):
        
        for idx in self.tableWidget.selectionModel().selectedIndexes():
            row_number = idx.row() # gets row number
        id_val = self.tableWidget.item(row_number,1).text()
        
        
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query = '''SELECT o.order_item_id
        from orders as o
        where o.order_billing_id = %s
        ''' % id_val
        try:
            cursor.execute(query)
            data = cursor.fetchall()
        except pymysql.InternalError as error:
            code, msg = error.args
            print("------->", code, msg)
            db.rollback()
        db.close()
        print(data)
        
    def populate_table(self):
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query = '''SELECT b.billing_datetime, b.billing_id , c.C_name
        
        from billing as b, customer_info as c
        where b.billing_customer_id = c.C_id
        '''
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in data:
                row_no = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_no)
                for column_no, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem()
                    
                    # Import QtCore to use this line
                    # This line will help sort numbers
                    if (type(data) == datetime.datetime):
                        data = str(data)
                    
                    item.setData(QtCore.Qt.EditRole,data)
                    
                    self.tableWidget.setItem(
                            row_no, column_no, item
                            )
            db.commit()
        except pymysql.InternalError as error:
            code, msg = error.args
            print("------->", code, msg)
            db.rollback()
        db.close()
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = orderWindow()
    w.show()
    sys.exit(app.exec_())
