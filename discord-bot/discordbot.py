import discord
from discord.ext import commands

TOKEN = 'NzYxMzUyMDM5MDY5NjQ2OTE5.X3ZWVw.oV6qkvnUB9g5r3_WWZJX3Xp7AtY'  # Bot token available at Discord's dev portal
prefix = '!'

bot = commands.Bot(command_prefix=prefix)


@bot.command()
async def connect(ctx):
    try:
        user_channel = ctx.author.voice.channel
    except AttributeError:
        return await ctx.send("You are not in a voice channel!")
    except:
        return await ctx.send("An error has occurred when connecting to voice.")

    bot_voice = ctx.voice_client
    if not bot_voice:
        await user_channel.connect()
    elif bot_voice.channel != user_channel:
        await bot_voice.disconnect()
        await user_channel.connect()


@bot.command()
async def disconnect(ctx):
    bot_voice = ctx.voice_client
    if bot_voice:
        await bot_voice.disconnect()


bot.run(TOKEN)