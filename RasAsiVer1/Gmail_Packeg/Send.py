import httplib2
import os
import oauth2client
from oauth2client import client, tools
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery
from sys import platform


def prost5():
    print('Hello World!')


def send(topic, message):
    SCOPES = 'https://www.googleapis.com/auth/gmail.send'
    if platform == 'win32':
        CLIENT_SECRET_FILE = 'C:\PythonProject\mygmail\client_secret.json'
    else:
        CLIENT_SECRET_FILE = '/home/pi/Downloads/client_secret.json'
    APPLICATION_NAME = 'Gmail API Python Send Email'

    def SendMessageInternal(service, user_id, message):
        try:
            print('mark #3')
            message = (service.users().messages().send(userId=user_id, body=message).execute())
            print('mark #4')
            print('Message Id: %s' % message['id'])
            print('mark #5')
            return message
        except errors.HttpError as error:
            print('An error occurred: %s' % error)

    def CreateMessage(sender, to, subject, msgHtml, msgPlain):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = to
        msg.attach(MIMEText(msgPlain, 'plain'))
        msg.attach(MIMEText(msgHtml, 'html'))
        raw = base64.urlsafe_b64encode(msg.as_bytes())
        raw = raw.decode()
        body = {'raw': raw}
        return body

    def get_credentials():                                                                                              #Удостоверение личности
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'gmail-python-email-send.json')
        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            credentials = tools.run_flow(flow, store)
            print('Storing credentials to ' + credential_path)
            input('...[press Enter]...')
        return credentials

    def SendMessage(sender, to, subject, msgHtml, msgPlain):
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)
        print('mark #1')
        message1 = CreateMessage(sender, to, subject, msgHtml, msgPlain)
        print('mark #2')
        SendMessageInternal(service, "me", message1)

    def main(topic, message):
        to = "zabavniy7@gmail.com"
        sender = "raspberry.assistant.py@gmail.com"
        subject = topic
        msgHtml = message
        msgPlain = message
        SendMessage(sender, to, subject, msgHtml, msgPlain)

    main(topic, message)

if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    prost5()