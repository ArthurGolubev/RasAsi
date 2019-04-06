from time import sleep
# from RasAsi_main import startTimeRasAsi
# from ..legacy_Gmail_Packeg import send, get_message
import threading
from RasAsiVer1.legacy_Gmail_Packeg.read_message import read_message
from RasAsiVer1.legacy_Gmail_Packeg.Send import send
from datetime import datetime
from RasAsiVer1.Time_Packeg.legacy_startTimeRasAsi import timeHasPassed, startTimeRasAsi
from emoji import emojize
from RasAsiVer1.External_Packeg.emojilist import ej
# from RasAsiVer1.WOrk_Packeg.LightDetailing.viewAU.viewAUrequests import vievAUrequests
from RasAsiVer2.Time_Packeg.TodayTasks import TodayTasks


def k2(t_stop):
    Tasks = TodayTasks()
    while not t_stop.is_set():
        cTime = datetime.now()
        # print(cTime.hour, cTime.minute)
        if cTime.hour == 00 and cTime.minute == 00:
            msg = emojize(f'{ej["слон"]} Время работы сервера:\t {str(timeHasPassed(startTimeRasAsi))}')
            send(topic='Server time ☁', message=msg)
        elif cTime.hour == 8 and cTime.minute == 20:
            Tasks.take_tasks()
        elif cTime.hour == 00 and cTime.minute == 1:
            Tasks.check()
            Tasks.clean()
        try:
            msgpipeline = read_message()
            if msgpipeline:
                print(msgpipeline)
                if 'Время\r\n' in msgpipeline:
                    msg = emojize(f'{ej["слон"]} Время работы сервера:\t {str(timeHasPassed(startTimeRasAsi))}')
                    send(topic='Server time', message=msg)
                    print(emojize(f'Время работы сервера было отправлено по внешнему запросу {datetime.now()}'))
                elif 'Хранилище\r\n' in msgpipeline:
                    print('Хранилище')
                else:
                    send(topic='Неподдерживаемая команда', message=f'Неподдерживаемая '
                    f'команда "{msgpipeline[0]}"<br/>Список поддерживаемых команд:<br/>1. Время')
        except:
            print('EXCEPTION!!!!!!!!!!!')
            send(topic='Ошибка', message='Ошибка при выполнении read_message<br/>'
                                         '1. следует отследить название ошибки<br/>'
                                         '2. следует проверить, продолжает ли работать time_management при '
                                         'вызове read_message через конструкцию try/except<br/>'
                                         '3. возобновиться ли работа в нормальном режиме после ошибки - '
                                         'единовременная ошибка или перманентная?')
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