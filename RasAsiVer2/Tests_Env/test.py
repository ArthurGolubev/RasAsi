import folium
import random
import math

x = random.uniform(0, 80)
y = random.uniform(0, 180)
map = folium.Map(location=[x, y], zoom_start=13, tiles='Stamen Terrain')
a, b = math.degrees(x), math.degrees(y)

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
link_google = fr'<a href="https://www.google.ru/maps/@{x},{y},3964m/data=!3m1!1e3?hl=ru", target="_blank">place - {x}, {y}<\a> 😉👌'

folium.Marker(location=[x, y], popup=link_google, icon=folium.Icon(color='gray')).add_to(map)

map.save('testmap.html')

# https://www.google.com/maps/@51.6878689,101.2675818,37546m/data=!3m1!1e3