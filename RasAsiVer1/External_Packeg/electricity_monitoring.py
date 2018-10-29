import time, datetime


def func1():
    variable1 = 1
    print(time.ctime())
    while variable1:
        print('func1_1')
        with open('/home/pi/Documents/logFileTime', 'w') as LF:
            LF.write(str(time.time()))
        print('ok')
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
            time.sleep(60)
            print(time.time())
            stopTime = datetime.timedelta(seconds=(time.time() - line1 - 60) // 1)
            print('try4')
            print(stopTime)
            with open('/home/pi/Documents/StopTime', 'a') as LF:
                LF.write(f'Дата - {datetime.datetime.now()} Время простоя - {str(stopTime)}\n')

    except:
        print('except1')
        func1()

    func1()