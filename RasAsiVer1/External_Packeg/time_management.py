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
    # sleep(checkTime()[1])
    print('mark #1')
    while not t_stop.is_set():
        """дабы не вызывать класс datetime при каждой проверки условий"""
        cHour, cMinutes = datetime.now().hour, datetime.now().minute
        if cHour == 12 or cHour == 0:
            """Коррекция времени"""
            print('сейчас 0 или 12 часов')
            sleep(checkTime()[0])
            print(datetime.now())
        elif cHour == 8 and cMinutes == 0:
            pass
        elif cHour == 1 and cMinutes == 45:
            send(topic='из time_managment', message='сейчас 1:45')
        else:
            print('mark #2')
            sleep(30)


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    currentTime()