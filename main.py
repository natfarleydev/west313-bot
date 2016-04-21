import telepot
import time
from telepot.delegate import per_chat_id, create_open
import weather_bot
import arxiv_plugin

####################################################

# If you want your features to be used as part of the bot, add them here
bot_features = [
    weather_bot,
    arxiv_plugin,
]

EXITAPP = False

class WestieBot(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        "docstring"
        super(WestieBot, self).__init__(seed_tuple, timeout)

    def on_message(self, msg):

        """Simple on message thing."""

        if "/die" in msg['text']:
            global EXITAPP
            self.sender.sendMessage("Daisy, Daisy, give mmmee yourrr aanswweeerr truuuee...")
            EXITAPP = True

        # bot features from modules
        bot_methods = {}
        for i in [x.__commands__ for x in bot_features]:
            print(i)
            bot_methods.update(i)
            print(bot_methods)

        for command, method in bot_methods.items():
            print("Executing {}".format(method.__name__))
            if command in msg['text']:
                method(self, msg)


def main():
    """Simple main."""
    import config
    bot = telepot.DelegatorBot(config.TG_KEY, [
        (per_chat_id(), create_open(WestieBot, timeout=10)),
    ])

    bot.message_loop()

    while not EXITAPP:
        time.sleep(1)

if __name__ == '__main__':
    main()
