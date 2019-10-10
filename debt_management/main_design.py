# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debt_management.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.people_label = QtWidgets.QLabel(self.centralwidget)
        self.people_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.people_label.setTextFormat(QtCore.Qt.RichText)
        self.people_label.setObjectName("people_label")
        self.horizontalLayout_2.addWidget(self.people_label)
        self.add_person_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_person_button.setMaximumSize(QtCore.QSize(66, 16777215))
        self.add_person_button.setObjectName("add_person_button")
        self.horizontalLayout_2.addWidget(self.add_person_button)
        self.transactions_label = QtWidgets.QLabel(self.centralwidget)
        self.transactions_label.setText("")
        self.transactions_label.setObjectName("transactions_label")
        self.horizontalLayout_2.addWidget(self.transactions_label)
        self.new_transaction_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_transaction_button.setEnabled(False)
        self.new_transaction_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.new_transaction_button.setObjectName("new_transaction_button")
        self.horizontalLayout_2.addWidget(self.new_transaction_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.people_total_label = QtWidgets.QLabel(self.centralwidget)
        self.people_total_label.setMinimumSize(QtCore.QSize(0, 50))
        self.people_total_label.setText("")
        self.people_total_label.setObjectName("people_total_label")
        self.gridLayout_2.addWidget(self.people_total_label, 1, 0, 1, 1)
        self.people_list = QtWidgets.QListWidget(self.centralwidget)
        self.people_list.setMaximumSize(QtCore.QSize(221, 16777215))
        self.people_list.setObjectName("people_list")
        self.gridLayout_2.addWidget(self.people_list, 0, 0, 1, 1)
        self.transactions_table = QtWidgets.QTableWidget(self.centralwidget)
        self.transactions_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.transactions_table.setColumnCount(4)
        self.transactions_table.setObjectName("transactions_table")
        self.transactions_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.transactions_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions_table.setHorizontalHeaderItem(3, item)
        self.transactions_table.horizontalHeader().setStretchLastSection(True)
        self.transactions_table.verticalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.transactions_table, 0, 1, 1, 1)
        self.transactions_total_label = QtWidgets.QLabel(self.centralwidget)
        self.transactions_total_label.setText("")
        self.transactions_total_label.setObjectName("transactions_total_label")
        self.gridLayout_2.addWidget(self.transactions_total_label, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 20))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Debt Manager"))
        self.people_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span\n"
                                                           "                                        style=\" font-size:12pt; font-weight:600;\">People</span></p></body></html>\n"
                                                           "                                    "))
        self.add_person_button.setText(_translate("MainWindow", "+ Add"))
        self.new_transaction_button.setText(_translate("MainWindow", "New Transaction"))
        item = self.transactions_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.transactions_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.transactions_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.transactions_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Description"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
