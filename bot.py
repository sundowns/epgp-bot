
import os
import discord
import commands
from dotenv import load_dotenv

# CONFIG
load_dotenv()
PREFIX = os.getenv('DISCORD_PREFIX', default='!')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord. Prefix is \'{PREFIX}\'')
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith(f"{PREFIX}epgp"):
        response = commands.handle_message(message.content)
        if response:
            await message.channel.send(response)


client.run(TOKEN)