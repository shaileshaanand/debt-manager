import sqlite3
import sys, os
from pathlib import Path
from collections import namedtuple

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .main_design import *
from .new_transaction_dialog import *
from .about_us import Ui_Dialog as About_Ui_Dialog

Person = namedtuple('Person', ['name', 'personid', 'total'])
Transaction = namedtuple(
    'Transaction', ['id', 'personid', 'desc', 'amount', 'date'])
version = "0.0.9"


class PersonListWidgetItem(QListWidgetItem):
    def __init__(self, person, *args):
        self.person = person
        self.ltext = person.name + f'  ({person.total})'
        super().__init__(self.ltext, *args)


class TransactionTableWidgetItem(QTableWidgetItem):
    def __init__(self, transaction, *args):
        self.transaction = transaction
        super().__init__(*args)


def get_total(transactions):
    sum = 0
    for transaction in transactions:
        sum += transaction.amount
    return sum


def get_grand_total(people):
    sum = 0
    for person in people:
        sum += person.total
    return sum


def initialize():
    cur.execute(
        "CREATE TABLE people (personid INTEGER NOT NULL PRIMARY KEY,name text, total real)")
    cur.execute(
        "CREATE TABLE transactions (transactionid INTEGER NOT NULL PRIMARY KEY,personid INTEGER, desc text, "
        "amount real, date date)")


def init_test():
    cur.execute(
        "CREATE TABLE people (personid INTEGER NOT NULL PRIMARY KEY,name text, total real)")
    cur.execute(
        "CREATE TABLE transactions (transactionid INTEGER NOT NULL PRIMARY KEY,personid INTEGER, desc text, "
        "amount real, date date)")
    insert_person(Person(personid=0, name="shailesh", total=0))
    insert_person(Person(personid=0, name="shailesh2", total=0))
    insert_person(Person(personid=0, name="shailesh3", total=0))
    insert_person(Person(personid=0, name="shailesh4", total=0))
    insert_person(Person(personid=0, name="shailesh5", total=0))
    insert_transaction(Transaction(0, 1, 'd1', 5, '2019-09-02'))
    insert_transaction(Transaction(0, 1, 'd2', -7, '2019-09-02'))
    insert_transaction(Transaction(0, 1, 'd3', 9, '2019-09-02'))
    insert_transaction(Transaction(0, 1, 'd4', 1, '2019-09-02'))
    insert_transaction(Transaction(0, 1, 'd5', 28, '2019-09-02'))
    insert_transaction(Transaction(0, 2, 'sdd1', 50, '2019-11-02'))
    insert_transaction(Transaction(0, 2, 'sdd1', -20, '2019-11-02'))
    insert_transaction(Transaction(0, 2, 'sdd1', 60, '2019-11-02'))


def insert_person(person):
    cur.execute(
        f'INSERT INTO people (name,total) VALUES ("{person.name}","{person.total}")')


def get_person_total(person: Person):
    return tuple(cur.execute(f'SELECT total FROM people WHERE personid={person.personid}'))[0][0]


def get_person(personid: int):
    name, personid, total = tuple(cur.execute(f'SELECT * FROM people WHERE personid={personid}'))[0]
    return Person(personid, name, total)


def insert_transaction(transaction):
    cur.execute(
        f'INSERT INTO transactions (personid,desc,amount,date) VALUES ("{transaction.personid}","{transaction.desc}","{transaction.amount}","{transaction.date}")')
    # prev_amount = tuple(cur.execute(f'SELECT total FROM people WHERE personid={transaction.personid}'))[0][0]
    prev_amount = get_person_total(get_person(transaction.personid))
    update_total(get_person(transaction.personid), prev_amount + transaction.amount)


def delete_person(person):
    cur.execute(f'DELETE FROM people WHERE personid={person.personid}')
    cur.execute(f'DELETE FROM transactions WHERE personid={person.personid}')


def update_total(person: Person, new_total: float):
    cur.execute(f'UPDATE people SET total={new_total} WHERE personid={person.personid}')


def delete_transaction(transaction: Transaction):
    cur.execute(f'DELETE FROM transactions WHERE transactionid={transaction.id}')
    prev_total = get_person_total(get_person(transaction.personid))
    new_total = prev_total - transaction.amount
    update_total(get_person(transaction.personid), new_total)


def update_transaction(transaction: Transaction, prev_amount):
    person = get_person(transaction.personid)
    cur.execute(
        f'UPDATE transactions SET desc="{transaction.desc}",amount={transaction.amount},date="{transaction.date}" WHERE transactionid={transaction.id}')
    update_total(person, get_person_total(person) + transaction.amount - prev_amount)


def rename_person(person: Person, new_name: str):
    cur.execute(f'UPDATE people SET name="{new_name}" WHERE personid={person.personid}')


def new_person():
    name, ok = QInputDialog.getText(MainWindow, "New Person", "Name:", )
    if ok:
        insert_person(Person(name, None, 0))
        refresh_people()


