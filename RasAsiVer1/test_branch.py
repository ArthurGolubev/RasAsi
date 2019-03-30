import base64
from email.mime.text import MIMEText
message_text = 'text'
message = MIMEText(message_text)
message['to'] = 'zabavniy7@gmail.com'
message['from'] = 'me'
message['subject'] = 'Тема письма____1'

dict_1 = {'raw': base64.urlsafe_b64encode(message.as_bytes())}
print(dict_1)
