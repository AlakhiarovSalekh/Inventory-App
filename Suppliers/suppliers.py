import os
from PyQt5 import uic, QtWidgets,QtCore
# import rec_rc
import pymysql
from Suppliers.addSupplier import addSupplierDialog
from Suppliers.editSupplier import editSupplierDialog

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/supp.ui')
Form, Base = uic.loadUiType(main_path)


class supplierWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        
        # Fill table with suppliers
        self.populate_table()
        
        #delete selected suppliers
        self.Delete.clicked.connect(self.deletesup)
         
        
        # Search button code
        self.searchButton.clicked.connect(self.search_Table)
        
        # Show all Button
        self.showAllButton.clicked.connect(self.populate_table)
        
        # Add supplier Button
        self.actionShow_Supplier.triggered.connect(self.addSupplier)
        
        # Only rows will be selected and not individual
        # cells by this line
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        
        # This for loop sets behavior of the Header on stretching
        for i in range(5):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i,QtWidgets.QHeaderView.Stretch)
            
        self.tableWidget.horizontalHeader().setSectionResizeMode(5,QtWidgets.QHeaderView.ResizeToContents)


        # Table widget cant be edited there itself with double click
        # We pop up new dialog box for this purpose
        # Thats why all the triggers are deactivated
        # and only Double click will work
        
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.doubleClicked.connect(self.editSupplier)
        self.tableWidget.setSortingEnabled(True)
        # self.tableWidget.setCurrentCell(0, 0)

    def fun(self,i):
        print("index clicked is"+i)
        
    def editSupplier(self):
        for idx in self.tableWidget.selectionModel().selectedIndexes():
            row_number = idx.row() # gets row number
        self.editWindow = editSupplierDialog()
        id_val = self.tableWidget.item(row_number,0).text()
        self.editWindow.prefetchText(id_val)
        self.editWindow.exec_()
        self.populate_table()
        
    def addSupplier(self):
        self.addWindow = addSupplierDialog()
        self.addWindow.exec_()
        
        self.populate_table()

    def populate_table(self):
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query = "SELECT * from supplier"
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
                    item.setData(QtCore.Qt.EditRole,data)
                    
                    self.tableWidget.setItem(
                            row_no, column_no, item
                            )
            db.commit()
        except:
            db.rollback()
        db.close()

    def search_Table(self):
        searchVal = self.searchInput.text()
        db=pymysql.connect("localhost","root","","ims")
        cursor=db.cursor()
        query = '''SELECT * from supplier
        where supp_name like"'''+searchVal+'''%"
        or supp_id like"'''+searchVal+'''"
        '''
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
        
        
    def deletesup(self):
        row=int(self.tableWidget.currentRow())
        id = int(self.tableWidget.item(row,0).text())
        db=pymysql.connect("localhost","root","","ims")
        cursor=db.cursor()
        query = ''' delete from supplier where supp_id = %s'''
        
        try:
            cursor.execute(query,id)
            self.tableWidget.removeRow (row)
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

    w = supplierWindow()
    w.show()
    sys.exit(app.exec_())
