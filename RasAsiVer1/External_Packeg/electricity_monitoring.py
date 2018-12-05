import time, datetime
from RasAsiVer1.Gmail_Packeg.Send import send, log
from RasAsiVer1 import t_stop

def func1(t_stop):
    print(time.ctime())
    while (not t_stop.set()):
        print(r'*\|/_________Записано_________\|/*')
        print(f'    {datetime.datetime.now()}')
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
        func1(t_stop)

    func1()
