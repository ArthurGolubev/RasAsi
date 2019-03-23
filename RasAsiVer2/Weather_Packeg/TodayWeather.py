from RasAsiVer2.Weather_Packeg.Weather import Weather


class TodayWeather:
    Krasnoyarsk_spreadsheetId = '103fPu9jlTmFcWKhRChdzP2Xva2SJa17wlK2YRWrhrSM'
    Novosibirsk_spreadsheetId = '1Dfh88Of9a1ekZWALq25XH4DD5mh1wQUal0kHqSgGWDQ'

    def __init__(self):
        Novosibirsk = Weather(place='novosibirsk')
        Novosibirsk.get_weather()
        Novosibirsk.update_spreadsheet(spreadsheet_id=self.Novosibirsk_spreadsheetId, values=Novosibirsk.day_weather[1:])
        """В случае создания и заполнения новой таблицы"""
        # Novosibirsk.make_spreadsheet()
        # Novosibirsk.update_spreadsheet(spreadsheet_id=Novosibirsk.spreadsheetId, values=Novosibirsk.day_weather[1:])

        Krasnoyarsk = Weather()
        Krasnoyarsk.get_weather()
        Krasnoyarsk.update_spreadsheet(spreadsheet_id=self.Krasnoyarsk_spreadsheetId, values=Krasnoyarsk.day_weather[1:])
        """В случае создания и заполнения новой таблицы"""
        # Krasnoyarsk.make_spreadsheet()
        # Krasnoyarsk.update_spreadsheet(spreadsheet_id=Krasnoyarsk.spreadsheetId, values=Krasnoyarsk.day_weather[1:])

# def today_weather():
#     Krasnoyarsk_spreadsheetId = '103fPu9jlTmFcWKhRChdzP2Xva2SJa17wlK2YRWrhrSM'
#     Novosibirsk_spreadsheetId = '1Dfh88Of9a1ekZWALq25XH4DD5mh1wQUal0kHqSgGWDQ'
#
#     Novosibirsk = Weather(place='novosibirsk')
#     Novosibirsk.get_weather()
#     Novosibirsk.update_spreadsheet(spreadsheet_id=Novosibirsk_spreadsheetId, values=Novosibirsk.day_weather[1:])
#     """В случае создания и заполнения новой таблицы"""
#     Novosibirsk.make_spreadsheet()
#     Novosibirsk.update_spreadsheet(spreadsheet_id=Novosibirsk.spreadsheetId, values=Novosibirsk.day_weather[1:])
    #
    # Krasnoyarsk = Weather()
    # Krasnoyarsk.get_weather()
    # Krasnoyarsk.update_spreadsheet(spreadsheet_id=Krasnoyarsk_spreadsheetId, values=Krasnoyarsk.day_weather[1:])
    # """В случае создания и заполнения новой таблицы"""
    # Krasnoyarsk.make_spreadsheet()
    # Krasnoyarsk.update_spreadsheet(spreadsheet_id=Krasnoyarsk.spreadsheetId, values=Krasnoyarsk.day_weather[1:])


if __name__ == '__main__':
    TodayWeather()
else:
    print(f'Подключен модуль {__name__}')
