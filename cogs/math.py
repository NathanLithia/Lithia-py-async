import discord
from discord.ext import commands
import base64
import hashlib
from tabulate import tabulate # pip install tabulate

HASH_TYPES = ['SHA1', 'SHA256', 'MD5']
FORMAT_TYPES = ['TABLE']
ENCODE_TYPES = ['BASE85', 'BASE64', 'BASE32', 'BASE16']
DECODE_TYPES = [] + ENCODE_TYPES

#https://stackoverflow.com/questions/17166074/most-efficient-way-of-making-an-if-elif-elif-else-statement-when-the-else-is-don

class Maths():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, no_pm=False, aliases=['form', 'format'])
    async def Format(self, ctx, TYPE: str = None, *, INPUT: str = None):
        if TYPE == "TABLE":
            await self.bot.say(f"{INPUT}")
            print(tabulate(INPUT))
            await self.bot.say(f"{type(INPUT)}")
        else:
            await self.bot.say(f"the method '{TYPE}' is not available, see {self.bot.prefix}Format types") 


    @commands.command(pass_context=True, no_pm=False, description='Base Encoder, Usage: ', aliases=['be', 'baseencode', 'encode'])
    async def Encode(self, ctx, TYPE: str = None, *, INPUT: str = None):
        """| Encodes inputs into a variety of formats """
        if TYPE == "BASE85":
            await self.bot.say(str(base64.b85encode(bytes(INPUT, 'utf-8')))[2:-1])
        elif TYPE == "BASE64":
            await self.bot.say(str(base64.b64encode(bytes(INPUT, 'utf-8')))[2:-1])
        elif TYPE == "BASE32":
            await self.bot.say(str(base64.b32encode(bytes(INPUT, 'utf-8')))[2:-1])
        elif TYPE == "BASE16":
            await self.bot.say(str(base64.b16encode(bytes(INPUT, 'utf-8')))[2:-1])
        elif TYPE == "types":
            await self.bot.say(f"Encoding types: {FORMAT_TYPES}")
        else:
            await self.bot.say(f"the method '{TYPE}' is not available, see {self.bot.prefix}Encode types") 


    @commands.command(pass_context=True, description='Base Decoder, Usage: ', aliases=['bd', 'basedecode', 'decode'])
    async def Decode(self, ctx, TYPE: str = None, *, INPUT: str = None):
        """| Decodes a variety of inputs"""
        if TYPE == "BASE85":
            await self.bot.say(str(base64.b85decode(bytes(INPUT, 'utf-8')))[2:-1])
        elif TYPE == "BASE64":
            await self.bot.say(str(base64.b64decode(bytes(INPUT, 'utf-8')))[2:-1])
        elif TYPE == "BASE32":
            await self.bot.say(str(base64.b32decode(bytes(INPUT, 'utf-8')))[2:-1])
        elif TYPE == "BASE16":
            await self.bot.say(str(base64.b16decode(bytes(INPUT, 'utf-8')))[2:-1])
        elif TYPE == "types":
            await self.bot.say(f"Decoding types: {DECODE_TYPES}")
        else:
            await self.bot.say(f"the method '{TYPE}' is not available, see {self.bot.prefix}Decode types")


    @commands.command(pass_context=True, no_pm=False, description='Base Hasher, Usage: ', aliases=['hash', 'hsh'])
    async def Hash(self, ctx, TYPE: str = None, *, INPUT: str = None):
        """| Hashes inputs into a variety of formats """
        if TYPE == "MD5":
            await self.bot.say(str(hashlib.md5(bytes(INPUT, 'utf-8')).hexdigest()))
        elif TYPE == "SHA256":
            await self.bot.say(str(hashlib.sha256(bytes(INPUT, 'utf-8')).hexdigest()))
        elif TYPE == "SHA1":
            await self.bot.say(str(hashlib.sha1(bytes(INPUT, 'utf-8')).hexdigest()))
        elif TYPE == "types":
            await self.bot.say(f"Hashing types: {HASH_TYPES}")
        else:
            await self.bot.say(f"the method '{TYPE}' is not available, see {self.bot.prefix}Hash types")


    @commands.command(pass_context=True, no_pm=False, description='Embedded Calculator, try >calculate 5*5 bop', aliases=['calculate', 'compute', 'calc'])
    async def Calc(self, ctx, *, message: str = None):
        """| Commit mathematical calculations."""
        mathswhitelist=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')', '(', '-', '=', '+', '/', '<', '>', '*', '.', ' ', '^', '!', '~', '&', '|', '%', ','] # https://stackoverflow.com/a/46799212
        if message == None:
            return await self.bot.say(f"{self.bot.prefix}calc 13.411/4.267```diff\n- 13.411/4.267\n+ 3.14295758143895```")
        if any(x not in mathswhitelist for x in message):
            return await self.bot.say("Error. Illigal Expression.")
        else:
            try:
                calculation = str('```diff\n- '+str(message)+'\n+ '+str(eval(message))+'```')
            except OverflowError:
                return await self.bot.say("Error. Overflow error.")
            except SyntaxError:
                return await self.bot.say("Error. Syntax error.")
            except ZeroDivisionError:
                return await self.bot.say("Error. Cannot divide by zero.")
            except TypeError:
                return await self.bot.say("Error. TypeError")
            if len(calculation) > 2000:
                return await self.bot.say("Error. Calculation Exceeds 2000 Characters.")
            else:
                await self.bot.say(calculation)


def setup(bot):
    bot.add_cog(Maths(bot))