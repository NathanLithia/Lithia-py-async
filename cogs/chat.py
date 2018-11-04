from discord.ext import commands
import discord
import datetime

class Chat():
    def __init__(self, bot):
        self.bot = bot


    def pingdiscord(self): #WINDOWS BASED PING #await self.bot.say(f"{ctx.message.author.mention} "+self.pingdiscord()) 
        import os
        ping = os.popen('ping gateway.discord.gg -n 1')
        result = ping.readlines()
        return str(result[2]).split('time=', 1)[-1].split(' TTL=', 1)[0]
        #return pingms = str((datetime.datetime.utcnow()-message.timestamp).microseconds/1000) #LEGACY PING


    @commands.command(pass_context=True, aliases=['ping'])
    async def Ping(self, ctx):
        """| Pong!"""
        await self.bot.say(f"{ctx.message.author.mention} Pong!")


    @commands.command(pass_context=True, hidden=True, aliases=['pong'])
    async def Pong(self, ctx):
        """| Ping!"""
        await self.bot.say(f"{ctx.message.author.mention} Ping!")


    @commands.command(pass_context=True, aliases=['say'])
    async def Say(self, ctx, message: str = None):
        """| Repeats input."""
        await self.bot.delete_message(ctx.message)
        await self.bot.say(str(ctx.message.content).split('say', 1)[1])

    @commands.command(pass_context=True, aliases=['yell'])
    async def Yell(self, ctx, message: str = None):
        """| Repeats input in TTS."""
        await self.bot.send_message(ctx.message.channel, message, tts=True)

    @commands.command(pass_context=True, hidden=True, aliases=['commands'])
    async def commandhelper(self, ctx):
        """| Redirect message for people listening to bot status"""
        await self.bot.say(f"{ctx.message.author.mention} You can view my commands with >help")


    @commands.command(pass_context=True, hidden=True)
    async def pat(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        await self.bot.say(f"pat pat, {member.mention}")


    @commands.command(pass_context=True, hidden=True)
    async def punch(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        await self.bot.say(f"***punches*** {member.mention}")


def setup(bot):
    bot.add_cog(Chat(bot))