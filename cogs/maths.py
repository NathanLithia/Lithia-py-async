import discord
from discord.ext import commands
import base64
import hashlib

HASH_TYPES = ['SHA1', 'SHA256', 'MD5']
ENCODE_TYPES = ['BASE85', 'BASE64', 'BASE32', 'BASE16']
DECODE_TYPES = ['BASE85', 'BASE64', 'BASE32', 'BASE16']

###                                                                               ###
### i can see you and yes the method for detecting input will be changed SOOOOOON ###
###                                                                               ###

class Maths():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, no_pm=False, description='Base Encoder, Usage: ', aliases=['be', 'baseencode', 'encode'])
    async def Encode(self, ctx, TYPE: str = None, *, INPUT: str = None):
        """| Encodes inputs into a variety of formats """
        if TYPE == "BASE85":
            return await self.bot.say(str(base64.b85encode(bytes(INPUT, 'utf-8')))[2:-1])
        if TYPE == "BASE64":
            return await self.bot.say(str(base64.b64encode(bytes(INPUT, 'utf-8')))[2:-1])
        if TYPE == "BASE32":
            return await self.bot.say(str(base64.b32encode(bytes(INPUT, 'utf-8')))[2:-1])
        if TYPE == "BASE16":
            return await self.bot.say(str(base64.b16encode(bytes(INPUT, 'utf-8')))[2:-1])
        if TYPE == "types":
            return await self.bot.say(f"Encoding types: {ENCODE_TYPES}")
        else:
            return await self.bot.say(f"the method '{TYPE}' is not available, see {self.bot.prefix}encode types")
        return 


    @commands.command(pass_context=True, description='Base Decoder, Usage: ', aliases=['bd', 'basedecode', 'decode'])
    async def Decode(self, ctx, TYPE: str = None, *, INPUT: str = None):
        """| Decodes a variety of inputs"""
        if TYPE == "BASE85":
            return await self.bot.say(str(base64.b85decode(bytes(INPUT, 'utf-8')))[2:-1])
        if TYPE == "BASE64":
            return await self.bot.say(str(base64.b64decode(bytes(INPUT, 'utf-8')))[2:-1])
        if TYPE == "BASE32":
            return await self.bot.say(str(base64.b32decode(bytes(INPUT, 'utf-8')))[2:-1])
        if TYPE == "BASE16":
            return await self.bot.say(str(base64.b16decode(bytes(INPUT, 'utf-8')))[2:-1])
        if TYPE == "types":
            return await self.bot.say(f"Decoding types: {DECODE_TYPES}")
        else:
            return await self.bot.say(f"the method '{TYPE}' is not available, see {self.bot.prefix}decode types")
        return

    @commands.command(pass_context=True, no_pm=False, description='Base Hasher, Usage: ', aliases=['hash', 'hsh'])
    async def Hash(self, ctx, TYPE: str = None, *, INPUT: str = None):
        """| Encodes inputs into a variety of formats """
        if TYPE == "MD5":
            return await self.bot.say(str(hashlib.md5(bytes(INPUT, 'utf-8')).hexdigest()))
        if TYPE == "SHA256":
            return await self.bot.say(str(hashlib.sha256(bytes(INPUT, 'utf-8')).hexdigest()))
        if TYPE == "SHA1":
            return await self.bot.say(str(hashlib.sha1(bytes(INPUT, 'utf-8')).hexdigest()))
        if TYPE == "types":
            return await self.bot.say(f"Hashing types: {HASH_TYPES}")
        else:
            return await self.bot.say(f"the method '{TYPE}' is not available, see {self.bot.prefix}Hash types")
        return 


    @commands.command(pass_context=True, no_pm=False, description='Embedded Calculator, try >calculate 5*5 bop', aliases=['calculate', 'compute', 'calc'])
    async def Calc(self, ctx, *, message: str = None):
        """| Commit mathematical calculations."""
        mathswhitelist=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')', '(', '-', '=', '+', '/', '<', '>', '*', '.', ' ', '^', '!', '~', '&', '|', '%', ','] # https://stackoverflow.com/a/46799212
        if message == None:
            await self.bot.say(f"{self.bot.prefix}calc 13.411/4.267```diff\n- 13.411/4.267\n+ 3.14295758143895```")
            return
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