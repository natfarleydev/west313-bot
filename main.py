import telepot
import time
from telepot.delegate import per_chat_id, create_open
import weather_bot

####################################################

# If you want your features to be used as part of the bot, add them here
bot_features = [
    weather_bot,
]

class WestieBot(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        "docstring"
        super(WestieBot, self).__init__(seed_tuple, timeout)

    def on_message(self, msg):

        """Simple on message thing."""

                # bot features from modules
        bot_methods = {}
        for i in [x.__commands__ for x in bot_features]:
            print(i)
            bot_methods.update(i)
            print(bot_methods)

        for command, method in bot_methods.items():
            if command in msg:
                method(self, msg)

        # TODO remove in favour of __commands__
        #OpenWeather Implementation, check for 'weather' in input string
       # if 'weather' in msg['text'].lower():
        #    weather_bot.weather_botCall(self, 'Birmingham,uk')
        #    print("Weather Bot Accessed by %s" % user)
#
def main():
    """Simple main."""
    import config
    bot = telepot.DelegatorBot(config.TG_KEY, [
        (per_chat_id(), create_open(WestieBot, timeout=10)),
    ])
    bot.message_loop(run_forever=True)

if __name__ == '__main__':
    main()
