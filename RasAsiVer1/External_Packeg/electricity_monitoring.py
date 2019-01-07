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
        with open('/home/pi/Documents/logFileTime', 'r') as LF:
            line1 = float(LF.readline())
            print('\n{:,^47}'.format(' mark #1 from: ') + '\n{: ^47}'.format(__name__) + '\n{:,^47}'.format(
                '') + '\n')  # <<<<_MARK_<<<<
            time.sleep(180)
            stopTime = datetime.timedelta(seconds=int(time.time() - line1 - 180))
            print(f'\nВремя простоя - {stopTime}')
            with open('/home/pi/Documents/StopTime', 'a') as LF1:
                if LF.readline():
                    LF1.write(f'Дата - {datetime.datetime.now()} Время простоя - {str(stopTime)} *user stop*\n')
                else:
                    LF1.write(f'Дата - {datetime.datetime.now()} Время простоя - {str(stopTime)}\n')

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
