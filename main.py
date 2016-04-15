import telepot
import time
from telepot.delegate import per_chat_id, create_open
import weather_bot

####################################################

class WestieBot(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        "docstring"
        super(WestieBot, self).__init__(seed_tuple, timeout)

    def on_message(self, msg):

        """Simple on message thing."""
	
	user = 'user'
	for key in msg:
		if key == 'from':
			user = msg['from']['username']

	#OpenWeather Implementation, check for 'weather' in input string
	if 'weather' in msg['text'].lower():
		weather_bot.weather_botCall(self,user,'Birmingham,uk')  
		print "Weather Bot Accessed by %s" % user

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
