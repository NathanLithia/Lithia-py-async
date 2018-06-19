from discord.ext import commands

class ERROR_HANDLER():
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, error, ctx):
        if isinstance(error, commands.BadArgument):
            await self.bot.say('BadArgument')
        if isinstance(error, commands.MissingRequiredArgument):
            await self.bot.say('MissingRequiredArgument')
        if isinstance(error, commands.CommandNotFound):
            return
        #if isinstance(error, commands.errors.)
        #    return




def setup(bot):
    bot.add_cog(ERROR_HANDLER(bot))
