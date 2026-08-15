# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Dialog_adv_search(object):
    
    def return_true(self):
        self.sel_category = self.comboBox.currentText()
        self.sel_brand = self.comboBox_2.currentText()
        self.sel_item = self.lineEdit.text()
        self.returning = (0,self.sel_item,self.sel_category,self.sel_brand)

        if(self.sel_category == '--Not Selected--'):
            self.returning = (3,self.sel_item,self.sel_category,self.sel_brand)
            
        elif(self.sel_brand == '--Not Selected--'):
            self.returning = (3,self.sel_item,self.sel_category,self.sel_brand)
            
        else:
            if(self.sel_item == ""):
                self.returning = (1,self.sel_item,self.sel_category,self.sel_brand)
            else:
                self.returning = (2,self.sel_item,self.sel_category,self.sel_brand)
                
    def return_false(self):
        self.returning = (0,self.sel_item,self.sel_category,self.sel_brand)
        
    def drop_menu(self):
        db = pymysql.connect("localhost","root","","ims" )
        cursor = db.cursor()
        cursor.execute("SELECT category_name FROM category group by category_name")
        data = cursor.fetchall()
        for category_name in data:
            self.comboBox.addItem(category_name[0])
        cursor.execute("SELECT brand_name FROM brand group by brand_name")
        data = cursor.fetchall()
        for brand_name in data:
            self.comboBox_2.addItem(brand_name[0])
        db.close()
        self.comboBox.activated.connect(self.combo_changed)
        
    def combo_changed(self):
      print(self.comboBox.currentText())
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(446, 376)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(446, 376))
        Dialog.setMaximumSize(QtCore.QSize(446, 376))
        Dialog.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.289773 rgba(191, 191, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
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
"\n"
"QLabel{\n"
"font-size:18px;\n"
"font-family:\"Times New Roman\";\n"
"font-weight: bold;\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 3)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 8, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 9, 0, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 8, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QtCore.QSize(300, 28))
        self.comboBox_2.setMaximumSize(QtCore.QSize(300, 28))
        self.comboBox_2.setStyleSheet("font-size:20px;\n"
"font-family:\"Times New Roman\";\n"
"\n"
"text-align:center;\n"
"left:50%;\n"
"right:50%;\n"
"text-align:center;\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 3, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 6, 1, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 4, 1, 1, 3)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(300, 28))
        self.comboBox.setMaximumSize(QtCore.QSize(300, 28))
        self.comboBox.setStyleSheet("font-size:20px;\n"
"font-family:\"Times New Roman\";\n"
"\n"
"text-align:center;\n"
"left:50%;\n"
"right:50%;\n"
"text-align:center;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 2, 1, 1)
        self.retranslateUi(Dialog)

        self.sel_category = self.comboBox.currentText()
        self.sel_brand = self.comboBox.currentText()
        self.sel_item = self.lineEdit.text()
        self.returning = (0,self.sel_item,self.sel_category,self.sel_brand)
        self.drop_menu()
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.return_true)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.rejected.connect(self.return_false)
        self.display_msg = QtWidgets.QMessageBox(Dialog)
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)


        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox, self.comboBox_2)
        Dialog.setTabOrder(self.comboBox_2, self.lineEdit)
        Dialog.setTabOrder(self.lineEdit, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.comboBox)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Advance Search"))
        self.label.setText(_translate("Dialog", "Category"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Item Name Can be Blank"))
        self.label_3.setText(_translate("Dialog", "Item Name"))
        self.label_2.setText(_translate("Dialog", "Brand"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_adv_search()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

