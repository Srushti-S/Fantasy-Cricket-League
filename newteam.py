
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 251)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tm_name = QtWidgets.QLineEdit(Dialog)
        self.tm_name.setGeometry(QtCore.QRect(100, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tm_name.setFont(font)
        self.tm_name.setObjectName("tm_name")
        self.tm_name.setMaxLength(10)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(150, 170, 91, 23))
        self.save_btn.setAutoDefault(False)
        self.save_btn.setDefault(False)
        self.save_btn.setFlat(False)
        self.save_btn.setObjectName("save_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Team"))
        self.tm_name.setPlaceholderText(_translate("Dialog", "enter team name"))
        self.label.setText(_translate("Dialog", "Create New Team"))
        self.save_btn.setText(_translate("Dialog", "Save"))

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
