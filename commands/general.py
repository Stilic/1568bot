from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Gets the bot's latency"""
        await ctx.send("Pong!\nLatency (in ms): {0}".format(round(self.bot.latency, 1)))