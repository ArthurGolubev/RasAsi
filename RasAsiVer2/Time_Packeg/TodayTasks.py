from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet
from random import choice
from RasAsiVer2.Google.GoogleTasks import GoogleTasks
import datetime

class TodayTasks:
    today_tasks = {}
    _spreadsheet_id = '1DvY6qzp32qP_BNTFU2opXlfQ0lpnjs1MnGZ7LWRJIbw'
    _tasklist_id = 'MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow'
    tasks = None
    daily = []

    def __init__(self):
        self.refresh_tasks()

    def refresh_tasks(self):
        self.tasks = GoogleSpreadsheet().get_spreadsheets_values(
            spreadsheet_id=self._spreadsheet_id,
            range_name='Лист1').get('values')
        # print('\nХранилище\n', self.tasks)

    def take_tasks(self, n=3):
        row_id = []
        task_id = []
        xn = 0
        for task in self.tasks:
            print(task)
            if not int(task[2]):
                xn += 1
        if n > xn:
            print(f'Осталось невыполненных заданий - {xn}')
            n = xn

        count_n = n
        while count_n:
            task = choice(self.tasks)
            if not int(task[2]) and task not in self.daily:
                count_n -= 1
                self.daily.append(task)
                row_id.append(self.tasks.index(task)+1)

        for i in range(n):
            id = GoogleTasks(mainID=self._tasklist_id).insert(task={'title': self.daily[-1-i][1]})
            task_id.append(id)
        task_id.reverse()
        for i in range(len(row_id)):
            self.today_tasks[task_id[i]] = row_id[i]

    def check(self):
        for id in self.today_tasks:
            task = GoogleTasks(mainID=self._tasklist_id).get_task(task_id=id)
            status = task.get('status')
            notes = task.get('notes')
            due = task.get('due')
            if status == 'completed':
                values = [[1, datetime.datetime.today().strftime('%d.%m.%Y'), notes]]
                GoogleSpreadsheet().update_spreadsheets_values(spreadsheet_id=self._spreadsheet_id,
                                                               range_name=f'Лист1!C{self.today_tasks.get(id)}',
                                                               values=values)
            elif status == 'needsAction' and due:
                notes = '❌deadline🤯⭕'
                date = due.split('T')
                date = date[0].split('-')
                date = f'{date[2]}.{date[1]}.{date[0]}'
                values = [[1, date, notes]]
                GoogleSpreadsheet().update_spreadsheets_values(spreadsheet_id=self._spreadsheet_id,
                                                               range_name=f'Лист1!C{self.today_tasks.get(id)}',
                                                               values=values)

    def day_completed(self):
        """

        :return:
        """
        today = (datetime.datetime.utcnow()-datetime.timedelta(hours=20)).isoformat('T') + 'Z'
        completed_tasks = GoogleTasks(mainID=self._tasklist_id).list_tasks(completedMin=today)

        GoogleSpreadsheet().append_spreadsheets_values(
            values=[[datetime.datetime.today().strftime('%d.%m.%Y'), len(completed_tasks)]],
            spreadsheet_id='158Z7-2JEL9-j5jD7TCp_u-XahllRudDp7NIOoSiya_k',
            range_name='Лист1')

    def clean(self):
        for id in self.today_tasks:
            task = GoogleTasks(mainID=self._tasklist_id).get_task(task_id=id)
            status = task.get('status')
            due = task.get('due')  # due - ожидаемый (set Deadline in GoogleTasks)
            if status == 'needsAction' and not due:
                GoogleTasks(mainID=self._tasklist_id).delete_task(task_id=id)
        self.daily.clear()
        self.today_tasks.clear()

    def put(self, material):
        """

        :param material: string from msg
        :return: Nothing
        """
        values = []
        values.append(datetime.datetime.today().strftime('%d.%m.%Y'))
        values.append(material)
        values.append(0)
        GoogleSpreadsheet().append_spreadsheets_values(values=[values],
                                                       spreadsheet_id=self._spreadsheet_id,
                                                       range_name='Лист1')

    def give_me_one(self):
        self.check()
        self.refresh_tasks()
        self.take_tasks(n=1)

    def give_me_specific_one(self, number):
        self.check()
        self.refresh_tasks()
        if (number.strip()).isdigit():
            task = self.tasks[int(number)-1]
            self.daily.append(task)
            id = GoogleTasks(mainID=self._tasklist_id).insert(task={'title': task[1]})
            self.today_tasks[id] = int(number)


if __name__ == '__main__':
    a = TodayTasks()
    a.day_completed()


