from selenium import webdriver
from RasAsiVer2.Weather_Packeg.GetWeather import GetWeather
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet
from datetime import datetime, timedelta


class Weather:

    def __init__(self, place, date=datetime.now().strftime('%d.%m.%Y'), feature=None, spreadsheetId=None):
        self.day_weather = None
        self._table = GoogleSpreadsheet()
        self.spreadsheetId = spreadsheetId
        self.place = place
        self.date = date
        if not feature:
            self.feature = ["Скорость ветра", "Осадки", "Температура",
                            "Облачность", "Влажность", "Атмосферное давление"]
        else:
            self.feature = []
            self.feature.append(feature)

    def get_weather(self):
        print(f'\n{self.place.capitalize()}')
        _browser = webdriver.Firefox()
        _browser.implicitly_wait(20)
        _browser.get(f'https://www.ventusky.com/{self.place}')
        _browser.find_element_by_xpath("//span[@id='aside_close_btn']").click()
        _weather = GetWeather(browser=_browser, get_date=self.date)
        for i in self.feature:
            _weather.get_values(i)
        self.day_weather = _weather.dict_formation()
        _browser.close()

    def make_spreadsheet(self):
        self._table.create_table(table_name=f'{self.place.capitalize()} {self.date}')
        self.spreadsheetId = self._table.spreadsheet_id
        self._table.update_spreadsheets_values(values=self._table.body_formation(values=self.day_weather),
                                               spreadsheet_id=self.spreadsheetId, range_name="Лист1!A1")

        '''почему не нужно указывать self.day_wether'''
    def append_spreadsheet(self, spreadsheet_id, values, range_='Лист1'):
        self._table.append_spreadsheets_values(spreadsheet_id=spreadsheet_id, values=values, range_name=range_,)

    def get_weather_data_set(self, spreadsheetId):
        weather_data_set = self._table.get_spreadsheets_values(spreadsheet_id=spreadsheetId, range_name='Лист1!A:G').get('values')
        return weather_data_set

