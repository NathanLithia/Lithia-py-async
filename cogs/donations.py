from discord.ext import commands
BTC_ADDRESS="1DHdyTRfiGLiYze4BEvzwZzy5XguDiSYpV"

DONATE_TEXT=f"""```diff
+ Consider donating to keep our bot running.
+ Use >crypto to find out how to obtain coins.
+ We only accept bitcoins for now.
-Bitcoin BTC-
{BTC_ADDRESS}
```"""
CRYPTO_TEXT=f"""```diff
- FAQ -

+ How can i obtain cryptocurrency coins? 
- Here are two nice crypto miners.
- https://www.nicehash.com/
- https://minergate.com/

+ Where can i convert my obtained currency to bitcoin?
- There are many trading sites online, here's one.
- https://hitbtc.com

+ What is lithia's Bitcoin address?
- Currently this is the only address.
  {BTC_ADDRESS}
- we also take kidneys as donations
```"""

class Donations():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, aliases=['donating', 'Donating', 'donate'])
    async def Donate(self):
        await self.bot.say(str(DONATE_TEXT))


    @commands.command(pass_context=True, aliases=['crypto', 'cryptocurrency', 'Cryptocurrency'])
    async def Crypto(self):
        await self.bot.say(str(CRYPTO_TEXT))


def setup(bot):
    bot.add_cog(Donations(bot))
