import os, shutil, datetime, time


def copyfun():
    print('\n-|copyfun|-\n'
          'Function in Progress...')
    TimeNow = datetime.datetime.now()
    os.chdir(r'G:\REMOTE SENSING IMG\DigitalGlobe')
    listDirPHDD = set(os.listdir())
    os.chdir(r'F:\REMOTE SENSING DATA')
    listDirPC = set(os.listdir())
    newDirInPHHD = listDirPHDD.difference(listDirPC)
    os.chdir(r'G:\REMOTE SENSING IMG\DigitalGlobe')

    createLogName = f'{TimeNow.day}-{TimeNow.month}-{TimeNow.year}_{TimeNow.hour}-{TimeNow.minute}'
    with open(rf'F:\REMOTE SENSING DATA\logFile_{createLogName}.txt', 'w') as logFile:
        logFile.write(f'Запуск программы\n{time.ctime()}\n')
        for i in newDirInPHHD:
            shutil.copytree(rf'G:\REMOTE SENSING IMG\DigitalGlobe\{i}', rf'F:\REMOTE SENSING DATA\{i}')
        endTime = datetime.datetime.now()
        elapsedTime = endTime - TimeNow
        logFile.write(f'Время копирования файлов - {elapsedTime}\n')
        print('Done!')
    option1 = input('Задача завершина\nОткрыть файл-лог? (1/0)\t')
    if int(option1):
        os.startfile(rf'F:\REMOTE SENSING DATA\logFile_{creatLogName}.txt')
    else:
        return 0


def prost2():
    print('privet from transfer')


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    copyfun()

