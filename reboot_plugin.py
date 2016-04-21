import sys

def exit_bot(bot, msg):
    bot.sender.sendMessage("Daisy, Daisy, give me your answer tru...")
    sys.exit(0)


__commands__ = {
    "/gotosleep": exit_bot
}
