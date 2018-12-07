import time, datetime
from RasAsiVer1.Gmail_Packeg.Send import send, log

def func1(t_stop):
    print(time.ctime())
    while not t_stop.is_set():
        print(r'*\|/_________Записано_________\|/*')
        print(f'    {datetime.datetime.now()}')
        with open('/home/pi/Documents/logFileTime', 'w') as LF:
            LF.write(str(time.time()))
        print(r'./|\_________Записано_________/|\.', '\n')
        time.sleep(60)


def electricity_monitoringFunction(t_stop):
    try:
        print('try1')
        with open('/home/pi/Documents/logFileTime', 'r') as LF:
            print('try2')
            line1 = float(LF.readline())
            print(line1)
            line2 = LF.readline()
            print(f'MARK #10000 {line2}')
            print('try3')
            print(time.time())
            time.sleep(5)
            print(time.time())
            stopTime = datetime.timedelta(seconds=int(time.time() - line1 - 180))
            print('try4')
            print(f'Время простоя - {stopTime}')
            with open('/home/pi/Documents/StopTime', 'a') as LF:
                if LF.readline():
                    LF.write(f'Дата - {datetime.datetime.now()} Время простоя - {str(stopTime)} *user stop*\n')
                    send(topic=f'Электричество - {time.ctime()}', message=log('/home/pi/Documents/StopTime'))
                else:
                    LF.write(f'Дата - {datetime.datetime.now()} Время простоя - {str(stopTime)}\n')
                    send(topic=f'Электричество - {time.ctime()}', message=log('/home/pi/Documents/StopTime'))

    except:
        print('except1')
        func1(t_stop)

    func1(t_stop)


def userDirectiv():
    with open('/home/pi/Documents/logFileTime', 'w') as LF:
        LF.write(str(time.time())+'\nuser stop')


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    """необходима передача аргумента Event из модуля threading"""