import os
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QInputDialog,QMessageBox
from Billing.addCustomer import addCustomerDialog
import pymysql
import datetime


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/billing.ui')
Form, Base = uic.loadUiType(main_path)
class billingWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.Search.clicked.connect(self.searchCust)
        self.addContact.clicked.connect(self.addCustomer)
        self.addItem.clicked.connect(self.addItems)
        self.deletes.clicked.connect(self.delete)
        self.Confirm.clicked.connect(self.entry)
        self.clear.clicked.connect(self.clears)
        self.Bill.clicked.connect(self.stockUpdate)

        self.customerNameLineEdit.setReadOnly(True)
        self.display.setReadOnly(True)

        self.populateCombo1()
        self.populateCombo2()
        self.cbox1.currentIndexChanged.connect(self.populateCombo2)

        self.display_msg = QtWidgets.QMessageBox(self)
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)

    def addCustomer(self):
        self.addCust = addCustomerDialog()
        self.addCust.exec_()
        adr = self.addCust.AdressInput.toPlainText()
        name=self.addCust.nameInput.text()
        self.customerNameLineEdit.setText(name)
        self.display.setPlainText(adr)
        self.contact.setText(self.addCust.phoneNumber1Input.text())

    def populateCombo1(self):
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query = "SELECT category_name from category"

        try:
            cursor.execute(query)
            comboBox1Content = cursor.fetchall()
            self.cbox1.clear()
            for i in range(len(comboBox1Content)):
                self.cbox1.addItem("")
                self.cbox1.setItemText(i, comboBox1Content[i][0])

        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)

        db.close()

    def populateCombo2(self):
        cbox1Text = self.cbox1.currentText()
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
        query ='''
        select item_name 
        from items, category 
        where item_category_id = category_id and category_name = "%s"
        '''%cbox1Text
        try:
            cursor.execute(query)
            comboBox2Content = cursor.fetchall()
            self.cbox2.clear()
            for i in range(len(comboBox2Content)):
                self.cbox2.addItem("")
                self.cbox2.setItemText(i, comboBox2Content[i][0])

        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)
        db.close()
        
    def searchCust(self):
        contact = self.contact.text()
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor = db.cursor()
       
        try:
            cursor.execute("select C_address from Customer_info where C_contact = %s",contact)
            data = cursor.fetchall()
            if data==():
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText("Customer NOT Found")
                self.display_msg.show()
            else:
                self.display.setPlainText(data[0][0])
                cursor.execute("select C_name from Customer_info where C_contact = %s", contact)
                data1 = cursor.fetchall()
                # print(data1)
                self.customerNameLineEdit.setText(data1[0][0])
        except pymysql.InternalError as error:
            code, msg = error.args
            print("-------", code, msg)
        db.close()
        
    def addItems(self):
        sum=0
        cbox2Text = self.cbox2.currentText()
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor= db.cursor()
        
        try:
            cursor.execute("select item_name,item_price from items where item_name = %s",cbox2Text)
            data=cursor.fetchall()
            #self.tableWidget.setRowCount(0)
            for row_data in data:
                quant=self.quantity.text()
                if(quant==""):
                    QMessageBox.about(self,'ERROR','ENTER THE QUANTITY') 
                else:
                    row_no = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_no)
                    for column_no, data in enumerate(row_data):
                        self.tableWidget.setItem(
                                row_no, column_no, QtWidgets.QTableWidgetItem(
                                        str(data)
                                        )
                                ) 
                        self.tableWidget.setItem(
                                row_no, 2, QtWidgets.QTableWidgetItem(
                                        str(quant)
                                        )
                                )
                    for row_no in range(self.tableWidget.rowCount()):
                        prices=int(self.tableWidget.item(row_no,1).text())
                        quantity=int(self.tableWidget.item(row_no,2).text())
                        result=prices*quantity
                        self.tableWidget.setItem(
                                row_no,3, QtWidgets.QTableWidgetItem(
                                        str(result)
                                        )
                                )
                                
                    for row in range(self.tableWidget.rowCount()):
                      net=int(self.tableWidget.item(row,3).text())
                      sum=sum+net
                      self.Total_out.setText(str(sum))
                        
                db.commit()
        except:
            db.rollback()
        db.close()
        
    '''def calculate(self):
        for row in range(self.tableWidget.rowCount()):
                price=int(self.tableWidget.item(row,1).text())
                print(price)
                quantity=int(self.tableWidget.item(row,2).text())
                print(quantity)
                result=price*quantity
                self.tableWidget.setItem(
                            row,3, QtWidgets.QTableWidgetItem(
                                    str(result)
                                    )
                            )
                            
    def total(self):
         sum=0
         for row in range(self.tableWidget.rowCount()):
              net=int(self.tableWidget.item(row,3).text())
              sum=sum+net
         print(sum)
         self.Total_out.setText(str(sum))'''
         
         
    def clears(self):
        rows=self.tableWidget.rowCount()
        # print(rows)
        while(rows>=0):
             self.tableWidget.removeRow(rows-1)
             rows -= 1
        self.Confirm.setEnabled(True)
       
    def delete(self):
        row=int(self.tableWidget.currentRow())
        total = int(self.Total_out.text())
        total=total-int(self.tableWidget.item(row,3).text())
        self.Total_out.setText(str(total))
        self.tableWidget.removeRow (row)
        
        
          
          
    def entry(self):
        contact = self.contact.text()
        if(contact==""):
            QMessageBox.about(self,'ERROR','Select the customer')    
        else:
            db = pymysql.connect("localhost", "root", "", "ims")
            cursor = db.cursor()
            bill_list = []
            contact = self.contact.text()
            cursor.execute("select C_id from Customer_info where C_contact = %s",contact)
            data=cursor.fetchall()
            if(self.tableWidget.rowCount()==0):
                QMessageBox.about(self,'ERROR','Enter the items')   
            else:
                
                cursor.execute("insert into billing(billing_customer_id) values (%s)",data[0][0])
                ids=int(cursor.lastrowid)
        
                for row in range(self.tableWidget.rowCount()):
                    bill_row = {}
                    cursor.execute('''
                    select item_id from items where item_name = "%s"
                    '''%self.tableWidget.item(row,0).text())
        
                    data = cursor.fetchall()
                    item=data[0][0]
                    quant=int(self.tableWidget.item(row,2).text())
                    net=int(self.tableWidget.item(row,3).text())
                    cursor.execute("INSERT INTO ORDERS(order_item_id,order_quantity,order_price,order_billing_id) values (%s,%s,%s,%s)",(item,quant,net,ids))
        
        
                    db.commit()
                    bill_row['item'] = self.tableWidget.item(row,0).text()
                    bill_row['quantity'] = quant
                    bill_row['sub_total'] = net
                    bill_row['price'] = self.tableWidget.item(row,1).text()
                    bill_list.append(bill_row)

                from jinja2 import Environment, PackageLoader, select_autoescape
                env = Environment(
                    loader=PackageLoader('main', 'templates'),
                    autoescape=select_autoescape(['html', 'xml'])
                )
        
                template = env.get_template('bill.html')
                address = self.display.toPlainText()
                name = self.customerNameLineEdit.text()
                phone = self.contact.text()
                total = self.Total_out.text()
                sourceHtml = template.render(address=address,name=name, bill_list=bill_list,phone = phone,total = total)
                from xhtml2pdf import pisa
                currentDT = datetime.datetime.now()
                s  =  str(currentDT.strftime("%Y%m%d-%H%M%S"))
                rel_path = resource_path("Print\\Bill"+str(s)+".pdf")
                outputFilename = rel_path
                resultFile = open(outputFilename, "w+b")
                pisaStatus = pisa.CreatePDF(
                        sourceHtml,                # the HTML to convert
                        dest=resultFile)           # file handle to recieve result
        
                # close output file
                resultFile.close()                 # close output file
                self.display_msg.setWindowTitle('Message')
                self.display_msg.setText("Bill in Print folder Click Generate Bill to update Stock")

                self.display_msg.show()
                self.Confirm.setEnabled(False)
                


        
    def stockUpdate(self):
        db = pymysql.connect("localhost", "root", "", "ims")
        cursor= db.cursor()
        flag  =0
        for row_no in range(self.tableWidget.rowCount()):
            item = (self.tableWidget.item(row_no, 0).text())
            cursor.execute("select item_id from items where item_name = %s", item)
            itemid = cursor.fetchall()
            # print("itemid = ",itemid)
            quant = int(self.tableWidget.item(row_no, 2).text())
            # print(itemid[0][0])
            cursor.execute("select stock_quantity from stock where stock_item_id = %s", itemid[0][0])
            quantity = cursor.fetchall()
            # print("quantity=",quantity)

            if ((quantity[0][0] - quant) < 0):
                self.display_msg.setWindowTitle('Error')
                self.display_msg.setText("Only " + str(quantity[0][0]) + " quantity is available for" + str(item))
                self.display_msg.show()
                flag = 1
        if flag == 0:
            for row_no in range(self.tableWidget.rowCount()):

                item = (self.tableWidget.item(row_no, 0).text())
                # print("item = ",item)
                try:
                    cursor.execute("select item_id from items where item_name = %s", item)
                    itemid = cursor.fetchall()
                    # print("itemid = ",itemid)
                    quant = int(self.tableWidget.item(row_no, 2).text())
                    # print(itemid[0][0])
                    cursor.execute("select stock_quantity from stock where stock_item_id = %s", itemid[0][0])
                    quantity = cursor.fetchall()
                    # print("quantity=",quantity)

                    if ((quantity[0][0] - quant) < 0):
                        self.display_msg.setWindowTitle('Error')
                        self.display_msg.setText('Only %s quantity available for %s', (quantity[0][0], item))
                        self.display_msg.show()

                    cursor.execute("update stock set stock_quantity = %s where stock_item_id = %s  ",
                                   ((quantity[0][0] - quant), itemid[0][0]))
                    db.commit()
                except:
                    db.rollback()
                    db.close()

            if self.customerNameLineEdit.text()!="":
                self.display_msg.setWindowTitle('Message')
                self.display_msg.setText("Stock Updated Successfully")
                self.display_msg.show()
                self.Confirm.setEnabled(True)
                self.clears()
                self.contact.setText("")
                self.customerNameLineEdit.setText("")













if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = billingWindow()
    w.show()
    sys.exit(app.exec_())
