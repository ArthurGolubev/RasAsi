import time, datetime
from RasAsiVer1.Gmail_Packeg.Send import send


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
            time.sleep(8)
            print(time.time())
            stopTime = datetime.timedelta(seconds=(time.time() - line1 - 180) // 1)
            print('try4')
            print(stopTime)
            dateNow = f'{datetime.datetime.now() - datetime.timedelta(microseconds=datetime.datetime.now().microsecond)}'
            with open('/home/pi/Documents/StopTime', 'a') as LF:
                LF.write(f'Дата - {dateNow} Время простоя - {str(stopTime)}\n')
                send(topic='Электричество', message = f'Дата - {datetime.datetime.now()} Время простоя - {str(stopTime)}\n')
            print('try5')
            with open('/home/pi/Documents/StopTime', 'r') as LF:
                time.sleep(10)
                def sf(LF):
                    list1= LF.readlines()
                    str1 = ''
                    for i in list1:
                        str1 = str1 + i + '<br/>'
                    print(str1)
                    return str1
                str2 = sf(LF)
                print('try6')
                send(topic=f'Электричество - {dateNow}', message=str2)


    except:
        print('except1')
        func1()

    func1()