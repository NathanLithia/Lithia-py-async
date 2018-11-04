from discord.ext import commands
import asyncio



class ERROR_HANDLER():
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, error, ctx):
        if isinstance(error, commands.BadArgument):
            await self.bot.timed_message(ctx.message.channel, f"```diff\n- Bad Argument: {error}\n\n+ For more information see {self.bot.prefix}errorhelp```")
            await self.bot.delete_message(ctx.message)
        if isinstance(error, commands.MissingRequiredArgument):
            await self.bot.timed_message(ctx.message.channel, f"```diff\n- Missing Required Argument: {error}\n+ For more information see {self.bot.prefix}errorhelp```")
            await self.bot.delete_message(ctx.message)
        if isinstance(error, commands.CommandOnCooldown):
            await self.bot.timed_message(ctx.message.channel, f"{ctx.message.author.mention}!```diff\n- Either a global command or {error}\n+ For more information see {self.bot.prefix}errorhelp```")
            await self.bot.delete_message(ctx.message)
        if isinstance(error, commands.CommandNotFound):
            if ctx.message.content.startswith( self.bot.user.mention ) == True or ctx.message.content.startswith( "<@!"+self.bot.user.id+">" ) == True:
                if ctx.message.content.startswith( self.bot.user.mention ) == True:
                    response = str(self.bot.brain.respond(str(ctx.message.content).lstrip(str(self.bot.user.mention))))
                else:
                    response = str(self.bot.brain.respond(str(ctx.message.content).lstrip(str("<@!"+self.bot.user.id+">"))))
                if response ==  "":
                    response = f"{ctx.message.author.mention} Sorry, i dont understand that at the moment."
                await self.bot.send_message(ctx.message.channel, response)
        else:
            print(f"{error}")


    @commands.command(pass_context=True, no_pm=True, hidden=True)
    async def errorhelp(self, ctx, message: str = None):
        """A handler to help people with less programming knowledge"""

        response = f"```diff\n- Oh no! Lithia has outputted an error!\n+ Not to fear! this usually means a little bit of code is still being worked on but you can report the issue at lithia's github\n+ you can find lithia's github at https://github.com/nathanlol5/Lithia-AIML\n```"

        await self.bot.send_message(ctx.message.channel, response)
        return


def setup(bot):
    bot.add_cog(ERROR_HANDLER(bot))
