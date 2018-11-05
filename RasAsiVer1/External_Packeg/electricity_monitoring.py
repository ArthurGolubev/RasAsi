import time, datetime
from RasAsiVer1.Gmail_Packeg.Send import send, log


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
            time.sleep(180)
            print(time.time())
            stopTime = datetime.timedelta(seconds=(time.time() - line1 - 180) // 1)
            print('try4')
            print(stopTime)
            with open('/home/pi/Documents/StopTime', 'a') as LF:
                LF.write(f'Дата - {datetime.datetime.now()} Время простоя - {str(stopTime)}\n')
            # with open('/home/pi/Documents/StopTime', 'r') as LF:
            #
            #     def sf(LF):
            #         list1= LF.readlines()
            #         str1 = ''
            #         for i in list1:
            #             str1 = str1 + i + '<br/>'
            #         print(str1)
            #         return str1
                time.sleep(10)
                send(topic=f'Электричество - {time.ctime()}', message=log('/home/pi/Documents/StopTime'))


    except:
        print('except1')
        func1()

    func1()