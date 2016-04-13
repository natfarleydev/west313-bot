import telepot
import time
from telepot.delegate import per_chat_id, create_open

##########OPENWEATHER API & APPKEY##################
import pyowm
owm = pyowm.OWM('238da21e83fcfa9f499bbad8d9b365d0')
####################################################

class WestieBot(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        "docstring"
        super(WestieBot, self).__init__(seed_tuple, timeout)

    def on_message(self, msg):

        """Simple on message thing."""
	
	#OpenWeather Implementation, check for 'weather' in input string
	if 'weather' in msg['text']:
	    weatherLocationW313 = owm.weather_at_place('Birmingham,GB')
	    w = weatherLocationW313.get_weather()
	    weather = {'Status': w.get_detailed_status(), 
		       'Time':w.get_reference_time(timeformat='iso'),
		       'Humidity': w.get_humidity(),
                       'Pressure': w.get_pressure(),
                       'Temperature' : w.get_temperature(unit='celsius'),
                       'Wind' : w.get_wind()}
			
	    self.sender.sendMessage(""" Weather at West 313 is currently: 
					\nDate/Time: %s \nStatus: %s \nTemperature: %s C, High: %s C, Low: %s C 
					\nHumidity: %s \nPressure: %s mb\nWind Speed: %s mph, %s Degrees"""
			           % (weather['Time'],weather['Status'],weather['Temperature']['temp'],
                                      weather['Temperature']['temp_max'],weather['Temperature']['temp_min'],
                                      weather['Humidity'],weather['Pressure']['press'],
				      weather['Wind']['speed'],weather['Wind']['deg'],))
        elif msg['text']:
            self.sender.sendMessage(
			    "I know naafing, code me: https://github.com/nasfarley88/west313-bot")

def main():
    """Simple main."""
    import config
    bot = telepot.DelegatorBot(config.TG_KEY, [
        (per_chat_id(), create_open(WestieBot, timeout=10)),

    ])
    bot.notifyOnMessage(run_forever=True)

if __name__ == '__main__':
    main()
