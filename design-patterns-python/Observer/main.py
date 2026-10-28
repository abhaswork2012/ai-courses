from weather_station import WeatherStation
from mobile import Mobile
from tv import TV


ws = WeatherStation()
tv = TV()
mobile = Mobile()

ws.add_observer(tv)
ws.update_temperature(25.0)
ws.add_observer(mobile)
ws.update_temperature(30.0)
ws.remove_observer(tv)
ws.update_temperature(35.0)