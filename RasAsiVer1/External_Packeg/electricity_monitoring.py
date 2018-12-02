import time, datetime
from RasAsiVer1.Gmail_Packeg.Send import send, log
from PyQt5 import QtWidgets, QtGui
from ..GUI.RasAsi_GUI import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def f1(self, n):
        self.ui.label.setFont(QtGui.QFont('SansSerif', 30))
        self.ui.label.setText(f'{n}')


def func1():
    variable1 = 1
    print(time.ctime())
    while variable1:
        print(r'*\|/_________Записано_________\|/*')
        print(f'    {datetime.datetime.now()}')
        application.f1(datetime.datetime.now())
        with open('/home/pi/Documents/logFileTime', 'w') as LF:
            LF.write(str(time.time()))
        print(r'./|\_________Записано_________/|\.', '\n')
        time.sleep(60)


def electricity_monitoringFunction():
    try:
        print('try1')
        with open('/home/pi/Documents/logFileTime', 'r') as LF:
            print('try2')
            line1 = float(LF.readline())
            print(line1)
            print('try3')
            print(time.time())
            time.sleep(180)
            print(time.time())
            stopTime = datetime.timedelta(seconds=(time.time() - line1 - 180) // 1)
            print('try4')
            print(f'Время простоя - {stopTime}')
            with open('/home/pi/Documents/StopTime', 'a') as LF:
                LF.write(f'Дата - {datetime.datetime.now()} Время простоя - {str(stopTime)}\n')
            send(topic=f'Электричество - {time.ctime()}', message=log('/home/pi/Documents/StopTime'))


    except:
        print('except1')
        func1()

    func1()
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())