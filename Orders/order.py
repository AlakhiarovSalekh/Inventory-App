import os
from PyQt5 import uic, QtWidgets, QtCore
# import rec_rc
import pymysql
import datetime
from Orders.orderDetails import orderDetails



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/order.ui')
Form, Base = uic.loadUiType(main_path)

class orderWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
            
        self.populate_table()
        
        self.showAllButton.clicked.connect(self.populate_table)
        
        self.generateByDateResult.clicked.connect(self.date)
        
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
        
        self.ord = orderDetails()
        id_val = self.tableWidget.item(row_number,1).text()
        self.ord.details(id_val)
        self.ord.exec_()
        
        
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
        
    def date(self):
        start = self.startDate.date()
        temp = QDate(start.year(),start.month(),start.day())
        asd = QDateTime(temp)
        start1 = asd.toPyDateTime()

        end = self.endDate.date()
        temp1 = QDate(end.year(),end.month(),end.day())
        if(start == end):
           temp1 = temp1.addDays(1)
           print(temp1)
        asd1 = QDateTime(temp1)
        end1 = asd1.toPyDateTime()
        
        
        
        db = pymysql.connect("localhost","root","","ims" )
        cursor=db.cursor()
        query = '''SELECT b.billing_datetime, b.billing_id ,c.C_name from billing as b, 
        customer_info as c where billing_datetime Between %s And %s and b.billing_customer_id = c.C_id'''
        try:
            cursor.execute(query,(start1,end1))
            data = cursor.fetchall()
            print(data)
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

        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = orderWindow()
    w.show()
    sys.exit(app.exec_())
