from RasAsiVer1.WOrk_Packeg.LightDetailing.GetAU24.getAU24 import getAU24
from RasAsiVer1.WOrk_Packeg.LightDetailing.viewAU.viewAUrequests import vievAUrequests


def commandList():
    while True:
        print('\n-|LightDetailing|-'
              '\nДоступные команды:\n'
              '1 - GetAU24\n'
              '2 - viewAU\n'
              '0 - back to main')
        command1 = input('\nВведите команжу:\t')

        if command1 == '1':
            user = input('Введите имя пользователя')
            getAU24(user)
            input('...[press Enter]...')
        elif command1 == '2':
            vievAUrequests()
            input('...[press Enter]...')
        elif command1 == '0':
            return 0
        else:
            print('\nВы ввели неверную команду\nпопробуйте сново')
            input('...[press Enter]...')
