from datetime import datetime, timedelta


def initTime():
    startTimeRasAsi = datetime.now()
    return startTimeRasAsi


def timeHasPassed(inittime):
    # TODO: сделать время без наносекунд в отправке "время простоя"
    t1 = datetime.now() - inittime
    t2 = t1 - timedelta(microseconds=t1.microseconds)
    print(t2)
    return t2


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
    startTimeRasAsi = initTime()
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    timeHasPassed()