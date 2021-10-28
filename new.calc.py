# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 485)
        Form.setStyleSheet("background-color: rgb(112, 83, 37);")
        self.pushButton_1 = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("1"))
        self.pushButton_1.setGeometry(QtCore.QRect(30, 120, 71, 51))
        self.pushButton_1.setStyleSheet("background-color:rgb(255, 241, 160)")
        self.pushButton_1.setObjectName("pushButton_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 60, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(255, 255, 212)")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("2"))
        self.pushButton_2.setGeometry(QtCore.QRect(110, 120, 71, 51))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 241, 160)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("3"))
        self.pushButton_3.setGeometry(QtCore.QRect(190, 120, 71, 51))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 241, 160)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("4"))
        self.pushButton_4.setGeometry(QtCore.QRect(30, 180, 71, 51))
        self.pushButton_4.setStyleSheet("background-color:rgb(255, 241, 160)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("5"))
        self.pushButton_5.setGeometry(QtCore.QRect(110, 180, 71, 51))
        self.pushButton_5.setStyleSheet("background-color:rgb(255, 241, 160)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("6"))
        self.pushButton_6.setGeometry(QtCore.QRect(190, 180, 71, 51))
        self.pushButton_6.setStyleSheet("background-color:rgb(255, 241, 160)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("7"))
        self.pushButton_7.setGeometry(QtCore.QRect(30, 250, 71, 51))
        self.pushButton_7.setStyleSheet("background-color:rgb(255, 241, 160)")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("8"))
        self.pushButton_8.setGeometry(QtCore.QRect(110, 250, 71, 51))
        self.pushButton_8.setStyleSheet("background-color:rgb(255, 241, 160)")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("9"))
        self.pushButton_9.setGeometry(QtCore.QRect(190, 250, 71, 51))
        self.pushButton_9.setStyleSheet("background-color:rgb(255, 241, 160)")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_equal = QtWidgets.QPushButton(Form, clicked = lambda: self.math())
        self.pushButton_equal.setGeometry(QtCore.QRect(30, 320, 71, 51))
        self.pushButton_equal.setStyleSheet("background-color: rgb(255, 255, 212)")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_0 = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("0"))
        self.pushButton_0.setGeometry(QtCore.QRect(110, 320, 71, 51))
        self.pushButton_0.setStyleSheet("background-color:rgb(255, 241, 160)")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_decimal = QtWidgets.QPushButton(Form, clicked = lambda: self.dot())
        self.pushButton_decimal.setGeometry(QtCore.QRect(190, 320, 71, 51))
        self.pushButton_decimal.setStyleSheet("background-color: rgb(255, 255, 212)")
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        self.pushButton_divide = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("/"))
        self.pushButton_divide.setGeometry(QtCore.QRect(280, 320, 71, 51))
        self.pushButton_divide.setStyleSheet("background-color: rgb(255, 255, 212)")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_minus = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("-"))
        self.pushButton_minus.setGeometry(QtCore.QRect(280, 180, 71, 51))
        self.pushButton_minus.setStyleSheet("background-color: rgb(255, 255, 212)")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_add = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("+"))
        self.pushButton_add.setGeometry(QtCore.QRect(280, 120, 71, 51))
        self.pushButton_add.setStyleSheet("background-color: rgb(255, 255, 212)")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_time = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("*"))
        self.pushButton_time.setGeometry(QtCore.QRect(280, 250, 71, 51))
        self.pushButton_time.setStyleSheet("background-color: rgb(255, 255, 212)")
        self.pushButton_time.setObjectName("pushButton_time")
        self.pushButton_CE = QtWidgets.QPushButton(Form, clicked = lambda: self.ce())
        self.pushButton_CE.setGeometry(QtCore.QRect(60, 390, 81, 41))
        self.pushButton_CE.setStyleSheet("background-color: rgb(255, 255, 212)")
        self.pushButton_CE.setObjectName("pushButton_CE")
        self.pushButton_C = QtWidgets.QPushButton(Form, clicked = lambda: self.press_it("C"))
        self.pushButton_C.setGeometry(QtCore.QRect(150, 390, 81, 41))
        self.pushButton_C.setStyleSheet("background-color: rgb(255, 255, 212)")
        self.pushButton_C.setObjectName("pushButton_C")
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.pushButton_Del = QtWidgets.QPushButton(Form, clicked = lambda: self.delete())
        self.pushButton_Del.setGeometry(QtCore.QRect(240, 390, 81, 41))
        self.pushButton_Del.setStyleSheet("background-color: rgb(255, 255, 212)")
        self.pushButton_Del.setObjectName("pushButton_Del")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def delete(self):
        screen = self.label.text()
        screen = screen[:-1]
        self.label.setText(screen)

    def ce(self):
        screen = self.label.text()
        x = -1
        symbol = ["+", "-", '*', '/']
        symsym = 0
        for i in screen:
            if i in symbol:
                symsym += 1
        if symsym == 0:
            self.label.setText("0")
        else:
            while screen[x] not in symbol:
                screen = screen[:x]
            self.label.setText(screen)
        
    def dot(self):
        screen = self.label.text()
        if screen[-1] != '.':
            self.label.setText(f'{screen}.')
    
    def math(self):
        screen = self.label.text()
        try:
            answer = eval(screen)
            self.label.setText(str(answer))
        except:
            self.label.setText("ERROR")

    def press_it(self, pressed):
        screen = self.label.text()
        symbol = ["+", "-", '*', '/']
        if pressed == 'C':
            self.label.setText("0")
        elif pressed in symbol and screen[-1] in symbol:
            screen = screen[:-1]
            self.label.setText(screen + pressed)
        elif pressed in symbol and screen[-1] == '.' :
            screen = screen[:-1]
            self.label.setText(screen + pressed)
        else:
            if self.label.text() == "0":
                self.label.setText("")
            self.label.setText(f'{self.label.text()}{pressed}')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.label.setText(_translate("Form", "0"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_equal.setText(_translate("Form", "="))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_decimal.setText(_translate("Form", "."))
        self.pushButton_divide.setText(_translate("Form", "/"))
        self.pushButton_minus.setText(_translate("Form", "-"))
        self.pushButton_add.setText(_translate("Form", "+"))
        self.pushButton_time.setText(_translate("Form", "*"))
        self.pushButton_CE.setText(_translate("Form", "CE"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.pushButton_Del.setText(_translate("Form", "Del"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())