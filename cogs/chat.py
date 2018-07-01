from discord.ext import commands
import discord
import datetime

class Chat():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """pong!"""
       # def pingdiscord():
       #     import os
       #     ping = os.popen('ping gateway.discord.gg -n 1')
       #     result = ping.readlines()
       #     return str(result[2]).split('time=', 1)[-1].split(' TTL=', 1)[0]
       # #pingms = str((datetime.datetime.utcnow()-ctx.message.timestamp).microseconds/1000)
        usermention = '<@'+ctx.message.author.id+'>'
       # await self.bot.say(usermention+" "+pingdiscord())
        await self.bot.say(usermention+" Pong!")


    @commands.command(pass_context=True, hidden=True)
    async def pong(self, ctx):
        """ping!"""
        usermention = '<@'+ctx.message.author.id+'>'
        await self.bot.say(usermention+" Ping!")


    @commands.command(pass_context=True)
    async def say(self, ctx, message: str = None):
        """repeats inputs!"""
        await self.bot.say(str(ctx.message.content).split('say', 1)[1])
        await self.bot.delete_message(ctx.message)


    @commands.command(pass_context=True, hidden=True, aliases=['commands'])
    async def commandhelper(self, ctx):
        """Redirect message for people listening to bot status"""
        user = '<@'+ctx.message.author.id+'>'
        await self.bot.say("%s You can view my commands with >help" % user)


    @commands.command(pass_context=True, hidden=True)
    async def pat(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        await self.bot.say("pat pat, "+str(member.mention))

    @commands.command(pass_context=True, hidden=True)
    async def punch(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        await self.bot.say("***punches***, "+str(member.mention))


def setup(bot):
    bot.add_cog(Chat(bot))