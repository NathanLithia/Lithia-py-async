from discord.ext import commands
import datetime

class Chat():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """pong!"""
        pingms = str((datetime.datetime.utcnow()-ctx.message.timestamp).microseconds/1000)
        usermention = '<@'+ctx.message.author.id+'>'
        await self.bot.say(usermention+" "+pingms+'ms')

    @commands.command(pass_context=True, hidden=True)
    async def commands(self, ctx):
        """Redirect message for people listening to bot status"""
        user = '<@'+ctx.message.author.id+'>'
        await self.bot.say("%s You can view my commands with >help" % user)

def setup(bot):
    bot.add_cog(Chat(bot))