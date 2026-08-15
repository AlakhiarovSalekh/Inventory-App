# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pricing.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from adv_search import Ui_Dialog_adv_search

class Ui_MainWindow(object):
    
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
            
    def advance_search(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_adv_search()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        req_tupple = ui.returning
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
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1089, 782)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.289773 rgba(191, 191, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
"    width: 150%;\n"
"height:20px;\n"
"    padding: 3%;\n"
"    background:#25D366;\n"
"    border-bottom: 2px solid #30C29E;\n"
"    border-top-style: none;\n"
"    border-right-style: none;\n"
"    border-left-style: none;    \n"
"    color: #fff;\n"
" border-radius: 10px;\n"
"font-size:20px;\n"
"color:purple;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: darkgreen;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 6, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 7, 7, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 1, 1, 6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 7, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("QLabel{\n"
"font-size:18px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 6)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(950, 550))
        self.tableWidget.setMaximumSize(QtCore.QSize(580, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("font: 11pt \"Arial\";\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(128)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(48)
        self.gridLayout.addWidget(self.tableWidget, 5, 1, 1, 6)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("QLabel{\n"
"font-size:28px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1089, 21))
        self.menubar.setObjectName("menubar")

        self.display_msg = QtWidgets.QMessageBox(MainWindow)
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)
        self.initial_pricing()
        self.lineEdit.setPlaceholderText("Master Search")
        self.pushButton.clicked.connect(self.regular_search)
        self.pushButton_4.clicked.connect(self.advance_search)
        self.pushButton_5.clicked.connect(self.update_price)



        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Master Search"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_5.setText(_translate("MainWindow", "Update Price"))
        self.pushButton_4.setText(_translate("MainWindow", "Advance Search"))
        self.label.setText(_translate("MainWindow", "Information of Prices"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Supplier Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item Id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Brand Name"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Quantity"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Pricing</span></p></body></html>"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Select Item Id to Update it\'s Price"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

