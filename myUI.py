# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\xlab\AD_upper_computer\myUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1127, 538)
        Dialog.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1121, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 15, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.widget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setContentsMargins(15, -1, -1, 15)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(0, 0, 15, -1)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.frame_7)
        self.label_16.setMinimumSize(QtCore.QSize(150, 0))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_16.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16, 0, QtCore.Qt.AlignLeft)
        self.label_17 = QtWidgets.QLabel(self.frame_7)
        self.label_17.setMinimumSize(QtCore.QSize(150, 0))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_17.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.frame_7)
        self.label_18.setMinimumSize(QtCore.QSize(150, 0))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_18.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.frame_7)
        self.label_19.setMinimumSize(QtCore.QSize(150, 0))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_19.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_6.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.frame_7)
        self.label_20.setMinimumSize(QtCore.QSize(150, 0))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_20.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_6.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.frame_7)
        self.label_21.setMinimumSize(QtCore.QSize(150, 0))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_21.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_6.addWidget(self.label_21)
        self.gridLayout.addWidget(self.frame_7, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 20, -1, 8)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalSlider_7 = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_7.setStyleSheet("")
        self.horizontalSlider_7.setMaximum(100000)
        self.horizontalSlider_7.setPageStep(10000)
        self.horizontalSlider_7.setTracking(True)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.verticalLayout_3.addWidget(self.horizontalSlider_7)
        self.horizontalSlider_12 = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_12.setMaximum(100000)
        self.horizontalSlider_12.setPageStep(10000)
        self.horizontalSlider_12.setProperty("value", 0)
        self.horizontalSlider_12.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_12.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_12.setObjectName("horizontalSlider_12")
        self.verticalLayout_3.addWidget(self.horizontalSlider_12)
        self.horizontalSlider_9 = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_9.setMaximum(100000)
        self.horizontalSlider_9.setPageStep(10000)
        self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_9.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_9.setObjectName("horizontalSlider_9")
        self.verticalLayout_3.addWidget(self.horizontalSlider_9)
        self.horizontalSlider_8 = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_8.setMaximum(100000)
        self.horizontalSlider_8.setPageStep(10000)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.verticalLayout_3.addWidget(self.horizontalSlider_8)
        self.horizontalSlider_11 = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_11.setMaximum(100)
        self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_11.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_11.setObjectName("horizontalSlider_11")
        self.verticalLayout_3.addWidget(self.horizontalSlider_11)
        self.horizontalSlider_10 = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_10.setMaximum(100)
        self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_10.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_10.setObjectName("horizontalSlider_10")
        self.verticalLayout_3.addWidget(self.horizontalSlider_10)
        self.gridLayout.addWidget(self.frame_2, 1, 3, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(-1, -1, 20, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"height: 13px;\n"
"font: 9pt \"黑体\";")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"height: 13px;\n"
"font: 9pt \"黑体\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"height: 13px;\n"
"font: 9pt \"黑体\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"height: 13px;\n"
"font: 9pt \"黑体\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"height: 13px;\n"
"font: 9pt \"黑体\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"height: 13px;\n"
"font: 9pt \"黑体\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(0, 11, 0, 7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.gridLayout.addWidget(self.frame_5, 1, 4, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QtCore.QSize(20, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(0, 11, 0, 7)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"黑体\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.gridLayout.addWidget(self.frame_4, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_14 = QtWidgets.QFrame(self.frame_6)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setContentsMargins(15, -1, 25, -1)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 12pt \"黑体\";")
        self.pushButton_6.setAutoRepeat(False)
        self.pushButton_6.setAutoExclusive(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 12pt \"黑体\";")
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 12pt \"黑体\";")
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 12pt \"黑体\";")
        self.pushButton_5.setAutoRepeat(False)
        self.pushButton_5.setAutoExclusive(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 3)
        self.horizontalLayout_6.setStretch(2, 3)
        self.horizontalLayout_6.setStretch(3, 2)
        self.gridLayout_2.addWidget(self.frame_14, 2, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout.setContentsMargins(10, -1, -1, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(self.frame_8)
        self.label_14.setMinimumSize(QtCore.QSize(70, 0))
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"黑体\";\n"
"")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"height: 13px;\n"
"font: 9pt \"黑体\";")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout.addWidget(self.lineEdit_7)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.gridLayout_2.addWidget(self.frame_8, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.frame_15 = QtWidgets.QFrame(self.frame_6)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setContentsMargins(26, 15, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_23 = QtWidgets.QLabel(self.frame_15)
        self.label_23.setMinimumSize(QtCore.QSize(70, 0))
        self.label_23.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_23.setStyleSheet("color: rgb(240, 240, 240);\n"
"color: rgb(176, 176, 176);\n"
"font: 10pt \"黑体\";\n"
"")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_7.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.frame_15)
        self.label_24.setMinimumSize(QtCore.QSize(70, 0))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_24.setStyleSheet("color: rgb(240, 240, 240);\n"
"color: rgb(176, 176, 176);\n"
"font: 10pt \"黑体\";\n"
"")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_7.addWidget(self.label_24)
        self.gridLayout_2.addWidget(self.frame_15, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_3.addWidget(self.frame_6, 2, 0, 1, 1)
        self.graphicsView = PlotWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 1, 3, 1)
        self.frame_12 = QtWidgets.QFrame(self.widget)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_5.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_10 = QtWidgets.QFrame(self.frame_12)
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.frame_10)
        self.frame_9.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_9.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setContentsMargins(18, -1, 18, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        self.label_13.setMinimumSize(QtCore.QSize(50, 0))
        self.label_13.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_13.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"display: flex;\n"
"")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBox = QtWidgets.QComboBox(self.frame_9)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 32))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"height: 13px;\n"
"font: 9pt \"黑体\";")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout_4.addWidget(self.frame_9)
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setContentsMargins(18, -1, 18, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_11)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 12pt \"黑体\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"border-radius: 15px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font: 12pt \"黑体\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.frame_11)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setContentsMargins(26, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.frame_13)
        self.label_15.setMinimumSize(QtCore.QSize(70, 0))
        self.label_15.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setStyleSheet("color: rgb(240, 240, 240);\n"
"color: rgb(176, 176, 176);\n"
"font: 10pt \"黑体\";\n"
"")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.label_22 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(70, 0))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setStyleSheet("color: rgb(240, 240, 240);\n"
"color: rgb(176, 176, 176);\n"
"font: 10pt \"黑体\";\n"
"")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_5.addWidget(self.label_22)
        self.verticalLayout_5.addWidget(self.frame_13, 0, QtCore.Qt.AlignLeft)
        self.gridLayout_3.addWidget(self.frame_12, 1, 0, 1, 1)
        self.gridLayout_3.setColumnMinimumWidth(0, 1)
        self.gridLayout_3.setColumnMinimumWidth(1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setRowStretch(1, 1)
        self.gridLayout_3.setRowStretch(2, 3)
        self.frame_12.raise_()
        self.frame_6.raise_()
        self.graphicsView.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Upper_Computer"))
        self.label_16.setText(_translate("Dialog", "正向刺激时间/us"))
        self.label_17.setText(_translate("Dialog", "负向刺激时间/us"))
        self.label_18.setText(_translate("Dialog", "第一段空白时间/us"))
        self.label_19.setText(_translate("Dialog", "第二段空白时间/us"))
        self.label_20.setText(_translate("Dialog", "正向刺激幅度"))
        self.label_21.setText(_translate("Dialog", "负向刺激幅度"))
        self.label_7.setText(_translate("Dialog", "100000"))
        self.label_8.setText(_translate("Dialog", "100000"))
        self.label_9.setText(_translate("Dialog", "100000"))
        self.label_10.setText(_translate("Dialog", "100000"))
        self.label_11.setText(_translate("Dialog", "100"))
        self.label_12.setText(_translate("Dialog", "100"))
        self.label.setText(_translate("Dialog", "0"))
        self.label_2.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "0"))
        self.label_5.setText(_translate("Dialog", "0"))
        self.label_4.setText(_translate("Dialog", "0"))
        self.label_6.setText(_translate("Dialog", "0"))
        self.pushButton_6.setText(_translate("Dialog", "既定刺激流程"))
        self.pushButton_4.setText(_translate("Dialog", "循环发送"))
        self.pushButton_3.setText(_translate("Dialog", "单次发送"))
        self.pushButton_5.setText(_translate("Dialog", "暂停"))
        self.label_14.setText(_translate("Dialog", "载波频率"))
        self.label_23.setText(_translate("Dialog", "当前状态："))
        self.label_24.setText(_translate("Dialog", "未发送数据"))
        self.label_13.setText(_translate("Dialog", "串口"))
        self.pushButton.setText(_translate("Dialog", "获取可用串口"))
        self.pushButton_2.setText(_translate("Dialog", "串口初始化"))
        self.label_15.setText(_translate("Dialog", "串口信息："))
        self.label_22.setText(_translate("Dialog", "未获取"))
from pyqtgraph import PlotWidget
