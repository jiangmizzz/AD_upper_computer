# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI6.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui6_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1396, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame{\n"
"    \n"
"    background-color: rgb(56, 57, 60);\n"
"border-radius:30px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(86, 88, 93);\n"
"    border-top-left-radius:30px;\n"
"    border-top-right-radius:30px;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(1240, 10, 121, 43))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"padding-bottom:5px;\n"
"}\n"
"")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icorn/最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"padding-bottom:5px;\n"
"}\n"
"")
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icorn/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(80, 0, 181, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(234, 234, 234)")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setGeometry(QtCore.QRect(40, 360, 111, 61))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(198, 198, 198,70);\n"
"border-radius:30px;\n"
"color:rgb(234, 234, 234)\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(410, 0, 181, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(234, 234, 234)")
        self.label_5.setObjectName("label_5")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(40, 110, 231, 221))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(20, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(234, 234, 234)")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setGeometry(QtCore.QRect(80, 20, 131, 41))
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(234, 234, 234)")
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 120, 141, 31))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 360, 111, 61))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(198, 198, 198,70);\n"
"border-radius:30px;\n"
"color:rgb(234, 234, 234)\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setGeometry(QtCore.QRect(270, 90, 471, 401))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setGeometry(QtCore.QRect(20, -10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(234, 234, 234)")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 191, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(234, 234, 234)")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        self.label_8.setGeometry(QtCore.QRect(20, 150, 141, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(234, 234, 234)")
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.frame_7)
        self.label_12.setGeometry(QtCore.QRect(20, 110, 171, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(234, 234, 234)")
        self.label_12.setObjectName("label_12")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setGeometry(QtCore.QRect(200, 0, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 80, 111, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 160, 111, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 270, 121, 61))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(198, 198, 198,70);\n"
"border-radius:30px;\n"
"color:rgb(234, 234, 234)\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 120, 111, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 270, 121, 61))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(198, 198, 198,70);\n"
"border-radius:30px;\n"
"color:rgb(234, 234, 234)\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_7)
        self.horizontalSlider.setGeometry(QtCore.QRect(330, 0, 101, 22))
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame_7)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(330, 80, 101, 22))
        self.horizontalSlider_2.setMaximum(10000)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.frame_7)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(330, 120, 101, 22))
        self.horizontalSlider_3.setMaximum(10000)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.frame_7)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(330, 160, 101, 22))
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setGeometry(QtCore.QRect(20, 190, 141, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(234, 234, 234)")
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 200, 111, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalSlider_5 = QtWidgets.QSlider(self.frame_7)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(330, 200, 101, 22))
        self.horizontalSlider_5.setMaximum(100)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setGeometry(QtCore.QRect(20, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(234, 234, 234)")
        self.label_10.setObjectName("label_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 40, 111, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalSlider_6 = QtWidgets.QSlider(self.frame_7)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(330, 40, 101, 22))
        self.horizontalSlider_6.setMaximum(1000)
        self.horizontalSlider_6.setSingleStep(10)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.theplot = pg.PlotWidget()
        self.data = [x for x in range(-100, 100)]
        self.plot = self.theplot.plot(self.data, pen='y')

        self.theplot.setBackground(QtGui.QColor(56, 57, 60))
        self.theplot.setYRange(-100, 100)
        self.theplot.setObjectName("theplot")

        self.horizontalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_3.addWidget(self.theplot)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1396, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "硬件连接"))
        self.pushButton.setText(_translate("MainWindow", "获取可用串口"))
        self.label_5.setText(_translate("MainWindow", "参数设置"))
        self.label.setText(_translate("MainWindow", "串口"))
        self.label_3.setText(_translate("MainWindow", "载波频率"))
        self.pushButton_4.setText(_translate("MainWindow", "串口初始化"))
        self.label_6.setText(_translate("MainWindow", "正向刺激时间/us"))
        self.label_7.setText(_translate("MainWindow", "第一段空白时间/us"))
        self.label_8.setText(_translate("MainWindow", "正向刺激幅度%"))
        self.label_12.setText(_translate("MainWindow", "第二端空白时间/us"))
        self.lineEdit.setText(_translate("MainWindow", "1000"))
        self.lineEdit_2.setText(_translate("MainWindow", "10"))
        self.lineEdit_3.setText(_translate("MainWindow", "80"))
        self.pushButton_5.setText(_translate("MainWindow", "发送数据"))
        self.lineEdit_6.setText(_translate("MainWindow", "40"))
        self.pushButton_6.setText(_translate("MainWindow", "波形预览"))
        self.label_9.setText(_translate("MainWindow", "负向刺激幅度%"))
        self.lineEdit_4.setText(_translate("MainWindow", "80"))
        self.label_10.setText(_translate("MainWindow", "负向刺激时间/us"))
        self.lineEdit_7.setText(_translate("MainWindow", "1000"))
import src_rc
