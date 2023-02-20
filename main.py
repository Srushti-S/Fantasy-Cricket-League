from newteam import Ui_Dialog as New # importing new window
from openteam import Ui_Dialog as Open # importing open window
from evaluatescore import Ui_Evaluate_MainWindow as Eval  # importing evaluate window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import re
import sqlite3
conn = sqlite3.connect('fantasy.db') # connecting database file
cur = conn.cursor()


class Ui_MainWindow(object):
    
    def __init__(self):
        
        # initialising counts
        self.count = 0
        self.totalcount=0
        self.max_WK = 1
        self.max_bat=5
        self.max_bowl=5
        self.max_ar=3
        #  initialising windows
        self.newDialog = QtWidgets.QMainWindow()
        self.new_screen = New()
        self.new_screen.setupUi(self.newDialog)
        
        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = Open()
        self.open_screen.setupUi(self.openDialog)
        
        self.EvaluateWindow = QtWidgets.QMainWindow()
        self.eval_screen = Eval()
        self.eval_screen.setupUi(self.EvaluateWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 706)
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        #Batsmen Counter
        self.batsmen = QtWidgets.QLabel(self.centralwidget)
        self.batsmen.setObjectName("batsmen")
        self.horizontalLayout.addWidget(self.batsmen)
        self.bat_count = QtWidgets.QLabel(self.centralwidget)
        self.bat_count.setObjectName("bat_count")
        self.horizontalLayout.addWidget(self.bat_count)
        #Bowlers Counter
        self.bowlers = QtWidgets.QLabel(self.centralwidget)
        self.bowlers.setObjectName("bowlers")
        self.horizontalLayout.addWidget(self.bowlers)
        self.bowl_count = QtWidgets.QLabel(self.centralwidget)
        self.bowl_count.setObjectName("bowl_count")
        self.horizontalLayout.addWidget(self.bowl_count)
        #All-Rounders Counter
        self.AR = QtWidgets.QLabel(self.centralwidget)
        self.AR.setObjectName("AR")
        self.horizontalLayout.addWidget(self.AR)
        self.ar_count = QtWidgets.QLabel(self.centralwidget)
        self.ar_count.setObjectName("ar_count")
        self.horizontalLayout.addWidget(self.ar_count)
        #Wicket-Keepers Counter
        self.WK = QtWidgets.QLabel(self.centralwidget)
        self.WK.setObjectName("WK")
        self.horizontalLayout.addWidget(self.WK)
        self.wk_count = QtWidgets.QLabel(self.centralwidget)
        self.wk_count.setObjectName("wk_count")
        self.horizontalLayout.addWidget(self.wk_count)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #Points Available and Used Counter
        self.ptsavail_label = QtWidgets.QLabel(self.centralwidget)
        self.ptsavail_label.setObjectName("ptsavail_label")
        self.horizontalLayout_2.addWidget(self.ptsavail_label)
        self.pt_avail = QtWidgets.QLabel(self.centralwidget)
        self.pt_avail.setObjectName("pt_avail")
        self.horizontalLayout_2.addWidget(self.pt_avail)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.ptsused_label = QtWidgets.QLabel(self.centralwidget)
        self.ptsused_label.setObjectName("ptsused_label")
        self.horizontalLayout_2.addWidget(self.ptsused_label)
        self.pt_used = QtWidgets.QLabel(self.centralwidget)
        self.pt_used.setObjectName("pt_used")
        self.horizontalLayout_2.addWidget(self.pt_used)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        #Players Categories
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pl_cat = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pl_cat.setFont(font)
        self.pl_cat.setObjectName("pl_cat")
        self.verticalLayout_8.addWidget(self.pl_cat, 0, QtCore.Qt.AlignHCenter)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(False)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        #Radio Buttons
            #Batsmen
        self.rb_bat = QtWidgets.QRadioButton(self.groupBox)
        self.rb_bat.setObjectName("rb_bat")
        self.horizontalLayout_4.addWidget(self.rb_bat)
            #Bowlers
        self.rb_bowl = QtWidgets.QRadioButton(self.groupBox)
        self.rb_bowl.setObjectName("rb_bowl")
        self.horizontalLayout_4.addWidget(self.rb_bowl)
            #All-Rounders
        self.rb_ar = QtWidgets.QRadioButton(self.groupBox)
        self.rb_ar.setObjectName("rb_ar")
        self.horizontalLayout_4.addWidget(self.rb_ar)
            #Wicket-Keeper
        self.rb_wk = QtWidgets.QRadioButton(self.groupBox)
        self.rb_wk.setObjectName("rb_wk")
        self.horizontalLayout_4.addWidget(self.rb_wk)
        self.verticalLayout_8.addWidget(self.groupBox)
        #Available Players List
        self.availplayer_list = QtWidgets.QListWidget(self.centralwidget)
        self.availplayer_list.setAutoFillBackground(True)
        self.availplayer_list.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 12pt \"Sylfaen\";")
        self.availplayer_list.setAutoScroll(True)
        self.availplayer_list.setObjectName("availplayer_list")
        self.verticalLayout_8.addWidget(self.availplayer_list)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        #Team Counter
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tm_nm = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tm_nm.setFont(font)
        self.tm_nm.setAlignment(QtCore.Qt.AlignCenter)
        self.tm_nm.setObjectName("tm_nm")
        self.horizontalLayout_11.addWidget(self.tm_nm)
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setEnabled(False)
        self.name.setMaxLength(10)
        self.name.setObjectName("name")
        self.horizontalLayout_11.addWidget(self.name)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.selected_player = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selected_player.setFont(font)
        self.selected_player.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_player.setObjectName("selected_player")
         #Players Count
        self.horizontalLayout_12.addWidget(self.selected_player)
        self.player_count = QtWidgets.QLabel(self.centralwidget)
        self.player_count.setAlignment(QtCore.Qt.AlignCenter)
        self.player_count.setObjectName("player_count")
        self.horizontalLayout_12.addWidget(self.player_count)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_10.addWidget(self.line_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem5)
        self.selectedplayer_list = QtWidgets.QListWidget(self.centralwidget)
        self.selectedplayer_list.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 12pt \"Sylfaen\";\n"
