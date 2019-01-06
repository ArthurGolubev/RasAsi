from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


def Read_msg():
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
    CLIENT_SECRET = 'C:\PythonProject\mygmail\client_secret.json'

    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
        creds = tools.run_flow(flow, store)

    GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

    threads = GMAIL.users().threads().list(userId='me', q='from:zabavniy7@gmail.com').execute().get('threads', [])
    print(threads)
    return threads
