import sys
sys.path.append("/home/nasfarley88/git/arxiv.py/")
import arxiv

def get_arxiv_link(bot, msg):
    results = arxiv.query(msg['text'].replace("/arxiv ", ""), max_results=1)
    bot.sender.sendMessage("Title: {}\nAuthor: {}".format(results[0]['title'], results[0]['author']))
    bot.sender.sendDocument(open(arxiv.download(results[0]), "rb"))


__commands__ = {
    "/arxiv": get_arxiv_link,
}
