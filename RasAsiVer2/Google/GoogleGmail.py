# TODO написать метод send
import base64
import datetime
from sys import platform
from httplib2 import Http
from apiclient import discovery
from oauth2client import file, client, tools
from RasAsiVer2.Decorators.Decorators import errors_decorator, time_decorator


class GoogleGmail:
    _SCOPE = ['https://www.googleapis.com/auth/gmail.readonly',
              'https://www.googleapis.com/auth/gmail.send',
              'https://www.googleapis.com/auth/gmail.modify']

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
    def list_unread_messages(self, userId='me', q='', labelIds='UNREAD'):
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

    @errors_decorator
    def decoded_messages(self, messages):
        """

        :param messages: list of messages
        :return: list of dictionaries consisting of decoded massages [{decoded_message1}, {decoded_message2}]
        """
        decoded_messages = []
        for message in messages:
            print(message)
            topic = message['payload']['headers'][19]['value']
            date = datetime.datetime.fromtimestamp(int(message['internalDate'])/1000)
            from_person = message['payload']['headers'][6]['value'].replace('>', '').replace('<', '')
            content = message['payload']['parts'][0]['body']['data']
            content = base64.urlsafe_b64decode(content).decode()
            print(topic)
            decoded_messages.append({
                'topic': topic,
                'from_person': from_person,
                'date': date,
                'content': content,
                'labelIds': message['labelIds'],
                'id': message['id']
            })
        return decoded_messages

    def send_message(self):
        pass

    @errors_decorator
    def change_labels(self, msg_id, userId='me', removeLabels=None, addLabelIds=None):

        if removeLabels and addLabelIds:
            body = {
                'removeLabelIds': removeLabels,
                'addLabelIds': addLabelIds
            }
        elif removeLabels:
            body = {
                'removeLabelIds': removeLabels
            }
        elif addLabelIds:
            body = {
                'addLabelIds': addLabelIds
            }
        else:
            print('Параметры для запроса не указаны')
            return None

        """

        :param msg_id:
        :param userId:
        :param removeLabels: ['UNREAD', 'my_LABEL']
        :param addLabelIds: ['UNREAD', 'my_LABEL']
        :return: None
        """
        self.GMAIL.users().messages().modify(id=msg_id, userId=userId, body=body).execute()

    @time_decorator
    def logic_get_message(self):
        msgs_id = self.list_unread_messages()
        messages = self.get_messages(msgs_id)
        decoded_messages = self.decoded_messages(messages)
        return decoded_messages


if __name__ == '__main__':
    a = GoogleGmail()
    msg = a.logic_get_message()[0]

    a.change_labels(msg_id=msg['id'], removeLabels=['UNREAD'])

