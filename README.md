# west313-bot
A telegram bot for the office

## Rules
 - New feature: new module
 - If you're a member of the office, your pull request will be accepted


## Weather Bot
To use the included weather bot you will require a free API key from [OpenWeather.org](http://openweathermap.org/). Once this has been obtained, add it to `config.py` as:

    WEATHER_KEY = "myspecialapikey"

## Network Rail Bot
To use the included Network Rail Train Movement Feed bot, you will require a username and password from [Network Rail Data Feeds](https://datafeeds.networkrail.co.uk/ntrod/login). The information must then also be added to `config.py` as:

	NR_USER = "myusername"
	NR_PASSWORD = "password"
	NR_TMVT_FEED_ID = "ID of Subscribed Train Feed"

## Installation

    pip install -r requirements.txt
    pip install git+ssh://git@github.com/nasfarley88/arxiv.py # for the modified arxiv library


