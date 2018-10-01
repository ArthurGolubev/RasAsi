import os, urllib.request, time

def prost():
    print('privet!!')
def download():
    file1_number = []
    with open('D:\REMOTE SENSING IMG\purl_list.txt', 'r') as file1:
        links_number = len(file1.readlines())                                                                           #пробегает по всем строчкам, возвращает количество
        file1.seek(0)                                                                                                   #Возвращает курсор в начало файла
        overallTime = time.time()                                                                                       #Присваевает начальное время запуска программы в секундах с начала эпохи переменной overallTime
        logFile = open(f'D:\REMOTE SENSING IMG\logFile.txt', 'a')
        logFile.write(f'Запуск программы\n{time.ctime()}\n')                                                            #записывает в файл текущую датувремя в понятной отформатированой форме
        logFile.close()
        for i in range(links_number - 1):                                                                               #считает i с 0, следовательно цифру количества ссылок (которая считается с 1, а не с 0) нужно убавить на 1
            logFile = open('D:\REMOTE SENSING IMG\logFile.txt', 'a')
            string1 = file1.readline().strip()                                                                          # .strip() удаляет лишние элементы в строке, такие как не явно присутствующий символ переноса на следующую строку /n
            list1 = string1.split('/')                                                                                  #Делит строку URL-пути на список из названий
            try:                                                                                                        #Если такой папки нет - создаёт (нужно для первой ииерации при каждом новом названии директории)
                os.makedirs(f'D:\REMOTE SENSING IMG\DigitalGlobe\{list1[3]}\{list1[4]}\{list1[5]}')
                os.chdir(f'D:\REMOTE SENSING IMG\DigitalGlobe\{list1[3]}\{list1[4]}\{list1[5]}')
                print(f'Итерация №{i+1} из {links_number}\n mark #1')
                logFile.write(f'Итерация №{i+1} из {links_number}\n mark #1\n\n')
                startTime = time.time()
                urllib.request.urlretrieve(f'{string1}', f'{i}_{list1[7]}')
                elapsedTime = time.time() - startTime
                print(f'скачался файл номер {i} - {list1[7]}\n')
                logFile.write(f'скачался файл номер {i} - {list1[7]}\n')
                logFile.write(f'Время скачивания {elapsedTime}\n')
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
                logFile.write(f'Время скачивания {elapsedTime}\n')
                logFile.close()
        logFile = open('D:\REMOTE SENSING IMG\logFile.txt', 'a')                                                        #Общий лог за скачивание
        logFile.write('\n\n')
        os.chdir(f'D:\REMOTE SENSING IMG\DigitalGlobe\{list1[3]}')
        overallTime = time.time() - overallTime
        listdir1 = os.listdir()
        v2 = 0
        for i2 in listdir1:                                                                                             #Если скачивалось в 2 и более директории
            os.chdir(f'D:\REMOTE SENSING IMG\DigitalGlobe\{list1[3]}\{i2}')
            logFile.write(f'Директория {os.getcwd()}\n файлов - {len(os.listdir())}\n')
            v2 += len(os.listdir())
        logFile.write(f'Общее время выполнение программы - {overallTime}\n')
        logFile.write(f'Скачано файлов {v2} из {links_number}')
        logFile.close

if __name__ != '__main__':
    print('ЗАПУСК МОДУЛЯ')
    # download()