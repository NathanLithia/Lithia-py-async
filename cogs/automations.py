from discord.ext import commands
import asyncio
import discord

### TODO ##
# Automatic Status change showing help, guilds, website etc
# Automatic JSON Database scrape??? every few months???
# Automatic Reboot??? (remake of wrapper required for this)

class AUTOMATIONS():
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(AUTOMATIONS(bot))
