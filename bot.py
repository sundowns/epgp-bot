
import os
import discord
import commands
from dotenv import load_dotenv

# CONFIG
load_dotenv()
PREFIX_CHAR = os.getenv('DISCORD_PREFIX', default='!')
TOKEN = os.getenv('DISCORD_TOKEN', default='')
GUILD = os.getenv('DISCORD_GUILD')
EPGP_LOGS_CHANNEL = os.getenv(
    'EPGP_LOGS_CHANNEL', default='epgp-standings-log')

PREFIX = f"{PREFIX_CHAR}epgp"

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

    if message.channel.name == EPGP_LOGS_CHANNEL and message.attachments:
        await commands.handle_fileupload(message.attachments[0])
    elif message.content.lower().startswith(PREFIX):
        response = commands.handle_message(message.content, prefix=PREFIX)
        if response:
            await message.channel.send(response)


client.run(TOKEN)
