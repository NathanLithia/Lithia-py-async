import discord
from discord.ext import commands
import youtube_dl

class Music():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def joinme(self, ctx, message: str = None):
        "join your channel"
        if message is None:
            channel = ctx.message.author.voice_channel
            await self.bot.join_voice_channel(channel)
        else:
            return

    @commands.command(pass_context=True, no_pm=True)
    async def leave(self, ctx, message: str = None):
        "leaves your voice channel"
        await self.bot.say("Attemping to leave, My Clients are: " + str(self.bot.voice_clients))
        for x in self.bot.voice_clients:
            if(x.server == ctx.message.server):
                await self.bot.say(str(x.server))
                return await x.disconnect()
        return

    @commands.command(pass_context=True, no_pm=True, description='For when you want to listen to some music.')
    async def play(self, ctx, url: str = None):
        "Plays music in your channel"
        if ctx.message.author.id == self.bot.data.operator:
            if url is None:
                return
            else:
                await self.bot.say("attempting to leave" + str(self.bot.voice_clients))
                for x in self.bot.voice_clients:
                  if(x.server == ctx.message.server):
                        await x.disconnect()
                channel = ctx.message.author.voice_channel
                vc = await self.bot.join_voice_channel(channel)
                player = await vc.create_ytdl_player(str(url))
                player.start()
            return
        else:
            return

def setup(bot):
    bot.add_cog(Music(bot))
