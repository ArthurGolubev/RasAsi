import threading
from sys import platform
from .External_Packeg.emojilist import ej
from .Time_Packeg.startTimeRasAsi import *
# from .Time_Packeg.time_management import k2
from RasAsiVer2.Time_Packeg.TimeManagement import TimeManagement

from .Gmail_Packeg import commandList as cL_Gmail_Packeg
from .Download_Packeg import commandList as cL_Download_Packeg
from .resService_Packeg import commandList as cL_resService_Packeg
# from .Time_Packeg import commandList as commandList_External_Packeg
from .Satellite_img_Packeg import commandList as cL_Setellite_img_Packeg
from .Time_Packeg.electricity_monitoring import electricity_monitoringFunction, userDirectiv
from .WOrk_Packeg import commandList as cL_WOrk_Packeg


# t_stop = threading.Event()
# if platform == 'linux':
#     t = threading.Thread(target=electricity_monitoringFunction, name='Treading_emF', args=(t_stop,))
#     t.start()
#
# t2 = threading.Thread(target=k2, name='T_time_manegement', args=(t_stop,))
# t2.start()

t = threading.Thread(target=TimeManagement().time_line, name='T_TimeManagement')
t.start()

def mainMenu():
    print('FROM mainMenu')
    while True:
        print('FROM cycle')
        print('\nСписок доступных команд:\n'
              '1 - Download_Packeg\n'
              '2 - Time_Packeg\n'
              '3 - program runtime\n'
              '4 - Gmail_Packeg\n'
              '5 - Setallite_img_Packeg\n'
              '6 - resService_Packeg\n'
              '7 - WOrk_Packeg\n'
              '0 - stop')
        command1 = input('Выберете пакет\t')
        if command1 == '1':
            cL_Download_Packeg()
        elif command1 == '0':
            print(f'...завершение программы...')
            if platform == 'linux':
                userDirectiv()
            t_stop.set()
            raise SystemExit
        # elif comand1 == '2':
        #     commandList_External_Packeg()
        elif command1 == '3':
            print(f'{ej["молния"]} {timeHasPassed(startTimeRasAsi)} {ej["молния"]}')
        elif command1 == '4':
            cL_Gmail_Packeg()
        elif command1 == '5':
            cL_Setellite_img_Packeg()
        elif command1 == '6':
            cL_resService_Packeg(t_stop)
        elif command1 == '7':
            cL_WOrk_Packeg()
        else:
            print('\nВы ввели неверную команду\nпопробуйте сново')
            input('...[press Enter]...')

"""
Импортируется пакет (библиотека) RasAsiVer1
Это инициализирует в ней файл __init__.py (RasAsiVer1/__init__.py)
1_В котором импортируется пакет (библиотека) Download_Packeg -> Download_Packeg/__init__.py
2_Это инициализирует в нём файл __init__.py (Download_Packeg/__init__.py)
3_Файл __init__.py (Download_Packeg/__init__.py) импортирует из файла downloadScript.py переменную a2
4_таким образом в Download_Packeg, а именно в его __init__.py содержится переменная a2
5_БЛАГОДАРЯ ЭТОМУ текущий файл __init__.py (RasAsiVer1->__init__.py) имеет возможность
импортировать переменную a2 из пакета Download_Packeg, которую он, в свою очередь, импортировал
в себя (в свой файл __init__.py) из файла downloadScript_04.py
6_Таким образом вместо обращения к переменной a2 через

RasAsiVer1.Download_Packeg.downloadScript.a2

мы можем обращатся к переменной просто
RasAsiVer1.a2
"""
