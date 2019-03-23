class Annotations:
    @staticmethod
    def min_max(atr_value, atr_name):
        if atr_name == 'Температура':
            SI = '°C'
        elif atr_name == 'Скорость ветра':
            SI = 'm/s'
        elif atr_name == 'Осадки':
            SI = 'mm'
        elif atr_name == 'Облачность':
            SI = '%'
        elif atr_name == 'Влажность':
            SI = '%'
        elif atr_name == 'Атмосферное давление':
            SI = 'hPa'
        annotations = [
            dict(x=atr_value.index(max(atr_value)), y=max(atr_value),
                 xref='x',
                 yref='y',
                 text=f'Макс. {atr_name} {max(atr_value)}{SI}',
                 showarrow=True,
                 font=dict(
                     family='Courier New, monospace',
                     size=16,
                     color='#f7f7ff'
                 ),
                 arrowhead=1,
                 arrowsize=1,
                 arrowwidth=2,
                 arrowcolor='#FF5555',
                 ax=0,
                 ay=-80,
                 bordercolor='#c7c7c7',
                 bordefwidth=2,
                 borderpad=4,
                 bgcolor='#F55F23',
                 opacity=0.8
                 ),
            dict(x=atr_value.index(min(atr_value)), y=min(atr_value),
                 xref='x',
                 yref='y',
                 text=f'Мин. {atr_name} {min(atr_value)}{SI}',
                 showarrow=True,
                 font=dict(
                     family='Courier New, monospace',
                     size=16,
                     color='#f7f7ff'
                 ),
                 arrowhead=1,
                 arrowsize=1,
                 arrowwidth=2,
                 arrowcolor='#FF5555',
                 ax=0,
                 ay=90,
                 bordercolor='#c7c7c7',
                 bordefwidth=2,
                 borderpad=4,
                 bgcolor='#F55F23',
                 opacity=0.8
                 )
        ]
        return annotations
