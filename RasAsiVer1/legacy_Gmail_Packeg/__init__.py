from .Send import prost5, send


def commandList():
    while True:
        print('\n-|legacy_Gmail_Packeg|-'
              '\nДоступные команды:\n'
              '1 - prost5\n'
              '2 - send\n'
              '0 - back to main')
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
