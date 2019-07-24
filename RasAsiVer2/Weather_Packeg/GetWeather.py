from time import sleep
# from RasAsiVer2.Database_Scripts.id_city import id_city
from RasAsiVer2.Database_Scripts.RasAsiDatabase import RasAsiDatabase
from RasAsiVer2.addiction_support import psutil_temperature


class GetWeather:
    _twentyFourHours = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
                        '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                        '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                        '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']

    def __init__(self, browser, get_date, temp):
        self.temp = temp
        self._name_dict = ''
        self._next12hours = []
        self._cha_dict = {}
        self.weather_log = {}
        self.browser = browser
        self.get_date = get_date
        sleep(10)
        for i in self._twentyFourHours:
            self._next12hours.append(get_date + ' ' + i)

    def get_values(self, attribute):
        characteristic_dict = {}
        self.browser.find_element_by_link_text(attribute).click()
        print(f'Сбор набора данных\t-|{attribute}|-')
        sleep(7)

        if attribute == 'Влажность':
            for i in self._next12hours[1::3]:
                print('mark #1', i)
                self.temp.temperature_sensor()

                self.browser.find_element_by_xpath(f"//span[@class='e']//a[@title='{i}']").click()
                sleep(7)
                c = self._get_characteristic()
                characteristic_dict.update({i: c})

        elif attribute == 'Осадки':
            self.browser.find_element_by_xpath("//div[@class='qj ua hv']//select//option[@value='rain-1h']").click()
            for i in self._next12hours:
                print('mark #1', i)
                self.temp.temperature_sensor()

                self.browser.find_element_by_xpath(f"//span[@class='e']//a[@title='{i}']").click()
                sleep(7)
                c = self._get_characteristic()
                characteristic_dict.update({i: c})

        elif attribute == 'Атмосферное давление':
            for i in self._next12hours:
                print('mark #1', i)
                self.temp.temperature_sensor()

                self.browser.find_element_by_xpath(f"//span[@class='e']//a[@title='{i}']").click()
                sleep(7)
                c = self._get_characteristic()
                self.browser.find_element_by_xpath("//div[@id='l'][@class='yy']").click()
                self.browser.find_element_by_xpath("//div[@id='l'][@class='yy']").click()
                sleep(5)
                c += ' / ' + self._get_characteristic()
                self.browser.find_element_by_xpath("//div[@id='l'][@class='yy']").click()
                characteristic_dict.update({i: c})

        elif attribute == 'Скорость ветра':
            self.browser.find_element_by_xpath("//div[@id='l'][@class='yy']").click()
            for i in self._next12hours:
                print('mark #1', i)
                self.temp.temperature_sensor()
                self.browser.find_element_by_xpath(f"//span[@class='e']//a[@title='{i}']").click()
                sleep(7)
                c = self._get_characteristic()
                characteristic_dict.update({i: c})
        else:
            for i in self._next12hours:
                print('mark #1', i)
                self.temp.temperature_sensor()
                self.browser.find_element_by_xpath(f"//span[@class='e']//a[@title='{i}']").click()
                sleep(7)
                c = self._get_characteristic()
                characteristic_dict.update({i: c})

        self._cha_dict = characteristic_dict
        self._name_dict = attribute
        self._compose_weather()

    def _get_characteristic(self):
        return self.browser.find_element_by_xpath("//div[@id='x']//a[@class='qo am zh']").get_attribute("data-value")

    def _compose_weather(self):
        self.weather_log[self._name_dict] = self._cha_dict

    def _hours(self, keys, hour):

        """
            формируется одна запись (строка) в таблицу по всем атрибутам
        :param keys: Атрибуты (Температура, Скорость ветра...)
        :param hour: К какому часу принадлежит строка записи
        :return: список записей (строк)
        """
        _t = []
        _t.append(f'{self.get_date} {hour}:00')
        for i in keys:
            _t.append(self.weather_log.get(i).get(f'{self.get_date} {hour}:00'))
        return _t

    def GoogleSpreadsheet_dict_formation(self, title=True): # TODO Отрефакторить?
        """

        :param title: Оглавление столбцов таблицы (Время, Температура, Влажность..)
        :return: Возвращает список записей (строк) в таблицу
        """
        keys = []

        for i in self.weather_log.keys():
            keys.append(i)

        _t00 = self._hours(keys, '00')
        _t01 = self._hours(keys, '01')
        _t02 = self._hours(keys, '02')
        _t03 = self._hours(keys, '03')
        _t04 = self._hours(keys, '04')
        _t05 = self._hours(keys, '05')
        _t06 = self._hours(keys, '06')
        _t07 = self._hours(keys, '07')
        _t08 = self._hours(keys, '08')
        _t09 = self._hours(keys, '09')
        _t10 = self._hours(keys, '10')
        _t11 = self._hours(keys, '11')
        _t12 = self._hours(keys, '12')
        _t13 = self._hours(keys, '13')
        _t14 = self._hours(keys, '14')
        _t15 = self._hours(keys, '15')
        _t16 = self._hours(keys, '16')
        _t17 = self._hours(keys, '17')
        _t18 = self._hours(keys, '18')
        _t19 = self._hours(keys, '19')
        _t20 = self._hours(keys, '20')
        _t21 = self._hours(keys, '21')
        _t22 = self._hours(keys, '22')
        _t23 = self._hours(keys, '23')

        keys.insert(0, 'Время')

        if title:
            weather = [
                keys,
                _t00, _t01, _t02, _t03, _t04, _t05,
                _t06, _t07, _t08, _t09, _t10, _t11,
                _t12, _t13, _t14, _t15, _t16, _t17,
                _t18, _t19, _t20, _t21, _t22, _t23
            ]
        else:
            weather = [
                _t00, _t01, _t02, _t03, _t04, _t05,
                _t06, _t07, _t08, _t09, _t10, _t11,
                _t12, _t13, _t14, _t15, _t16, _t17,
                _t18, _t19, _t20, _t21, _t22, _t23
            ]

        return weather

    def database_list_formation(self, place, upass):
        idplace = RasAsiDatabase().id_place(upass=upass, place=place)
        keys = self.weather_log.keys()

        weather = []

        for i in self._twentyFourHours:
            entry = []
            entry.append(idplace)
            entry.append(f'{self.get_date} {i}')
            for i2 in keys:
                if i2 == 'Атмосферное давление':

                    hpa = self.weather_log.get(i2).get(f'{self.get_date} {i}').split(' / ')[0]
                    mmhg = self.weather_log.get(i2).get(f'{self.get_date} {i}').split(' / ')[1]
                    entry.append(hpa.split(' ')[0])
                    entry.append(mmhg.split(' ')[0])
                else:
                    temp_var = self.weather_log.get(i2).get(f'{self.get_date} {i}')

                    if not temp_var:
                        entry.append(self.weather_log.get(i2).get(f'{self.get_date} {i}'))
                    else:
                        entry.append(self.weather_log.get(i2).get(f'{self.get_date} {i}').split(' ')[0].replace(',', '.'))

            weather.append(tuple(entry))

        return weather


