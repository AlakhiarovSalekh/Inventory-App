# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Contact.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import math
d1  = -1
d2 = -1
class Ui_MainWindow(object):
    def main_window(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
        
    def intitial_read(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM customer_info LIMIT 100")
        data = cursor.fetchall()
        for row_data in data:
            row_number = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()
        
    def search_by_mob(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        tel = self.lineEdit.text()
        if (tel.isdigit()):
            cursor.execute("SELECT * FROM customer_info where C_contact = %s",tel)
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
            cursor.execute("SELECT * FROM customer_info where billing_id = %s",bill)
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
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1496, 982)
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
"    background: #43D1AF;\n"
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
"    background: Green;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.selected_date1=-1
        self.selected_date2=-1
        self.display_msg = QtWidgets.QMessageBox(MainWindow)
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)
        
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 15, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 13, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 9, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 13, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 21, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(700, 550))
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
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(129)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(48)
        self.gridLayout.addWidget(self.tableWidget, 5, 3, 23, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("QLabel{\n"
"font-size:18px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("QLabel{\n"
"font-size:28px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 21, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 16, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet("QLabel{\n"
"font-size:18px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 19, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("QLabel{\n"
"font-size:18px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 13, 5, 1, 1)
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget_2.sizePolicy().hasHeightForWidth())
        self.calendarWidget_2.setSizePolicy(sizePolicy)
        self.calendarWidget_2.setMinimumSize(QtCore.QSize(248, 180))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.gridLayout.addWidget(self.calendarWidget_2, 14, 5, 3, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 4, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 23, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 19, 6, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 14, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 23, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(150)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(150, 150))
        self.label_9.setMaximumSize(QtCore.QSize(200, 200))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/Contact/Contact/Bill.png"))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 16, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("QLabel{\n"
"font-size:18px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 5, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 2, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(250, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 14, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 23, 1, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QtCore.QSize(248, 180))
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 9, 5, 3, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 20, 5, 2, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 17, 5, 2, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 6, 6, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 13, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 16, 6, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 9, 6, 2, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 13, 6, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 23, 6, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 9, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setStyleSheet("QLabel{\n"
"font-size:18px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 15, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setStyleSheet("QLabel{\n"
"font-size:18px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem20, 0, 5, 5, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem21, 12, 5, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 6, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem23, 23, 4, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem24, 6, 2, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem25, 28, 3, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem26, 0, 1, 5, 1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem27, 14, 2, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem28, 21, 2, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem29, 16, 2, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem30, 15, 4, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem31, 23, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(150, 150))
        self.label_8.setMaximumSize(QtCore.QSize(150, 150))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/Contact/Contact/contact.png"))
        self.label_8.setObjectName("label_8")


        self.intitial_read()
        self.pushButton_3.clicked.connect(self.search_by_mob)
        self.pushButton_2.clicked.connect(self.search_by_bill)
        self.calendarWidget.clicked.connect(self.showDate1)
        self.calendarWidget_2.clicked.connect(self.showDate2)
        self.pushButton.clicked.connect(self.search_by_date)

        
        self.gridLayout.addWidget(self.label_8, 9, 1, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem32, 26, 5, 3, 1)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem33, 26, 1, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1496, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bill Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Bill Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Customer Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Address"))
        self.label_2.setText(_translate("MainWindow", "Information of table"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Customer Information</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "To Date 2"))
        self.label_5.setText(_translate("MainWindow", "From Date 1"))
        self.pushButton.setText(_translate("MainWindow", "Serach"))
        self.label_4.setText(_translate("MainWindow", "Search by Date"))
        self.pushButton_3.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.label_7.setText(_translate("MainWindow", "Search by Bill ID"))
        self.label_3.setText(_translate("MainWindow", "Search by Contact"))
        
    

import contact_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

