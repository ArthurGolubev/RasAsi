import threading
from time import sleep
from datetime import datetime, timedelta
from RasAsiVer2.Google.GoogleGmail import GoogleGmail
from RasAsiVer2.Time_Packeg.TodayTasks import TodayTasks
from RasAsiVer2.Decorators.Decorators import time_decorator
from RasAsiVer2.Time_Packeg.TransportCard import TransportCard
from RasAsiVer2.Decorators.Decorators import logging_decorator
from RasAsiVer2.Weather_Packeg.WeatherTomorrow import WeatherTomorrow
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet


class TimeManagement:
    Task = TodayTasks()
    my_TK = threading.Thread(target=TransportCard(who='me').transport_card, name='threading_TransportCard')
    weather = threading.Thread(target=WeatherTomorrow().weather_tomorrow, name='threading_weather')

    def __init__(self):
        self.messages = {}
        self.startTimeRasAsi = datetime.now()
        self.cache_variables = {
            'tasks_taken': None,    # switch
            '01:00': None,          # switch
            '03:00': None,          # switch
            '23:50': None,          # switch
        }

    # @logging_decorator
    def time_line(self):
        while True:
            cTime = datetime.now()
            self.messages = self._view_messages()
            if self.messages:
                for message in self.messages:
                    if message['from_person'] == 'zabavniy7@gmail.com': # TODO проверка должна проводится в 26 строке. Если отправил RasAsi для RasAsi - out of range

                        if message['topic'] == 'Время':
                            self._server_time()
                        elif message['topic'] == 'Хранилище':
                            self._Task_put(material=message['content'])
                        elif message['topic'] == 'Дай мне один':
                            if len(message['content'].strip()):
                                print(message['content'])
                                self.Task.give_me_specific_one(message['content'])
                            else:
                                self.Task.give_me_one()

                        elif message['topic'] == 'Лента':
                            self._lenta_discount(number=message['content'])
                        else:
                            self._unsupported_command(message['topic'])

            if cTime.hour == 0 and cTime.minute in [0, 1, 2]:
                self.cache_variables['01:00'] = 0   # nullification (new day)
                self.cache_variables['03:00'] = 0   # nullification (new day)
                self.cache_variables['23:50'] = 0   # nullification (new day)

            elif cTime.hour == 1:
                if cTime.minute in [0, 1, 2] and not self.cache_variables['01:00']:
                    self.cache_variables['01:00'] = 1
                    self.my_TK.start()
            elif cTime.hour == 3:
                if cTime.minute in [0, 1, 2] and not self.cache_variables['03:00']:
                    self.cache_variables['03:00'] = 1
                    self.weather.start()
            elif cTime.hour == 8:
                if cTime.minute in [0, 1, 2] and not self.cache_variables['tasks_taken']:
                    self.cache_variables['tasks_taken'] = 1
                    self.Task.take_tasks()
            elif cTime.hour == 23:
                if cTime.minute in [50, 51, 52] and not self.cache_variables['23:50']:
                    self.cache_variables['23:50'] = 1
                    self._server_time()
                    self._Task_check_clean_refresh()
                    self.cache_variables['tasks_taken'] = 0

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

    def _Task_check_clean_refresh(self):
        self.Task.check()
        self.Task.day_completed()
        self.Task.clean()
        self.Task.refresh_tasks()

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
