from RasAsiVer2.Weather_Packeg.Weather import Weather
from RasAsiVer2.Decorators.Decorators import logging_decorator
from RasAsiVer2.Weather_Packeg.WeatherChart import WeatherChart
from RasAsiVer2.Database_Scripts.append_today_weather import append_today_weather


class WeatherToday:
    Krasnoyarsk_spreadsheetId = '1fgjOxFNxjnUIRRIA60xnWCpYyLRg0txuazimsbg1Km4'
    Novosibirsk_spreadsheetId = '1LZF9yopCmDpUUkjSPSu4krwwJ0IFOHV7Qioz_4SuFm0'

    def __init__(self, upass):
        self.upass = upass

    # @logging_decorator
    def weather_today(self):
        Krasnoyarsk = Weather(place='krasnoyarsk', upass=self.upass)
        Krasnoyarsk.get_weather()
        Krasnoyarsk.append_spreadsheet(spreadsheet_id=self.Krasnoyarsk_spreadsheetId)

        Novosibirsk = Weather(place='novosibirsk', upass=self.upass)
        Novosibirsk.get_weather()
        Novosibirsk.append_spreadsheet(spreadsheet_id=self.Novosibirsk_spreadsheetId)

        Krasnoyarsk.append_database()
        Novosibirsk.append_database()

        WeatherChart().chart()

    @logging_decorator
    def today_place(self, place):  # TODO Доделать
        spec_place = Weather(place=place)
        spec_place.get_weather()
        spec_place.make_spreadsheet()
        # spec_place.append_spreadsheet(spreadsheet_id=self.spec_place_spreadsheetId, values=spec_place.day_weather[1:])


if __name__ == '__main__':
    WeatherToday(upass='').weather_today() # TODO удалить
else:
    print(f'Подключен модуль {__name__}')
