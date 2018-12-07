from datetime import datetime
from time import sleep
from ..Gmail_Packeg import send


def checkTime():
    whatMinutes = datetime.now().minute
    whatSeconds = datetime.now().second
    waitHour = ((60 - whatMinutes)*60) - whatSeconds
    waitMinute = 60 - whatSeconds
    print(f'следующий час наступит через - {waitHour} секунд')
    """возвращает кортеж"""
    return waitHour, waitMinute


def currentTime(t_stop):
    """при запуске Rasberry Asistent"""
    print(f'\nВремя включения - {datetime.now()}')
    sleep(checkTime()[1])
    print('mark #1')
    print(f'\n{datetime.now()}')
    cHour = datetime.now().hour
    cMinutes = 0
    while not t_stop.is_set():
        """дабы не вызывать класс datetime при каждой проверки условий"""
        # cHour, cMinutes = datetime.now().hour, datetime.now().minute
        if cHour == 12 or cHour == 0:
            """Коррекция времени"""
            print('сейчас 0 или 12 часов')
            sleep(checkTime()[0])
            print(datetime.now())
        elif cHour == 8 and cMinutes == 0:
            pass
        elif cHour == 2 and cMinutes == 15:
            send(topic='из time_managment', message='сейчас 2:15')
            sleep(60)
        else:
            print('mark #2')
            sleep(60)
        cMinutes += 1
        print(f'Time: {cHour}:{cMinutes}')
        if cMinutes == 60:
            cHour += 1
            cMinutes = 0


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    currentTime()