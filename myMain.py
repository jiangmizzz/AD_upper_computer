 
#导入程序运行必须模块
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, qApp
#导入designer工具生成的login模块
from myUI3 import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
#导入串口模块
import serial
import serial.tools.list_ports
#导入画图模块
import pyqtgraph as pg
#数字处理，取对数
import math
 
class MyMainForm(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        # super()用来调用父类(基类)的方法,super().__init__() 就是调用父类的init方法
        super(MyMainForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        #qApp.setStyleSheet()
        self.ui.setupUi(self)#初始化主窗口
        #初始化各参数值，文本框和滑动条用这几个参数维护
        self.param:list[int] = [0, 0, 0, 0, 0, 0, 0]
        self.totalTime:int = int(sum(self.param[0:4]))
        #画图，制定画布大小，添加绿色和黄色画笔
        self.ui.graphicsView.setYRange(-100, 100)
        self.ui.graphicsView.setXRange(0, 100)
        self.line_green = pg.PlotCurveItem(clear=True, pen="g", name="Green")
        self.line_yellow = pg.PlotCurveItem(clear=True, pen="y", name="Yellow")
        self.ui.graphicsView.addItem(self.line_green)
        self.ui.graphicsView.addItem(self.line_yellow)
        #self.line_yellow.setData([-200, 400], [0, 0])
        self.drawGraph()
        #初始化界面上的文本框和拖动条，要加()才有效，比较奇妙
        self.setData()

        #获取串口
        self.portList: list
        self.ui.pushButton.clicked.connect(self.getSerial)
        self.ifInitable: bool = False #默认未获取串口
        self.ifReady: bool = False #默认串口未初始化
        self.port: serial.Serial #选择的串口对象
        self.ui.pushButton_2.clicked.connect(self.initSerial)
        #发送数据
        self.dataToSend:str  #要发送的字符串
        self.ui.pushButton_3.clicked.connect(self.sendData)

        #文字框改变拖动条，我这里这个顺序太难受了hhh
        self.ui.lineEdit.textChanged.connect(lambda: self.drag(0))
        self.ui.lineEdit_3.textChanged.connect(lambda: self.drag(1))
        self.ui.lineEdit_4.textChanged.connect(lambda: self.drag(2))
        self.ui.lineEdit_5.textChanged.connect(lambda: self.drag(3))
        self.ui.lineEdit_2.textChanged.connect(lambda: self.drag(4))
        self.ui.lineEdit_6.textChanged.connect(lambda: self.drag(5))
        self.ui.lineEdit_7.textChanged.connect(lambda: self.drag(6))

        #拖动条改变文字框
        self.ui.horizontalSlider_7.valueChanged.connect(lambda: self.changeText(0))
        self.ui.horizontalSlider_12.valueChanged.connect(lambda: self.changeText(1))
        self.ui.horizontalSlider_9.valueChanged.connect(lambda: self.changeText(2))
        self.ui.horizontalSlider_8.valueChanged.connect(lambda: self.changeText(3))
        self.ui.horizontalSlider_11.valueChanged.connect(lambda: self.changeText(4))
        self.ui.horizontalSlider_10.valueChanged.connect(lambda: self.changeText(5))

        


    #获取串口
    def getSerial(self)->None:
        #获取串口信息列表
        self.portList = serial.tools.list_ports.comports()
        if(self.portList.__len__()==0):#记得加()
            self.ifInitable == False
            qApp.setStyleSheet("QPushButton{background-color: Silver;}")
            QMessageBox.information(self, "提示",
                                    "<font color=\"#FFFFFF\">未找到串口!请检查接线和电脑接口</font>",
                                    QMessageBox.Ok, 
                                    QMessageBox.Ok)#返回值是按下的按钮
        else:
            self.ifInitable = True
            for port in self.portList:
                print(port)
                self.ui.comboBox.addItem(port.device)

    #初始化当前串口
    def initSerial(self)->None:
        #检查当前是否已经有选中的串口
        if(self.ifInitable == False):
            result1 = QMessageBox.warning(self, "提示",
                                "<font color=\"#FFFFFF\">没有可用串口！</font>",
                                QMessageBox.Retry|QMessageBox.Cancel, 
                                QMessageBox.Cancel)#返回值是按下的按钮
            if(result1 == QMessageBox.Retry):
                self.getSerial()
        else:
            name = self.ui.comboBox.currentText()
            try:
                self.port = serial.Serial(port=name,baudrate=115200,bytesize=8,parity='N',stopbits=1)
                if (self.port.is_open):
                    self.ifReady = True
                    QMessageBox.information(self, "提示",
                                "<font color=\"#FFFFFF\">串口初始化成功！</font>",
                                QMessageBox.Ok, 
                                QMessageBox.Ok)

            except Exception as e:
                self.ifReady = False
                result2 = QMessageBox.critical(self, "错误",
                                            "<font color=\"#FFFFFF\">串口初始化失败! Error: "+str(e)+"</font>",
                                            QMessageBox.Retry|QMessageBox.Cancel, 
                                            QMessageBox.Cancel)#返回值是按下的按钮
                if(result2 == QMessageBox.Retry):
                    self.initSerial()#重试

    #发送数据
    def sendData(self)->None:
        if(self.ifReady == False):
            result1 = QMessageBox.warning(self, "提示",
                                            "<font color=\"#FFFFFF\">串口还未初始化！</font>",
                                            QMessageBox.Retry|QMessageBox.Cancel, 
                                            QMessageBox.Cancel)#返回值是按下的按钮
            if(result1 == QMessageBox.Retry):
                self.initSerial()#进入初始化
        else:
            totalTime: int = self.totalTime #周期总时间
            if(totalTime == 0):
                QMessageBox.warning(self, "提示",
                                "<font color=\"#FFFFFF\">总时间不能为0！</font>",
                                QMessageBox.Ok,
                                QMessageBox.Ok)
            freq: int = int(1000000/totalTime)#频率
            highProportion: int = int(self.param[0]/totalTime * 1000)#high占空比
            lowProportion: int = int(self.param[1]/totalTime * 1000)#low占空比
            firstBlank: int = int (self.param[2]/totalTime * 1000)#第一段空白
            secondBlank: int = int (self.param[3]/totalTime * 1000)#第二段空白
            self.dataToSend = str(str(self.param[6]) + "@" + #载波频率
                                 str(freq) + "@" + #调制波频率
                                 str(self.param[4]) + "@" + #正range
                                 str(self.param[5]) + "@" + #负range
                                 str(highProportion) + "@" + #high占空比
                                 str(lowProportion) + "@" + #low占空比
                                 str(firstBlank) + "@" + #第一段空白
                                 str(secondBlank) + #第二段空白
                                 "\r\n")#.encode("utf-8")
            #print(self.dataToSend)
            try:
                result3 = QMessageBox.information(self, "确认",
                                "<font color=\"#FFFFFF\">请确认您要发送的数据："+"\r\n"+self.dataToSend+"</font>",
                                QMessageBox.Ok|QMessageBox.Cancel, 
                                QMessageBox.Ok)
                if(result3==QMessageBox.Ok):
                    self.port.write(self.dataToSend.encode("utf-8"))
                    QMessageBox.information(self, "提示",
                                "<font color=\"#FFFFFF\">数据发送成功！</font>",
                                QMessageBox.Ok, 
                                QMessageBox.Ok)
            except Exception as e:
                result2 = QMessageBox.critical(self, "错误",
                                            "<font color=\"#FFFFFF\">数据发送失败! Error:"+str(e)+"</font>",
                                            QMessageBox.Retry|QMessageBox.Cancel, 
                                            QMessageBox.Cancel)#返回值是按下的按钮
                if(result2 == QMessageBox.Retry):
                    self.sendData()#重试
                
    #画图
    def drawGraph(self)->None:
        if(self.totalTime == 0):
            self.line_green.setData([-200, 400], [0, 0])#初始图像
        else:
            #取对数，减少空白和刺激时间的差异
            log = lambda x: 0 if x==0 else int(math.log(x)*2)
            high = lambda x: 0 if highTime==0 else x
            low = lambda x: 0 if lowTime==0 else x
            highTime:int = log(self.param[0])
            lowTime:int = log(self.param[1])
            blank1:int = log(self.param[2])
            blank2:int = log(self.param[3])
            highRange:int = self.param[4]
            lowRange:int = self.param[5]
            totalTime = highTime+lowTime+blank1+blank2

            #坐标描点
            Xlist:list[int] = [-200]
            Ylist:list[int] = [0]
            tail: int = -100 #上一个波形的末尾，需要接上下一个波形
            tmpY:list[int] = [0, high(highRange), high(highRange), 0, 0, -low(lowRange), -low(lowRange), 0, 0] 
            tmpX:list[int] = []    
            for i in range(math.ceil(300/totalTime)):
                tmpX = [tail, tail+1, tail+highTime+1, tail+highTime+2, tail+highTime+blank1+2, tail+highTime+blank1+3,
                        tail+totalTime-blank2+3, tail+totalTime-blank2+4, 
                        tail+totalTime+4]
                tail = tail + totalTime+4   #稍斜一点，纯为了效果
                Xlist.extend(tmpX)
                Ylist.extend(tmpY) #将新波形加在原来波形的后面
            Xlist.append(400)
            Ylist.append(0)
            self.line_green.setData(Xlist, Ylist)

            
    #更新参数在界面上的显示
    def setData(self)->None:
        self.ui.horizontalSlider_7.setValue(int(self.param[0]))
        self.ui.horizontalSlider_12.setValue(int(self.param[1]))
        self.ui.horizontalSlider_9.setValue(int(self.param[2]))
        self.ui.horizontalSlider_8.setValue(int(self.param[3]))
        self.ui.horizontalSlider_11.setValue(self.param[4])
        self.ui.horizontalSlider_10.setValue(self.param[5])
        self.ui.lineEdit.setText(str(self.param[0]))
        self.ui.lineEdit_3.setText(str(self.param[1]))
        self.ui.lineEdit_4.setText(str(self.param[2]))
        self.ui.lineEdit_5.setText(str(self.param[3]))
        self.ui.lineEdit_2.setText(str(self.param[4]))
        self.ui.lineEdit_6.setText(str(self.param[5]))
        self.ui.lineEdit_7.setText(str(self.param[6]))

        self.totalTime = int(sum(self.param[0:4]))
        self.drawGraph()

    #根据文字框改变拖动条
    def drag(self, num:int)->None:
        text:str = ""
        if(num == 0):
            text = self.ui.lineEdit.text()
        elif(num==1):
            text = self.ui.lineEdit_3.text()
        elif(num==2):
            text = self.ui.lineEdit_4.text()
        elif(num==3):
            text = self.ui.lineEdit_5.text()
        elif(num==4):
            text = self.ui.lineEdit_2.text()
        elif(num==5):
            text = self.ui.lineEdit_6.text()
        elif(num==6):
            text = self.ui.lineEdit_7.text()

        if(text==""):
            self.param[num] = 0
        else:
            self.param[num] = int(text)
        self.setData()

    #根据拖动条改变文字
    def changeText(self, num:int)->None:
        if(num == 0):
            self.param[0] = self.ui.horizontalSlider_7.value()
        elif(num==1):
            self.param[1] = self.ui.horizontalSlider_12.value()
        elif(num==2):
            self.param[2] = self.ui.horizontalSlider_9.value()
        elif(num==3):
            self.param[3] = self.ui.horizontalSlider_8.value()
        elif(num==4):
            self.param[4] = self.ui.horizontalSlider_11.value()
        elif(num==5):
            self.param[5] = self.ui.horizontalSlider_10.value()
        self.setData()



if __name__ == "__main__":
    # 注意：需要加上这一行，自适应缩放，使实际显示效果和QTdesigner中保持一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) 
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

