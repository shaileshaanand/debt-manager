# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_us.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(494, 133)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.source_code_link = QtWidgets.QLabel(Dialog)
        self.source_code_link.setObjectName("source_code_link")
        self.gridLayout.addWidget(self.source_code_link, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About Debt Manager"))
        self.label.setText(_translate("Dialog", "Debt Manager version {}\n"
                                                "Author : Shailesh Aanand\n"
                                                "Released under the GPLv3 License\n"
                                                "Notebook icon made by Smashicons from flaticon.com"))
        self.source_code_link.setText(_translate("Dialog",
                                                 "<html><head/><body><p align=\"center\">Source Code : <a href=\"https://github.com/shaileshaanand/debt-manager\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/shaileshaanand/debt-manager</span></a></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
