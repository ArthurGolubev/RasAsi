# TODO: добавить метод просмотра информации о метаданных (запрос на вывод описания эвента)
# TODO: написать метод интерактивного ввода селекта от пользователя
# TODO: Добавить кастомную функцию для добавления нужного описания к определённым метаданным
# TODO: Добавить запрос на координаты X и Y, который запускает сайт гугл планета земля и вставляет нужные координаты


import os
from sys import platform
from .input_link import add_settelite_link
from .download_fromDB import download

def commandList():
    variable1 = 0
    if platform == 'linux':
        print('\n{:,^47}'.format(' mark #TTTTT from: ') + '\n{: ^47}'.format(__name__) + '\n{:,^47}'.format('') + '\n')  #<<<<_MARK_<<<<
        if not os.path.exists('/media/pi/PORTABLE HDD/REMOTE SENSING IMG'):
            print('\n{:,^47}'.format(' mark #MMM from: ') + '\n{: ^47}'.format(__name__) + '\n{:,^47}'.format('') + '\n')  #<<<<_MARK_<<<<
            os.mkdir('/media/pi/PORTABLE HDD/REMOTE SENSING IMG/Download/purl_list')

    while variable1 == 0:
        print('\n-|Satellite_img_Packeg|-'
              '\nДоступные команды:\n1 - add_settelite_link\n2 - download\n0 - back to main')
        command1 = input('\nВведите команду:\t')
        if command1 == '1':
            add_settelite_link()
            input('...[press Enter]...')
        elif command1 == '2':
            download()
            input('...[press Enter]...')
        elif command1 == '0':
            return 0
        else:
            print('\nВы ввели неверную команду\nпопробуйте сново')
            input('...[press Enter]...')