def new_transaction():
    def new_transaction_accepted():
        if dui.given_button.isChecked():
            amount = float(dui.amount.text())
        else:
            amount = -float(dui.amount.text())
        insert_transaction(Transaction(None, clicked_person.personid, dui.description.text(), amount,
                                       dui.date.selectedDate().toString("yyyy-MM-dd")))
        current_person_item = refresh_people(clicked_person.personid)
        select_person(current_person_item)

    clicked_person: Person = ui.people_list.selectedItems()[0].person
    transaction_dialog = QDialog(MainWindow)
    dui = Ui_Dialog()
    dui.setupUi(transaction_dialog)
    dui.amount.setValidator(QRegExpValidator(QRegExp("[0-9]+.[0-9]+")))
    dui.groupBox.setTitle(f'New transaction for {clicked_person.name}')
    dui.buttonBox.accepted.connect(new_transaction_accepted)
    dui.amount.selectAll()
    transaction_dialog.exec_()
    transaction_dialog.show()


def get_transactions(person):
    transactions = []
    for transactionid, personid, desc, amount, date in tuple(
            cur.execute(f'SELECT * FROM transactions WHERE personid={person.personid}')):
        transactions.append(Transaction(transactionid, personid, desc, amount, date))
    return transactions


def get_people():
    people = []
    for personid, name, total in tuple(cur.execute('SELECT * FROM people')):
        people.append(Person(name, personid, total))
    return people


def update_total_transaction_amount(transactions_total, name):
    if transactions_total > 0:
        ui.transactions_total_label.setText(f'Total ₹{transactions_total} to take from {name}')
    elif transactions_total < 0:
        ui.transactions_total_label.setText(f'Total ₹{-transactions_total} to give to {name}')
    else:
        ui.transactions_total_label.setText(f'Total ₹{transactions_total} due from {name}')


def select_person(person_item: PersonListWidgetItem):
    person_item.setSelected(True)
    refresh_transactions(person_item.person)


def person_selection_changed():
    if len(ui.people_list.selectedItems()) != 0:
        person_item = ui.people_list.selectedItems()[0]
        if not ui.new_transaction_button.isEnabled():
            ui.new_transaction_button.setEnabled(True)
        refresh_transactions(person_item.person)


def clear_transactions():
    ui.transactions_label.setText("")
    ui.transactions_table.setRowCount(0)
    ui.transactions_total_label.setText("")
    ui.new_transaction_button.setEnabled(False)


def refresh_transactions(person: Person):
    transactions = get_transactions(person)
    transactions_total = get_total(transactions)
    update_total_transaction_amount(transactions_total, person.name)
    ui.transactions_label.setText('Transactions for ' + person.name)
    ui.transactions_table.setRowCount(len(transactions))
    for i, transaction in enumerate(transactions):
        if transaction.amount >= 0:
            amount_item = TransactionTableWidgetItem(transaction, str(transaction.amount))
            given_taken_item = TransactionTableWidgetItem(transaction, "Given")
            bg_color = QColor("#81c784")
        else:
            amount_item = TransactionTableWidgetItem(transaction, str(-transaction.amount))
            given_taken_item = TransactionTableWidgetItem(transaction, "Taken")
            bg_color = QColor("#e57373")
        date_item = TransactionTableWidgetItem(transaction, transaction.date)
        date_item.setFlags(Qt.ItemIsSelectable)
        date_item.setForeground(QColor("black"))
        date_item.setBackground(bg_color)
        ui.transactions_table.setItem(i, 0, date_item)
        amount_item.setFlags(Qt.ItemIsSelectable)
        amount_item.setForeground(QColor("black"))
        amount_item.setTextAlignment(Qt.AlignCenter)
        amount_item.setBackground(bg_color)
        given_taken_item.setFlags(Qt.ItemIsSelectable)
        given_taken_item.setForeground(QColor("black"))
        given_taken_item.setTextAlignment(Qt.AlignCenter)
        given_taken_item.setBackground(bg_color)
        ui.transactions_table.setItem(i, 1, amount_item)
        ui.transactions_table.setItem(i, 2, given_taken_item)
        desc_item = TransactionTableWidgetItem(transaction, transaction.desc)
        desc_item.setFlags(Qt.ItemIsSelectable)
        desc_item.setForeground(QColor("black"))
        desc_item.setBackground(bg_color)
        ui.transactions_table.setItem(i, 3, desc_item)


def refresh_people(person_item_to_return: int = None):
    ui.people_list.clear()
    people = get_people()
    for person in people:
        person_item = PersonListWidgetItem(person)
        ui.people_list.addItem(person_item)
        if person.personid == person_item_to_return:
            cur_person_item = person_item
    total_amount = get_grand_total(people)
    if total_amount < 0.0:
        ui.people_total_label.setText(f'Total {-total_amount} to give.')
    elif total_amount > 0.0:
        ui.people_total_label.setText(f'Total {total_amount} to take.')
    else:
        ui.people_total_label.setText(f'No Overall Debt.')
    if person_item_to_return is not None:
        return cur_person_item


