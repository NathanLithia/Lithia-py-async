from discord.ext import commands
import asyncio



class AUTOMATIONS():
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(AUTOMATIONS(bot))
