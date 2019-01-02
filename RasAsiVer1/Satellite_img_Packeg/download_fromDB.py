import os
import time
import subprocess
import urllib.request
from sys import platform
from ..Gmail_Packeg.Send import send, log
from .work_composition.my_query import *
from .work_composition.queri_select import query_select
from .work_composition.query_insert import query_insert1
# TODO: добавление сайза в GB для метаданных, добавление примерного времени скачивания в метаданные события


def download():
    if platform == 'win32':
        HDD = input('укажите букву жёсткого диска:\t')
        keypath1 = fr'{HDD.upper()}:\REMOTE SENSING IMG\Download'
    elif platform == 'linux':
        keypath1 = r'/media/pi/PORTABLE HDD/REMOTE SENSING IMG/Download'
    print(f'keypath1 - {keypath1}')
    file1_number = []
    available_metadata = query_select(DBq1)
    if not available_metadata:
        print('В базе данных пока нет эвентов')
        return 0
    else:
        print('Доступны следующие эвенты:')
    for i in range(len(available_metadata)):
        print(f'{available_metadata[i][0]} - {available_metadata[i][1]}')
    ucommand = input('\nУкажите id эвента\t')
    listlink = query_select(DBq2, ucommand)
    print('Количество скачеваемых элементов: ', len(listlink))
    overallTime = time.time()
    TimeNow = datetime.datetime.now()
    createlogName = f'{TimeNow.day}-{TimeNow.month}-{TimeNow.year}_time-{TimeNow.hour}-{TimeNow.minute}'
    if not os.path.exists(os.path.join(keypath1, 'logFiles')):
        os.makedirs(os.path.join(keypath1, 'logFiles'))
    with open(os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt'), 'a') as logFile:
        logFile.write(f'Запуск программы\n{time.ctime()}\n\n')
    links_number = len(listlink)
    for i in range(links_number):
        plist = listlink[i][0].split('/')
        if plist[2] == 'opendata.digitalglobe.com':
            SOURCE = 'DigitalGlobe'
            try:
                os.makedirs(os.path.join(keypath1, 'DigitalGlobe', plist[3], plist[4], plist[5]))
                os.chdir(os.path.join(keypath1, 'DigitalGlobe', plist[3], plist[4], plist[5]))
                downloadFuc(plist, listlink[i][0], i, links_number, createlogName, keypath1)
            except FileExistsError:
                os.chdir(os.path.join(keypath1, 'DigitalGlobe', plist[3], plist[4], plist[5]))
                file1_number.extend(os.listdir())
                '''количество уникальных файлов, а значит пройденных итераций'''
                '''важно при прерывании и последующем возобнавлении скачивания1'''
                amountfiledir = len(set(file1_number))
                print(f'Файлов в папке - {amountfiledir}')
                if i < amountfiledir - 1:
                    # TODO: добавить beautiful_message
                    print(f'файл {plist[7]} пропущен')
                    continue
                downloadFuc(plist, listlink[i][0], i, links_number, createlogName, keypath1)
    with open(os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt'), 'a') as logFile:
        logFile.write('\n\n')
        os.chdir(os.path.join(keypath1, SOURCE, plist[3]))
        overallTime = time.time() - overallTime
        listdir1 = os.listdir()
        totalfiles = 0
        totalsize = 0
        for i1 in listdir1:
            sizeDir = 0
            os.chdir((os.path.join(keypath1, SOURCE, plist[3], i1)))
            listdir2 = os.listdir()
            for i2 in listdir2:
                os.chdir(os.path.join(keypath1, SOURCE, plist[3], i1, i2))
                totalfiles += len(os.listdir())
                for i3 in os.listdir():
                    '''проход по файлам'''
                    sizeDir += os.path.getsize(i3)
                logFile.write(f'Директория {os.getcwd()}\nфайлов - {len(os.listdir())}\n')
                logFile.write(f'Размер директории - {int(sizeDir / 1024 / 1024 / 1024)} GB\n\n')
                totalsize = totalsize + sizeDir
        dtime = datetime.timedelta(seconds=int(overallTime))
        tsize = int(totalsize / 1024 / 1024 / 1024)
        logFile.write(f'Общее время выполнение программы - {dtime}\n')
        logFile.write(f'Скачано файлов {totalfiles} из {links_number - 1}\n')
        logFile.write(f'Скачано {tsize} GB')
        dtime = dtime.total_seconds()
        timekitchen = datetime.time(hour=int(dtime / 3600), minute=int((dtime % 3600) / 60), second=int(dtime % 60))
        print(timekitchen)
        query_insert1(DBq3, (timekitchen, tsize, plist[3]))
    send(topic='Загрузка завершена!',
         message=log(os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt')))
    print('Done!')
    ucommand = input('Задача завершина\nОткрыть файл-лог? (1/0)\t')
    if ucommand == '1':
        if platform == 'win32':
            os.startfile(os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt'))
        else:
            subprocess.call(['xdg-open', os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt')])
    else:
        return 0




def downloadFuc(list1, string1, i, links_number, createlogName, keypath1):
    with open(os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt'), 'a') as logFile:
        print(f'\nИтерация №{i+1} из {links_number}')
        logFile.write(f'Итерация №{i+1} из {links_number}\n')
        startTime = time.time()
        urllib.request.urlretrieve(f'{string1}', f'{i}_{list1[7]}')
        elapsedTime = time.time() - startTime
        print(f'скачался файл номер {i} - {list1[7]}')
        file1Size = int((os.path.getsize(f'{i}_{list1[7]}'))/1024/1024)
        print(f'Средняя скорость {elapsedTime/(file1Size)} MB/sec')
        print(f'...Processing {1 + int(i * (100 / links_number))}%...')
        logFile.write(f'скачался файл номер {i} - {list1[7]}\n')
        logFile.write(f'Время скачивания {datetime.timedelta(seconds=elapsedTime//1)}\n')
        logFile.write(f'Размер файла - {file1Size} MB\n\n')


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    download()
