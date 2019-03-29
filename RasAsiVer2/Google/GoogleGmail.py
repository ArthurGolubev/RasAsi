import time
import base64
from sys import platform
from httplib2 import Http
from apiclient import discovery
from oauth2client import file, client, tools
from RasAsiVer2.Decorators.Decorators import errors_decorator


class GoogleGmail:
    _SCOPE = ['https://www.googleapis.com/auth/gmail.readonly',
              'https://www.googleapis.com/auth/gmail.send',
              'https://www.googleapis.com/auth/gmail.labels']

    store = file.Storage('RasAsi_storage.json')

    if platform == 'win32':
        _client_secret = r'C:\Users\ArthurGo\Downloads\client_secret.json'  # Laptop
        # client_secret = r'C:\PythonProject\mygmail\client_secret.json'  # PC
    elif platform == 'linux':
        _client_secret = r'/home/pi/Downloads/client_secret.json'
    else:
        print(f'Платформа {platform} не поддерживается')

    @errors_decorator
    def __init__(self):
        creds = self.store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(self._client_secret, self._SCOPE)
            creds = tools.run_flow(flow, self.store)

        self.GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

    @errors_decorator
    def unread_messages(self, userId='me', q='', labelIds='UNREAD'):
        _response = self.GMAIL.users().messages().list(userId=userId, q=q, labelIds=labelIds).execute()
        msg_id =[]
        if 'messages' in _response:
            for i in _response['messages']:
                msg_id.append(i['id'])
        else:
            print('Сообщений нет')
        return msg_id

    @errors_decorator
    def get_messages(self, msg_id):
        if msg_id:
            messages = []
            for i in msg_id:
                messages.append(self.GMAIL.users().messages().get(userId='me', id=i).execute())
                print(messages)
            return messages

    def read_message(self, message):
        topic = message['payload']['headers'][19]['value']
        date = time.ctime(int(message['internalDate'])/1000)
        p = 0
        for i in message['payload']['headers']:
            print(p, i['value'])
            p += 1
        from_person = message['payload']['headers'][6]['value'].replace('>', '').replace('<', '')
        content = message['payload'] #['parts'][0]['body']['data']
        # c1 = base64.urlsafe_b64decode(content).decode()
        print(message)

if __name__ == '__main__':
    a = GoogleGmail()
    msg_id = a.unread_messages()
    messages = a.get_messages(msg_id)
    for i in messages:
        a.read_message(i)
    print(messages[0]['payload']['headers'][19]['value'])

