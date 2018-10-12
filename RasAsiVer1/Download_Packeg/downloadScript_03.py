import urllib.request, time, os, datetime


def prost():
    print('privet from download!!')

def download():
    file1_number = []
    with open('D:\REMOTE SENSING IMG\purl_list.txt', 'r') as file1:
        links_number = len(file1.readlines())                                                                           #пробегает по всем строчкам, возвращает количество
        file1.seek(0)                                                                                                   #Возвращает курсор в начало файла
        overallTime = time.time()                                                                                       #Присваевает начальное время запуска программы в секундах с начала эпохи переменной overallTime
        TimeNow = datetime.datetime.now()
        createlogName = f'{TimeNow.day}-{TimeNow.month}-{TimeNow.year}_{TimeNow.hour}-{TimeNow.minute}'
        logFile = open(f'D:\REMOTE SENSING IMG\logFile{createlogName}.txt', 'a')
        logFile.write(f'Запуск программы\n{time.ctime()}\n')                                                            #записывает в файл текущую датувремя в понятной отформатированой форме
        logFile.close()
        for i in range(links_number - 1):                                                                               #считает i с 0, следовательно цифру количества ссылок (которая считается с 1, а не с 0) нужно убавить на 1
            """
            нижную строчку тоже можно записать в функцию downloadFun
            """
            # logFile = open(fr'D:\REMOTE SENSING IMG\logFile{createlogName}.txt', 'a')
            string1 = file1.readline().strip()                                                                          # .strip() удаляет лишние элементы в строке, такие как не явно присутствующий символ переноса на следующую строку /n
            list1 = string1.split('/')                                                                                  #Делит строку URL-пути на список из названий
            try:                                                                                                        #Если такой папки нет - создаёт (нужно для первой ииерации при каждом новом названии директории)
                os.makedirs(f'D:\REMOTE SENSING IMG\DigitalGlobe\{list1[3]}\{list1[4]}\{list1[5]}')
                os.chdir(f'D:\REMOTE SENSING IMG\DigitalGlobe\{list1[3]}\{list1[4]}\{list1[5]}')
                print(f'Итерация №{i+1} из {links_number}\n mark #1')
                """
                нижную строчку тоже можно записать в функцию downloadFun
                """
                # logFile.write(f'Итерация №{i+1} из {links_number}\n mark #1\n\n')
                """
                Возможно вынести в отдельную функцию нижестоящие 4 строчки
                """
                downloadFuc(list1, string1, i, links_number)                                                            #Скорее всего не будет работать, потому что в ней локальные переменные. Нужно передать в неё переменные -string1, list1, i
                # startTime = time.time()
                # urllib.request.urlretrieve(f'{string1}', f'{i}_{list1[7]}')
                # elapsedTime = time.time() - startTime
                # file1Size = (os.path.getsize(f'{i}_{list1[7]}'))//1024//1024
                """
                Хочу посчитать размер данного файла
                возможно вынести в отдельную функцию
                """
                # file1Size = os.path.getsize(f'{i}_{list1[7]}')

                """
                
                """
                print(f'скачался файл номер {i} - {list1[7]}\n')
                logFile.write(f'скачался файл номер {i} - {list1[7]}\n')
                logFile.write(f'Время скачивания {datetime.timedelta(seconds=elapsedTime//1)}\n')
            except FileExistsError:                                                                                     #Если папка уже существует (создалоась при первой итерации для уникального названия директории)
                os.chdir(f'D:\REMOTE SENSING IMG\DigitalGlobe\{list1[3]}\{list1[4]}\{list1[5]}')
                file1_number.extend(os.listdir())                                                                       #расширяемый список всех скачаных файлов (итерация 1 - файл1, файл2. итерация 2 - файл1, файл2, файл1, файл2, файл3)
                print(f'файлов в папке - {len(set(file1_number))}')                                                     #длинна множества set уникальных имён файлов
                print(len(set(file1_number)))
                v1 = len(set(file1_number))                                                                             #количество уникальных имён (скачанных файлов), а значит пройденных итераций по строкам файла
                print('mark #2 ', v1)
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
                    print(f'файл {list1[7]} пропущен\n')
                    continue                                                                                            #пропуск итераций до последнего скачанного файла
                print(f'Итерация №{(i+1)} из {links_number}')                                                          #Позволяет перекачать последний файл в последовательности
                logFile.write(f'Итерация №{(i+1)} из {links_number}\n\n')                                              #Нужно в случае, если последний запуск программы был прерван на середине загрузки файла
                startTime = time.time()
                urllib.request.urlretrieve(f'{string1}', f'{i}_{list1[7]}')
                elapsedTime = time.time() - startTime
                print(f'скачался файл номер {i+1} - {list1[7]}\n')
                logFile.write(f'скачался файл номер {i+1} - {list1[7]}\n')
                logFile.write(f'Время скачивания {datetime.timedelta(seconds=elapsedTime//1)}\n')
            logFile.close()
        logFile = open(fr'D:\REMOTE SENSING IMG\logFile{createlogName}.txt', 'a')                                       #Общий лог за скачивание
        logFile.write('\n\n')
        os.chdir(f'D:\REMOTE SENSING IMG\DigitalGlobe\{list1[3]}')
        overallTime = time.time() - overallTime
        listdir1 = os.listdir()
        v2 = 0

        """
        посмотреть путь для просмотра файлов
        """
        for i2 in listdir1:                                                                                             #Если скачивалось в 2 и более директории
            os.chdir(f'D:\REMOTE SENSING IMG\DigitalGlobe\{list1[3]}\{i2}')
            logFile.write(f'Директория {os.getcwd()}\nфайлов - {len(os.listdir())}\n')
            v2 += len(os.listdir())
        logFile.write(f'Общее время выполнение программы - {datetime.timedelta(seconds = overallTime//1)}\n')
        logFile.write(f'Скачано файлов {v2} из {links_number}')
        logFile.close
    print('Done!')
    option1 = input('Задача завершина\nОткрыть файл-лог? (1/0)\t')
    if int(option1):
        os.startfile('D:\REMOTE SENSING IMG\logFile.txt')
    else:
        return 0

def downloadFuc(list1, string1, i, link_numbers):
    with open(fr'D:\REMOTE SENSING IMG\logFile{createlogName}.txt', 'a') as logFile:
        logFile.write(f'Итерация №{i+1} из {links_number}\n mark #1\n\n')
        startTime = time.time()
        urllib.request.urlretrieve(f'{string1}', f'{i}_{list1[7]}')
        elapsedTime = time.time() - startTime
        file1Size = (os.path.getsize(f'{i}_{list1[7]}')) // 1024 // 1024
    """
    Сюда нужно перенести и запись в лог времени скачивания
    """


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    download()
