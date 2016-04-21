import config

##########OPENWEATHER API & APPKEY##################
import pyowm,pickle
owm = pyowm.OWM(config.WEATHER_KEY)
####################################################

# This is not a *true* self, but it's as good a name as any
def weather_botCall(self, msg):
    user = 'user'
    for key in msg:
    	if key == 'from':
        	user = msg['from']['username']
    weatherLocationW313 = owm.weather_at_place('Birmingham,uk')
    w = weatherLocationW313.get_weather()
    weather = {'Status': w.get_detailed_status(),
                    'Time':w.get_reference_time(timeformat='iso'),
                    'Humidity': w.get_humidity(),
                    'Pressure': w.get_pressure(),
                    'Temperature' : w.get_temperature(unit='celsius'),
                    'Wind' : w.get_wind()}

    self.sender.sendMessage(""" Hello %s! The weather for today at West 313 is currently: 
                                    \nDate/Time: %s \nStatus: %s \nTemperature: %s C, High: %s C, Low: %s C 
                                    \nHumidity: %s \nPressure: %s mb\nWind Speed: %s mph, %s Degrees"""
                               % (user,weather['Time'],weather['Status'],weather['Temperature']['temp'],
                                  weather['Temperature']['temp_max'],weather['Temperature']['temp_min'],
                                  weather['Humidity'],weather['Pressure']['press'],
                                  weather['Wind']['speed'],weather['Wind']['deg'],))

__commands__ = {
        "/weather": weather_botCall
}
