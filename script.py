# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(316, 473)
        MainWindow.setStyleSheet("background-color=\'#000\'")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(80, 350, 78, 50))
        self.btn2.setObjectName("btn2")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(80, 400, 78, 50))
        self.btn0.setObjectName("btn0")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(158, 350, 78, 50))
        self.btn3.setObjectName("btn3")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(2, 350, 78, 50))
        self.btn1.setObjectName("btn1")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(80, 300, 78, 50))
        self.btn5.setObjectName("btn5")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(2, 300, 78, 50))
        self.btn4.setObjectName("btn4")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(158, 300, 78, 50))
        self.btn6.setObjectName("btn6")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(158, 250, 78, 50))
        self.btn9.setObjectName("btn9")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(80, 250, 78, 50))
        self.btn8.setObjectName("btn8")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(2, 250, 78, 50))
        self.btn7.setObjectName("btn7")
        self.btnResult = QtWidgets.QPushButton(self.centralwidget)
        self.btnResult.setGeometry(QtCore.QRect(236, 400, 78, 50))
        self.btnResult.setObjectName("btnResult")
        self.btnMinus = QtWidgets.QPushButton(self.centralwidget)
        self.btnMinus.setGeometry(QtCore.QRect(236, 300, 78, 50))
        self.btnMinus.setObjectName("btnMinus")
        self.btnMultiple = QtWidgets.QPushButton(self.centralwidget)
        self.btnMultiple.setGeometry(QtCore.QRect(236, 250, 78, 50))
        self.btnMultiple.setObjectName("btnMultiple")
        self.btnPlus = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlus.setGeometry(QtCore.QRect(236, 350, 78, 50))
        self.btnPlus.setObjectName("btnPlus")
        self.btnDivide = QtWidgets.QPushButton(self.centralwidget)
        self.btnDivide.setGeometry(QtCore.QRect(236, 200, 78, 50))
        self.btnDivide.setMouseTracking(False)
        self.btnDivide.setObjectName("btnDivide")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(10, 30, 291, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelResult.sizePolicy().hasHeightForWidth())
        self.labelResult.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelResult.setFont(font)
        self.labelResult.setTextFormat(QtCore.Qt.AutoText)
        self.labelResult.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelResult.setObjectName("labelResult")
        self.btnErase = QtWidgets.QPushButton(self.centralwidget)
        self.btnErase.setGeometry(QtCore.QRect(236, 150, 78, 50))
        self.btnErase.setMouseTracking(False)
        self.btnErase.setObjectName("btnErase")
        self.btnDot = QtWidgets.QPushButton(self.centralwidget)
        self.btnDot.setGeometry(QtCore.QRect(158, 400, 78, 50))
        self.btnDot.setObjectName("btnDot")
        self.btnNegate = QtWidgets.QPushButton(self.centralwidget)
        self.btnNegate.setGeometry(QtCore.QRect(2, 400, 78, 50))
        self.btnNegate.setObjectName("btnNegate")
        self.btnC = QtWidgets.QPushButton(self.centralwidget)
        self.btnC.setGeometry(QtCore.QRect(158, 150, 78, 50))
        self.btnC.setMouseTracking(False)
        self.btnC.setObjectName("btnC")
        self.btnCE = QtWidgets.QPushButton(self.centralwidget)
        self.btnCE.setGeometry(QtCore.QRect(80, 150, 78, 50))
        self.btnCE.setMouseTracking(False)
        self.btnCE.setObjectName("btnCE")
        self.btnRoot = QtWidgets.QPushButton(self.centralwidget)
        self.btnRoot.setGeometry(QtCore.QRect(158, 200, 78, 50))
        self.btnRoot.setMouseTracking(False)
        self.btnRoot.setObjectName("btnRoot")
        self.btnSqr = QtWidgets.QPushButton(self.centralwidget)
        self.btnSqr.setGeometry(QtCore.QRect(80, 200, 78, 50))
        self.btnSqr.setMouseTracking(False)
        self.btnSqr.setObjectName("btnSqr")
        self.btnPercent = QtWidgets.QPushButton(self.centralwidget)
        self.btnPercent.setGeometry(QtCore.QRect(2, 150, 78, 50))
        self.btnPercent.setMouseTracking(False)
        self.btnPercent.setObjectName("btnPercent")
        self.btnInvert = QtWidgets.QPushButton(self.centralwidget)
        self.btnInvert.setGeometry(QtCore.QRect(2, 200, 78, 50))
        self.btnInvert.setMouseTracking(False)
        self.btnInvert.setObjectName("btnInvert")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 316, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

                # Set up buttons to execute function
        self.btn0.clicked.connect(lambda: self.clicked(self.btn0.text()))
        self.btn1.clicked.connect(lambda: self.clicked(self.btn1.text()))
        self.btn2.clicked.connect(lambda: self.clicked(self.btn2.text()))
        self.btn3.clicked.connect(lambda: self.clicked(self.btn3.text()))
        self.btn4.clicked.connect(lambda: self.clicked(self.btn4.text()))
        self.btn5.clicked.connect(lambda: self.clicked(self.btn5.text()))
        self.btn6.clicked.connect(lambda: self.clicked(self.btn6.text()))
        self.btn7.clicked.connect(lambda: self.clicked(self.btn7.text()))
        self.btn8.clicked.connect(lambda: self.clicked(self.btn8.text()))
        self.btn9.clicked.connect(lambda: self.clicked(self.btn9.text()))
                
        self.btnPlus.clicked.connect(lambda: self.clicked(self.btnPlus.text()))
        self.btnMinus.clicked.connect(lambda: self.clicked(self.btnMinus.text()))
        self.btnMultiple.clicked.connect(lambda: self.clicked(self.btnMultiple.text()))
        self.btnDivide.clicked.connect(lambda: self.clicked(self.btnDivide.text()))

        self.btnErase.clicked.connect(lambda: self.clicked(self.btnErase.text()))
        self.btnNegate.clicked.connect(lambda: self.clicked(self.btnNegate.text()))
        self.btnDot.clicked.connect(lambda: self.clicked(self.btnDot.text()))
        self.btnC.clicked.connect(lambda: self.clicked(self.btnC.text()))
        self.btnCE.clicked.connect(lambda: self.clicked(self.btnCE.text()))
        self.btnPercent.clicked.connect(lambda: self.clicked(self.btnPercent.text()))
        self.btnSqr.clicked.connect(lambda: self.clicked(self.btnSqr.text()))
        self.btnRoot.clicked.connect(lambda: self.clicked(self.btnRoot.text()))
        self.btnInvert.clicked.connect(lambda: self.clicked(self.btnInvert.text()))
                
        self.btnResult.clicked.connect(lambda: self.clicked(self.btnResult.text()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn2.setShortcut(_translate("MainWindow", "2"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn0.setShortcut(_translate("MainWindow", "0"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn3.setShortcut(_translate("MainWindow", "3"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn1.setShortcut(_translate("MainWindow", "1"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn5.setShortcut(_translate("MainWindow", "5"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn4.setShortcut(_translate("MainWindow", "4"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn6.setShortcut(_translate("MainWindow", "6"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn9.setShortcut(_translate("MainWindow", "9"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn8.setShortcut(_translate("MainWindow", "8"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn7.setShortcut(_translate("MainWindow", "7"))
        self.btnResult.setText(_translate("MainWindow", "="))
        self.btnResult.setShortcut(_translate("MainWindow", "Enter"))
        self.btnMinus.setText(_translate("MainWindow", "-"))
        self.btnMinus.setShortcut(_translate("MainWindow", "-"))
        self.btnMultiple.setText(_translate("MainWindow", "*"))
        self.btnMultiple.setShortcut(_translate("MainWindow", "*"))
        self.btnPlus.setText(_translate("MainWindow", "+"))
        self.btnPlus.setShortcut(_translate("MainWindow", "+"))
        self.btnDivide.setText(_translate("MainWindow", "/"))
        self.btnDivide.setShortcut(_translate("MainWindow", "/"))
        self.labelResult.setText(_translate("MainWindow", "0"))
        self.btnErase.setText(_translate("MainWindow", "<-"))
        self.btnErase.setShortcut(_translate("MainWindow", "Backspace"))
        self.btnDot.setText(_translate("MainWindow", "."))
        self.btnDot.setShortcut(_translate("MainWindow", ",, ."))
        self.btnNegate.setText(_translate("MainWindow", "+/-"))
        self.btnC.setText(_translate("MainWindow", "C"))
        self.btnCE.setText(_translate("MainWindow", "CE"))
        self.btnRoot.setText(_translate("MainWindow", "√x"))
        self.btnSqr.setText(_translate("MainWindow", "x²"))
        self.btnPercent.setText(_translate("MainWindow", "%"))
        self.btnInvert.setText(_translate("MainWindow", "1/x"))
    
    def clicked(self, text):
        import re
        from math import sqrt

        def sqr(x):
            return x**2

        count = self.labelResult.text()
        numbers = count
        numbers = re.split(r'[- + * /]', numbers) # Create a list of numbers separating by operators
        n = numbers[len(numbers)-1] # Number of numbers 
        others = ['=', '+/-', '<-', '.', 'C', 'CE', '√x', '1/x', 'x²', '%'] # Characters that can't be directly inserted in count
        #ops = ['+', '-', '*', '/']
        #nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        
        if text not in others: # In case the program only needs to add character at the end of our count
            if count[len(count)-1] == ')':
                index = count.find(n)
                count = count[:index] + text
            else:
                count = count+str(text)
                
            count = str(count)
            #print(n)
            if n != '':
                if n[0] == '0': # Remove left zeros
                    count = count.replace(n, n[1:])
        else:            
            if text == '=':
                count = count.replace('√', 'sqrt')
                count = str(round(eval(count), 5)) # Count the value on string
                
            elif text == '<-':
                count = count[:-1] # Erase last number
                if count == '':
                    count = '0' # Makes sure the display don't show nothing

            elif text == '+/-':
                if count[0] != '-': # Add Minus if it doesn't have
                    count = '-'+count 
                else:  # Remove Minus if it's there
                    count = count[1:]

            elif text == '.': 
                if '.' not in n: # Allow to insert "." if there isn't any in that number 
                    if n == '': 
                        count = count+'0.' # If there is no number after operator, put "0."
                    else:
                        count = count+str(text)
            
            elif text == 'C':
                count = '0' # Erase everything

            elif text == 'CE':
                count = count.replace(n, '0') # Erase latest number

            elif text == '√x':
                if n == '':
                    count = count+'√(0)'
                else:
                    index = count.find(n) 
                    count = count[:index] + '√(' + count[index:] + ')' # Put latest number in between  '√()' so the program process it to make the sqrt()

            elif text == 'x²':
                if n == '':
                    count = count+'√(0)'
                else:
                    index = count.find(n) 
                    count = count[:index] + 'sqr(' + count[index:] + ')' # Put latest number in between  'sqr()'
            
            #elif text == '%':
            #    index = count.find(n[len(n)-2])
            #    if '.' in n:
            #        index = count.find(n[len(n)-2])
            #        print(index)
            #    else:
            #        count = count[:index] + '.' + count[index:]

            elif text == '1/x':
                if n != '0' and n != '':
                    index = count.find(n) # Get latest number
                    count = count[:index] + '(1/' + count[index:] + ')' # Put number in between (1/number)

        self.labelResult.setText(str(count)) # Show count

if __name__ == "__main__":
    import sys
            
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())