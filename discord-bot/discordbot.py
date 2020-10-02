import discord
from discord.ext import commands
import importlib

# Using importlib since other bot directory names contained a '-' and I've done so too to follow suit
general_cog = getattr(importlib.import_module('discord-bot.cogs.GeneralCommands'), 'GeneralCog')

TOKEN = 'NzYxMzUyMDM5MDY5NjQ2OTE5.X3ZWVw.1n94g_HfhBUuna_-GatdfBfHl5c'  # Bot token available at Discord's dev portal
prefix = '!'

bot = commands.Bot(command_prefix=prefix)


def setup(bot):
    bot.add_cog(general_cog(bot))


setup(bot)
bot.run(TOKEN)
