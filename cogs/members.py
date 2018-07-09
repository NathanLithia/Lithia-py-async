import discord
from discord.ext import commands

class Members():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['joined'])
    async def Joined(self, member : discord.Member):
        """| Says when a member joined."""
        await self.bot.say('{0.name} joined in {0.joined_at}'.format(member))


    @commands.command(pass_context=True, aliases=['bot'])
    async def Bot(self, ctx, member: discord.Member = None):
        """| Checks if a user is a bots."""
        if member is None:
            member = ctx.message.author
        return await self.bot.say(str(member.bot))


def setup(bot):
    bot.add_cog(Members(bot))
