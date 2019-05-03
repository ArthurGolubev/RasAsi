import os
import base64
import datetime
import mimetypes
from sys import platform
from httplib2 import Http
from apiclient import discovery
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from oauth2client import file, client, tools
from email.mime.multipart import MIMEMultipart
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
        # _client_secret = r'/home/pi/Downloads/client_secret.json'  # raspbian
        _client_secret = r'/home/rasasi/RasAsi/credentials/client_secret.json'  # ubuntu mate
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
        # else:
        #     print('Сообщений нет')
        return msg_id

    @errors_decorator
    def get_messages(self, msg_id):
        if msg_id:
            messages = []
            for i in msg_id:
                messages.append(self.GMAIL.users().messages().get(userId='me', id=i).execute())
            return messages

    @errors_decorator
    def decoded_messages(self, messages):
        """

        :param messages: list of messages
        :return: list of dictionaries consisting of decoded massages [{decoded_message1}, {decoded_message2}]
        """
        decoded_messages = []
        for message in messages:
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

    @errors_decorator
    def send_message(self, message_text, userId='me', from_='Асистент Малинка', to='zabavniy7@gmail.com', topic=''):

        message = MIMEText(message_text)
        message['To'] = to
        message['From'] = from_
        message['Subject'] = topic
        message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        message = self.GMAIL.users().messages().send(userId=userId, body=message).execute()
        return message

    @errors_decorator  # TODO доделать метод
    def send_message_with_attachment(self,
                                     message_text,
                                     file_dir,
                                     file_name,
                                     userId='me',
                                     from_='Асистент малинка',
                                     to='zabavniy7@gmail.com',
                                     topic=''):
        message = MIMEMultipart

        msg = MIMEText(message_text)
        msg['to'] = to
        msg['From'] = from_
        msg['Subject'] = topic

        path = os.path.join(file_dir, file_name)
        content_type, encoding = mimetypes.guess_type(path)

        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        if main_type == 'text':
            with open(path, 'rb') as f:
                payload = MIMEText(f.read(), _subtype=sub_type)
        elif main_type == 'image':
            with open(path, 'rb') as f:
                payload = MIMEImage(f.read(), _subtype=sub_type)
        else:
            with open(path, 'rb') as f:
                payload = MIMEBase(main_type, sub_type)
                payload.set_payload(f.read())
        payload.add_header('Контенто-содержащий', 'attachment', filename=file_name)
        message.attach(msg, payload)
        message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        message = self.GMAIL.users().messages().send(userId=userId, body=message)
        return message

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

    # @time_decorator
    @errors_decorator
    def logic_get_message(self):
        msgs_id = self.list_unread_messages()
        messages = self.get_messages(msgs_id)
        if messages:
            decoded_messages = self.decoded_messages(messages)
            for message in decoded_messages:
                self.change_labels(msg_id=message['id'], removeLabels=('UNREAD', ))
            return decoded_messages


if __name__ == '__main__':
    a = GoogleGmail()
    a.send_message_with_attachment(message_text='Держи 😊',
                                   file_dir='C:\PycharmProjects\RasAsi\RasAsiVer2\Weather_Packeg',
                                   file_name='ChartWeather.html',
                                   topic='Прикреплён график погоды 👍☁')


