from discord.ext import commands
from discord import Member


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx):
        """Says what do you want"""
        await ctx.send(ctx.message.content.replace(self.bot.command_prefix + "say ", ""))