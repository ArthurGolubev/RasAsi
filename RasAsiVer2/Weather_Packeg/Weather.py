from sys import platform
from selenium import webdriver
from datetime import datetime, timedelta
from RasAsiVer2.Weather_Packeg.GetWeather import GetWeather
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet
from RasAsiVer2.addiction_support.psutil_temperature import TemperatureSensor
from RasAsiVer2.Database_Scripts.append_today_weather import append_today_weather


class Weather:

    if platform == 'win32':
        executable_path = r'C:\PycharmProjects\RasAsi\credentials\geckodriver.exe'  # Laptop
        # executable_path = r'C:\PythonProject\RasAsi\credentials\geckodriver.exe'  # PC
    elif platform == 'linux':
        executable_path = r'/home/rasasi/RasAsi/credentials/geckodriver'  # Ubuntu Mate
    else:
        print(f'Платформа {platform} не поддерживается')

    temp = TemperatureSensor()

    def __init__(self, place, upass, id_date_day, feature=None, spreadsheetId=None):
        self.upass = upass
        self.id_date_day = id_date_day
        self._table = GoogleSpreadsheet()
        self.spreadsheetId = spreadsheetId
        self.place = place
        # self.date = (datetime.now()+timedelta(1)).strftime('%d.%m.%Y')      # next day weather
        self.date = datetime.now().strftime('%d.%m.%Y')                     # today weather
        # self.tomorrow = (datetime.now()+timedelta(1)).date().day            # next day weather
        self.tomorrow = datetime.now().date().day                           # today  weather

        if not feature:
            self.feature = ["Скорость ветра", "Осадки", "Температура",
                            "Облачность", "Влажность", "Атмосферное давление"]
        else:
            self.feature = []
            self.feature.append(feature)

    def get_weather(self):
        print(f'\n{self.place.capitalize()}')

        _options_webdriver = webdriver.FirefoxOptions()
        _options_webdriver.set_preference("intl.accept_languages", "ru")

        _browser = webdriver.Firefox(executable_path=self.executable_path, options=_options_webdriver)
        _browser.implicitly_wait(220)
        _browser.get(f'https://www.ventusky.com/{self.place}')
        _browser.find_element_by_xpath("//span[@id='aside_close_btn']").click()                                         #close right panel
        _browser.find_element_by_xpath('//div[@class="qj l hv"]/div[@class="xx"]/select/option[@value="off"]').click()  #off wind animation
        _browser.find_element_by_xpath(f"//div[@id='m']/a[@class='s t']").click()                                       #calendar
        _browser.find_element_by_xpath(f"//table//tr//td//a[contains(text(), '{self.tomorrow}')]").click()              #calendar
        self._weather = GetWeather(browser=_browser, get_date=self.date, temp=self.temp)
        for i in self.feature:
            self._weather.get_values(i)
        _browser.close()

    def make_spreadsheet(self):
        self._table.create_table(table_name=f'{self.place.capitalize()} {self.date}')
        self.spreadsheetId = self._table.spreadsheet_id
        self._table.update_spreadsheets_values(values=self._table.body_formation(
            values=self._weather.GoogleSpreadsheet_dict_formation()),
            spreadsheet_id=self.spreadsheetId, range_name="Лист1!A1")

    def append_spreadsheet(self, spreadsheet_id, range_='Лист1'):
        self._table.append_spreadsheets_values(
            spreadsheet_id=spreadsheet_id,
            values=self._weather.GoogleSpreadsheet_dict_formation()[1:],
            range_name=range_)

    def append_database(self):
        append_today_weather(values=self._weather.database_list_formation(place=self.place, upass=self.upass),
                             upass=self.upass)

    def get_weather_data_set(self, spreadsheetId):
        weather_data_set = self._table.get_spreadsheets_values(
            spreadsheet_id=spreadsheetId,
            range_name='Лист1!A:G').get('values')
        return weather_data_set

