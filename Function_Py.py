# -*- coding: utf-8 -*-
import sys
from sympy import *
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(423, 163)
        Widget.setMinimumSize(QSize(423, 163))
        Widget.setMaximumSize(QSize(423, 163))
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 321, 41))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 0, 101, 41))
        self.textEdit_2 = QTextEdit(Widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 40, 321, 41))
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 40, 101, 41))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 120, 21, 41))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.textEdit_3 = QTextEdit(Widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(20, 120, 31, 41))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 120, 21, 41))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.textEdit_4 = QTextEdit(Widget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(70, 120, 31, 41))
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(100, 120, 71, 41))
        self.textEdit_5 = QTextEdit(Widget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(170, 120, 251, 41))
        self.textEdit_6 = QTextEdit(Widget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(0, 80, 321, 41))
        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(320, 80, 101, 41))
        self.pushButton.clicked.connect(PaintEvent)
        ui.pushButton_2.clicked.connect(slottwo)
        self.pushButton_3.clicked.connect(slotthree)
        ui.pushButton_4.clicked.connect(slotfour)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Function_Py", None))
        self.textEdit.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8bf7\u8f93\u5165\u51fd\u6570</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u7ed8\u56fe", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u6c42\u5bfc", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u4ece", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u5230", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u6c42\u5b9a\u79ef\u5206", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"\u6c42\u4e0d\u5b9a\u79ef\u5206", None))
    # retranslateUi

@Slot()
def PaintEvent():
    print("Hello World!")
    x = np.linspace(-10,10,300)
    ostr = ui.textEdit.toPlainText()
    y = eval(ostr)
    plt.figure(figsize=(12,6), dpi=100)
    plt.plot(x, y)
    plt.grid(linestyle="--",alpha=0.1)
    plt.show()

@Slot()
def slottwo():
    ostr = ui.textEdit.toPlainText()
    x = symbols('x')
    ui.textEdit_2.setPlainText(str(sp.diff(ostr, x)))

@Slot()
def slotthree():
    ostr = ui.textEdit.toPlainText()
    x = symbols('x')
    ofloat = eval(ui.textEdit_3.toPlainText())
    tfloat = eval(ui.textEdit_4.toPlainText())
    ui.textEdit_5.setPlainText(str(integrate(ostr,(x,ofloat,tfloat))))

@Slot()
def slotfour():
    ostr = ui.textEdit.toPlainText()
    x = symbols('x')
    ui.textEdit_6.setPlainText(str(integrate(ostr,x)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Widget()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
