import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Каталог кофе')
        self.pushButton.clicked.connect(self.work_with_base)

    def work_with_base(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee_info WHERE variety = ?""", (self.comboBox.currentText(),)).fetchall()[0]
        self.lineEdit.setText(result[2])
        self.lineEdit_2.setText(result[3])
        self.plainTextEdit.setPlainText(result[4])
        self.lcdNumber.display(result[5])
        self.lcdNumber_2.display(result[6])
        self.lineEdit_3.setText(result[7])
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())