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
        print(self.tasks)

    def take_tasks(self, n=3):
        row_id = []
        task_id = []
        xn = 0
        for task in self.tasks:
            # print(i)
            if not int(task[2]):
                xn += 1
        if n > xn:
            print(f'Осталось невыполненных заданий - {xn}')
            n = xn

        if n < 3:
            print('mark 0')
            count = 0
            for task in self.tasks:
                if not int(task[2]) and task not in self.daily:
                    self.daily.append(task)
                    row_id.append((self.tasks.index(task)+1))
                    count += 1
            if count:
                for i in self.daily:
                    id = GoogleTasks(mainID=self._tasklist_id).insert(task={'title': i[1]})
                    task_id.append(id)
                for i in range(len(row_id)):
                    self.today_tasks[task_id[i]] = row_id[i]
        else:
            while n:
                print(1)
                task = choice(self.tasks)
                if not int(task[2]) and task not in self.daily:
                    n -= 1
                    self.daily.append(task)
                    row_id.append(self.tasks.index(task)+1)
            for i in self.daily:
                id = GoogleTasks(mainID=self._tasklist_id).insert(task={'title': i[1]})
                task_id.append(id)
            for i in range(len(row_id)):
                self.today_tasks[task_id[i]] = row_id[i]

    def check(self):
        for id in self.today_tasks:
            status = GoogleTasks(mainID=self._tasklist_id).get_task(task_id=id).get('status')
            if status == 'completed':
                GoogleSpreadsheet().update_spreadsheets_values(spreadsheet_id=self._spreadsheet_id,
                                                               range_name=f'Лист1!C{self.today_tasks.get(id)}',
                                                               values=[[1, datetime.datetime.today().strftime('%d.%m.%Y')]])

    def clean(self):
        for id in self.today_tasks:
            status = GoogleTasks(mainID=self._tasklist_id).get_task(task_id=id).get('status')
            if status == 'needsAction':
                GoogleTasks(mainID=self._tasklist_id).delete_task(task_id=id)
        self.daily.clear()

    def put(self, material):
        """

        :param material: string from msg
        :return: Nothing
        """
        material = material.split(' ')
        material.insert(1, datetime.datetime.today().strftime('%d.%m.%Y'))
        material.append(0)
        GoogleSpreadsheet().append_spreadsheets_values(values=[material[1:]],
                                                       spreadsheet_id=self._spreadsheet_id,
                                                       range_name='Лист1')

    def give_me_one(self):
        self.check()
        self.refresh_tasks()
        self.take_tasks(n=1)


if __name__ == '__main__':
    a = TodayTasks()  # Собрал все задания из хранилища
    a.take_tasks()  # если задние не выполнено добавляю 3 штуки
    input('pause\t')
    a.check()  # если выполнил задание, следует его отметить
    input('pause\t')
    a.give_me_one()  # хочу ещё 1 задание
    input('pause\t')
    a.clean()  # TODO запуск в полночь


