
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 242)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.finalscore = QtWidgets.QLabel(Dialog)
        self.finalscore.setGeometry(QtCore.QRect(210, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.finalscore.setFont(font)
        self.finalscore.setAlignment(QtCore.Qt.AlignCenter)
        self.finalscore.setObjectName("finalscore")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.rank = QtWidgets.QLabel(Dialog)
        self.rank.setGeometry(QtCore.QRect(210, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.rank.setFont(font)
        self.rank.setAlignment(QtCore.Qt.AlignCenter)
        self.rank.setObjectName("rank")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Final Score "))
        self.label.setText(_translate("Dialog", "Your Score:"))
        self.finalscore.setText(_translate("Dialog", "0"))
        self.label_2.setText(_translate("Dialog", "Your Rank:"))
        self.rank.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
