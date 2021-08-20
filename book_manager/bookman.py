# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from book import show_books, add_book, edit_book, delete_book
from Dialog import Ui_Dialog
from data_model import Book
conn = sqlite3.connect("books.db")

books = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global books
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_1 = QtWidgets.QListWidget(self.centralwidget)
        self.list_1.setGeometry(QtCore.QRect(170, 20, 831, 601))
        self.list_1.setObjectName("list_1")
        books = show_books(conn)
        for item in books:
            newitem = QtWidgets.QListWidgetItem(
                f"Name: {item[0]}\nPath: {item[1]}\nTags: {', '.join(item[2])}\nNotes: {item[3]}\n")
            font = QtGui.QFont('Times', 12)
            font.setBold(True)
            font.setWeight(50)
            newitem.setFont(font)
            self.list_1.addItem(newitem)
        self.list_1.itemDoubleClicked.connect(self.open_properties)
        # self.list_1.item
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.BrightText, brush)
        self.label.setPalette(palette)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Icons/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(20, 80, 111, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/add.svg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add.setIcon(icon)
        self.button_add.setObjectName("button_add")
        self.button_add.clicked.connect(self.add_books)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 151, 261))
        self.groupBox.setObjectName("groupBox")
        self.button_search = QtWidgets.QPushButton(self.groupBox)
        self.button_search.setGeometry(QtCore.QRect(40, 180, 41, 31))
        self.button_search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/search.webp"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_search.setIcon(icon1)
        self.button_search.setObjectName("button_search")
        self.button_search.clicked.connect(self.search_books)
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_1.setGeometry(QtCore.QRect(10, 40, 95, 20))
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 80, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 100, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 150, 113, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 220, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_all)
        self.groupBox.raise_()
        self.list_1.raise_()
        self.label.raise_()
        self.button_add.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BookMan"))
        self.button_add.setText(_translate("MainWindow", " Add Book"))
        self.groupBox.setTitle(_translate("MainWindow", "Search"))
        self.radioButton_1.setText(_translate("MainWindow", "Name"))
        self.radioButton_2.setText(_translate("MainWindow", "Link"))
        self.radioButton_3.setText(_translate("MainWindow", "Tags"))
        self.radioButton_4.setText(_translate("MainWindow", "Notes"))
        self.label_2.setText(_translate("MainWindow", "Search by"))
        self.label_3.setText(_translate("MainWindow", "KeyWord"))
        self.pushButton.setText(_translate("MainWindow", "Clear Search"))

    def show_all(self):
        self.list_1.clear()
        global books
        # print(books)
        for item in books:
            newitem = QtWidgets.QListWidgetItem(
                f"Name: {item[0]}\nPath: {item[1]}\nTags: {', '.join(item[2])}\nNotes: {item[3]}\n")
            font = QtGui.QFont('Times', 12)
            font.setBold(True)
            font.setWeight(50)
            newitem.setFont(font)
            self.list_1.addItem(newitem)
        # print("Clicked")
        self.lineEdit.clear()

    def search_books(self):
        global books
        results = []
        searchtext = self.lineEdit.text()
        field = [self.radioButton_1.isChecked(), self.radioButton_2.isChecked(
        ), self.radioButton_3.isChecked(), self.radioButton_4.isChecked()]
        ind = field.index(True)
        for i in books:
            if searchtext in i[ind]:
                results.append(i)
        self.list_1.clear()
        for item in results:
            newitem = QtWidgets.QListWidgetItem(
                f"Name: {item[0]}\nPath: {item[1]}\nTags: {', '.join(item[2])}\nNotes: {item[3]}\n")
            font = QtGui.QFont('Times', 12)
            font.setBold(True)
            font.setWeight(50)
            newitem.setFont(font)
            self.list_1.addItem(newitem)

    def add_books(self):
        global books
        res = self.open_dialog_box()
        name = res[0].split('/')[-1]
        Dialog2 = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog2, path=res[0], name=name, add=1)
        Dialog2.show()
        s = Dialog2.exec_()
        if s == 1:
            if ui.data['path'] not in [i[1] for i in books]:
                books.append([ui.data['name'], ui.data['path'],
                              ui.data['tags'], ui.data['notes']])
                item = books[-1]
                newitem = QtWidgets.QListWidgetItem(
                    f"Name: {item[0]}\nPath: {item[1]}\nTags: {', '.join(item[2])}\nNotes: {item[3]}\n")
                font = QtGui.QFont('Times', 12)
                font.setBold(True)
                font.setWeight(50)
                newitem.setFont(font)
                self.list_1.addItem(newitem)
                add_book(conn, Book(ui.data['name'], ui.data['path'], ', '.join(
                    item[2]), ui.data['notes']))

    def open_dialog_box(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        return filename
        # print(filename)

    def open_properties(self, item):
        global books
        lines = item.text().split('\n')
        final = []
        for index, i in enumerate(lines):
            lines[index] = i.strip()
            val = ' '.join(lines[index].split(' ')[1:])
            final.append(val)
        Dialog2 = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(
            Dialog2, path=final[1], name=final[0], tags=final[2], notes=final[3])
        Dialog2.show()
        s = Dialog2.exec_()
        if s == 1:
            if ui.data['delete'] is True:
                for index, i in enumerate(books):
                    if i[1] == final[1]:
                        ind = index
                        break
                delete_book(conn, books[ind][1])
                del books[ind]
                self.show_all()
            else:
                # Ok is clicked
                for index, i in enumerate(books):
                    if i[1] == final[1]:
                        ind = index
                        break
                books[index][0] = ui.data['name']
                books[index][1] = ui.data['path']
                books[index][2] = ui.data['tags']
                books[index][3] = ui.data['notes']
                edit_book(conn, 'name', books[index][0], books[index][1])
                edit_book(conn, 'tags', ', '.join(
                    books[index][2]), books[index][1])
                edit_book(conn, 'notes', books[index][3], books[index][1])
                self.show_all()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
