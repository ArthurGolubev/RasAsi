from RasAsiVer2.Database.CreateTables import CreateTables
from RasAsiVer2.Database.RasAsiDatabase import RasAsiDatabase
from RasAsiVer2.Map.Map import Map
# CreateTables(upass=input('pass ')).create_location()
# RasAsiDatabase().add_map_location(location=(52.3810, 129.4842), upass=input('pass '))
RasAsiDatabase().add_map_location(location=(22.3810, 20.4842), upass=input('pass '))
# locations = RasAsiDatabase().get_map_location(upass=input('pass '))
# print(locations)
# print(type(locations[0][1]))
# print(locations[0][1]+11)
# print(locations[0][1])
Map().show_places(upass=input('pass '))
