
import os
from PyQt5 import QtGui, uic, QtWidgets
from functools import partial
import rec_rc
import pymysql

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/orderDetails.ui')
Form, Base = uic.loadUiType(main_path)

class orderDetails(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        
        self.orders.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.orders.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.orders.doubleClicked.connect(self.details)
        
        
    def details(self,id_val):
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query = '''SELECT it.item_name,o.order_quantity,o.order_price
        from orders as o,items as it
        where o.order_billing_id = %s and o.order_item_id = it.item_id
        ''' % id_val
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            
            self.orders.setRowCount(0)
            for row_data in data:
                row_no = self.orders.rowCount()
                self.orders.insertRow(row_no)
                for column_no, data in enumerate(row_data):
                    self.orders.setItem(
                            row_no, column_no, QtWidgets.QTableWidgetItem(
                                    str(data)
                                    )
                            )
            db.commit()
        except pymysql.InternalError as error:
            code, msg = error.args
            print("------->", code, msg)
            db.rollback()
        db.close()
        
        sum=0
        for row in range(self.orders.rowCount()):
              net=int(self.orders.item(row,2).text())
              sum=sum+net
        
        self.total.setText(str(sum))
        
        
        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = orderDetails()
    w.show()
    sys.exit(app.exec_())
    