"")
        self.selectedplayer_list.setObjectName("selectedplayer_list")
        self.verticalLayout_10.addWidget(self.selectedplayer_list)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setEnabled(True)
        self.exit.setObjectName("exit")
        self.horizontalLayout_7.addWidget(self.exit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.NEW = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("new.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NEW.setIcon(icon1)
        self.NEW.setObjectName("NEW")
        self.OPEN = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OPEN.setIcon(icon2)
        self.OPEN.setObjectName("OPEN")
        self.SAVE = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SAVE.setIcon(icon3)
        self.SAVE.setObjectName("SAVE")
        self.SAVE.setEnabled(False)
        self.EVALUATE = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("evaluate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EVALUATE.setIcon(icon4)
        self.EVALUATE.setObjectName("EVALUATE")
        self.Rule = QtWidgets.QAction(MainWindow)
        self.Rule.setObjectName("Rule")
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.Instructions = QtWidgets.QAction(MainWindow)
        self.Instructions.setObjectName("Instructions")
        self.Rule_3 = QtWidgets.QAction(MainWindow)
        self.Rule_3.setObjectName("Rule_3")
        self.Rules = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("rules.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Rules.setIcon(icon5)
        self.Rules.setObjectName("Rules")
        self.menuManage_Teams.addAction(self.NEW)
        self.menuManage_Teams.addAction(self.OPEN)
        self.menuManage_Teams.addAction(self.SAVE)
        self.menuManage_Teams.addAction(self.EVALUATE)
        self.menuHelp.addAction(self.Rules)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Actions
        self.NEW.triggered.connect(self.new_team)
        self.new_screen.save_btn.clicked.connect(self.load_name)
        self.rb_bat.clicked.connect(self.show_names)
        self.rb_bowl.clicked.connect(self.show_names)
        self.rb_ar.clicked.connect(self.show_names)
        self.rb_wk.clicked.connect(self.show_names)
        self.availplayer_list.itemDoubleClicked.connect(self.take_names)
        self.selectedplayer_list.itemDoubleClicked.connect(self.remove_names)
        self.SAVE.triggered.connect(self.save_teams)
        self.OPEN.triggered.connect(self.file_open)
        self.open_screen.open_btn.clicked.connect(self.open_team)
        self.EVALUATE.triggered.connect(self.file_evaluate)
        self.Rules.triggered.connect(self.team_selection_rules)
        self.exit.clicked.connect(self.quit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket League"))
        self.label.setText(_translate("MainWindow", "Your Selections :"))
        self.batsmen.setText(_translate("MainWindow", "    Batsmen :"))
        self.bat_count.setText(_translate("MainWindow", "  ##  "))
        self.bowlers.setText(_translate("MainWindow", "          Bowlers :"))
        self.bowl_count.setText(_translate("MainWindow", "  ##  "))
        self.AR.setText(_translate("MainWindow", "          All Rounders :"))
        self.ar_count.setText(_translate("MainWindow", "  ##  "))
        self.WK.setText(_translate("MainWindow", "          Wicket Keepers :"))
        self.wk_count.setText(_translate("MainWindow", "  ##  "))
        self.ptsavail_label.setText(_translate("MainWindow", "Points Available:  "))
        self.pt_avail.setText(_translate("MainWindow", "  00  "))
        self.ptsused_label.setText(_translate("MainWindow", "Points Used:  "))
        self.pt_used.setText(_translate("MainWindow", "  00  "))
        self.pl_cat.setText(_translate("MainWindow", "Player Categories"))
        self.rb_bat.setText(_translate("MainWindow", "BAT"))
        self.rb_bowl.setText(_translate("MainWindow", "BOWL"))
        self.rb_ar.setText(_translate("MainWindow", "AR"))
        self.rb_wk.setText(_translate("MainWindow", "WK"))
        self.tm_nm.setText(_translate("MainWindow", "Team Name :"))
        self.selected_player.setText(_translate("MainWindow", "Selected Players:"))
        self.player_count.setText(_translate("MainWindow", "##"))
        self.exit.setText(_translate("MainWindow", "Exit Application"))
        self.exit.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.NEW.setText(_translate("MainWindow", "NEW Team"))
        self.NEW.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.OPEN.setText(_translate("MainWindow", "OPEN Team"))
        self.OPEN.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.SAVE.setText(_translate("MainWindow", "SAVE Team"))
        self.SAVE.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.EVALUATE.setText(_translate("MainWindow", "EVALUATE Score"))
        self.EVALUATE.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.Rule.setText(_translate("MainWindow", "Rules"))
        self.Rule.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        self.Instructions.setText(_translate("MainWindow", "Instructions"))
        self.Instructions.setShortcut(_translate("MainWindow", "Shift+I"))
        self.Rule_3.setText(_translate("MainWindow", "Rules"))
        self.Rules.setText(_translate("MainWindow", "Rules"))
        self.Rules.setShortcut(_translate("MainWindow", "Ctrl+R"))
        
    def team_selection_rules(self):
        msg=QMessageBox()
        msg.setWindowTitle("Fantasy Cricket League Rules")
        msg.setText('''● There cannot be more than 5 batsmen, 5 bowlers and 3 all-rounder in the team.
         \n● There must be 1 wicket keeper in the team.
         \n● There must be 11 players in the team
         \n● Once team created, it can't be changed''')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
    
    def new_team(self):
        self.SAVE.setEnabled(True)
        self.availplayer_list.setEnabled(True)
        self.selectedplayer_list.setEnabled(True)
        self.newDialog.show()

    def show_names(self):
        self.availplayer_list.clear()
        if self.rb_bat.isChecked()==True:
            cur.execute('SELECT player FROM match WHERE type = "Batsman";')
            bats_data = cur.fetchall()
            for data in bats_data:
                self.availplayer_list.addItem(data[0])
                       
        elif self.rb_bowl.isChecked()==True:
            cur.execute("SELECT player from match WHERE type = 'Bowler';")
            bowl_data = cur.fetchall()
            for data in bowl_data:
                self.availplayer_list.addItem(data[0])
        
        elif self.rb_ar.isChecked()==True:
            cur.execute("SELECT player from match WHERE type = 'Allrounder';")
            all_data = cur.fetchall()
            for data in all_data:
                self.availplayer_list.addItem(data[0])

        else:
            cur.execute("SELECT player FROM match WHERE type = 'WicketKeeper';")
            WK_data = cur.fetchall()
            for data in WK_data:
                self.availplayer_list.addItem(data[0])
    
    def load_name(self):
        msg = QtWidgets.QMessageBox()
        teamName = self.new_screen.tm_name.text()
        cur.execute('SELECT DISTINCT name from teams;')
        names = cur.fetchall()
        regex = re.compile('''[@_!#$%^'&"+*,.(=)<->?/\|}{~:]''') 
       
        if len(teamName) == 0:
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
       
        else:
            if(regex.search(teamName) == None) and teamName.isdigit()==False:
                for i in names:
                    if i[0]==teamName:
                        msg.setIcon(QtWidgets.QMessageBox.Information)
                        msg.setText("Team with same name already exists!!\nPlease choose another name")
                        msg.setWindowTitle("Invalid Team Name")
                        msg.exec_()
                        self.new_screen.tm_name.clear()
                        break
                else:
                    self.reset()
                    self.new_screen.tm_name.clear()
                    self.newDialog.close()
            else: 
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Team name should be combination of characters and digits!!")
                msg.setWindowTitle("Invalid Team Name")
                self.new_screen.tm_name.clear()
                msg.exec_()
    def reset(self):
        self.availplayer_list.clear()
        self.selectedplayer_list.clear()
        teamName = self.new_screen.tm_name.text()
        self.groupBox.setEnabled(True)
        self.name.setEnabled(True)
        self.pt_avail.setText(str('1000'))
        self.pt_used.setText(str('0'))
        self.bat_count.setText(str('0'))
        self.bowl_count.setText(str('0'))
        self.wk_count.setText(str('0'))
        self.ar_count.setText(str('0'))
        self.player_count.setText(str('0'))
        self.name.setText(str(teamName))

    def take_names(self):
        msg = QMessageBox()
        
        if self.rb_wk.isChecked() and self.max_WK is not 0 or self.rb_bat.isChecked() and self.max_bat is not 0 or self.rb_bowl.isChecked() and self.max_bowl is not 0 or self.rb_ar.isChecked() and self.max_ar is not 0:
            flag=0
            item = self.availplayer_list .takeItem(self.availplayer_list .currentRow())
            item = item.text()
            cur.execute("SELECT value FROM stats WHERE player = '" + item + "';")
            play_pt = cur.fetchall()
            actual_pt = self.pt_avail.text()
            actual_pt = int(actual_pt) - int(play_pt[0][0])
            if actual_pt<=0:
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error")
                msg.setText("Insufficient points!")
                msg.exec_()
                self.availplayer_list.addItem(item)
                flag=1
            else:
                self.selectedplayer_list.addItem(item)
                self.pt_avail.setText(str(actual_pt))
                added_pt = self.pt_used.text()
                add_pt = int(added_pt) + int(play_pt[0][0])
                self.pt_used.setText(str(add_pt))
            
        else:
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Selection Error")
            if self.rb_bat.isChecked() and self.max_bat==0:
                msg.setText("You cannot select more than 5 batsmen")
            elif self.rb_bowl.isChecked() and self.max_bowl==0:
                msg.setText("You cannot select more than 5 bowlers")
            elif self.rb_ar.isChecked() and self.max_ar==0:
                msg.setText("You cannot select more than 3 all-rounders")
            else:
                msg.setText("You cannot select more than 1 wicketkeeper")
            msg.exec_()
            
        if self.rb_bat.isChecked() and self.max_bat is not 0 and flag==0:
            self.max_bat = self.max_bat - 1
            bat_total = self.bat_count.text()
            bat_total = int(bat_total)+1
            self.bat_count.setText(str(bat_total))
            self.count=int(self.count)+1
            self.player_count.setText(str(self.count))
        elif self.rb_bowl.isChecked() and self.max_bowl is not 0 and flag==0:
            self.max_bowl = self.max_bowl - 1
            bowl_total = self.bowl_count.text()
            bowl_total = int(bowl_total)+1
            self.bowl_count.setText(str(bowl_total))
            self.count=int(self.count)+1
            self.player_count.setText(str(self.count))

        elif self.rb_wk.isChecked() and self.max_WK is not 0 and flag==0:
            self.max_WK = self.max_WK - 1
            WK_total = self.wk_count.text()
            WK_total = int(WK_total)+1
            self.wk_count.setText(str(WK_total))
            self.count=int(self.count)+1
            self.player_count.setText(str(self.count))

        elif self.rb_ar.isChecked() and self.max_ar is not 0 and flag==0:
            self.max_ar = self.max_ar - 1
            All_total = self.ar_count.text()
            All_total = int(All_total)+1
            self.ar_count.setText(str(All_total))
            self.count=int(self.count)+1
            self.player_count.setText(str(self.count))
            
    def remove_names(self):
        self.count=int(self.count)-1
        self.player_count.setText(str(self.count))
        item = self.selectedplayer_list.takeItem(self.selectedplayer_list.currentRow())
        cur.execute("SELECT type FROM match WHERE player = '" + item.text() + "';")
        type_data = cur.fetchall()
        if type_data[0][0] == 'Batsman':
            if self.rb_bat.isChecked():
                self.availplayer_list .addItem(item)
            self.max_bat = self.max_bat + 1
            bat_total = self.bat_count.text()
            bat_total = int(bat_total)-1
            self.bat_count.setText(str(bat_total))
            
        elif type_data[0][0] == 'Bowler':
            if self.rb_bowl.isChecked():
                self.availplayer_list .addItem(item)
            self.max_bowl = self.max_bowl + 1
            bowl_total = self.bowl_count.text()
            bowl_total = int(bowl_total)-1
            self.bowl_count.setText(str(bowl_total))
            
        elif type_data[0][0] == 'WicketKeeper':
            if self.rb_wk.isChecked():
                self.availplayer_list .addItem(item)
            self.max_WK = self.max_WK + 1
            WK_total = self.wk_count.text()
            WK_total = int(WK_total)-1
            self.wk_count.setText(str(WK_total))
            
        elif type_data[0][0] == 'Allrounder':
            if self.rb_ar.isChecked():
                self.availplayer_list .addItem(item)
            self.max_ar = self.max_ar + 1
            All_total = self.ar_count.text()
            All_total = int(All_total)-1
            self.ar_count.setText(str(All_total))
            
        item = item.text()
        cur.execute("SELECT value FROM stats WHERE player = '" + item + "';")
        play_pt = cur.fetchall()
        actual_pt = self.pt_used.text()
        actual_pt = int(actual_pt) - int(play_pt[0][0])
        self.pt_used.setText(str(actual_pt))
        added_pt = self.pt_avail.text()
        add_pt = int(added_pt) + int(play_pt[0][0])
        self.pt_avail.setText(str(add_pt))

    def save_teams(self):
        msg = QMessageBox()
        team_list = []
        team_name = self.name.text()
        for x in range(self.selectedplayer_list.count()):
             team_list.append(self.selectedplayer_list.item(x).text())
        self.totalcount = len(team_list)
            
        if self.totalcount > 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('More than 11 players are not allowed!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
        
        elif self.totalcount < 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Less than 11 players are not allowed!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
            
        elif self.wk_count.text()=='0':
            msg.setIcon(QMessageBox.Warning)
            msg.setInformativeText('Team must contain 1 Wicket-keeper!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()

        else:
            try:
                for i in team_list:
                    cur.execute("SELECT points,type FROM match WHERE player = '" + str(i) + "';")
                    player_data = cur.fetchall()
                    cur.execute("INSERT INTO teams (name, players,cat, value) VALUES (?,?,?,?);", (team_name, i, player_data[0][1], player_data[0][0]))
                    conn.commit()
                    flag=0
            except:
                msg.setIcon(QMessageBox.Critical)
                msg.setInformativeText('Error in operation!')
                msg.setWindowTitle("Selection Error")
                msg.exec_()

            if flag==0:
                msg.setIcon(QMessageBox.Information)
                msg.setInformativeText('Team Saved Successfully!')
                msg.setWindowTitle("Team Saved")
                msg.exec_()
                self.file_evaluate()
                
    def file_open(self):
        self.open_screen.setupUi(self.openDialog)
        self.openDialog.show()
        self.open_screen.open_btn.clicked.connect(self.open_team)
        
    def open_team(self):
        self.SAVE.setEnabled(False)
        self.openDialog.close()
        self.reset()
        self.player_count.setText(str(11))
        teamname = self.open_screen.open_cb.currentText()
        self.name.setText(teamname)
        cur.execute("SELECT players from teams WHERE name= '" + teamname + "';")
        record = cur.fetchall()
        score = []
        for i in record:
            cur.execute("SELECT value from stats WHERE player='" + str(i[0]) + "';")
            y = cur.fetchone()
            score.append(y[0])
        for i in record:
             self.selectedplayer_list.addItem(i[0])
        sum = 0
        for i in score:
             sum += i
        total=1000-sum
        self.pt_avail.setText(str(total))
        self.pt_used.setText(str(sum))
        self.show_names()
        cur.execute("SELECT count(players) FROM teams WHERE cat ='Batsman' and name = '" + teamname + "'; ")
        bats_total = cur.fetchone()
        self.bat_count.setText(str(bats_total[0]))
        cur.execute("SELECT count(players) FROM teams WHERE cat ='Bowler' and name = '" + teamname + "'; ")
        bowl_total = cur.fetchone()
        self.bowl_count.setText(str(bowl_total[0]))
        cur.execute("SELECT count(players) FROM teams WHERE cat ='WicketKeeper' and name = '" + teamname + "'; ")
        wicket_total = cur.fetchone()
        self.wk_count.setText(str(wicket_total[0]))
        cur.execute("SELECT count(players) FROM teams WHERE cat ='Allrounder' and name = '" + teamname + "'; ")
        all_total = cur.fetchone()
        self.ar_count.setText(str(all_total[0]))
        self.availplayer_list.setEnabled(False)
        self.selectedplayer_list.setEnabled(False)
        
    def file_evaluate(self):
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.EvaluateWindow.show()

    def quit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText('Are you sure you want to quit?')
        msg.setWindowTitle("Fantasy Cricket League")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        value=msg.exec_()
        if value==QMessageBox.Yes:
            msg.setIcon(QMessageBox.Information)
            msg.setText('Thanks for Playing...............Hope you enjoyed!!')
            msg.setWindowTitle("Fantasy Cricket League")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
