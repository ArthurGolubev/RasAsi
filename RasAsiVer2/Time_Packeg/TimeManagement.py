import threading
from time import sleep
from datetime import datetime, timedelta
from RasAsiVer2.Google.GoogleGmail import GoogleGmail
from RasAsiVer2.Time_Packeg.TodayTasks import TodayTasks
from RasAsiVer2.Decorators.Decorators import time_decorator
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet


class TimeManagement:
    Task = TodayTasks()

    def __init__(self):
        self.messages = {}
        self.startTimeRasAsi = datetime.now()

    def time_line(self):
        while True:
            cTime = datetime.now()
            self.messages = self._view_messages()
            if self.messages:
                for message in self.messages:
                    if message['from_person'] == 'zabavniy7@gmail.com':

                        if message['topic'] == 'Время':
                            self._server_time()
                        elif message['topic'] == 'Хранилище':
                            self._Task_put(material=message['content'])
                        elif message['topic'] == 'Дай мне один':
                            self.Task.give_me_one()
                        elif message['topic'] == 'Лента':
                            self._lenta_discount(number=message['content'])
                        else:
                            self._unsupported_command(message['topic'])

            if cTime.hour == 0:
                if cTime.minute == 0:
                    self._server_time()
                    self._Task_check_clean()

            elif cTime.hour == 8:
                if cTime.minute == 20:
                    self.Task.take_tasks()

            sleep(60)

    def _view_messages(self):
        messages = GoogleGmail().logic_get_message()
        return messages

    @time_decorator
    def _server_time(self):
        cTime = datetime.now() - self.startTimeRasAsi
        cTime = cTime - timedelta(microseconds=cTime.microseconds)
        GoogleGmail().send_message(
            topic='Server time ☁', message_text=f'🎉👌 Время работы сервера:\t {cTime}')

    def _Task_put(self, material):
        self.Task.put(material=material.strip())

    def _Task_check_clean(self):
        self.Task.check()
        self.Task.clean()

    def _lenta_discount(self, number):
        date = datetime.now().strftime('%d.%m.%Y')
        GoogleSpreadsheet().append_spreadsheets_values(values=[[date, int(number)]],
                                                       spreadsheet_id='1SEOxlcQcaVQAhvzAalPUlgpiRWrG0-ji3M8RrZbMnTE',
                                                       range_name='Лист1')

    def _unsupported_command(self, command):
        GoogleGmail().send_message(topic='🤢 Неподдерживаемая команда 🤯',
                                 message_text=f'Команда "{command}" не поддерживается,'
                                 f'список поддерживаемых команд:\n'
                                 f'1. Время\n2. Хранилище\n3. Дай мне один\n4. Лента')


if __name__ == '__main__':
    t = threading.Thread(target=TimeManagement().time_line, name='T_TimeManagement')
    t.start()
else:
    print(f'Подключен модуль {__name__}')
