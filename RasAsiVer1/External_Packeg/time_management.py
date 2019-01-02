from datetime import datetime
from time import sleep
from ..Gmail_Packeg import send


def k2(t_stop):
    while not t_stop.is_set():
        cTime = datetime.now().time()
        if cTime.minute == 3:
            send(topic='Час прошёл', message=f'письмо отправленно в {datetime.now()}')
        sleep(60)


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    k2()