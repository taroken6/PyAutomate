import discord
from discord.ext import commands


class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('!help'))

    @commands.command()
    async def connect(self, ctx):
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

    @commands.command()
    async def disconnect(self, ctx):
        bot_voice = ctx.voice_client
        if bot_voice:
            await bot_voice.disconnect()
