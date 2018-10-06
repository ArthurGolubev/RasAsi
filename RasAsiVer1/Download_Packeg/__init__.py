from .downloadScript_03 import download, prost
from .file_transfer import copyfun, prost2


def listOfOrder():
    variable1 = 0
    while variable1 == 0:
        print('\n-|Download_Packeg|-'
              '\nДоступные команды:\n1 - prost\n2 - prost 2\n3 - download\n4 - copyfun\n5 - back to main')
        comand1 = input('\nВведите команду:\t')
        if comand1 == '1':
            prost()
            input('...[press Enter]...')
        elif comand1 == '2':
            prost2()
            input('...[press Enter]...')
        elif comand1 == '3':
            download()
        elif comand1 == '4':
            copyfun()
        elif comand1 == '5':
            return 0
        else:
            print('\nВы ввели не верную команду\nпопробуйте сново')
            input('...[press Enter]...')


"""
получается достаёт из текущей папки скрипт downloadScript_03
и импортирует из него переменную a2
это значит, что переменная a2 теперь лежит в файле __init__
в дериктории Download_Packeg/__init__.py
"""