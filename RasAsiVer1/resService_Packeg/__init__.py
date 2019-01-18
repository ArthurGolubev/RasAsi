from .time_management_RES import time_managment_RES


# TODO: переписать все while varible == 0 в while True


def commandList(tEvent):
    while True:
        print(tEvent)
        print('\n-|resService_Packeg|-'
              '\nДоступные команды:\n'
              '1 - time_managment_RES\n'
              '0 - back to main')
        command1 = input('\nВведите команду:\t')
        if command1 == '0':
            return 0
        elif command1 == '1':
            time_managment_RES(tEvent)
            input('...[press Enter]...')
        else:
            print('\nВы ввели неверную команду\nпопробуйте сново')
            input('...[press Enter...]')
