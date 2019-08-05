import random
import folium
import datetime
from sys import platform
from RasAsiVer2.Google.GoogleDrive import GoogleDrive
from RasAsiVer2.Database.RasAsiDatabase import RasAsiDatabase


class Map:

    def get_place(self):
        x = random.uniform(0, 80)
        y = random.uniform(0, 180)

        m = folium.Map(
            location=[x, y],
            tiles='Stamen Terrain',
            zoom_start=8,
            control_scale=True

        )
        folium.raster_layers.TileLayer('OpenStreetMap').add_to(m)
        folium.LayerControl().add_to(m)
        marker_text = fr'Coordinate - {x}, {y}\n' \
            fr'<a href="https://www.google.ru/maps/@{x},{y}' \
            fr',3964m/data=!3m1!1e3?hl=ru", target="_blank">GoogleEarth<\a> 😉👌'
        folium.Marker(location=[x, y], popup=marker_text, icon=folium.Icon(icon='cloud', color='green')).add_to(m)
        folium.Circle(location=(x, y), radius=185000).add_to(m)
        # folium.Circle(location=(x, y), radius=285000).add_to(m)

        if platform == 'linux':
            path = f'/home/rasasi/map_rasasi/{datetime.datetime.today().date()}.html'
            m.save(path)
            GoogleDrive().upload(files=path, folder_id='1Xgc2cD7oXqalPzX19oV6Lgev9I_30W0G')
        else:
            path = f'{datetime.datetime.today().date()}.html'
            m.save(path)

    def show_places(self, upass):
        locations = RasAsiDatabase().get_map_location(upass=upass)

        m = folium.Map(
            location=[20, 90],
            tiles='Stamen Terrain',
            zoom_start=2,
            control_scale=True

        )
        folium.raster_layers.TileLayer('OpenStreetMap').add_to(m)
        folium.LayerControl().add_to(m)

        for location in locations:
            marker_text = fr'Coordinate - {location[1]}, {location[2]}\n' \
                fr'<a href="https://www.google.ru/maps/@{location[1]},{location[2]}' \
                fr',3964m/data=!3m1!1e3?hl=ru", target="_blank">GoogleEarth<\a> 😉👌\n' \
                fr'{location[3]}'
            folium.Marker(
                location=(location[1], location[2]),
                popup=folium.Popup(html=marker_text, max_width=200),
                icon=folium.Icon(icon='cloud', color='green'),
            ).add_to(m)

            folium.Circle(
                location=(location[1], location[2]),
                radius=100000,
                popup=marker_text,
                icon=folium.Icon(icon='cloud', color='green')
            ).add_to(m)

        if platform == 'linux':
            path = f'/home/rasasi/map_rasasi/locations.html'
            m.save(path)
            GoogleDrive().upload(files=path, folder_id='1Xgc2cD7oXqalPzX19oV6Lgev9I_30W0G')
        else:
            path = f'location.html'
            m.save(path)


if __name__ == '__main__':
    # Map().get_map()
    Map().show_places(locations=[(54.8042, 161.8459), (52.3810, 129.4842)])