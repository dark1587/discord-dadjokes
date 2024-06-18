import requests

from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='dadjoke', help='Responds with a random dadjoke.')
async def dadjoke(ctx):
    query = "https://feck.ing/jokes"
    response = requests.get(query)
    output = response.json()['joke']

    await ctx.send(output)

bot.run(TOKEN)
