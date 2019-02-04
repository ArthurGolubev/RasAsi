from RasAsiVer1.WOrk_Packeg.LightDetailing.viewAU.viewAUrequests import vievAUrequests


def commandList():
    while True:
        print('\n-|viewAU|-'
              '\nДоступные команды:\n'
              '1 - vievAUrequests\n'
              '0 - back to main')
        command1 = input('\nВведите команжу:\t')

        if command1 == '1':
            vievAUrequests()
            input('...[press Enter]...')
        elif command1 == '0':
            return 0
        else:
            print('\nВы ввели неверную команду\nпопробуйте сново')
            input('...[press Enter]...')
