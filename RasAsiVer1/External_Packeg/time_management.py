from datetime import datetime
from time import sleep
# from RasAsi_main import startTimeRasAsi
# from ..Gmail_Packeg import send, get_message
from RasAsiVer1.Gmail_Packeg.message_text import read_message
from RasAsiVer1.Gmail_Packeg.Send import send
from datetime import datetime
from RasAsiVer1.External_Packeg.startTimeRasAsi import timeHasPassed, startTimeRasAsi


def k2(t_stop):
    while not t_stop.is_set():
        cTime = datetime.now().time()
        if cTime.hour == 21:
            print('1')
        if 'Время\r\n' in read_message():
            send(topic='Server time', message=f'Время работы сервера:\t {str(timeHasPassed(startTimeRasAsi))}')
            print('Время работы сервера было отправлено по внешнему запросу')
        print(cTime.hour)
        sleep(60)


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    '''Необходим аргумент для запуска.
        Аргумент находится в RasAsiVer1 __init__
        Аргумент подаёт команду в функцию,
        когда модуль запущен, как ещё один поток программы'''
    k2()