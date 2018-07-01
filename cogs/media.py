from discord.ext import commands
import discord

class Profile():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def pic(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        await self.bot.send_message(ctx.message.channel, member.avatar_url)


def setup(bot):
    bot.add_cog(Profile(bot))