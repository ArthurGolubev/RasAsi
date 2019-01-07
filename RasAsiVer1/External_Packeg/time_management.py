from datetime import datetime
from time import sleep
# from RasAsi_main import startTimeRasAsi
from ..Gmail_Packeg import send, get_message
from datetime import datetime


def k2(t_stop):
    while not t_stop.is_set():
        cTime = datetime.now().time()
        # if cTime.minute == 3:
        #     send(topic='Час прошёл', message=f'письмо отправленно в {datetime.now()}')
        if cTime.hour == 21:
            list1 = get_message.Read_msg()
            for i in list1:
                if i.get('snippet') == 'время':
                    print('OK GO')
                    # send(topic='ВРЕМЯ ПРИШЛО', message=f'{datetime.now()-startTimeRasAsi}')
        print(cTime.hour)
        sleep(60)


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    k2()