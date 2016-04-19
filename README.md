# west313-bot
A telegram bot for the office

## Rules
 - New feature: new module
 - If you're a member of the office, your pull request will be accepted

## Weather Bot
To use the included weather bot you will require a free API key from [OpenWeather.org](http://openweathermap.org/). Once this has been obtained, replace the line:


<code>owm = pyowm.OWM(pickle.load(open(".weather_key.dat","rb")))</code>


with the following:


<code>owm = pyowm.OWM('\<yourKeyHere\>')</code>
