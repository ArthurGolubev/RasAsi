import os, time
from sys import platform
from httplib2 import Http
from apiclient import discovery
from oauth2client import tools, file, client

def google_init():
    Tasks_SCOPE = 'https://www.googleapis.com/auth/tasks'
    Spreadsheet_SCOPE = 'https://www.googleapis.com/auth/spreadsheets'
    Gmail_SCOPE = ['https://www.googleapis.com/auth/gmail.readonly',
                   'https://www.googleapis.com/auth/gmail.send',
                   'https://www.googleapis.com/auth/gmail.modify']

    if platform == 'win32':
        path_credential = r'C:\PycharmProjects\RasAsi\credentials'  # Laptop
        # path_credential = r'C:\PythonProject\RasAsi\credentials'  # PC
        _client_secret = path_credential + r'\client_secret.json'
    elif platform == 'linux':
        # path_credential = r'/home/pi/Downloads'  # raspbian
        path_credential = r'PycharmProjects/RasAsi/credentials'  # Ubuntu
        _client_secret = path_credential + r'/client_secret.json'
    else:
        print(f'Платформа {platform} не поддерживается')

    store = file.Storage(os.path.join(path_credential, 'RasAsi_Tasks.json'))
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(_client_secret, Tasks_SCOPE)
        creds = tools.run_flow(flow, store)
        discovery.build('gmail', 'v1', http=creds.authorize(Http()))
    discovery.build('tasks', 'v1', credentials=creds)
    time.sleep(2)

    store = file.Storage(os.path.join(path_credential, 'RasAsi_mail.json'))
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(_client_secret, Gmail_SCOPE)
        creds = tools.run_flow(flow, store)
    discovery.build('gmail', 'v1', http=creds.authorize(Http()))
    time.sleep(2)

    store = file.Storage(os.path.join(path_credential, 'RasAsi_Spreadsheets.json'))
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(_client_secret, Spreadsheet_SCOPE)
        creds = tools.run_flow(flow, store)
        discovery.build('gmail', 'v1', http=creds.authorize(Http()))
    discovery.build('sheets', 'v4', http=creds.authorize(Http()))

if __name__ == '__main__':
    google_init()