from RasAsiVer2.Database.CreateTables import CreateTables
from RasAsiVer2.Weather_Packeg.WeatherForecast import WeatherForecast

WeatherForecast(upass=input('pass ')).weather_today(tomorrow=True)
# CreateTables(upass=input('pass ')).create_weather_journal_tomorrow()
