from sys import platform
# from .Time_Packeg.legacy_startTimeRasAsi import *
# from .WOrk_Packeg import commandList as cL_WOrk_Packeg
from .Download_Packeg import commandList as cL_Download_Packeg
# from .legacy_Gmail_Packeg import commandList as cL_Gmail_Packeg
from RasAsiVer2.Threads import threads
# from .resService_Packeg import commandList as cL_resService_Packeg
# from .Satellite_img_Packeg import commandList as cL_Setellite_img_Packeg
# from .Time_Packeg.electricity_monitoring import electricity_monitoringFunction, userDirectiv


threads.start_threads()

def mainMenu():
    print('FROM mainMenu')
    while True:
        print('FROM cycle')
        print('\nСписок доступных команд:\n'  # TODO правки. Переделать
              '1 - Download_Packeg\n'
              '2 - Time_Packeg\n'
              '3 - program runtime\n'
              '4 - legacy_Gmail_Packeg\n'
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
                # userDirectiv()
                input('pause\t')
            raise SystemExit
        # elif comand1 == '2':
        #     commandList_External_Packeg()
        elif command1 == '3':
            print(3)
        elif command1 == '4':
            # cL_Gmail_Packeg()
            input('pause\t')
        elif command1 == '5':
            cL_Setellite_img_Packeg()
        elif command1 == '6':
            print(6)
        elif command1 == '7':
            cL_WOrk_Packeg()
        else:
            print('\nВы ввели неверную команду\nпопробуйте сново')
            input('...[press Enter]...')