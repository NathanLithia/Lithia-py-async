import discord
from discord.ext import commands
import youtube_dl
import datetime
import psutil
import hashlib
import ast

class Developers():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, hidden=True)
    async def reboot(self, ctx):
        """| Reboots the bot."""
        if ctx.message.author.id == self.bot.operator:
            await self.bot.say("```SubUnit\nRebooting <"+self.bot.user.name+"> : "+str(datetime.datetime.now())+"z```")
            await self.bot.close()


    @commands.command(pass_context=True, hidden=True, aliases=['eval'])
    async def evaluate(self, ctx, *, message: str = None):
        """| Evaluate"""
        if ctx.message.author.id == self.bot.operator:
            code = message
            await self.bot.say('```diff\n- '+code+'\n'+str(eval(code))+'```')
        else:
            return


    @commands.command(pass_context=True, hidden=True)
    async def reload(self, ctx, extension_name : str):
        """| Reloads an extension."""
        if ctx.message.author.id == self.bot.operator:
            self.bot.unload_extension(extension_name)
            try:
                self.bot.load_extension(extension_name)
            except (AttributeError, ImportError) as e:
                await self.bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                return
            await self.bot.say(f"```SubUnit\nReloaded <{extension_name}> : "+str(datetime.datetime.now())+"z```")
            print(f"reloaded: <{extension_name}>")


    @commands.command(pass_context=True, hidden=True)
    async def createinvite(self, ctx, channel):
        """| Creates an invite."""
        if ctx.message.author.id == self.bot.operator:
            server_channel = self.bot.get_channel(channel)
            invitelinknew = await self.bot.create_invite(server_channel, xkcd = True, max_uses = 1)
            await self.bot.say(invitelinknew)


    @commands.command(pass_context=True, hidden=True)
    async def unban(self, ctx, server, member: None):
        """| Reloads an extension."""
        if ctx.message.author.id == self.bot.operator:
            if member is None:
                member = ctx.message.author
            servers = self.bot.get_server(server)
            await self.bot.unban(servers, ctx.message.author)


    @commands.command(pass_context=True, hidden=True)
    async def kick(self, ctx, userName: discord.User):
        """| Kicks user."""
        if ctx.message.author.id == self.bot.operator:
            if userName != None:
                return await self.bot.kick(userName)
            else:
                return


    @commands.command(pass_context=True, hidden=True)
    async def clean(self, ctx, xlines: int): #purge_from(channel, *, limit=100, check=None, before=None, after=None, around=None)
        """| Cleans chat."""
        if ctx.message.author.id == self.bot.operator:
            print(xlines)
            self.bot.purge_from(ctx.message.channel, limit=xlines)
            return


    @commands.command(pass_context=True, no_pm=True, hidden=True)
    async def appen(self, ctx, message: str = None):
        """Debug."""
        if ctx.message.author.id == self.bot.operator:
            role = discord.utils.get(ctx.message.server.roles, name=message)
            return await self.bot.add_roles(ctx.message.author, role)


    @commands.command(pass_context=True, no_pm=True, hidden=True)
    async def remov(self, ctx, message: str = None):
        """Debug."""
        if ctx.message.author.id == self.bot.operator:
            role = discord.utils.get(ctx.message.server.roles, name=message)
            return await self.bot.remove_roles(ctx.message.author, role)


    def insert_returns(self, body):
        # insert return stmt if the last expression is a expression statement
        if isinstance(body[-1], ast.Expr):
            body[-1] = ast.Return(body[-1].value)
            ast.fix_missing_locations(body[-1])
        # for if statements, we insert returns into the body and the orelse
        if isinstance(body[-1], ast.If):
            self.insert_returns(body[-1].body)
            self.insert_returns(body[-1].orelse)
        # for with blocks, again we insert returns into the body
        if isinstance(body[-1], ast.With):
            self.insert_returns(body[-1].body)


    @commands.command(pass_context=True, no_pm=True, hidden=True)
    async def eval_fn(self, ctx, *, cmd):
        """Evaluates input.
        Input is interpreted as newline seperated statements.
        If the last statement is an expression, that is the return value.
        Usable globals:
        - `bot`: the bot instance
        - `discord`: the discord module
        - `commands`: the discord.ext.commands module
        - `ctx`: the invokation context
        - `__import__`: the builtin `__import__` function
        Such that `>eval 1 + 1` gives `2` as the result.
        The following invokation will cause the bot to send the text '9'
        to the channel of invokation and return '3' as the result of evaluating
        >eval ```
        a = 1 + 2
        b = a * 2
        await ctx.send(a + b)
        a
        ```
        """
        if ctx.message.author.id == self.bot.operator:
            fn_name = "_eval_expr"
            cmd = cmd.strip("` ")
            # add a layer of indentation
            cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
            # wrap in async def body
            body = f"async def {fn_name}():\n{cmd}"
            parsed = ast.parse(body)
            body = parsed.body[0].body
            self.insert_returns(body)
            env = {
                'bot': self.bot,
                'discord': discord,
                'commands': commands,
                'ctx': ctx,
                '__import__': __import__
            }
            exec(compile(parsed, filename="<ast>", mode="exec"), env)
            result = (await eval(f"{fn_name}()", env))
            await self.bot.say(result)


def setup(bot):
    bot.add_cog(Developers(bot))
