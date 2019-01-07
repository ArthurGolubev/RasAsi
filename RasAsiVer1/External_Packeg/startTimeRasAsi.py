from datetime import datetime, timedelta


def initTime():
    startTimeRasAsi = datetime.now()
    return startTimeRasAsi


def timeHasPassed(inittime):
    # TODO: сделать время без наносекунд в отправке "время простоя"
    cTime = datetime.now() - inittime
    formTime = cTime - timedelta(microseconds=cTime.microsecond)

    return formTime


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
    startTimeRasAsi = initTime()
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    timeHasPassed()