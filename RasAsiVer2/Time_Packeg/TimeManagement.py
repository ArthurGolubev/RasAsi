import threading
from time import sleep
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from RasAsiVer2.Google.GoogleGmail import GoogleGmail
from RasAsiVer2.Time_Packeg.TodayTasks import TodayTasks
from RasAsiVer2.Decorators.Decorators import time_decorator
from RasAsiVer2.Decorators.Decorators import logging_decorator
from RasAsiVer2.Weather_Packeg.TodayWeather import TodayWeather
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet


class TimeManagement:
    Task = TodayTasks()

    def __init__(self):
        self.messages = {}
        self.startTimeRasAsi = datetime.now()
        self.cache_variables = {
            'tasks_taken': None,    # switch
            '23:50': None,          # switch
            '15:50': None,          # switch
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
                                self.Task.give_me_specific_one(message['content'])
                            else:
                                self.Task.give_me_one()

                        elif message['topic'] == 'Лента':
                            self._lenta_discount(number=message['content'])
                        else:
                            self._unsupported_command(message['topic'])

            if cTime.hour == 0 and cTime.minute in [0, 1, 2, 3]:
                self.cache_variables['23:50'] = 0   # nullification (new day)

            elif cTime.hour == 8:
                if cTime.minute in [5, 6, 7] and not self.cache_variables['tasks_taken']:
                    self.Task.take_tasks()
                    self.cache_variables['tasks_taken'] = 1
            elif cTime.hour == 19:
                if cTime.minute in [28, 29, 30] and not self.cache_variables['15:50']:
                    self.cache_variables['15:50'] = 1
                    TodayWeather().today_weather()
            elif cTime.hour == 23:
                if cTime.minute in [50, 51, 52] and not self.cache_variables['23:50']:
                    self._server_time()
                    self._Task_check_clean_refresh()
                    self.cache_variables['tasks_taken'] = 0
                    self.cache_variables['23:50'] = 1

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

    def _transport_card(self):
        number = GoogleSpreadsheet().get_spreadsheets_values(
            spreadsheet_id='1vqDWkRh8ERwxkRtyum-0bffbmjp7KMJn-SpAgNnYtyM',
            range_name='Лист1').get('values')[0][0]
        browser = webdriver.Firefox(
            executable_path=r'C:\PycharmProjects\RasAsi\RasAsiVer2\Weather_Packeg\geckodriver.exe')
        browser.implicitly_wait(20)

        browser.get('https://www.krasinform.ru/')
        browser.find_element_by_xpath("//input[@type='text'][@name='card_num']").send_keys(f'{number}')
        sleep(5)
        browser.find_element_by_xpath("//input[@type='text'][@name='card_num']").send_keys(Keys.ENTER)
        transport_unit = browser.find_elements_by_xpath("//table[@class='table']//td")
        transport_unit = int(transport_unit[1].text.split(' ')[0])
        if transport_unit < 225:
            GoogleGmail().send_message(topic='Проездной 🧐🚌💰',
                                       message_text=f'Оставшийся баланс на транспортной карте: {transport_unit} руб.')


if __name__ == '__main__':
    t = threading.Thread(target=TimeManagement().time_line, name='T_TimeManagement')
    t.start()
else:
    print(f'Подключен модуль {__name__}')
