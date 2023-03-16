# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readfile.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 816)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 1001, 761))
        self.tabWidget.setMinimumSize(QtCore.QSize(1001, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(21, 21, 21);\n"
"color: rgb(0, 0, 0);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(240, 360, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboport = QtWidgets.QComboBox(self.tab)
        self.comboport.setGeometry(QtCore.QRect(330, 540, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboport.setFont(font)
        self.comboport.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboport.setObjectName("comboport")
        self.port_text = QtWidgets.QLabel(self.tab)
        self.port_text.setGeometry(QtCore.QRect(330, 470, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.port_text.setFont(font)
        self.port_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.port_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.port_text.setObjectName("port_text")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(290, 30, 331, 301))
        self.label_12.setStyleSheet("")
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/image/ele.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.connectbt = QtWidgets.QPushButton(self.tab)
        self.connectbt.setGeometry(QtCore.QRect(610, 550, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.connectbt.setFont(font)
        self.connectbt.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.connectbt.setObjectName("connectbt")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 471, 481))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(14, 189, 154);\n"
"color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.status1 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.status1.setGeometry(QtCore.QRect(20, 40, 431, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status1.setFont(font)
        self.status1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.status1.setObjectName("status1")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(890, 260, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(520, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(600, 245, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(600, 45, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(600, 145, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(890, 160, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(520, 260, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(520, 160, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(890, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(30, 30, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 255, 255);\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(890, 350, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.x1 = QtWidgets.QPushButton(self.tab_2)
        self.x1.setGeometry(QtCore.QRect(530, 450, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.x1.setFont(font)
        self.x1.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.x1.setObjectName("x1")
        self.y1 = QtWidgets.QPushButton(self.tab_2)
        self.y1.setGeometry(QtCore.QRect(630, 400, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.y1.setFont(font)
        self.y1.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.y1.setObjectName("y1")
        self.y2 = QtWidgets.QPushButton(self.tab_2)
        self.y2.setGeometry(QtCore.QRect(630, 500, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.y2.setFont(font)
        self.y2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.y2.setObjectName("y2")
        self.hb = QtWidgets.QPushButton(self.tab_2)
        self.hb.setGeometry(QtCore.QRect(630, 450, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hb.setFont(font)
        self.hb.setStyleSheet("background-color: rgb(255, 121, 3);")
        self.hb.setObjectName("hb")
        self.z2 = QtWidgets.QPushButton(self.tab_2)
        self.z2.setGeometry(QtCore.QRect(860, 470, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.z2.setFont(font)
        self.z2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.z2.setObjectName("z2")
        self.x2 = QtWidgets.QPushButton(self.tab_2)
        self.x2.setGeometry(QtCore.QRect(730, 450, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.x2.setFont(font)
        self.x2.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.x2.setObjectName("x2")
        self.z1 = QtWidgets.QPushButton(self.tab_2)
        self.z1.setGeometry(QtCore.QRect(860, 420, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.z1.setFont(font)
        self.z1.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.z1.setObjectName("z1")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(640, 350, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.test1 = QtWidgets.QPushButton(self.tab_2)
        self.test1.setGeometry(QtCore.QRect(560, 560, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.test1.setFont(font)
        self.test1.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 255, 0);")
        self.test1.setObjectName("test1")
        self.test2 = QtWidgets.QPushButton(self.tab_2)
        self.test2.setGeometry(QtCore.QRect(740, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.test2.setFont(font)
        self.test2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.test2.setObjectName("test2")
        self.back1 = QtWidgets.QPushButton(self.tab_2)
        self.back1.setGeometry(QtCore.QRect(70, 640, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back1.setFont(font)
        self.back1.setStyleSheet("background-color: rgb(255, 233, 219);")
        self.back1.setObjectName("back1")
        self.next1 = QtWidgets.QPushButton(self.tab_2)
        self.next1.setGeometry(QtCore.QRect(280, 640, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.next1.setFont(font)
        self.next1.setStyleSheet("background-color: rgb(255, 233, 219);")
        self.next1.setObjectName("next1")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(40, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.stopbt = QtWidgets.QPushButton(self.tab_3)
        self.stopbt.setGeometry(QtCore.QRect(790, 230, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.stopbt.setFont(font)
        self.stopbt.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.stopbt.setObjectName("stopbt")
        self.stratbt = QtWidgets.QPushButton(self.tab_3)
        self.stratbt.setGeometry(QtCore.QRect(600, 230, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.stratbt.setFont(font)
        self.stratbt.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 255, 0);")
        self.stratbt.setObjectName("stratbt")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(80, 100, 471, 481))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(14, 189, 154);\n"
"color: rgb(255, 255, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.status2 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.status2.setGeometry(QtCore.QRect(20, 40, 431, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status2.setFont(font)
        self.status2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.status2.setObjectName("status2")
        self.hb_2 = QtWidgets.QPushButton(self.tab_3)
        self.hb_2.setGeometry(QtCore.QRect(710, 320, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.hb_2.setFont(font)
        self.hb_2.setStyleSheet("background-color: rgb(255, 121, 3);")
        self.hb_2.setObjectName("hb_2")
        self.openfile = QtWidgets.QPushButton(self.tab_3)
        self.openfile.setGeometry(QtCore.QRect(700, 130, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.openfile.setFont(font)
        self.openfile.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.openfile.setObjectName("openfile")
        self.back2 = QtWidgets.QPushButton(self.tab_3)
        self.back2.setGeometry(QtCore.QRect(40, 630, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back2.setFont(font)
        self.back2.setStyleSheet("background-color: rgb(255, 233, 219);")
        self.back2.setObjectName("back2")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionAuto = QtWidgets.QAction(MainWindow)
        self.actionAuto.setObjectName("actionAuto")
        self.actionBrowefile = QtWidgets.QAction(MainWindow)
        self.actionBrowefile.setObjectName("actionBrowefile")
        self.actionMain = QtWidgets.QAction(MainWindow)
        self.actionMain.setObjectName("actionMain")
        self.actionManual_2 = QtWidgets.QAction(MainWindow)
        self.actionManual_2.setObjectName("actionManual_2")
        self.actionAuto_2 = QtWidgets.QAction(MainWindow)
        self.actionAuto_2.setObjectName("actionAuto_2")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pick and Place Machine"))
        self.port_text.setText(_translate("MainWindow", "Port"))
        self.connectbt.setText(_translate("MainWindow", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status"))
        self.label_4.setText(_translate("MainWindow", "mm"))
        self.label_5.setText(_translate("MainWindow", "X :"))
        self.lineEdit_5.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt;\"><br/></span></p></body></html>as"))
        self.lineEdit_5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.lineEdit_3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt;\"><br/></span></p></body></html>"))
        self.lineEdit_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.lineEdit_4.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt;\"><br/></span></p></body></html>"))
        self.lineEdit_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "mm"))
        self.label_7.setText(_translate("MainWindow", "Z :"))
        self.label_6.setText(_translate("MainWindow", "Y :"))
        self.label_2.setText(_translate("MainWindow", "mm"))
        self.label_9.setText(_translate("MainWindow", "Manual Mode"))
        self.label_11.setText(_translate("MainWindow", "Z"))
        self.x1.setText(_translate("MainWindow", "←"))
        self.y1.setText(_translate("MainWindow", "↑"))
        self.y2.setText(_translate("MainWindow", "↓"))
        self.hb.setText(_translate("MainWindow", "HOME "))
        self.z2.setText(_translate("MainWindow", "Down"))
        self.x2.setText(_translate("MainWindow", "→"))
        self.z1.setText(_translate("MainWindow", "Up"))
        self.label_10.setText(_translate("MainWindow", "X/Y"))
        self.test1.setText(_translate("MainWindow", "PICK"))
        self.test2.setText(_translate("MainWindow", "PLACE"))
        self.back1.setText(_translate("MainWindow", "Back"))
        self.next1.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Manual"))
        self.label_8.setText(_translate("MainWindow", "Auto Mode"))
        self.stopbt.setText(_translate("MainWindow", "Stop"))
        self.stratbt.setText(_translate("MainWindow", "Start"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Status"))
        self.hb_2.setText(_translate("MainWindow", "HOME "))
        self.openfile.setText(_translate("MainWindow", "Open File"))
        self.back2.setText(_translate("MainWindow", "Back"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Auto"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionAuto.setText(_translate("MainWindow", "Auto"))
        self.actionBrowefile.setText(_translate("MainWindow", "Open File"))
        self.actionMain.setText(_translate("MainWindow", "Main"))
        self.actionManual_2.setText(_translate("MainWindow", "Manual Mode"))
        self.actionAuto_2.setText(_translate("MainWindow", "Auto Mode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())