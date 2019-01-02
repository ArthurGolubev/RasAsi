import datetime
from sys import platform
from .work_composition.my_query import *
from .work_composition.query_insert import query_insert1
from .work_composition.input_metadata import input_metadata
from .work_composition.initial_request import initial_request

# TODO: написать документацию к модулю


def add_settelite_link():
    """Добавление ссылок в БД (на скачивание спутниковых снимков)"""
    todays_id = initial_request()
    existmetadata = {}
    LinkList = []

    if platform == 'win32':
        HDD = input('укажите букву жёсткого диска:\t')
        keypath1 = fr'{HDD.upper()}:\REMOTE SENSING IMG\Download\purl_list\linkToDB.txt'
    elif platform == 'linux':
        # TODO: добавить путь для скачки на HDD_DB
        keypath1 = r'/media/pi/PORTABLE HDD/REMOTE SENSING IMG/Download/purl_list/linkToDB.txt'
    with open(keypath1) as F:
        '''Считываение всех строк из файла со ссылками в спсиок "a" '''
        a = F.readlines()
        if not a:
            print('Файл linkToDB.txt не содержит ссылок для добавления в базу данных')
            return 0
        else:
            for i in range(len(a)):
                print('\n{:,^47}'.format(' mark #1 from: ') + '\n{: ^47}'.format(__name__) + '\n{:,^47}'.format('') + '\n')  #<<<<_MARK_<<<<
                print(a[i])
                # TODO: Добавить бьютифул месадж?
                print('Чтение строк из файла с ссылками')
                print(f'итерация {i+1}')
                if a[i].isspace():
                    '''Если в файле встречается пустая строка, то пропустить эту итерацию'''
                    print('{:-^47}'.format(f'пустая строка {i+1}'))
                    continue
                else:
                    '''Если есть лишние пробелы до или после ссылки - убрать. Распарсить ссылку на элементы списка'''
                    plist = a[i].strip().split('/')
                    if plist[2] == 'opendata.digitalglobe.com':
                        SOURSE = 'DigitalGlobe'
                        if not existmetadata:
                            '''Первая, обязательная итерация для проверки методынных к ссылке'''
                            """
                            Отправляем пустой словарь, для запуска функции, которой нужен словарь.
                            Взамен получаем словарь со значениями для запуска этой функции во второй итерации
                            """

                            existmetadata = input_metadata(plist, existmetadata)
                            id_metadata = existmetadata.get(plist[3])
                            print(id_metadata)
                        else:
                            '''Вторая и последующие итерации для проверки методанных к ссылке'''

                            print('В предыдущей итерации был возвращён словарь с имеющимися метаданными')
                            existmetadata = input_metadata(plist, existmetadata)
                            id_metadata = existmetadata.get(plist[3])
                        print(f'a{[i]}:\t', a[i].strip())
                        print('id для привязки данной ссылки к методанным ->', id_metadata)
                        dataformat = a[i].strip()[-4:]
                        print('Формат данных:\t', dataformat)
                        print("id для привязки данной ссылки к дате добавления ->", todays_id)

                        """
                        формирую элемент списка для вставки в DB
                        """
                        datekitchen = plist[5].split('-')
                        LinkList.append((
                            todays_id,
                            id_metadata,
                            a[i].strip(),
                            plist[4],
                            dataformat,
                            datetime.date(year=int(datekitchen[0]), month=int(datekitchen[1]), day=int(datekitchen[2]))
                        ))
    '''передовать множественной вставкой не эффективно: если хоть одна строка дублируется - отмена всей транзакции'''
    for i in LinkList:
        query_insert1(DBq4, i)


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    add_settelite_link()