from dataclasses import dataclass
import discord
import re

E_MESSAGE_PATTERN = re.compile('\s*[eE]\s*')

class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.previous_notification = None

    async def on_ready(self):
        print(f'{self.user} connected to discord')

    async def on_message(self, message):
        if message.author.bot:
            return

        elif message.channel.id == 489891521341161473 and \
                message.author.id == 113417954699321344 and \
                'twitch.tv/leioslabs' in message.content:
            self.previous_notification = message.created_at

        elif E_MESSAGE_PATTERN.fullmatch(message.content):
            # TODO
            return
