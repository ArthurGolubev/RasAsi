import plotly
from plotly import graph_objs
from datetime import datetime
from RasAsiVer2.Weather_Packeg.Weather import Weather
from RasAsiVer2.Tests_Env.Plotly.payload.annotations import Annotations


class WeatherChart:
    Krasnoyarsk_spreadsheetId = '1fgjOxFNxjnUIRRIA60xnWCpYyLRg0txuazimsbg1Km4'
    Novosibirsk_spreadsheetId = '1LZF9yopCmDpUUkjSPSu4krwwJ0IFOHV7Qioz_4SuFm0'

    def __init__(self):
        self.today = datetime.today()

        self.data = []
        self.chart_name = f'ChartWeather 18.03.2019 - {self.today.day}.{self.today.month}.{self.today.year}.html'

        _Novosibirsk = Weather(place='novosibirsk')
        Novosibirsk_data_set = _Novosibirsk.get_weather_data_set(spreadsheetId=self.Novosibirsk_spreadsheetId)
        print(Novosibirsk_data_set)

        _Krasnoyarsk = Weather(place='krasnoyarsk')
        Krasnoyarsk_data_set = _Krasnoyarsk.get_weather_data_set(self.Krasnoyarsk_spreadsheetId)
        print(Krasnoyarsk_data_set)

        self.Novosibirsk = self._data_processing(Novosibirsk_data_set)
        self.Krasnoyarsk = self._data_processing(Krasnoyarsk_data_set)

    def _data_processing(self, data_set):
        time = []
        temperature = []
        wind_speed = []
        precipitation = []
        overcast = []
        humidity = []
        atmosphere_pressure = []
        for i in data_set[1:]:
            time.append(i[0])
            justVariable = i[3].split(' ')[0]
            if not justVariable[0].isdigit():
                temperature.append(int(justVariable[1:])*-1)
            else:
                temperature.append(int(justVariable))
            precipitation.append(float(i[2].split(' ')[0].replace(',', '.')))
            wind_speed.append(int(i[1].split(' ')[0]))
            overcast.append(int(i[4].split(' ')[0]))
            atmosphere_pressure.append(int(i[6].split(' ')[0]))
        for i in data_set[2::3]:
            humidity.append(int(i[5].split(' ')[0]))
        return time, wind_speed, precipitation, temperature, overcast, humidity, atmosphere_pressure

    def _trace(self, place, name):  # TODO возможность сменить цвет
        trace = []
        for i in range(1, 7):
            trace.append(
                graph_objs.Scatter(
                    x=place[0],
                    y=place[i],
                    legendgroup='G1',
                    name=name
                ))
        return trace

    def _data(self):
        self.data.extend(self._trace(self.Novosibirsk, 'Новосибирск'))
        self.data.extend(self._trace(self.Krasnoyarsk, 'Красноярск'))

    def chart(self):
        self._data()
        updatemenus = list([
            dict(active=-1,
                 buttons=list([
                     dict(
                         label='Температура',
                         method='update',
                         args=[
                             {'visible': [False, False, True, False, False, False]},
                             {'title': 'Температура',
                              'annotations': Annotations.min_max(self.Krasnoyarsk[3], 'Температура')
                              }
                         ]
                     ),
                     dict(label='Скорость ветра',
                          method='update',
                          args=[
                              {'visible': [True, False, False, False, False, False]},
                              {'title': 'Скорость ветра',
                               'annotations': Annotations.min_max(self.Krasnoyarsk[1], 'Скорость ветра')}
                          ]),
                     dict(label='Осадки',
                          method='update',
                          args=[
                              {'visible': [False, True, False, False, False, False]},
                              {'title': 'Осадки',
                               'annotations': Annotations.min_max(self.Krasnoyarsk[2], 'Осадки')}
                          ]),
                     dict(label='Облачность',
                          method='update',
                          args=[
                              {'visible': [False, False, False, True, False, False]},
                              {'title': 'Облачность',
                               'annotations': Annotations.min_max(self.Krasnoyarsk[4], 'Облачность')}
                          ]),
                     dict(label='Влажность',
                          method='update',
                          args=[
                              {'visible': [False, False, False, False, True, False]},
                              {'title': 'Влажность',
                               'annotations': Annotations.min_max(self.Krasnoyarsk[5], 'Влажность')}
                          ]),
                     dict(label='Атмосферное давление',
                          method='update',
                          args=[
                              {'visible': [False, False, False, False, False, True]},
                              {'title': 'Атмосферное давление',
                               'annotations': Annotations.min_max(self.Krasnoyarsk[6], 'Атмосферное давление')}
                          ])
                 ]))
        ])

        layout = dict(title="Температура в °C", showlegend=True, updatemenus=updatemenus)
        fig = dict(data=self.data, layout=layout)
        # plotly.offline.plot(fig, auto_open=True, filename=self.chart_name)
        plotly.offline.plot(fig, auto_open=False, filename='ChartWeather.html')


if __name__ == '__main__':
    a = WeatherChart()
    a.chart()
else:
    f'Подключен модуль {__name__}'
