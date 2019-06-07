import os.path
from sys import platform
from apiclient import discovery
from oauth2client import tools, file, client
from RasAsiVer2.Decorators.Decorators import errors_decorator, time_decorator


class GoogleTasks:
    _SCOPE = 'https://www.googleapis.com/auth/tasks'

    if platform == 'win32':
        path_credential = r'C:\PycharmProjects\RasAsi\credentials'  # Laptop
        # path_credential = r'C:\PythonProject\RasAsi\credentials'  # PC
        _client_secret = path_credential + r'\client_secret.json'
    elif platform == 'linux':
        # path_credential = r'/home/pi/Downloads'  # raspbian
        path_credential = r'/PycharmProjects/RasAsi/credential'  # Ubuntu
        _client_secret = path_credential + r'/client_secret.json'
    else:
        print(f'Платформа {platform} не поддерживается')

    store = file.Storage(os.path.join(path_credential, 'RasAsi_Tasks.json'))
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(_client_secret, _SCOPE)
        creds = tools.run_flow(flow, store)

    _TASKS = discovery.build('tasks', 'v1', credentials=creds)

    def __init__(self, mainID):
        self.mainID = mainID

    @errors_decorator
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

    @errors_decorator
    def list_tasks(self, completedMin=None):
        """

        :param completedMin: lower bound of time from which to look for completed tasks -> date[1:3]
        string, format - RFC 3339 -> '2019-10-15T12:00:00.000Z'
        :return: list of tasks
        """
        tasks = self._TASKS.tasks().list(tasklist=self.mainID, showHidden=True, completedMin=completedMin).execute()
        if tasks.get('items'):
            return tasks['items']

    @errors_decorator
    def get_task(self, task_id):
        task = self._TASKS.tasks().get(tasklist=self.mainID, task=task_id).execute()
        return task

    @errors_decorator
    def delete_task(self, task_id):
        self._TASKS.tasks().delete(tasklist=self.mainID, task=task_id).execute()

    @errors_decorator
    def insert(self, task):
        """

        :param task:
        task = {
            'title': 'New Task',
            'notes': 'Please complete me',
            'due': '2019-10-15T12:00:00.000Z'
        }

        :return:
        return Task id
        """
        result = self._TASKS.tasks().insert(tasklist=self.mainID, body=task).execute()
        return result.get('id')

    def update(self):  # TODO ???
        pass


if __name__ == '__main__':
    a = GoogleTasks()
    a.callAPI()
    # a.get_tasks()
    # a.get1()
    a.insert()
else:
    print(f'Подключен модуль {__name__}')
