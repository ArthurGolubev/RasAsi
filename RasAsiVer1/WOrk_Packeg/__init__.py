from RasAsiVer1.WOrk_Packeg.LightDetailing import commandList as cL


def commandList():
    while True:
        print('\n-|WOrk_Packeg|-'
              '\nДоступные команды:\n'
              '1 - LightDetailing\n'
              '0 - back to main')
        command1 = input('\nВведите команжу:\t')
        if command1 == '1':
            cL()
            input('...[press Enter]...')
        elif command1 == '0':
            return 0
        else:
            print('\nВы ввели неверную команду\nпопробуйте сново')
            input('...[press Enter]...')
