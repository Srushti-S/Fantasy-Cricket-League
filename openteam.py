
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
conn = sqlite3.connect('fantasy.db')
cur = conn.cursor()


class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(427, 344)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 70, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.open_cb = QtWidgets.QComboBox(Dialog)
        self.open_cb.setGeometry(QtCore.QRect(120, 140, 181, 31))
        self.open_cb.setObjectName("open_cb")
        self.open_btn = QtWidgets.QPushButton(Dialog)
        self.open_btn.setGeometry(QtCore.QRect(170, 210, 91, 51))
        self.open_btn.setObjectName("open_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        tm= cur.execute("SELECT DISTINCT name FROM teams;")  # fetching team names
        teams= tm.fetchall()
        for i in teams:
            self.open_cb.addItem(i[0])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Open Team"))
        self.label.setText(_translate("Dialog", "Select Team Name"))
        self.open_btn.setText(_translate("Dialog", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
