from discord.ext.commands.core import command
from config import CONFIG
from discord.ext import commands
from discord import Member, Embed, Color
from commands import general, fun

try:
    prefix = CONFIG["prefix"]
except KeyError:
    prefix = "se!"

bot = commands.Bot(command_prefix=prefix, help_command=None)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

class help(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = Embed(color=Color.blurple(), description="")
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

bot.help_command = help()
bot.add_cog(general.General(bot))
bot.add_cog(fun.Fun(bot))
bot.run(CONFIG["discord_token"])
