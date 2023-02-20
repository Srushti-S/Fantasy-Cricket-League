from score import Ui_Dialog as Score  # Score window

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
conn = sqlite3.connect('fantasy.db')
cur = conn.cursor()

class Ui_Evaluate_MainWindow(object):
    def __init__(self):
        self.flag=0
        # initialising score window
        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen = Score()
        self.score_screen.setupUi(self.scoreDialog)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 607)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("rgb(231, 231, 231)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectteam_cb = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        self.selectteam_cb.setFont(font)
        self.selectteam_cb.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.selectteam_cb.setObjectName("selectteam_cb")
        self.selectteam_cb.addItem("")
        self.horizontalLayout.addWidget(self.selectteam_cb)
        self.selectmatch_cb = QtWidgets.QComboBox(self.centralwidget)
        self.selectmatch_cb.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.selectmatch_cb.setFont(font)
        self.selectmatch_cb.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.selectmatch_cb.setObjectName("selectmatch_cb")
        self.selectmatch_cb.addItem("")
        self.horizontalLayout.addWidget(self.selectmatch_cb)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("rgb(231, 231, 231)")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.players_lw = QtWidgets.QListWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.players_lw.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.players_lw.setFont(font)
        self.players_lw.setStyleSheet("")
        self.players_lw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.players_lw.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.players_lw.setObjectName("players_lw")
        self.verticalLayout_4.addWidget(self.players_lw)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("rgb(231, 231, 231)")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.scores_lw = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.scores_lw.setFont(font)
        self.scores_lw.setStyleSheet("")
        self.scores_lw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scores_lw.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.scores_lw.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.scores_lw.setObjectName("scores_lw")
        self.verticalLayout_3.addWidget(self.scores_lw)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.calcscore_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calcscore_btn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.calcscore_btn.setFont(font)
        self.calcscore_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.calcscore_btn.setStyleSheet("")
        self.calcscore_btn.setAutoDefault(False)
        self.calcscore_btn.setObjectName("calcscore_btn")
        self.horizontalLayout_4.addWidget(self.calcscore_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        tm= cur.execute("SELECT DISTINCT name FROM teams;")  # fetching team names
        teams= tm.fetchall()
        for i in teams:
            self.selectteam_cb.addItem(i[0])

        self.selectteam_cb.activated.connect(self.show_match)
        selected_team = self.selectteam_cb.currentText()
        self.loadteam(selected_team)
        self.selectteam_cb.currentTextChanged.connect(self.loadteam)
        self.calcscore_btn.clicked.connect(self.final_score)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Evaluate Score"))
        self.label.setText(_translate("MainWindow", " Evaluate the Performance of your Fantasy Team"))
        self.selectteam_cb.setCurrentText(_translate("MainWindow", "Select Team"))
        self.selectteam_cb.setItemText(0, _translate("MainWindow", "Select Team"))
        self.selectmatch_cb.setItemText(0, _translate("MainWindow", "Match1"))
        self.label_3.setText(_translate("MainWindow", "Players"))
        self.label_2.setText(_translate("MainWindow", "Points"))
        self.calcscore_btn.setStatusTip(_translate("MainWindow", "calculating score"))
        self.calcscore_btn.setText(_translate("MainWindow", "Calculate Score"))

    def show_match(self):
        self.selectmatch_cb.setEnabled(True)
        self.flag=1
        
    def loadteam(self, tnm):
        self.players_lw.clear()
        self.scores_lw.clear()
        x = cur.execute("SELECT players from teams WHERE name='" + tnm + "';")
        player = x.fetchall()
        for j in player:
            self.players_lw.addItem(j[0])
        z = cur.execute("SELECT value from teams WHERE name='" + tnm + "';")
        value = z.fetchall()
        for k in value:
            self.scores_lw.addItem(str(k[0]))

    def final_score(self):
        total_score = 0
        team_nm = self.selectteam_cb.currentText()  # current teamname
        a = cur.execute("SELECT SUM(value) from teams WHERE name='" + team_nm + "';")
        total_score = a.fetchall()
        try:
            cur.execute("UPDATE teams SET score ='"+ str(total_score[0][0]) +"' WHERE name='" + team_nm + "';")
            conn.commit()
        except:        
            conn.rollback()
        count=0
        b=cur.execute("SELECT distinct name,score from teams;") #where name = '" + team_nm + "';")
        result=b.fetchall()
        dict={}
        for l in result:
            dict[l[0]]=l[1]
        sort_score = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        for m in sort_score:
            count=count+1
            if m[0]==team_nm:
                break
        self.score_screen.finalscore.setText(str(total_score[0][0]))  # opening score dialog box and setting final score
        if self.flag==1:
            self.score_screen.rank.setText(str(count))
        else:
             self.score_screen.rank.setText(str('None'))
        self.scoreDialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Evaluate_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
