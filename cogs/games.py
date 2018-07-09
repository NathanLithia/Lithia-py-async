import random
from discord.ext import commands
import json
import aiohttp
import urllib.request

planetside_servers = ['BRIGGS', '25', 'JAEGER',  '19', 'CONNERY', '1', 'MILLER',  '10', 'EMERALD', '19', 'COLBALT', '13']

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

warframe_help_cmd = """```diff
- Warframe help prompt
+ Warframe help

- Query item information
+ Warframe item <ITEM>

- Query item "Selling" orders
+ Warframe selling <ITEM>

- Query item "Buying" orders
+ Warframe buying <ITEM>

- Join Talons Drunken Pirates! Consider >donating
+ https://discord.gg/tTbYxHE
```"""

def WJSON(WEB_URL):
    WEB_DATA = urllib.request.urlopen(WEB_URL)
    WEB_BYTES = WEB_DATA.read()
    WEB_JSON = WEB_BYTES.decode("utf8")
    #WEB_BYTES.close()
    return WEB_JSON

class Games():
    def __init__(self, bot):
        self.bot = bot

### TODO ###
# ADD MORE FUNCTIONALITY
# USE A JSON PARSER
# CLEAN UP CODE

#https://Waframe.market
#FOR API SEE
#https://docs.google.com/document/d/1121cjBNN4BeZdMBGil6Qbuqse-sWpEXPpitQH5fb_Fo

    @commands.command(pass_context=True)
    @commands.cooldown(2, 1, commands.BucketType.default)
    async def cool(self, ctx, modify : str = None, *, message : str = None):
        return await self.bot.say("cooldowntest")


    @commands.command(pass_context=True, aliases=['warframe', 'wf', 'WF'])
    @commands.cooldown(2, 1, commands.BucketType.default)
    async def Warframe(self, ctx, modify : str = None, *, message : str = None):
        """| Information module for Warframe."""
        if modify == None or modify == "help":
            return await self.bot.say(f"{warframe_help_cmd}")
        else: #the actual code
            return


    @commands.command(pass_context=True, aliases=['planetside', 'ps2', 'PS2', 'Ps2', 'Planetside2', 'planetside2', 'ps'])
    @commands.cooldown(2, 1, commands.BucketType.default)
    async def Planetside(self, ctx, modify : str = None, *, message : str = None):
        """| Information module for Planetside2."""
        if modify == None or modify == "help":
            return await self.bot.say(f"{planetside_help_cmd}")
        else: #the actual code
            if modify == "servers" or message == "Servers":
                return await self.bot.say(f"```diff\n-{planetside_servers}```")

            if modify == "online" and message != None:
                if ctx.message.author.id == self.bot.operator:
                    LOAD_PROMPT = await self.bot.say(f"Querying online database... please wait")
                    WEB_JSON = WJSON(f"http://census.daybreakgames.com/get/ps2:v2/characters_online_status/?character_name={message}")
                    return await self.bot.edit_message(LOAD_PROMPT, f"<{message}'s online status=<{WEB_JSON}>")

            if modify == "population":
                if ctx.message.author.id == self.bot.operator:
                    LOAD_PROMPT = await self.bot.say(f"Querying online database... please wait")
                    if message == "briggs" or message == "25":
                        WEB_JSON = WJSON("http://ps2.fisu.pw/api/population/?world=25")
                        return await self.bot.edit_message(LOAD_PROMPT, f"<{message}'s data=<{WEB_JSON}>")
                    if message == "jaeger" or message == "19":
                        WEB_JSON = WJSON("http://ps2.fisu.pw/api/population/?world=19")
                        return await self.bot.edit_message(LOAD_PROMPT, f"<{message}'s data=<{WEB_JSON}>")
                    if message == "connery" or message == "1":
                        WEB_JSON = WJSON("http://ps2.fisu.pw/api/population/?world=1")
                        return await self.bot.edit_message(LOAD_PROMPT, f"<{message}'s data=<{WEB_JSON}>")
                    if message == "miller" or message == "10":
                        WEB_JSON = WJSON("http://ps2.fisu.pw/api/population/?world=10")
                        return await self.bot.edit_message(LOAD_PROMPT, f"<{message}'s data=<{WEB_JSON}>")
                    if message == "emerald" or message == "19":
                        WEB_JSON = WJSON("http://ps2.fisu.pw/api/population/?world=19")
                        return await self.bot.edit_message(LOAD_PROMPT, f"<{message}'s data=<{WEB_JSON}>")
                    if message == "cobalt" or message == "13":
                        WEB_JSON = WJSON("http://ps2.fisu.pw/api/population/?world=13")
                        return await self.bot.edit_message(LOAD_PROMPT, f"<{message}'s data=<{WEB_JSON}>")
                    else:
                        return await self.bot.edit_message(LOAD_PROMPT, f"i cannot find the server '{message}'.")
                else:
                    return await self.bot.say(f"This command is locked down for now sorry :c")
                
                

            if modify == "status" or modify == "Status":
                if message == None:
                    return await self.bot.say(f"<PLAYER CANNOT BE NONE>")
                else:
                    return await self.bot.say(f"<{message}'s Stats>")

            return await self.bot.say("<INSERT USEFULL CODE HERE>")


def setup(bot):
    bot.add_cog(Games(bot))
