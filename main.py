from UI2 import *
from UI6 import *
import serial
import serial.tools.list_ports
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
class loginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui6_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(self.get_serial_info)
        self.ui.pushButton_4.clicked.connect(self.serial_init)
        self.ui.pushButton_6.clicked.connect(self.add_data)
        self.ui.pushButton_5.clicked.connect(self.send_data)
        self.ui.horizontalSlider.valueChanged.connect(self.renew1)
        self.ui.horizontalSlider_2.valueChanged.connect(self.renew2)
        self.ui.horizontalSlider_3.valueChanged.connect(self.renew3)
        self.ui.horizontalSlider_4.valueChanged.connect(self.renew4)
        self.ui.horizontalSlider_5.valueChanged.connect(self.renew5)
        self.ui.horizontalSlider_6.valueChanged.connect(self.renew6)
        self.ui.lineEdit.textChanged.connect(self.new1)
        self.ui.lineEdit_2.textChanged.connect(self.new2)
        self.ui.lineEdit_6.textChanged.connect(self.new3)
        self.ui.lineEdit_3.textChanged.connect(self.new4)
        self.ui.lineEdit_4.textChanged.connect(self.new5)
        self.ui.lineEdit_7.textChanged.connect(self.new6)
        self.show()

    def new1(self):
        if(self.ui.lineEdit.text()==""):
            self.ui.horizontalSlider.setValue(0)
        else:
            self.ui.horizontalSlider.setValue(int(self.ui.lineEdit.text()))

    def new2(self):
        if (self.ui.lineEdit_2.text() == ""):
            self.ui.horizontalSlider_2.setValue(0)
        else:
            self.ui.horizontalSlider_2.setValue(int(self.ui.lineEdit_2.text()))

    def new3(self):
        if (self.ui.lineEdit_6.text() == ""):
            self.ui.horizontalSlider_3.setValue(0)
        else:
            self.ui.horizontalSlider_3.setValue(int(self.ui.lineEdit_6.text()))

    def new4(self):
        if(self.ui.lineEdit_3.text()==""):
            self.ui.horizontalSlider_4.setValue(0)
        else:
            self.ui.horizontalSlider_4.setValue(int(self.ui.lineEdit_3.text()))

    def new5(self):
        if(self.ui.lineEdit_4.text()==""):
            self.ui.horizontalSlider_5.setValue(0)
        else:
            self.ui.horizontalSlider_5.setValue(int(self.ui.lineEdit_4.text()))

    def new6(self):
        if(self.ui.lineEdit_7.text()==""):
            self.ui.horizontalSlider_6.setValue(0)
        else:
            self.ui.horizontalSlider_6.setValue(int(self.ui.lineEdit_7.text()))

    def renew1(self):
        self.num1 = str(self.ui.horizontalSlider.value())
        self.ui.lineEdit.setText(self.num1)
        self.add_data()

    def renew2(self):
        self.num2 = str(self.ui.horizontalSlider_2.value())
        self.ui.lineEdit_2.setText(self.num2)
        self.add_data()

    def renew3(self):
        self.num3 = str(self.ui.horizontalSlider_3.value())
        self.ui.lineEdit_6.setText(self.num3)
        self.add_data()

    def renew4(self):
        self.num4 = str(self.ui.horizontalSlider_4.value())
        self.ui.lineEdit_3.setText(self.num4)
        self.add_data()

    def renew5(self):
        self.num5 = str(self.ui.horizontalSlider_5.value())
        self.ui.lineEdit_4.setText(self.num5)
        self.add_data()

    def renew6(self):
        self.num6 = str(self.ui.horizontalSlider_6.value())
        self.ui.lineEdit_7.setText(self.num6)
        self.add_data()
    #更新波形图
    def add_data(self):
        # self.num 是正负刺激的总时间
        self.kongbai_time1 = int(self.ui.lineEdit_2.text())
        self.kongbai_time2 = int(self.ui.lineEdit_6.text())
        self.kongbai_time1_plot = int(int(self.ui.lineEdit_2.text())/10)
        self.kongbai_time2_plot = int(int(self.ui.lineEdit_6.text())/10)

        #确定我的参数，正负时间，正负幅值，中间的时间
        self.zheng_time = int(self.ui.lineEdit.text())
        self.fu_time= int(self.ui.lineEdit_7.text())

        self.zheng_time_plot = int(int(self.ui.lineEdit.text())/20)
        self.fu_time_plot = int(int(self.ui.lineEdit_7.text())/20)
        self.zheng_range = int(self.ui.lineEdit_3.text())
        self.fu_range = -1*int(self.ui.lineEdit_4.text())

        self.ui.data.clear()
        self.last =500
        self.x=self.zheng_time_plot
        self.case=0
        while((self.last-self.x)>0):
            if self.case==0:
                self.ui.data += [self.zheng_range for x in range(0,self.zheng_time_plot)]
                self.last -= self.x
                self.x=self.kongbai_time1_plot
                self.case =1
            elif self.case ==1:
                self.ui.data += [0 for x in range(0,self.kongbai_time1_plot)]
                self.last -= self.x
                self.x = int(self.fu_time_plot)
                self.case =2
            elif self.case ==2:
                self.ui.data += [self.fu_range for x in range(0,self.fu_time_plot)]
                self.last -= self.x
                self.x = int(self.kongbai_time2_plot)
                self.case =3
            else :
                self.ui.data += [0 for x in range(0,int(self.kongbai_time2_plot))]
                self.last -= self.x
                self.x = self.zheng_time_plot
                self.case =0

        if self.case ==0:
            self.ui.data += [self.zheng_range for x in range(0,self.last)]
        elif self.case ==1:
            self.ui.data += [0 for x in range(0, self.last)]
        elif self.case == 2:
            self.ui.data += [self.fu_range for x in range(0, self.last)]
        else:
            self.ui.data += [0 for x in range(0, self.last)]

        self.ui.plot = self.ui.theplot.plot(self.ui.data, pen='y',clear=True)

    #切换界面
    def go_to_interface(self):
        account = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if account == "123" and password == "123":
            self.win=interfaceWindow()
            self.close()
        else:
            pass

    #拖动
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_2.setIcon(QtGui.QIcon(u":/icons/icons/maxsize.png"))
        else:
            self.showMaximized()
            self.ui.pushButton_2.setIcon(QtGui.QIcon(u":/icons/icons/minimizeWhite.png"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    # 获取可用串口列表
    def get_serial_info(self):

        # 打印可用串口列表
        # self.need_serial = ''

        self.plist = list(serial.tools.list_ports.comports())
        if len(self.plist) <= 0:
            print('未找到串口')
            qm = QMessageBox.warning(self, '提示窗口', '未找到串口!请检查接线和电脑接口。',
                                     QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
            if qm == QMessageBox.Yes:
                print('Yes')
            else:
                print('No')
        else:
            for i in list(self.plist):
                self.ui.comboBox.addItem(i.name)

    # 串口初始化
    def serial_init(self):

        self.port = self.ui.comboBox.currentText()

        try:
            self.ser = serial.Serial(port=self.port,baudrate=115200,bytesize=8,parity='N',stopbits=1)
            print(self.ser)
            if self.ser.is_open:
                print('串口正常')
        except Exception as e:

            QMessageBox.warning(self, 'tips!', str(e), QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
            print('异常：', e)

    def send_data(self):
        #
        # ct = datetime.datetime.now()                       #获取当前系统时间
        # ct_str = ct.strftime("%Y-%m-%d %H:%M:%S")          #格式化当前系统时间（字符形式）

        try:
            # 获取相应的数据
            self.ciji_time = int(int(self.ui.lineEdit_7.text())+int(self.ui.lineEdit.text()))
            self.all_hz = int(1000000 / (self.kongbai_time1 + self.kongbai_time2 + self.ciji_time))
            self.high_proportion = int(
                1000 * self.zheng_time / (self.kongbai_time1 + self.kongbai_time2 + self.ciji_time))
            self.low_proportion = int(1000 * self.fu_time / (self.kongbai_time1 + self.kongbai_time2 + self.ciji_time))
            self.blank_first_proportion = int(
                1000 * self.kongbai_time1 / (self.kongbai_time1 + self.kongbai_time2 + self.ciji_time))
            self.blank_second_proportion = int(
                1000 * self.kongbai_time2 / (self.kongbai_time1 + self.kongbai_time2 + self.ciji_time))
            # 获取相应的波形self.send
            # 格式 载波频率@调制波频率@正range@负range@high占空比@low占空比@第一段空白@第二段空白
            print(self.ui.lineEdit_5.text() + "@" + str(
                self.all_hz) + "@" + self.ui.lineEdit_3.text() + "@" + self.ui.lineEdit_4.text() + "@" + str(
                self.high_proportion) + "@" + str(self.low_proportion) + "@" + str(self.blank_first_proportion) + "@")

            self.senddata = (self.ui.lineEdit_5.text() + "@" + str(
                self.all_hz) + "@" + self.ui.lineEdit_3.text() + "@" + self.ui.lineEdit_4.text() + "@" + str(
                self.high_proportion) + "@" + str(self.low_proportion) + "@" + str(
                self.blank_first_proportion) + "@" + "\r\n").encode("utf-8")
            self.ser.write(self.senddata)

            # print(self.senddata)

        except Exception as e:
            QMessageBox.warning(self, 'tips!', str(e), QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)


class interfaceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui2_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = loginWindow()
    sys.exit(app.exec_())
