import urllib.request, time, os, datetime, subprocess
from sys import platform
from RasAsiVer1.Gmail_Packeg.Send import send, log

def prost():
    print('privet from download!!')

def download():
    if platform == 'win32':
        keypath1 = r'D:\REMOTE SENSING IMG\Download'
    elif platform == 'linux':
        keypath1 = r'/media/pi/PORTABLE HDD/REMOTE SENSING IMG/Download'
    print(f'keypath1 - {keypath1}')
    file1_number = []
    os.chdir(os.path.join(keypath1, 'purl_list'))
    listdir0 = os.listdir()
    print('Доступны файлы с ссылками:')
    variable1 = 0
    for i in listdir0:
        print(f'{variable1} - {i}')
        variable1 = variable1 + 1
    variable2 = int(input('\nУкажите порядковый номер файла\t'))
    print(listdir0[variable2])
    with open(os.path.join(keypath1, 'purl_list', listdir0[variable2]), 'r') as file1:
        links_number = len(file1.readlines())                                                                           #пробегает по всем строчкам, возвращает количество
        file1.seek(0)                                                                                                   #Возвращает курсор в начало файла
        overallTime = time.time()                                                                                       #Присваевает начальное время запуска программы в секундах с начала эпохи переменной overallTime
        TimeNow = datetime.datetime.now()
        createlogName = f'{TimeNow.day}-{TimeNow.month}-{TimeNow.year}_time-{TimeNow.hour}-{TimeNow.minute}'
        logFile = open(os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt'), 'a')
        logFile.write(f'Запуск программы\n{time.ctime()}\n\n')                                                          #записывает в файл текущую датувремя в понятной отформатированой форме
        logFile.close()
        for i in range(links_number - 1):                                                                               #считает i с 0, следовательно цифру количества ссылок (которая считается с 1, а не с 0) нужно убавить на 1
            string1 = file1.readline().strip()                                                                          # .strip() удаляет лишние элементы в строке, такие как не явно присутствующий символ переноса на следующую строку /n
            list1 = string1.split('/')                                                                                  #Делит строку URL-пути на список из названий
            try:                                                                                                        #Если такой папки нет - создаёт (нужно для первой ииерации при каждом новом названии директории)
                os.makedirs(os.path.join(keypath1, 'DigitalGlobe', list1[3], list1[4], list1[5]))
                os.chdir(os.path.join(keypath1, 'DigitalGlobe', list1[3], list1[4], list1[5]))
                downloadFuc(list1, string1, i, links_number, createlogName, keypath1)

            except FileExistsError:                                                                                     #Если папка уже существует (создалоась при первой итерации для уникального названия директории)
                os.chdir(os.path.join(keypath1, 'DigitalGlobe', list1[3], list1[4], list1[5]))
                file1_number.extend(os.listdir())                                                                       #расширяемый список всех скачаных файлов (итерация 1 - файл1, файл2. итерация 2 - файл1, файл2, файл1, файл2, файл3)
                print(f'файлов в папке - {len(set(file1_number))}\n')                                                   #длинна множества set уникальных имён файлов
                v1 = len(set(file1_number))                                                                             #количество уникальных имён (скачанных файлов), а значит пройденных итераций по строкам файла с сылками
                """
                парсит количество файлов в папке по текущей ссылке. Добавляет уникальные элементы в множество set
                каждый раз обнавляет переменную v1
                при добавлении уникальных имён из других папок в множество, его длинна меняется и присваевается переменной v1
                так если количество файлов в папке 23, то v1 = 23 и начинает скачивать последний файл в папке
                а при переходе в другую папку, например с 43 файлами, то 43 файла добавятся в set (43 раза) а длинна
                множества set увеличится на 43 и станет 66. Переменной v1 присвоется 66 и итерации дойдут до 66, т.е. до 66
                ссылки по счёту и начнётся скачивание последнего файла уже в этой папке.

                при переходе обратно в первую папку v1 будет на той итерации, на которой идёт ссылка для скачивания файла
                следующего по счёту в эту папку
                """
                if i < v1-1:
                    print(f'файл {list1[7]} пропущен')
                    continue                                                                                            #пропуск итераций до последнего скачанного файла

                downloadFuc(list1, string1, i, links_number, createlogName, keypath1)

        with open(os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt'), 'a') as logFile:                                #Общий лог за скачивание
            logFile.write('\n\n')
            os.chdir(os.path.join(keypath1, 'DigitalGlobe', list1[3]))
            overallTime = time.time() - overallTime
            listdir1 = os.listdir()
            v2 = 0
            allSize = 0
            for i2 in listdir1:                                                                                         #Если скачивалось в 2 и более директории
                sizeDir = 0
                os.chdir(os.path.join(fr'{keypath1}', 'DigitalGlobe', list1[3], i2))
                listdir2 = os.listdir()
                for i3 in listdir2:
                    os.chdir(os.path.join(keypath1, 'DigitalGlobe', list1[3], i2, i3))
                    v2 += len(os.listdir())
                    for i4 in os.listdir():
                        sizeDir = sizeDir + os.path.getsize(i4)
                logFile.write(f'Директория {os.getcwd()}\nфайлов - {len(os.listdir())}\n')
                logFile.write(f'Размер директории - {int(sizeDir/1024/1024/1024)} GB\n\n')
                allSize = allSize + sizeDir
            logFile.write(f'Общее время выполнение программы - {datetime.timedelta(seconds = overallTime//1)}\n')
            logFile.write(f'Скачано файлов {v2} из {links_number-1}\n')
            logFile.write(f'Скачано {int(allSize/1024//1024/1024)} GB')
    send(topic='Загрузка завершена!', message=log(os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt')))
    print('Done!')
    option1 = input('Задача завершина\nОткрыть файл-лог? (1/0)\t')
    if option1 == '1':
        if platform == 'win32':
            os.startfile(os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt'))
        else:
            subprocess.call(['xdg-open', os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt')])
    else:
        return 0


def downloadFuc(list1, string1, i, links_number, createlogName, keypath1):
    with open(os.path.join(keypath1, 'logFiles', f'logFile{createlogName}.txt'), 'a') as logFile:
        print(f'Итерация №{i+1} из {links_number-1}\n')                                                                #Позволяет перекачать последний файл в последовательности
        logFile.write(f'Итерация №{i+1} из {links_number-1}\n')                                                        #Нужно в случае, если последний запуск программы был прерван на середине загрузки файла
        startTime = time.time()
        urllib.request.urlretrieve(f'{string1}', f'{i}_{list1[7]}')
        elapsedTime = time.time() - startTime
        print(f'скачался файл номер {i} - {list1[7]}\n')
        print(f'...Processing {1+int(i*(100/links_number))}%...')
        file1Size = int((os.path.getsize(f'{i}_{list1[7]}'))/1024/1024)
        logFile.write(f'скачался файл номер {i} - {list1[7]}\n')
        logFile.write(f'Время скачивания {datetime.timedelta(seconds=elapsedTime//1)}\n')
        logFile.write(f'Размер файла - {file1Size} MB\n\n')


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    download()
