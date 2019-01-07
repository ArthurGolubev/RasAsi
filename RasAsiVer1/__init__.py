# TODO: навести красоту в импортах
from .Download_Packeg import commandList as commandList_Download_Packeg
# from .External_Packeg import commandList as commandList_External_Packeg
from .Gmail_Packeg import commandList as commandList_Gmail_Packeg
from .External_Packeg.electricity_monitoring import electricity_monitoringFunction, userDirectiv
from .External_Packeg.time_management import k2
from sys import platform
import threading
from .Satellite_img_Packeg import commandList as commandList_Setellite_img_Packeg
from .External_Packeg.startTimeRasAsi import *


t_stop = threading.Event()
if platform == 'linux':
    t = threading.Thread(target=electricity_monitoringFunction, name='Treading_emf', args=(t_stop,))
    t.start()

t2 = threading.Thread(target=k2, name='T_time_manegement', args=(t_stop,))
t2.start()


def mainMenu():
    variable1 = 0
    print('FROM mainMenu')
    while variable1 == 0:
        print('FROM cycle')
        print('\nСписок доступных команд:\n'
              '1 - Download_Packeg\n'
              '2 - External_Packeg\n'
              '3 - program runtime\n'
              '4 - Gmail_Packeg\n'
              '5 - Setallite_img_Packeg\n'
              '0 - stop')
        command1 = input('Выберете пакет\t')
        if command1 == '1':
            commandList_Download_Packeg()
        elif command1 == '0':
            print(f'...завершение программы...')
            if platform == 'linux':
                userDirectiv()
            t_stop.set()
            raise SystemExit
        # elif comand1 == '2':
        #     commandList_External_Packeg()
        elif command1 == '3':
            print(timeHasPassed(startTimeRasAsi))
        elif command1 == '4':
            commandList_Gmail_Packeg()
        elif command1 == '5':
            commandList_Setellite_img_Packeg()
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