def person_right_clicked(pos):
    if ui.people_list.itemAt(pos) is not None:
        select_person(ui.people_list.itemAt(pos))
        menu = QMenu()
        menu.addAction(QApplication.style().standardIcon(QStyle.SP_TrashIcon), "Delete").triggered.connect(
            person_delete_clicked)
        menu.addAction("Rename").triggered.connect(person_rename_clicked)
        menu.exec_(QCursor.pos())


def person_delete_clicked():
    person_name = ui.people_list.selectedItems()[0].person.name
    confirm_box = QMessageBox(MainWindow)
    confirm_box.setText(
        f"Are you sure you want to delete {person_name}.\nAll transactions from {person_name} will be lost.")
    camcel_button = confirm_box.addButton(QMessageBox.Cancel)
    ok_button = confirm_box.addButton(QMessageBox.Ok)
    confirm_box.exec_()
    if confirm_box.clickedButton() == ok_button:
        delete_person(ui.people_list.selectedItems()[0].person)
        refresh_people()
        clear_transactions()


def person_rename_clicked():
    person = ui.people_list.selectedItems()[0].person
    new_name, ok = QInputDialog().getText(MainWindow, "Edit Name", "New Name", text=person.name)
    if ok:
        rename_person(person, new_name)
        renamed_person_item = refresh_people(person.personid)
        select_person(renamed_person_item)


def get_QDate(date: str):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    return QDate(year, month, day)


def transactions_table_right_clicked(pos):
    def delete_clicked():
        confirm_box = QMessageBox(MainWindow)
        confirm_box.setText(
            f"Are you sure you want to delete the transaction:\n{clicked_transaction.desc}")
        camcel_button = confirm_box.addButton(QMessageBox.Cancel)
        ok_button = confirm_box.addButton(QMessageBox.Ok)
        confirm_box.exec_()
        if confirm_box.clickedButton() == ok_button:
            delete_transaction(clicked_transaction)
            person_item = refresh_people(clicked_transaction.personid)
            person_item.setSelected(True)
            refresh_transactions(person_item.person)

    def edit_clicked():
        def edit_confirmed():
            if dui.given_button.isChecked():
                amount = float(dui.amount.text())
            else:
                amount = -float(dui.amount.text())
            update_transaction(
                Transaction(clicked_transaction.id, clicked_transaction.personid, dui.description.text(), amount,
                            dui.date.selectedDate().toString("yyyy-MM-dd")), prev_amount)
            person_item = refresh_people(clicked_transaction.personid)
            person_item.setSelected(True)
            refresh_transactions(person_item.person)

        prev_amount = clicked_transaction.amount
        transaction_dialog = QtWidgets.QDialog(MainWindow)
        dui = Ui_Dialog()
        dui.setupUi(transaction_dialog)
        if clicked_transaction.amount >= 0:
            dui.given_button.setChecked(True)
            dui.amount.setText(str(clicked_transaction.amount))
        else:
            dui.taken_button.setChecked(True)
            dui.amount.setText(str(-clicked_transaction.amount))
        dui.date.setSelectedDate(get_QDate(clicked_transaction.date))
        dui.description.setText(clicked_transaction.desc)
        dui.amount.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+.[0-9]+")))
        dui.buttonBox.accepted.connect(edit_confirmed)
        transaction_dialog.exec_()
        transaction_dialog.show()

    if ui.transactions_table.itemAt(pos) is not None:
        clicked_transaction: Transaction = ui.transactions_table.itemAt(pos).transaction
        transaction_menu = QMenu()
        transaction_menu.addAction("Delete", delete_clicked)
        transaction_menu.addAction("Edit", edit_clicked)
        transaction_menu.exec_(QCursor.pos())


cur = None
conn = None
ui = None
MainWindow = None


def main():
    global cur, conn, ui, MainWindow
    path = Path('~/.config/debt_management/').expanduser()
    file = Path('data.db')
    os.makedirs(path, exist_ok=True)
    try:
        conn = sqlite3.connect(str(path / file))
        cur = conn.cursor()
        if len(tuple(cur.execute(f'SELECT name FROM sqlite_master WHERE type="table" AND name="people"'))) == 0:
            initialize()
            # init_test()
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.add_person_button.clicked.connect(new_person)
        ui.new_transaction_button.clicked.connect(new_transaction)
        ui.transactions_table.setContextMenuPolicy(Qt.CustomContextMenu)
        ui.transactions_table.customContextMenuRequested.connect(transactions_table_right_clicked)
        ui.transactions_table.verticalHeader().setVisible(False)
        ui.people_list.itemSelectionChanged.connect(person_selection_changed)
        ui.people_list.setContextMenuPolicy(Qt.CustomContextMenu)
        ui.people_list.customContextMenuRequested.connect(person_right_clicked)
        ui.people_total_label.setAlignment(Qt.AlignCenter)
        about = QDialog(MainWindow)
        about_us_ui = About_Ui_Dialog()
        about_us_ui.setupUi(about)
        about_us_ui.label.setText(about_us_ui.label.text().format(version))
        about_us_ui.label.setAlignment(Qt.AlignCenter)
        ui.menuAbout.triggered.connect(about.show)
        MainWindow.show()
        refresh_people()
        sys.exit(app.exec_())
    finally:
        conn.commit()
        cur.close()
        conn.close()
