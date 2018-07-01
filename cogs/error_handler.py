from discord.ext import commands



class ERROR_HANDLER():
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, error, ctx):

        if isinstance(error, commands.BadArgument):
            await self.bot.send_message(ctx.message.channel, 'BadArgument')

        if isinstance(error, commands.MissingRequiredArgument):
            await self.bot.send_message(ctx.message.channel, 'MissingRequiredArgument')

        if isinstance(error, commands.CommandNotFound):
            if ctx.message.content.startswith( self.bot.user.mention ) == True or ctx.message.content.startswith( "<@!"+self.bot.user.id+">" ) == True:

                if ctx.message.content.startswith( self.bot.user.mention ) == True:
                    response = str(self.bot.brain.respond(str(ctx.message.content).lstrip(str(self.bot.user.mention))))
                else:
                    response = str(self.bot.brain.respond(str(ctx.message.content).lstrip(str("<@!"+self.bot.user.id+">"))))
                    
                if response ==  "":
                    response = f"{ctx.message.author.mention}That is a little too abstract for me to process at this time."
                await self.bot.send_message(ctx.message.channel, response)
            return

        #if isinstance(error, commands.errors.)
        #    return

def setup(bot):
    bot.add_cog(ERROR_HANDLER(bot))
