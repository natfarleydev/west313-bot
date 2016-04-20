import asyncio
import telepot
# Strange bug doesn't allow to use async directle like telepot.async
from telepot import async as tpasync

import requests
import random
import html

import dataset
import re

import config
import utils

class WestieBot(tpasync.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        "docstring"
        super(WestieBot, self).__init__(seed_tuple, timeout)
        # This is a dirty trick, but somewhat hilarious
        _ = self.sender.sendMessage
        async def sendmessage(string):
            return await _(
                random.choice([
                    "Hey slug head. ",
                    "",
                    "",
                    "",
                    ""
                ])+string+
                random.choice([
                    " Slug head.",
                    "",
                    "",
                    "",
                    ""
                ]))

        self.sender.sendMessage = sendmessage


    async def on_message(self, msg):
        """Simple on message thing."""

        if "text" in msg:
            if "rpnf" in msg['text'].lower() or "neutron flow" in msg['text'].lower():
                await self.sender.sendMessage(utils.random_quote("doctorwho"), parse_mode="Markdown")

            if "force_burns" in msg['text'].lower() or "these are not the droids you are looking for" in msg['text'].lower():
                await self.sender.sendMessage(random_quote("starwars"), parse_mode="Markdown")

            if "codeme" in msg['text'].lower():
                await self.sender.sendMessage(
                    "I know naafing, code me: https://github.com/nasfarley88/west313-bot")

            if "#officesoundtrack" in msg['text'].lower():
                await self.add_to_office_soundtrack(msg)

            if "/playitagain" in msg['text'].lower():
                with dataset.connect(config.DBASE_LOCATION) as db:
                    office_soundtrack_table = db['office_soundtrack']
                    await self.sender.sendMessage(random.choice(list(office_soundtrack_table.all()))['url'])

            if "/deleteentry" in msg['text'].lower():
                await self.delete_entry(msg)

            if "/spike" in msg['text'].lower():
                await self.sender.sendMessage("Tracing...")
                await asyncio.sleep(random.random()*6)
                await self.sender.sendMessage("Your IP is: {}.{}.{}.{}".format(
                    random.randint(1,127),
                    random.randint(1,127),
                    random.randint(1,127),
                    random.randint(1,127)
                ))
                await self.sender.sendChatAction("typing")
                await asyncio.sleep(random.random()*2+0.5)
                await self.sender.sendMessage("Better luck next time.")



    async def add_to_office_soundtrack(self, msg):
        matches = re.findall(r"(https?://\S+)", msg['text'])
        with dataset.connect(config.DBASE_LOCATION) as db:
            office_soundtrack_table = db['office_soundtrack']
            for match in matches:
                if not office_soundtrack_table.find(url=match):
                    office_soundtrack_table.insert(dict(url=match))
                    await self.sender.sendMessage("Added {} to database.".format(match))
                else:
                    await self.sender.sendMessage("URL already in database.")

    async def delete_entry(self, msg):
        with dataset.connect(config.DBASE_LOCATION) as db:
            office_soundtrack_table = db['office_soundtrack']
            await self.sender.sendMessage("\n".join(["{id}) {url}".format(**x) for x in office_soundtrack_table.all()]))
            await self.sender.sendMessage("Delete which entry?")
            answer = await self.listener.wait()
            is_deleted = office_soundtrack_table.delete(id=answer['text'])
            if is_deleted:
                await self.sender.sendMessage("Deleted.")
            else:
                await self.sender.sendMessage("No matching ID found, nothing deleted.")
