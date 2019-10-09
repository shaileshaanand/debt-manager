# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_transaction_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(381, 376)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.amount = QtWidgets.QLineEdit(self.groupBox)
        self.amount.setObjectName("amount")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.amount)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.date = QtWidgets.QCalendarWidget(self.groupBox)
        self.date.setObjectName("date")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.date)
        self.description = QtWidgets.QLineEdit(self.groupBox)
        self.description.setObjectName("description")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.description)
        self.taken_button = QtWidgets.QRadioButton(self.groupBox)
        self.taken_button.setObjectName("taken_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.taken_button)
        self.given_button = QtWidgets.QRadioButton(self.groupBox)
        self.given_button.setEnabled(True)
        self.given_button.setChecked(True)
        self.given_button.setObjectName("given_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.given_button)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Transaction"))
        self.label.setText(_translate("Dialog", "Amount"))
        self.amount.setText(_translate("Dialog", "0.0"))
        self.label_2.setText(_translate("Dialog", "Date"))
        self.label_3.setText(_translate("Dialog", "Description"))
        self.taken_button.setText(_translate("Dialog", "Taken"))
        self.given_button.setText(_translate("Dialog", "Given"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
