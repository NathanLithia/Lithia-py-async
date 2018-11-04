from discord.ext import commands
import discord

class Info():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, aliases=['pfp', 'upic'])
    async def UPic(self, ctx, member: discord.Member = None):
        """Prints user display image"""
        if member is None:
            member = ctx.message.author
        pfpembed=discord.Embed(title=member.name)
        pfpembed.set_image(url=member.avatar_url)
        await self.bot.send_message(ctx.message.channel, embed=pfpembed)


    @commands.command(pass_context=True, aliases=['uinfo'])
    async def UInfo(self, ctx, member: discord.Member = None):
        """Prints user info"""
        if member is None:
            member = ctx.message.author
        stats = f"""
        Joined: {member.joined_at}
        Created: {member.created_at}
        Status: {member.status}
        Playing: {member.game}
        Nick: {member.nick}
        Name: {member.name}
        ID: {member.id}
        Bot: {member.bot}
        Discriminator: {member.discriminator}
        Top_role: {member.top_role}
        """
        usrembed=discord.Embed(title='User Information')
        usrembed.set_thumbnail(url=member.avatar_url)
        usrembed.add_field(name='USER STATS', value=stats, inline=True)
        await self.bot.send_message(ctx.message.channel, embed=usrembed)

    @commands.command(pass_context=True, aliases=['spic'])
    async def SPic(self, ctx):
        """Prints server display image"""
        srvembed=discord.Embed(title=ctx.message.server.name)
        srvembed.set_image(url=ctx.message.server.icon_url)
        await self.bot.send_message(ctx.message.channel, embed=srvembed)


    @commands.command(pass_context=True, aliases=['sinfo'])
    async def SInfo(self, ctx):
        """Prints server info"""
        stats = f"""
        Name: {ctx.message.server.name}
        Owner: {ctx.message.server.owner}
        Member_count: {ctx.message.server.member_count}
        Created_at: {ctx.message.server.created_at}
        ID: {ctx.message.server.id}
        Region: {ctx.message.server.region}
        Default_channel: {ctx.message.server.default_channel}
        Afk_channel: {ctx.message.server.afk_channel}
        Afk_timeout: {ctx.message.server.afk_timeout}
        """
        srvembed=discord.Embed(title='Server Information')
        srvembed.set_thumbnail(url=ctx.message.server.icon_url)
        srvembed.add_field(name='SERVER STATS', value=stats, inline=True)
        await self.bot.send_message(ctx.message.channel, embed=srvembed)


def setup(bot):
    bot.add_cog(Info(bot))