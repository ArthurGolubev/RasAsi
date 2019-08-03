import folium
import random
import math

import os
import json
import requests
import urllib.request

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
# vis1 = json.loads(requests.get(f'{url}/vis1.json').text)
# vis1 = json.loads('C:/Users/ArthurGo/Downloads/MyPlot.html')
# json.loads(urllib.request.urlopen('C:/Users/ArthurGo/Downloads/MyPlot.html'))
# vis2 = json.loads(requests.get(f'{url}/vis2.json').text)
# vis3 = json.loads(requests.get(f'{url}/vis3.json').text)


# antarctic_ice_edge = f'{url}/antarctic_ice_edge.json'
# antarctic_ice_shelf_topo = f'{url}/antarctic_ice_shelf_topo.json'

# print('vis1 - ',t)
# print('\n\n\nvis1 - ',vis2)

x = random.uniform(0, 80)
y = random.uniform(0, 180)
# map = folium.Map(location=[x, y], zoom_start=13, tiles='Stamen Terrain')
map = folium.Map(
    location=[-59.1759, -11.6016],
    tiles='CartoDB positron',
    zoom_start=3,
    control_scale=True# Limited levels of zoom for free Mapbox tiles.
)


# folium.GeoJson(
#     antarctic_ice_edge,
#     name='geojson'
# ).add_to(map)

# folium.TopoJson(
#     json.loads(requests.get(antarctic_ice_shelf_topo).text),
#     'objects.antarctic_ice_shelf',
#     name='topojson', tooltip='FOREST'
# ).add_to(map)
folium.map.CustomPane('st', z_index=625, pointer_events=False).add_to(map)
folium.LayerControl().add_to(map)  # nice


# print('x - ', x, 'y - ', y)
#
# map = folium.Map(
#     location=[56.025883, 92.9657853],
    # location=[x, y],
    # zoom_start=10,
    # tiles='https://api.tiles.mapbox.com/v4/' + mapboxTilesetId + '/{z}/{x}/{y}.png?access_token=' + mapboxAccessToken,
    # attr='mapbox.com'
# )
# folium.LayerControl().add_to(map)
x = 26.3255296
y = 37.4353237
l = [x, y]
link_google = fr'<a href="https://www.google.ru/maps/@{x},{y},3964m/data=!3m1!1e3?hl=ru", target="_blank">place - {x}, {y}<\a> 😉👌'

folium.Marker(location=l, popup=link_google, tooltip='tooltip', icon=folium.Icon(icon='tree', prefix='fa')).add_to(map)
# folium.Marker(location=[x+.1, y+.1], popup=folium.Popup(max_width=450).add_child(folium.Vega(t, width=1000, height=1000))).add_to(map)
# folium.Marker(location=[x+.1, y], popup=folium.Popup(max_width=450).add_child(folium.Vega(vis2, width=450, height=250))).add_to(map)
# folium.Marker(location=[x, y+.1], popup=folium.Popup(max_width=450).add_child(folium.Vega(vis3, width=450, height=250))).add_to(map)

# folium.CircleMarker(radius=100, location=(x, y), popup='Динамичный, измеряется в пикселях', color='crimson', fill=True).add_to(map)
# folium.Circle(radius=1000, location=(x, y), popup='Статичный, измеряется в единицах карты', color='crimson', fill=False).add_to(map)

map.add_child(folium.LatLngPopup())
# map.add_child(folium.ClickForMarker(popup='SOM OTOBROJENIE'))  # add marker to click
# map.fit_bounds([[52.193636, -2.221575], [52.636878, -1.139759]], max_zoom=10)
# folium.vector_layers.Circle(location=l, radius=140).add_to(map)
# folium.vector_layers.PolyLine(locations=[(x, y), (x+.3,y+.3), (x+.4, y-.12)]).add_to(map)
# folium.vector_layers.Polygon(locations=[(x-.1, y-.1), (x+.33,y+.34), (x+.42, y-.12)]).add_to(map)
folium.vector_layers.Polygon(locations=[(x-1, y-1), (x-1, y+1), (x+1, y+1), (x+1, y-1)]).add_to(map)
folium.vector_layers.Polygon(locations=[(x-1.4, y-1.4), (x-1.4, y+1.4), (x+1.4, y+1.4), (x+1.4, y-1.4)], bubbling_mouse_events=True).add_to(map)
map.save('testmap.html')

# https://www.google.com/maps/@51.6878689,101.2675818,37546m/data=!3m1!1e3