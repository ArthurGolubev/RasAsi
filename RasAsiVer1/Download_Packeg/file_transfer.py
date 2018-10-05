import os


def copyfun():
    os.chdir(r'G:\REMOTE SENSING IMG\DigitalGlobe')
    listDirPHDD = set(os.listdir())
    os.chdir(r'F:\REMOTE SENSING DATA')
    listDirPC = set(os.listdir())
    newDirInPHHD = listDirPHDD.difference(listDirPC)
    os.chdir(r'G:\REMOTE SENSING IMG\DigitalGlobe')

    for i2 in os.walk(r'G:\REMOTE SENSING IMG\DigitalGlobe'):
        print(i2)
    numberFile = 0

def prost2():
    print('privet from transfer')

if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    # copyfun()
# for i in newDirInPHHD:
#     st = time.time()
#     shutil.copytree(rf'G:\REMOTE SENSING IMG\DigitalGlobe\{i}', rf'F:\REMOTE SENSING DATA\{i}', ignore=shutil.ignore_patterns('*.rrd', '*.aux'))
#     et = time.time() - st
#     print(et)
