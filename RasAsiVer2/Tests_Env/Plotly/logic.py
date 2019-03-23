from RasAsiVer2.Weather_Packeg.Weather import Weather
from RasAsiVer2.Tests_Env.Plotly.payload.annotations import Annotations
import plotly
from plotly import graph_objs

# TODO 2 блок кода - формирование имеющихся данных
Krasnoyarsk_spreadsheetId = '103fPu9jlTmFcWKhRChdzP2Xva2SJa17wlK2YRWrhrSM'
Novosibirsk_spreadsheetId = '1Dfh88Of9a1ekZWALq25XH4DD5mh1wQUal0kHqSgGWDQ'
# Novosibirsk_spreadsheetId = '1GVAdbAt8eaGVE5qK-lLtILRzGvr4omVl3r3y-Qxd2vQ' # copy

Novosibirsk = Weather(place='novosibirsk')
Novosibirsk_data_set = Novosibirsk.get_weather_data_set(spreadsheetId=Novosibirsk_spreadsheetId)
print(Novosibirsk_data_set)

Krasnoyarsk = Weather()
Krasnoyarsk_data_set = Krasnoyarsk.get_weather_data_set(spreadsheetId=Krasnoyarsk_spreadsheetId)
print(Krasnoyarsk_data_set)


def jf(data_set):
    _time = []
    _temperature = []
    _windforce = []
    for i in data_set[1:]:
        print(type(i[0]))
        _time.append(i[0])
        justVariable = i[3].split(' ')[0]
        if not justVariable[0].isdigit():
            _temperature.append(int(justVariable[1:])*-1)
        else:
            _temperature.append(int(justVariable))

        _windforce.append(int(i[1].split(' ')[0]))

    return _time, _temperature, _windforce

Krasnoyarsk = jf(Krasnoyarsk_data_set)
Novosibirsk = jf(Novosibirsk_data_set)

print(min(Krasnoyarsk[1]))
print(Krasnoyarsk[1].index(-3))



trace0 = graph_objs.Scatter(
    x = Krasnoyarsk[0],
    y = Krasnoyarsk[1],
    legendgroup='G1',
    name='Красноярск',
    ids=['s', 's', 't', 't', 's', 's', 't', 's', 's', 't', 't', 's', 's', 't', 's', 's', 't', 't', 's', 's', 't', 't', 'e', 't']
)
trace1 = graph_objs.Scatter(
    x = Novosibirsk[0],
    y = Novosibirsk[1],
    legendgroup='G1',
    opacity=0.5,
    name='Новосибирск',
    customdata=[1, 2, 3],
    # hoverinfo='x',
    line=dict(
        dash='dash',
        width=2,
        color='Crimson'
    )

)


data = [trace0, trace1]  # TODO 1 блок - формирование анотации
HH_annotations=[
                                            dict(x=Krasnoyarsk[1].index(max(Krasnoyarsk[1])), y=max(Krasnoyarsk[1]),
                                                 xref='x',
                                                 yref='y',
                                                 text='max Temperature',
                                                 showarrow=True,
                                                 font=dict(
                                                        family='Courier New, monospace',
                                                        size=16,
                                                        color='#f7f7ff'
                                                    ),
                                                 arrowhead=1,
                                                 arrowsize=1,
                                                 arrowwidth=2,
                                                 arrowcolor='#636363',
                                                 ax=0,
                                                 ay=-80,
                                                 bordercolor='#c7c7c7',
                                                 borderwidth=2,
                                                 borderpad=4,
                                                 bgcolor='#ff7f0e',
                                                 opacity=0.8
                                                 ),]


LL_annotations=[
                                            dict(x=Krasnoyarsk[1].index(min(Krasnoyarsk[1])), y=min(Krasnoyarsk[1]),
                                                 xref='x',
                                                 yref='y',
                                                 text='min Temperature',
                                                 showarrow=True,
                                                 font=dict(
                                                        family='Courier New, monospace',
                                                        size=16,
                                                        color='#f7f7ff'
                                                    ),
                                                 arrowhead=1,
                                                 arrowsize=1,
                                                 arrowwidth=2,
                                                 arrowcolor='#636363',
                                                 ax=0,
                                                 ay=-80,
                                                 bordercolor='#c7c7c7',
                                                 borderwidth=2,
                                                 borderpad=4,
                                                 bgcolor='#ff7f0e',
                                                 opacity=0.8
                                                 ),]


updatemenus = list([
    dict(active =-1,
         buttons=list([
             dict(label='Max',
                  method='update',
                  args=[{'visible': [True, True]},
                        {'title': 'Oe',
                         'annotations': Annotations.max_Temperature(Krasnoyarsk)}]),
             dict(label = 'Min',
                  method = 'update',
                  args = [{'visible': [True, True]},
                         {'title': 'min',
                          'annotations': LL_annotations}]),
         ]))
])

layout = dict(title="Температура в °C", showlegend=False, updatemenus=updatemenus)
fig = dict(data=data, layout=layout)

x = plotly.offline.plot(fig, auto_open=True, filename='MyPlot.html')


