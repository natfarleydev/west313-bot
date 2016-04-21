def random_quote(show):
        resp = requests.get(
            "http://api.chrisvalleskey.com/fillerama/get.php?count=100&format=json&show={}".format(show))
        choice = random.choice(resp.json()['db'])
        message_to_send = html.unescape("{quote} - _{source}_".format(**choice))
        return message_to_send
