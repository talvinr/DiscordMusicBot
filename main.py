import discord
from discord.exe import commands

import music

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup()

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

client.run("OTU5ODU0ODI1Mzc2NDY0OTY3.Ykh8dw.Jnwp7pLElBKqBgCWgUa2dCjA3J8")
