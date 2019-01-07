import os

def prost3():
    print('Hello from Process Managment Packeg!')


# def getpid():
#     print(os.getppid())
#     raise SystemExit

if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    prost3()