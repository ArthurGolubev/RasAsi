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

def k2(t_stop):
    while not t_stop.is_set():
        cTime = datetime.now().time()
        print(cTime)
        if cTime.minute == 3:
            print('\n{:,^47}'.format(' mark #1 from: ') + '\n{: ^47}'.format(__name__) + '\n{:,^47}'.format('') + '\n')  #<<<<_MARK_<<<<
            send(topic='Час прошёл', message=f'письмо отправленно в {datetime.now()}')
        sleep(60)
# def currentTime(t_stop):
#     """при запуске Rasberry Asistent"""
#     print(f'\nВремя включения - {datetime.now()}')
#     sleep(checkTime()[1])
#     print('mark #1')
#     print(f'\n{datetime.now()}')
#     cHour = datetime.now().hour
#     cMinutes = 0
#     while not t_stop.is_set():
#         """дабы не вызывать класс datetime при каждой проверки условий"""
#         if cMinutes == 0 and (cHour == 0 or cHour == 6 or cHour == 12 or cHour == 18):
#             """Коррекция времени"""
#             print('коррекция времени')
#             sleep(checkTime()[0])
#             cHour = datetime.now().hour
#             cMinutes = 0
#             print(f'коррекция времени - {datetime.now()}')
#             send(topic='Коррекция времени',
#                  message=f'время {datetime.now()}, по внутренним часам {cHour}:00')
#         elif cHour == 8 and cMinutes == 0:
#             pass
#         elif cHour == 2 and cMinutes == 15:
#             send(topic='из time_managment', message='сейчас 2:15')
#             sleep(60)
#         else:
#             print('mark #2')
#             sleep(60)
#         cMinutes += 1
#         print(f'Time: {cHour}:{cMinutes} {datetime.now()}')
#         if cMinutes == 60:
#             cHour += 1
#             cMinutes = 0
#             send(topic='Час прошёл',
#                  message=f'письмо отправленно в {datetime.now()}Время по внутренним часам {cHour}:00')


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    # currentTime()
    k2()