from .Download_Packeg import listOfOrder as listOfOrder_Download_Packeg
# from .External_Packeg import listOfOrder as listOfOrder_External_Packeg
from .External_Packeg.electricity_monitoring import electricity_monitoringFunction
from sys import platform
import datetime


startTimeRasAsi = datetime.datetime.now()


def mainMenu():
    variable1 = 0
    print('FROM mainMenu')
    # if platform == 'linux':
    #     electricity_monitoringFunction()
    while variable1 == 0:
        print('FROM cycle')
        print('\nСписок доступных команд:\n1 - Download_Packeg\n2 - External_Packeg\n3 - program runtime\n0 - stop')
        comand1 = input('Выберете пакет\t')
        if comand1 == '1':
            pass
            # listOfOrder_Download_Packeg()
        elif comand1 == '0':
            raise SystemExit
        # elif comand1 == '2':
        #     listOfOrder_External_Packeg()
        elif comand1 == '3':
            print(datetime.datetime.now() - startTimeRasAsi)
        else:
            print('\nВы ввели не верную команду\nпопробуйте сново')
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
