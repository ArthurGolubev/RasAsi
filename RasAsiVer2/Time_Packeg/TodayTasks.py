from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet
from random import choice
from RasAsiVer2.Google.GoogleTasks import GoogleTasks


class TodayTasks:
    today_tasks = {}
    _spreadsheet_id = '1DvY6qzp32qP_BNTFU2opXlfQ0lpnjs1MnGZ7LWRJIbw'
    _tasklist_id = 'MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow'

    def __init__(self):  # TODO Ежедневный перезапуск данного класа обнавляет список задач из хранилища
        '''в тоже время, экземпляр класса сутки будет хранить то, какие задачи были взяты их хранилища'''
        """в конце дня можно уточнить, сделал ли я эти задачи. По индексам можно отметить задачи в хранилище"""
        self.tasks = GoogleSpreadsheet().get_spreadsheets_values(
            spreadsheet_id=self._spreadsheet_id,
            range_name='Лист1').get('values')

    def take_tasks(self):
        row_id = []
        task_id = []
        n = 3
        daily = []
        while n:
            task = choice(self.tasks)
            if not int(task[1]) and task not in daily:
                n -= 1
                daily.append(task)
                row_id.append(self.tasks.index(task)+1)
        print(daily)
        for i in daily:
            id = GoogleTasks(mainID=self._tasklist_id).insert(task={'title': i[0]})
            task_id.append(id)
        for i in range(len(row_id)):
            self.today_tasks[task_id[i]] = row_id[i]

    def check(self):
        input('pause\t')
        for id in self.today_tasks:
            status = GoogleTasks(mainID=self._tasklist_id).get_task(task_id=id).get('status')
            if status == 'completed':
                GoogleSpreadsheet().update_spreadsheets_values(spreadsheet_id=self._spreadsheet_id,
                                                               body=GoogleSpreadsheet().body_formation([[1]]),
                                                               range_name=f'Лист1!B{self.today_tasks.get(id)}')

    def clean(self):
        for id in self.today_tasks:
            status = GoogleTasks(mainID=self._tasklist_id).get_task(task_id=id).get('status')
            if status == 'needsAction':
                GoogleTasks(mainID=self._tasklist_id).delete_task(task_id=id)



if __name__ == '__main__':
    a = TodayTasks()  # TODO сделать метод "give_me_one"
    a.take_tasks()
    a.check()
    a.clean()  # TODO запуск в полночь

