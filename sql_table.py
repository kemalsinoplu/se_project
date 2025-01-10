import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_ui.ui", self)
        self.tableWidget.setColumnWidth(0, 150) 
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100) 
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)  
        self.tableWidget.setColumnWidth(5, 150)  


        self.tableWidget.setHorizontalHeaderLabels(["Brand", "Model", "Price", "Year", "KM", "City"])
        self.loaddata()

    def loaddata(self):
        connection = sqlite3.connect('cars.sqlite')  # Veritabanına bağlan
        cur = connection.cursor()

        # Veritabanından tüm verileri çek
        sqlstr = 'SELECT brand, model, price, year, km, city FROM carsdata' 
        results = cur.execute(sqlstr).fetchall()

        # Tabloya verileri yükle
        self.tableWidget.setRowCount(len(results))  # Satır sayısını ayarla
        for tablerow, row in enumerate(results):
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))  # Brand
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))  # Model
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))  # Price
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))  # Year
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))  # KM
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))  # City

        connection.close()  # Veritabanı bağlantısını kapat

# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")