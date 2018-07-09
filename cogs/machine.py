from discord.ext import commands
import psutil
import datetime

class System():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, hidden=True)
    async def battery(self, ctx):
        """| Outputs system temperatures"""
        if ctx.message.author.id == self.bot.operator:
            await self.bot.say(str(psutil.sensors_battery()))


    @commands.command(pass_context=True, hidden=True)
    async def temps(self, ctx):
        """| Outputs system temperatures"""
        if ctx.message.author.id == self.bot.operator:
            await self.bot.say(str(psutil.sensors_temperatures()))


def setup(bot):
    bot.add_cog(System(bot))
