import random
from discord.ext import commands
import discord
import json
import aiohttp
import urllib.request
import datetime

planetside_servers = ['BRIGGS', '25', 'JAEGER', '19', 'CONNERY', '1', 'MILLER', '10', 'EMERALD', '19', 'COLBALT', '13', '40', 'SOLTECH']

planetside_help_cmd = """```diff
- Planetside help prompt
+ Planetside help
+ Planetside servers
- Player Online Status
+ Planetside status <USERNAME>
- Player Character Stats
+ Planetside character <USERNAME>
- Server Population
+ Planetside population <SERVER>
- Server alert status
+ Planetside alert <SERVER>
- Brought to you by Talons Drunken Pirates! Consider >donating
+ https://discord.gg/tTbYxHE
```"""

class Games():
    def __init__(self, bot):
        self.bot = bot

### TODO ###
# CONVERT URLLIB REQUESTS TO AIOHTTP
# ADD MORE FUNCTIONALITY
# CLEAN UP CODE

# AIOHTTP EXAMPLE
#   async with aiohttp.ClientSession() as cs:
#       async with cs.get('http://random.cat/meow') as r:
#           res = await r.json()
#           await client.send_message(channel, res['file'])

    def WJSON(self, URL):
        seconds = 10
        try:
            output = json.loads(urllib.request.urlopen(URL, timeout=seconds).read().decode("utf8"))
        except urllib.error.URLError:
            return 'URLERROR'
        else:
            return output

    def ps2pop(self, message):
        world = "http://ps2.fisu.pw/api/population/?world"
        message = message.upper()
        if message == "BRIGGS" or message == "25":
            return self.WJSON(f"{world}=25")
        elif message == "CONNERY" or message == "1":
            return self.WJSON(f"{world}=1")
        elif message == "MILLER" or message == "10":
            return self.WJSON(f"{world}=10")
        elif message == "EMERALD" or message == "19":
            return self.WJSON(f"{world}=19")
        elif message == "COBALT" or message == "13":
            return self.WJSON(f"{world}=13")
        elif message == "JAEGER" or message == "19":
            return self.WJSON(f"{world}=19")
        elif message == "SOLTECH" or message == "40":
            return self.WJSON(f"{world}=40")
        else:
            return False


    @commands.command(pass_context=True, aliases=['planetside', 'ps2', 'PS2', 'Ps2', 'Planetside2', 'planetside2', 'ps'])
    @commands.cooldown(2, 1, commands.BucketType.default)
    async def Planetside(self, ctx, modify: str = None, *, message: str = None):
        """| Information module for Planetside2."""
        await self.bot.send_typing(ctx.message.channel)
        if modify == None or modify == "help":
            return await self.bot.say(f"{planetside_help_cmd}")
        else:
            if modify.upper() == "SERVERS":
                return await self.bot.say(f"```diff\n-{planetside_servers}```")

            elif modify.upper() == "ONLINE" and message != None:
                if ctx.message.author.id == self.bot.operator:
                    LOAD_PROMPT = await self.bot.say(f"Contacting DBG. Please wait!")
                    WEB_JSON = self.WJSON(f"http://census.daybreakgames.com/get/ps2:v2/characters_online_status/?character_name={message}")
                    return await self.bot.edit_message(LOAD_PROMPT, f"<{message}'s online status=<{WEB_JSON}>")

            elif modify.upper() == "POPULATION" or  modify.upper() == "POP":
                LOAD_PROMPT = await self.bot.say(f"Contacting Fisu. Please wait!")
                await self.bot.timed_delete(ctx.message, 64)
                await self.bot.timed_delete(LOAD_PROMPT, 64)
                if any(server in message.upper() for server in planetside_servers):
                    ps2 = self.ps2pop(message)
                    if ps2 == 'URLERROR':
                        return await self.bot.edit_message(LOAD_PROMPT, f'``Request timeout "ps2.fisu.pw"``')
                    ncpop = ps2['result'][0]['nc']; vspop = ps2['result'][0]['vs']; trpop = ps2['result'][0]['tr']
                    total = ncpop+vspop+trpop

                    if max(trpop, ncpop, vspop) == 0:
                        embedcolor = 0xc0c0c0
                        overpopfac = "Dead Server"
                    elif trpop == max(trpop, ncpop, vspop):
                        embedcolor = 0xa40000
                        overpopfac = "TR"
                    elif ncpop == max(trpop, ncpop, vspop):
                        embedcolor = 0x0080ff
                        overpopfac = "NC"
                    elif vspop == max(trpop, ncpop, vspop):
                        embedcolor = 0x740084
                        overpopfac = "VS"

                    ps2embed=discord.Embed(title=f'Planetside 2', color=embedcolor)
                    ps2embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/883060220779532288/zViSqVuM_400x400.jpg")
                    ps2embed.add_field(name=f'{message.upper()}', value=f'NC: {ncpop}\nVS: {vspop}\nTR: {trpop}', inline=True)
                    ps2embed.add_field(name='POPULATION', value=f'Total: {total}\nOP: {overpopfac}', inline=True)
                    ps2embed.set_footer(text=f"{datetime.datetime.utcnow()}")
                    await self.bot.edit_message(LOAD_PROMPT, f'``{ctx.message.author.name}``', embed=ps2embed)
                    return
                else:
                    await self.bot.edit_message(LOAD_PROMPT, f"Server not listed: '{message}'.")
                    return

            elif modify == "status" or modify == "Status":
                if message == None:
                    return await self.bot.say(f"<PLAYER CANNOT BE NONE>")
                else:
                    return await self.bot.say(f"<{message}'s Stats>")

            return await self.bot.say("<INSERT USEFULL CODE HERE>")



def setup(bot):
    bot.add_cog(Games(bot))
