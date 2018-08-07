# -*- coding: utf-8 -*-

from rtmbot import RtmBot
from rtmbot.core import Plugin
import random

import secret

class HelloPlugin(Plugin):
    def process_message(self, data):
        results = ['🐕 🐕 🐕', '회고했댕?', '산책 좋아요', '간식주라 간식!']

        if '댕댕' in data['text']:
            num = random.randrange(0,3)
            self.outputs.append([data['channel'], results[num]])


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}

bot = RtmBot(config)
bot.start()
