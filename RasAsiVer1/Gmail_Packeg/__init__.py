from .Send import prost5, send


def commandList():
    variable1 = 0
    while variable1 == 0:
        print('\n-|Gmail_Packeg|-'
              '\nДоступные команды:\n1 - prost5\n2 - send\n0 - back to main')
        command1 = input('\nВведите команду:\t')
        if command1 == '0':
            return 0
        elif command1 == '1':
            prost5()
            input('...[press Enter]...')
        elif command1 == '2':
            topic = input('Укажите тему сообщения:\t')
            message = input('Введите текст сообщения:\t')
            send(topic, message)
            input('...[press Enter]...')
        else:
            print('\nВы ввели неверную команду\nпопробуйте сново')
            input('...[press Enter...]')