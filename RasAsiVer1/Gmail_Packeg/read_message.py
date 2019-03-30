import base64
from RasAsiVer1.Gmail_Packeg.get_message import get_message


def read_message():
    msglist = get_message()
    if msglist:
        print('Обработка')
        msglist_text = []
        for i in range(len(msglist)):

            print(f'Письмо №{i+1}')
            print('Тема сообщения:\t', msglist[i]['payload']['headers'][19]['value'])
            '''текст сообщения'''
            '''Чтение данных предоставленных в кодеровке base64. Декодирование сообщения'''
            data1 = msglist[i]['payload']['parts'][0]['body']['data']
            k1 = base64.urlsafe_b64decode(data1)
            k2 = k1.decode()
            msglist_text.append(k2)
            # print(k2)
            # print(msglist_text)
        return msglist_text


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    read_message()
