import os.path
from sys import platform
from apiclient import discovery
from oauth2client import tools, file, client
import datetime

class GoogleTasks:
    _SCOPE = 'https://www.googleapis.com/auth/tasks'

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

    store = file.Storage(os.path.join(path_credential, 'RasAsi_Tasks.json'))
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(_client_secret, _SCOPE)
        creds = tools.run_flow(flow, store)

    _TASKS = discovery.build('tasks', 'v1', credentials=creds)

    def __init__(self, mainID='MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow'):
        self.mainID = mainID

    def list_tasks(self, completedMin=None):
        completedMin = (datetime.datetime.utcnow()-datetime.timedelta(hours=32)).isoformat('T') + 'Z'

        """

        :param completedMin: lower bound of time from which to look for completed tasks -> date[1:3]
        string, format - RFC 3339 -> '2019-10-15T12:00:00.000Z'
        :return: list of tasks
        """
        tasks = self._TASKS.tasks().list(tasklist=self.mainID, showHidden=True, completedMin=completedMin, maxResults='100').execute()
        if tasks.get('items'):
            for i in tasks.get('items'):
                print(i)
            print(len(tasks.get('items')))
        # for task in tasks['items']:
        #     print(task)
        print(datetime.datetime.utcnow().isoformat('T'))
        print(datetime.datetime.utcnow())
        print(completedMin)

    def callAPI(self):  # TODO ???
        result = self._TASKS.tasklists().list().execute()
        items = result.get('items', [])

        if not items:
            print('No task lists found.')
        else:
            print('Task lists:')
            for item in items:
                print(u'{0} {1}'.format(item['title'], item['id']))
                self.mainID = item['id']

if __name__ == '__main__':
    p = GoogleTasks()
    p.list_tasks()