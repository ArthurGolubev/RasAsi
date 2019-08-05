import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os
from sys import platform

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

    if platform == 'win32':
        path_credential = r'C:\PycharmProjects\RasAsi\credentials'  # Laptop
        # path_credential = r'C:\PythonProject\RasAsi\credentials'  # PC
        _client_secret = path_credential + r'\client_secret.json'
    elif platform == 'linux':
        # path_credential = r'/home/pi/Downloads'  # raspbian
        path_credential = r'/home/rasasi/RasAsi/credentials'  # Ubuntu
        _client_secret = path_credential + r'/client_secret.json'
    else:
        print(f'Платформа {platform} не поддерживается')

    store = file.Storage(os.path.join(path_credential, 'RasAsi_mail.json'))
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(_client_secret, _SCOPE)
        creds = tools.run_flow(flow, store)

    GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))


    def SendMessage(self, user_id, message):
      """Send an email message.

      Args:
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.

      Returns:
        Sent Message.
      """
      message = (self.GMAIL.users().messages().send(userId=user_id, body=message).execute())

    def CreateMessage(self, sender, to, subject, message_text):
      """Create a message for an email.

      Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

      Returns:
        An object containing a base64url encoded email object.
      """
      message = MIMEText(message_text, 'html')
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject
      return {'raw': base64.urlsafe_b64encode(message.as_bytes().decode())}


    def CreateMessageWithAttachment(self, sender, to, subject, message_text, file_dir,
                                    filename):
      """Create a message for an email.

      Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.
        file_dir: The directory containing the file to be attached.
        filename: The name of the file to be attached.

      Returns:
        An object containing a base64url encoded email object.
      """
      message = MIMEMultipart()
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject

      msg = MIMEText(message_text, 'html')
      message.attach(msg)

      path = os.path.join(file_dir, filename)
      content_type, encoding = mimetypes.guess_type(path)

      if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
      main_type, sub_type = content_type.split('/', 1)
      if main_type == 'text':
        fp = open(path, 'rb')
        msg = MIMEText(fp.read(), _subtype=sub_type)
        fp.close()
      elif main_type == 'image':
        fp = open(path, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
      elif main_type == 'audio':
        fp = open(path, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
      else:
        fp = open(path, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()

      msg.add_header('Content-Disposition', 'attachment', filename=filename)
      message.attach(msg)

      return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


if __name__ == '__main__':
    msg = GoogleGmail().CreateMessageWithAttachment(
        sender='me',
        to='zabavniy7@gmail.com',
        subject='test',
        message_text='some text',
        file_dir=r'C:\Users\ArthurGo\Downloads',
        filename='test.jpg'
    )
    GoogleGmail().SendMessage(user_id='zabavniy7@gmail.com', message=msg)