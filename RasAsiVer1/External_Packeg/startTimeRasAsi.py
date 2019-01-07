from datetime import datetime, timedelta


def initTime():
    startTimeRasAsi = datetime.now()
    return startTimeRasAsi


def timeHasPassed(inittime):
    # TODO: сделать время без наносекунд в отправке "время простоя"

    cTime = datetime.now()
    print('CURRENT cTime 1', cTime)
    microSec = cTime.microsecond
    cTime = cTime - inittime
    print('CURENT cTime 2', cTime)
    formTime = cTime - timedelta(microseconds=microSec)
    return formTime


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
    startTimeRasAsi = initTime()
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    timeHasPassed()