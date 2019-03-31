from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
from sys import platform


def get_message():
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify']
    if platform == 'win32':
        CLIENT_SECRET_FILE = 'C:\PythonProject\mygmail\client_secret.json'
    elif platform == 'linux':
        CLIENT_SECRET_FILE = '/home/pi/Downloads/client_secret.json'
    else:
        print(f'Платформа {platform} не поддерживается')

    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        creds = tools.run_flow(flow, store)

    GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

    try:
        messages = GMAIL.users().messages().list(userId='me', q='from:zabavniy7@gmail.com').execute()['messages']
        specificMsglist = []
        for i in messages:
            specificMsg = GMAIL.users().messages().get(userId='me', id=i['id']).execute()
            mdate = datetime.datetime.fromtimestamp(int(specificMsg['internalDate']) / 1000)

            if mdate.date() == datetime.date.today() and 'UNREAD' in specificMsg['labelIds']:
                GMAIL.users().messages().modify(userId='me', id=i['id'], body={'removeLabelIds': ['UNREAD'],
                                                                               'addLabelIds': [
                                                                                   'Label_5076690750399729789']}).execute()
                specificMsglist.append(specificMsg)
            elif mdate.date() <= datetime.date.today() - datetime.timedelta(days=7):
                print(f'Устаревшее сообщение "...{specificMsg["snippet"]}..."')
                GMAIL.users().messages().trash(userId='me', id=i['id']).execute()
                print('удалено')
                specificMsglist.append(specificMsg)

        return specificMsglist

    except KeyError:
        print('По данному запросу сообщений нет')
        return None

    '''получить список ID label'''
    # results = GMAIL.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])
    #
    # if not labels:
    #     print('No labels found.')
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print(label['name'] + " " + label['id'])


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    get_message()
