from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet
from random import choice
from RasAsiVer2.Google.GoogleTasks import GoogleTasks

class TakeTasks:
    spreadsheet_id = '1DvY6qzp32qP_BNTFU2opXlfQ0lpnjs1MnGZ7LWRJIbw'

    def __init__(self):
        a = GoogleSpreadsheet()
        result = a.get_spreadsheets_values(spreadsheet_id=self.spreadsheet_id, range_name='Лист1')
        self.tasks = result.get('values')

    def TakeTask(self):
        n = 3
        daily = []
        while n:
            task = choice(self.tasks)
            if not int(task[1]) and task not in daily:
                n -= 1
                daily.append(task)
        print(daily)
        for i in daily:
            GoogleTasks(mainID='MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow').insert(task={'title': i[0]})
        # print(daily[0][0])


if __name__ == '__main__':
    a = TakeTasks()
    a.TakeTask()
