import random
from discord.ext import commands
import discord


class RNG():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['rollc'])
    async def RollC(self, dice : str):
        """| Rolls a dice in NdN format and prints in the classic style"""
        if len(dice) >= 100:
            await self.bot.say('Too much! try rolling less')
            return
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return
        rolldata = (str(random.randint(1, limit)) for r in range(rolls))
        result = ', '.join(rolldata)
        await self.bot.say(result)


    @commands.command(pass_context=True, aliases=['rolle'])
    async def RollE(self, ctx, dice : str):
        """| Rolls a dice in NdN format wrapped in an embed."""
        if len(dice) >= 100:
            await self.bot.say('Too much! try rolling less')
            return
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return
        evaldata = ' + '.join(str(random.randint(1, limit)) for r in range(rolls))
        total = eval(evaldata)
        dicevalue = evaldata.replace(' + ', ',')
        if len(dicevalue) >= 1000:
            dicevalue = 'Dice data exceeds 1000 character limit for embed fields!'
        rollembed=discord.Embed(title=f'{ctx.message.author.name} Rolled {dice}')
        rollembed.set_thumbnail(url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/emoji-one/104/game-die_1f3b2.png")
        rollembed.add_field(name='DICE', value=f"({dicevalue})", inline=True)
        rollembed.add_field(name='TOTAL', value=f'({total})', inline=True)
        await self.bot.say(f"{ctx.message.author.mention}", embed=rollembed)


    @commands.command(pass_context=True, aliases=['roll'])
    async def Roll(self, ctx, dice : str):
        """| Rolls a dice in NdN format."""
        if len(dice) >= 100:
            await self.bot.say('Too much! try rolling less')
            return
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return
        rolldata = (str(random.randint(1, limit)) for r in range(rolls))
        evaldata = ' + '.join(rolldata)
        total = eval(evaldata)
        await self.bot.say(f"``({evaldata.replace(' + ', ', ')})`` ``(TOTAL:{total})`` {ctx.message.author.mention}")


    @commands.command(description='For when you wanna settle the score some other way', aliases=['choose'])
    async def Choose(self, *choices : str):
        """| Chooses between multiple choices."""
        await self.bot.say(random.choice(choices))


def setup(bot):
    bot.add_cog(RNG(bot))
