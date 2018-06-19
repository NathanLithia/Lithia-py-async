from discord.ext import commands
import datetime
operator = "175182469656477696"

class Developers():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def reboot(self, ctx):
        """Reboots the bot."""
        if ctx.message.author.id == operator:
            await self.bot.say("```SubUnit\nRebooting <"+self.bot.user.name+"> : "+str(datetime.datetime.now())+"z```")
            await self.bot.close()

    @commands.command(pass_context=True, no_pm=False, hidden=True, aliases=['eval'])
    async def evaluate(self, ctx, *, message: str = None):
        """Evaluate"""
        if ctx.message.author.id == operator:
            code = message
            await self.bot.say('```diff\n- '+code+'\n'+str(eval(code))+'```')
        else:
            return

    @commands.command(pass_context=True)
    async def reload(self, ctx, extension_name : str):
        """Reloads an extension."""
        if ctx.message.author.id == operator:
            self.bot.unload_extension(extension_name)
            try:
                self.bot.load_extension(extension_name)
            except (AttributeError, ImportError) as e:
                await self.bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                return
            await self.bot.say("```SubUnit\nReloaded <{}> : ".format(extension_name)+str(datetime.datetime.now())+"z```")

def setup(bot):
    bot.add_cog(Developers(bot))
