
import os
import discord
from dotenv import load_dotenv

# CONFIG
load_dotenv()
PREFIX = os.getenv('DISCORD_PREFIX', default='!')
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)