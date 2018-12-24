# print('print from __q1__')
from . import *
from work_composition.config import *
# TODO посмотреть и, возможно, переписать инициализацию в пакетах, как тут!


def query_insert1(zapros, *argument2):
    print(f'запрос:\n{zapros}\nаргументы: {argument2}')
    connection1 = mysql.connector.connect(**config)
    cursor = connection1.cursor()
    try:
        if isinstance(*argument2, tuple):
            '''Если передан кортеж значений'''
            cursor.execute(zapros, *argument2)
        else:
            '''если передан один аргумент'''
            cursor.execute(zapros, argument2)
        print('ДОБАВЛЕНО')
    except mysql.connector.errors.IntegrityError:

        '''бьютифул меседж'''

        if len(f'запрос: {zapros}') > len(f'аргументы: {argument2}'):
            '''для динамического форматирования строки вывода "красивого" сообщения в зависимости от длинны сообщения'''
            message = len(f'запрос: {zapros}')
        else:
            message = len(f'аргументы: {argument2}')

        messagelen = '{' + f':-^{message}' + '}'
        print(messagelen.format(''))
        '''бьютифул месадж'''

        print('УЖЕ СУЩЕСТВУЕТ')
        print(messagelen.format(''))
    finally:
        last_id = cursor.lastrowid
        print('{:-^47}'.format(f'return last_id: {last_id}'))
        connection1.commit()
        cursor.close()
        connection1.close()

    return last_id


# TODO: сделать функцию beautiful_message. передача множества аргументов: 1(обязательный) - само сообщение
 # в верхннем колонтитуле
 # 2 - верхняя строка сообщения. 3 - нижняя строка сообщение. сравнение по типу *арг up=arg[0], down=arg[-1]
 # arg - это передача списка, состоящего из сообщений. последний (может быть второй обязательный)
 # аргумент - должен (может) содержать из каких символов формировать форматирование
 # возможно использовать именованные аргументы
        # TODO: добавить beautiful message в вывод везде, где есть вывод
        # TODO: сделать функцию mark #x? с передачей в неё номер mark по типу mark(1) -> print('mark #1')
        # TODO: а если передать сообщение (строку, а не число), то выведет mark('МОЯ СТРОКА') -> print(mark)
        # TODO: сделать класс по работе с базой данных
