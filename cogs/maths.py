import discord
from discord.ext import commands

class Maths():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=False, description='Embedded Calculator, try >calculate 5*5', aliases=['calculate', 'compute'])
    async def calc(self, ctx, *, message: str = None):
        """Commit mathematical calculations."""
        mathswhitelist=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')', '(', '-', '=', '+', '/', '<', '>', '*', '.', ' ', '^', '!', '~', '&', '|', '%', ','] # https://stackoverflow.com/a/46799212
        await self.bot.send_typing(ctx.message.channel)
        if any(x not in mathswhitelist for x in message):
            await self.bot.say("Error. InvalidExpression.")
        else:
            try:
                calculation = str('```diff\n- '+str(message)+'\n+ '+str(eval(message))+'```')
            except OverflowError:
                return await self.bot.say("Error. Overflow error.")
            except SyntaxError:
                return await self.bot.say("Error. Syntax error.")
            except ZeroDivisionError:
                return await self.bot.say("Error. Cannot divide by zero.")
            if len(calculation) > 2000:
                return await self.bot.say("Error. Calculation Exceeds 2000 Characters.")
            else:
                await self.bot.say(calculation)

def setup(bot):
    bot.add_cog(Maths(bot))