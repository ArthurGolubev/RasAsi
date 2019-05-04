from sys import platform
from RasAsiVer2.Weather_Packeg.Weather import Weather
from RasAsiVer2.Weather_Packeg.WeatherChart import WeatherChart


class WeatherTomorrow:
    # if platform == 'win32':
    #     Krasnoyarsk_spreadsheetId = '1jI4NvcuSguqD94xmvqJyk05awNksXOtKNp8jLQ67veo'
    #     Novosibirsk_spreadsheetId = '12YsaSrM4RJXOlXWmfxYL-w0nIdQN9OS0AcvdE_Simcc'
    # elif platform == 'linux':
    #     Krasnoyarsk_spreadsheetId = '1fgjOxFNxjnUIRRIA60xnWCpYyLRg0txuazimsbg1Km4'
    #     Novosibirsk_spreadsheetId = '1LZF9yopCmDpUUkjSPSu4krwwJ0IFOHV7Qioz_4SuFm0'

    def weather_tomorrow(self):
        Krasnoyarsk = Weather(place='krasnoyarsk')
        Krasnoyarsk.get_weather()
        Krasnoyarsk.append_spreadsheet(spreadsheet_id=self.Krasnoyarsk_spreadsheetId, values=Krasnoyarsk.day_weather[1:])

        Novosibirsk = Weather(place='novosibirsk')
        Novosibirsk.get_weather()
        Novosibirsk.append_spreadsheet(spreadsheet_id=self.Novosibirsk_spreadsheetId, values=Novosibirsk.day_weather[1:])

        WeatherChart().chart()  # TODO Разкоментировать в рабочей версии

    def today_place(self, place):  # TODO Доделать
        spec_place = Weather(place=place)
        spec_place.get_weather()
        spec_place.make_spreadsheet()
        # spec_place.append_spreadsheet(spreadsheet_id=self.spec_place_spreadsheetId, values=spec_place.day_weather[1:])




if __name__ == '__main__':
    WeatherTomorrow().weather_tomorrow()
else:
    print(f'Подключен модуль {__name__}')
