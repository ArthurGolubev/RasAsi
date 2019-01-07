from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
import base64


def get_message():
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify']
    CLIENT_SECRET = 'C:\PythonProject\mygmail\client_secret.json'

    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
        creds = tools.run_flow(flow, store)

    GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))
    messages = GMAIL.users().messages().list(userId='me', q='from:zabavniy7@gmail.com').execute()['messages']
    specificMsglist = []

    # results = GMAIL.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])
    #
    # if not labels:
    #     print('No labels found.')
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print(label['name'] + " " + label['id'])






    for i in messages:
        specificMsg = GMAIL.users().messages().get(userId='me', id=i['id']).execute()
        mdate = datetime.datetime.fromtimestamp(int(specificMsg['internalDate'])/1000)

        if mdate.date() == datetime.date.today() and 'UNREAD' in specificMsg['labelIds']:
            GMAIL.users().messages().modify(userId='me', id=i['id'], body={'removeLabelIds': ['UNREAD'],
                                                                           'addLabelIds': [
                                                                               'Label_5076690750399729789']}).execute()

            specificMsglist.append(specificMsg)
            # print(specificMsg)
            #
            # print('Тема сообщения:\t', specificMsg['payload']['headers'][19]['value'])
            # data1 = specificMsg['payload']['parts'][0]['body']['data']
            # k1 = base64.urlsafe_b64decode(data1)
            # k2 = k1.decode()
            # print(k2)

        elif mdate.date() == datetime.date.today() - datetime.timedelta(days=7):
            print(f'Устаревшее сообщение "...{messages["snippet"]}..."')
            GMAIL.users().massage().trash(userId='me', id=i['id']).execute()
            print('удалено')

    return specificMsglist


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    get_message()
