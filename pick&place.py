from PyQt5 import QtCore, QtGui, QtWidgets 
import sys
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from readfile4 import Ui_MainWindow
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
from PyQt5.QtWidgets import QFileDialog
import serial
import time as tm
from tkinter import *
from tkinter import filedialog
import serial.tools.list_ports as port_list
import importlib
import os
import image

class readfile4(Ui_MainWindow):
    def __init__(self) -> None:
        super().setupUi(MainWindow)
        os.chdir(r'D:\project_1\mortor')
        MainWindow.setWindowTitle("PICK AND PLACE PROGRAM")
        MainWindow.setWindowIcon(QtGui.QIcon("bam.png"))

        self.gcn()
        self.timerfn1()
        self.timerfn3()
        self.connect_serial()
        self.xval = 0
        self.yval = 0
        self.zval = 0
        self.n=0
        self.i = 0
        self.i1 = 0
        self.reedfunc1= []

        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,False)

    def connect_serial(self):
        self.ports = list(port_list.comports())
        for self.p in self.ports:
            self.comboport.addItem(self.p.name)

    def gcn(self):
        self.back1.clicked.connect(self.backclick1)
        self.back2.clicked.connect(self.backclick2)
        self.next1.clicked.connect(self.nextclick)
        self.connectbt.clicked.connect(self.connectclick)
        self.x1.clicked.connect(self.x1click)
        self.x2.clicked.connect(self.x2click)
        self.y1.clicked.connect(self.y1click)
        self.y2.clicked.connect(self.y2click)
        self.z1.clicked.connect(self.z1click)
        self.z2.clicked.connect(self.z2click)
        self.hb.clicked.connect(self.homeclick1)
        self.hb_2.clicked.connect(self.homeclick2)
        self.lineEdit_3.textChanged.connect(self.setx)
        self.lineEdit_4.textChanged.connect(self.sety)
        self.lineEdit_5.textChanged.connect(self.setz)
        self.stratbt.clicked.connect(self.autost)
        self.stopbt.clicked.connect(self.autosp)
        self.test1.clicked.connect(self.test_1)
        self.test2.clicked.connect(self.test_2)
        self.comboport.currentIndexChanged.connect(self.portserial_func)
        self.openfile.clicked.connect(self.openfileclick)

    def connectclick(self):
        self.tabWidget.setCurrentIndex(1)
        self.comboport.setEnabled(False)
        self.tabWidget.setTabEnabled(0,False)
        self.tabWidget.setTabEnabled(1,True)
        self.tabWidget.setTabEnabled(2,False)

    def backclick1(self):
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabEnabled(0,True)
        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,False)

    def backclick2(self):
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget.setTabEnabled(1,True)
        self.tabWidget.setTabEnabled(0,False)
        self.tabWidget.setTabEnabled(2,False)

    def nextclick(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget.setTabEnabled(2,True)
        self.tabWidget.setTabEnabled(0,False)
        self.tabWidget.setTabEnabled(1,False)
        self.openfile.setEnabled(False)
        self.stratbt.setEnabled(False)
        self.stopbt.setEnabled(False)

    def portserial_func(self):
        try :
            self.portdata = self.comboport.currentText()
            self.ser = serial.Serial(self.portdata,115200)
            self.enable_func()
            print(self.portdata)
        except :
            pass

    def openfileclick(self):
        self.openfile.setEnabled(False)
        self.hb_2.setEnabled(False)
        self.stratbt.setEnabled(True)
        print('open')
        try :
            self.dialog = QFileDialog().getOpenFileName()
            print(self.dialog[0])
            # self.status2.appendPlainText("Select file :"+str(self.dialog[0]))
            
            self.opf = open(self.dialog[0],'r', encoding='utf-16', errors='ignore')
            self.lines = self.opf.readlines()
            self.list_cutout = [str(x) for x in range(0, 9)]
            self.list_cutout.append('.')
            self.list_cutout.append('-')
            self.data1 = []
            self.data2 = []
            self.value1=0
            self.lendata1 = 0
            self.status2.appendPlainText("Select file :"+str(self.dialog[0]))
            for self.i in range(1,len(self.lines)):
                self.data1.append(self.lines[self.i].strip().split('\t'))
            self.lendata1 = len(self.data1)
        except :
            self.status2.appendPlainText("Select file : Not Select file??")
            self.openfile.setEnabled(True)
            self.stratbt.setEnabled(False)


    def timerfn1(self):
        self.tm1 = QtCore.QTimer()
        self.tm1.timeout.connect(self.autofn)

    def timerfn3(self):
        self.tm3 = QtCore.QTimer()
        self.tm3.timeout.connect(self.autost)

    def autofn(self):
        try:
            self.status2.appendPlainText("In progress")   
            self.name = 0
            self.lendata1 = self.lendata1-1
            if self.lendata1 == 7:
                self.status2.appendPlainText("Success")
                self.tm3.stop()
                self.tm1.stop()
            if self.lendata1 < 7:
                self.tm1.stop()
                self.lendata1 = len(self.data1)
            self.data2 =self.data1[self.lendata1]
            # print(self.data2)
            for self.i in range(len(self.data2[2])):
                if self.data2[2][self.i] == 'm':
                    self.pointer = self.i
            for self.i1 in range(len(self.data2[3])):
                if self.data2[3][self.i1] == 'm':
                    self.pointer1 = self.i1
            for self.i2 in range(len(self.data2[1])):
                if self.data2[1][self.i2] == 'R':
                    self.pointer2 = self.data2[1][self.i2]
                    self.ser.write(("c"+str((self.pointer2))).encode())
                    print("c")
                    tm.sleep(3)
                    self.ser.write(("v"+str((self.pointer2))).encode())
                    print("v")
                    tm.sleep(2)
                    self.ser.write(("s"+str((self.pointer2))).encode())
                    print("s")
                    tm.sleep(2)
                    self.ser.write(("b"+str((self.pointer2))).encode())
                    print("b")
                    tm.sleep(2)
                    self.ser.write(("n"+str((self.pointer2))).encode())
                    print("n")
                    tm.sleep(2)
                    self.ser.write(("m"+str((self.pointer2))).encode())
                    print("m")
                    tm.sleep(2)
                    self.ser.write(("j"+str((self.pointer2))).encode())
                    print("j")
                    tm.sleep(2)
                    self.ser.write(("a"+str((self.pointer2))).encode())
                    print("a")
                    tm.sleep(2)
                    self.ser.write(("g"+str((self.pointer2))).encode())
                    print("g")
                    tm.sleep(2)
                    self.ser.write(("f"+str((self.pointer2))).encode())
                    print("f")
                    tm.sleep(2)

            for self.i3 in range(len(self.data2[1])):
                if self.data2[1][self.i3] == 'C':
                    self.pointer3 = self.data2[1][self.i3]
                    self.ser.write(("w"+str((self.pointer3))).encode())
                    print("w")
                    tm.sleep(2)
                    self.ser.write(("e"+str((self.pointer3))).encode())
                    print("e")
                    tm.sleep(2)
                    self.ser.write(("p"+str((self.pointer3))).encode())
                    print("p")
                    tm.sleep(2)
                    self.ser.write(("1"+str((self.pointer3))).encode())
                    print("1")
                    tm.sleep(2)
                    self.ser.write(("2"+str((self.pointer3))).encode())
                    print("2")
                    tm.sleep(2)
                    self.ser.write(("3"+str((self.pointer3))).encode())
                    print("3")
                    tm.sleep(2)
                    self.ser.write(("4"+str((self.pointer3))).encode())
                    print("4")
                    tm.sleep(2)
                    self.ser.write(("5"+str((self.pointer3))).encode())
                    print("5")
                    tm.sleep(2)
                    self.ser.write(("a"+str((self.pointer3))).encode())
                    print("a")
                    tm.sleep(2)
                    self.ser.write(("6"+str((self.pointer3))).encode())
                    print("6")
                    tm.sleep(2)
                    self.ser.write(("7"+str((self.pointer3))).encode())
                    print("7")
                    tm.sleep(2)

            self.rad1 = 0 
            self.p3 = self.data2[9][1:]+'i'
            for self.j3 in range(len(self.p3)):
                if self.p3[self.j3] == 'i':
                    self.pointer4 = self.j3
                    self.rad1 = int(self.p3[:self.pointer4-1])

            self.value1 = ((float(self.data2[2][1:self.pointer-1]))**2)**0.5
            self.value2 = ((float(self.data2[3][1:self.pointer1-1]))**2)**0.5
            self.value3 = (int(self.data2[9][1:self.pointer4]))
            
            tm.sleep(2)

            self.ser.write(("o"+str((self.value1*10)+3)).encode())
            print("o")
            tm.sleep(1)
        
            self.ser.write(("y"+str((self.value2*10)-18)).encode()) 
            print("y")
            tm.sleep(1)

            self.ser.write(("t"+str((self.value3*4.444444))).encode())
            print("t")
            tm.sleep(1)
                
            self.ser.write(("i"+str(70*10)).encode()) 
            print("i")
            tm.sleep(2)

            self.ser.write(("d").encode())
            print("d")
            tm.sleep(2)

            self.ser.write(("z"+str(70*10)).encode()) 
            print("z")
            tm.sleep(1)

            self.ser.write(("r"+str((self.value3*4.444444))).encode())
            print("r")
            tm.sleep(1)

            self.ser.write(("u"+str((self.value2*10)-18)).encode())
            print("u")
            tm.sleep(1)
            
            self.ser.write(("x"+str((self.value1*10)+3)).encode())
            print("x")
            tm.sleep(1)

            self.openfile.setEnabled(True)
            
        except  IndexError:
            print('IndexError')
        except AttributeError:
            self.status2.appendPlainText("Not Select file??")
            self.ser.write("d".encode())

    def autost(self):
        print("start")
        self.status2.appendPlainText("Start Auto Mode!")
        self.stratbt.setDisabled(True)
        self.openfile.setDisabled(True)
        self.hb.setDisabled(True)
        self.stopbt.setDisabled(False)
        self.tm1.start(1000)

    def test_1(self):
        self.status1.appendPlainText("Pick Mode")
        self.ser.write("a".encode())

    def test_2(self):
        self.status1.appendPlainText("Place Mode")
        self.ser.write("d".encode())          
    
    def autosp(self):
        print("stop")
        self.status2.appendPlainText("Stop Auto Mode")
        self.stopbt.setDisabled(True)
        self.stratbt.setDisabled(False)
        self.tm1.stop()

    def setx(self):
        pass

    def sety(self):
        pass

    def setz(self):
        pass

    def x1click(self):
        self.xval -= 1
        self.lineEdit_3.setText(str(self.xval))
        self.linex1 = float(self.xval) 
        self.ser.write(('x'+(str(10))).encode())

    def x2click(self):
        self.xval += 1
        self.lineEdit_3.setText(str(self.xval))
        self.linex2 = float(self.xval) 
        self.ser.write(('o'+str(10)).encode())

    def y1click(self):
        self.yval += 1
        self.lineEdit_4.setText(str(self.yval))
        self.liney1 = float(self.yval)
        self.ser.write(("y"+str(10)).encode())  

    def y2click(self):
        self.yval -= 1
        self.lineEdit_4.setText(str(self.yval))
        self.liney2 = float(self.yval)
        self.ser.write(("u"+str(10)).encode())
        
    def z1click(self):
        self.zval += 1
        self.lineEdit_5.setText(str(self.zval))
        self.linez1 = float(self.zval)
        self.ser.write(("z"+str(10)).encode())     

    def z2click(self):
        self.zval -= 1
        self.lineEdit_5.setText(str(self.zval))
        self.linez2 = float(self.zval)
        self.ser.write(("i"+str(10)).encode()) 

    def homeclick1(self):
        self.status1.appendPlainText("Home Mode")
        self.ser.write(("l").encode())
        self.ser.write(("k").encode())
        self.ser.write(("q").encode())
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        print('home')

    def homeclick2(self):
        self.status2.appendPlainText("Home Mode")
        self.ser.write(("l").encode())
        self.ser.write(("k").encode())
        self.ser.write(("q").encode())
        self.openfile.setEnabled(True)
        print('home')
     
if __name__ == "__main__":
    obj = readfile4()
    MainWindow.show()
    sys.exit(app.exec_())