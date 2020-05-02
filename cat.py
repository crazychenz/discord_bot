import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        if message.content == '!uptime':
            await message.channel.send('¯\_(ツ)_/¯')

client = MyClient()
client.run(TOKEN)
