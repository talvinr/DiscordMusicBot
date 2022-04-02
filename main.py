import discord
from discord.exe import commands

import music

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup()

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

client.run("")
