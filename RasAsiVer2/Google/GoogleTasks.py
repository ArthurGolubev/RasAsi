# TODO рефакторинг: добавить свежий метод добавления пачки задач
import pickle
import os.path
import pickle
from sys import platform
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GoogleTasks:
    _SCOPE = 'https://www.googleapis.com/auth/tasks'
    if platform == 'win32':
        # path1 = r'C:\PythonProject\mygmail\client_secret.json'  # PC
        path1 = r'C:\PycharmProjects\client_secret.json'
    elif platform == 'linux':
        path1 = '/home/pi/Downloads/client_secret.json'
    else:
        print(f'Платформа {platform} не поддерживается')

    def __init__(self, mainID):
        self.mainID = mainID
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.path1, self._SCOPE)
                creds = flow.run_local_server()
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self._TASKS = build('tasks', 'v1', credentials=creds)

    def callAPI(self):
        result = self._TASKS.tasklists().list().execute()
        items = result.get('items', [])

        if not items:
            print('No task lists found.')
        else:
            print('Task lists:')
            for item in items:
                print(u'{0} {1}'.format(item['title'], item['id']))
                self.mainID = item['id']

    def get_tasks(self):
        tasks = self._TASKS.tasks().list(tasklist=self.mainID, showHidden=True).execute()
        for task in tasks['items']:
            print(task.get('title'), task)
        print(tasks)

    def get_task(self, task_id):
        task = self._TASKS.tasks().get(tasklist=self.mainID, task=task_id).execute()
        return task

    def delete_task(self, task_id):
        self._TASKS.tasks().delete(tasklist=self.mainID, task=task_id).execute()

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

    def update(self):
        pass


if __name__ == '__main__':
    a = GoogleTasks()
    a.callAPI()
    # a.get_tasks()
    # a.get1()
    a.insert()
else:
    print(f'Подключен модуль {__name__}')
