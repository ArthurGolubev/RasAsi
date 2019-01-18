from .downloadScript_04 import download, prost


def commandList():
    while True:
        print('\n-|Download_Packeg|-'
              '\nДоступные команды:\n'
              '1 - prost\n2 - prost 2\n'
              '3 - download\n4 - copyfun\n'
              '0 - back to main')
        command1 = input('\nВведите команду:\t')
        if command1 == '1':
            prost()
            input('...[press Enter]...')
        # elif command1 == '2':
        #     prost2()
            input('...[press Enter]...')
        elif command1 == '3':
            download()
            input('...[press Enter]...')
        # elif command1 == '4':
        #     copyfun()
            input('...[press Enter]...')
        elif command1 == '0':
            return 0
        else:
            print('\nВы ввели неверную команду\nпопробуйте сново')
            input('...[press Enter]...')


"""
получается достаёт из текущей папки скрипт downloadScript_03
и импортирует из него переменную a2
это значит, что переменная a2 теперь лежит в файле __init__
в дериктории Download_Packeg/__init__.py
"""