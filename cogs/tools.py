from discord.ext import commands
import youtube_dl
import discord
import datetime
import psutil
import hashlib

class Developers():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, hidden=True)
    async def reboot(self, ctx):
        """| Reboots the bot."""
        if ctx.message.author.id == self.bot.operator:
            await self.bot.say("```SubUnit\nRebooting <"+self.bot.user.name+"> : "+str(datetime.datetime.now())+"z```")
            await self.bot.close()


    @commands.command(pass_context=True, hidden=True, aliases=['eval'])
    async def evaluate(self, ctx, *, message: str = None):
        """| Evaluate"""
        if ctx.message.author.id == self.bot.operator:
            code = message
            await self.bot.say('```diff\n- '+code+'\n'+str(eval(code))+'```')
        else:
            return


    @commands.command(pass_context=True, hidden=True)
    async def reload(self, ctx, extension_name : str):
        """| Reloads an extension."""
        if ctx.message.author.id == self.bot.operator:
            self.bot.unload_extension(extension_name)
            try:
                self.bot.load_extension(extension_name)
            except (AttributeError, ImportError) as e:
                await self.bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                return
            await self.bot.say(f"```SubUnit\nReloaded <{extension_name}> : "+str(datetime.datetime.now())+"z```")
            print(f"reloaded: <{extension_name}>")


    @commands.command(pass_context=True, hidden=True)
    async def createinvite(self, ctx, channel):
        """| Creates an invite."""
        if ctx.message.author.id == self.bot.operator:
            server_channel = self.bot.get_channel(channel)
            invitelinknew = await self.bot.create_invite(server_channel, xkcd = True, max_uses = 1)
            await self.bot.say(invitelinknew)


    @commands.command(pass_context=True, hidden=True)
    async def unban(self, ctx, server, member: None):
        """| Reloads an extension."""
        if ctx.message.author.id == self.bot.operator:
            if member is None:
                member = ctx.message.author
            servers = self.bot.get_server(server)
            await self.bot.unban(servers, ctx.message.author)


    @commands.command(pass_context=True, hidden=True)
    async def kick(self, ctx, userName: discord.User):
        """| Kicks user."""
        if ctx.message.author.id == self.bot.operator:
            if userName != None:
                return await self.bot.kick(userName)
            else:
                return


    @commands.command(pass_context=True, hidden=True)
    async def clean(self, ctx, xlines):
        """| Cleans chat."""
        if ctx.message.author.id == self.bot.operator:
            return


def setup(bot):
    bot.add_cog(Developers(bot))
