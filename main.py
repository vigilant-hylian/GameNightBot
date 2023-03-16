import os
import discord
from datetime import *
from datetime import timedelta
from dotenv import load_dotenv

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(TOKEN)

# now = datetime.now()
# game = datetime(2023, 3, 22, 14, 30)

# print(now)
# print(game)
# print(now+timedelta(days=28))