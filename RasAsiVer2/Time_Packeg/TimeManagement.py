 # TODO Сделать ежедневный прогноз (присылать)
 # TODO сделать формирование ОБЩЕГО отчёта в одном письме
 # TODO сделать метод и соответствующую таблицу для сбора погоды на следующий день
  # потом можно будет сделать график, который сравнивает отличия прогноза на сегодня и прогноза на день вперёд
  # (текущего дня и сделанного вчера прогноза на сегодня)
from time import sleep
from getpass import getpass
from psycopg2 import OperationalError
from datetime import datetime, timedelta
from RasAsiVer2.Google.GoogleGmail import GoogleGmail
from RasAsiVer2.Time_Packeg.TodayTasks import TodayTasks
from RasAsiVer2.Decorators.Decorators import time_decorator
from RasAsiVer2.Database.RasAsiDatabase import RasAsiDatabase
from RasAsiVer2.Time_Packeg.TodayTasks_v2 import TodayTasksV2
from RasAsiVer2.Time_Packeg.TransportCard import TransportCard
from RasAsiVer2.Decorators.Decorators import logging_decorator
from RasAsiVer2.Weather_Packeg.WeatherToday import WeatherToday
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet
from RasAsiVer2.addiction_support.psutil_temperature import TemperatureSensor


class TimeManagement:
    temp = TemperatureSensor()
    RAD = RasAsiDatabase()

    upass = getpass()
    _test_connection_ok = 0
    while not _test_connection_ok:
        try:
            _test_connection_ok = RAD.test_connection(upass=upass)
            print('password is correct 😁👍')
        except OperationalError:
            print('incorrect password 🤯, try again 😓')
            upass = getpass()

    Task = TodayTasks()
    Task_v2 = TodayTasksV2(upass=upass)  # TODO Перевести в RAD?

    def __init__(self):
        self.messages = {}
        self.startTimeRasAsi = datetime.now()
        self.cache_variables = {
            'tasks_taken': None,    # switch
            'today_id': None,       # switch
            'weather': None,        # switch
            '00:00': None,          # switch
            '01:00': None,          # switch
            '03:00': None,          # switch
            '23:50': None,          # switch

        }

    @logging_decorator
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
                                self.Task_v2.refresh_v2()
                                self.Task_v2.get_specific_one_v2(int(message['content']))
                            else:
                                self.Task_v2.refresh_v2()
                                self.Task_v2.get_3_tasks(n=1)
                        elif message['topic'] == 'Лента':
                            self._lenta_discount(number=message['content'])
                        elif message['topic'] == 'Проездной':
                            TransportCard(who='me').transport_card()
                        elif message['topic'] == 'Погода':
                            WeatherToday(upass=self.upass).weather_today()
                        elif message['topic'] == 'Прогноз':
                            RasAsiDatabase().daily_forecast(upass=self.upass)
                        else:
                            self._unsupported_command(message['topic'], message['content'])

            if cTime.hour == 0 and cTime.minute in [0, 1, 2]:
                self.cache_variables['00:00'] = 0       # nullification (new day)
                self.cache_variables['01:00'] = 0       # nullification (new day)
                self.cache_variables['03:00'] = 0       # nullification (new day)
                self.cache_variables['23:50'] = 0       # nullification (new day)
                self.cache_variables['weather'] = 0     # nullification (new day)
                self.cache_variables['today_id'] = 0    # nullification (new day)

            elif cTime.hour == 0:
                if cTime.minute in [8, 9, 37] and not self.cache_variables['00:00']:
                    self.cache_variables['00:00'] = 1
                    # self.RAD.dump_rasasi_database(upass=self.upass)  # TODO Разкоментировать
                    self.RAD.task_completed_today(upass=self.upass)
            elif cTime.hour == 1:
                if cTime.minute in [0, 1, 2] and not self.cache_variables['01:00']:
                    self.cache_variables['01:00'] = 1
                    TransportCard(who='me').transport_card()
            elif cTime.hour == 3:
                if cTime.minute in [0, 1, 2] and not self.cache_variables['03:00']:
                    self.cache_variables['03:00'] = 1
                    WeatherToday(upass=self.upass).weather_today()
                    self.cache_variables['weather'] = 1
            elif cTime.hour == 8:
                if cTime.minute in [0, 1, 2] and not self.cache_variables['tasks_taken']:
                    self.cache_variables['tasks_taken'] = 1
                    # self.Task.take_tasks()
                    self.Task_v2.get_3_tasks()

                    today = datetime.today()
                    day = today.strftime('%j')
                    if int(today.year)%4 == 0:
                        nday = 366 - int(day)
                    else:
                        nday = 365 - int(day)
                    GoogleGmail().send_message(topic=f'День {day} ☀🔆 осталось {nday}', message_text='😗☺')
                    RasAsiDatabase().daily_forecast(upass=self.upass)
                elif cTime.minute in [5, 6, 7] and not self.cache_variables['weather']:
                    GoogleGmail().send_message(topic='☁🌫 Погода не получена', message_text='Не удолось получить погоду')
                    self.cache_variables['weather'] = 1
            elif cTime.hour == 23:
                if cTime.minute in [50, 51, 52] and not self.cache_variables['23:50']:
                    self.cache_variables['23:50'] = 1
                    self._server_time()
                    self._Task_check_clean_refresh()
                    # self.Task_v2.clear_v2()
                    self.cache_variables['tasks_taken'] = 0

            self.temp.temperature_sensor()
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
        self.Task.put(material=material.strip())  # TODO Дублирующий метод пока v2 не отработан
        self.Task_v2.put_v2(content=material.strip())

    def _Task_check_clean_refresh(self):
        # self.Task.check()
        # self.Task.day_completed()
        # self.Task.clean()
        # self.Task.refresh_tasks()
        self.Task_v2.refresh_v2()
        self.Task_v2.clear_v2()

    def _lenta_discount(self, number):
        date = datetime.now().strftime('%d.%m.%Y')
        GoogleSpreadsheet().append_spreadsheets_values(values=[[date, int(number)]],
                                                       spreadsheet_id='1SEOxlcQcaVQAhvzAalPUlgpiRWrG0-ji3M8RrZbMnTE',
                                                       range_name='Лист1')
        RasAsiDatabase().lenta_discount(upass=self.upass, discount=int(number))

    def _unsupported_command(self, command, content=None):
        GoogleGmail().send_message(topic='🤢 Неподдерживаемая команда 🤯',
                                 message_text=f'Команда "{command}" не поддерживается,'
                                 f'список поддерживаемых команд:\n'
                                 f'1. Время\n2. Хранилище\n3. Дай мне один\n4. Лента\n'
                                 f'5. Проездной\n'
                                 f'Сообщение: {content}')


if __name__ == '__main__':
    TimeManagement().time_line()
else:
    print(f'Подключен модуль {__name__}')
