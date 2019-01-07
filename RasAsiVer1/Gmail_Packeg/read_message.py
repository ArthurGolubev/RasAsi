import base64
from get_message import get_message


def read_message():
    msglist = get_message()
    print('Получено', len(msglist))
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
    return msglist_text


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    read_message()
