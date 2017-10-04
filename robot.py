import discord
import asyncio
from discord.ext.commands import Bot
from os import system
import sys
import os
import time
import datetime
import LithiaLibs
from random import randint
from google import search
from translate import translator
import aiml

print("Loading..")
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml basic")


my_bot = Bot(command_prefix=">", pm_help=True)
#175182469656477696 Owner
@my_bot.event
async def on_message(message):
    if message.author.bot == False: #Lets Log all chat in console with colours.
        LithiaLibs.prRed("<" + str(message.author) + ">" + ": " + message.content + " | AT: <" + str(message.server) + "> IN: <" + str(message.channel) + ">")
        await my_bot.process_commands(message)
    elif message.author.id == my_bot.user.id:
        LithiaLibs.prGreen("LithiaBot@" + ": " + message.content + " | AT: <" + str(message.server) + "> IN: <" + str(message.channel) + ">")
    elif message.author.bot == True:
        LithiaLibs.prYellow("<" + str(message.author) + ">" + ": " + message.content + " | AT: <" + str(message.server) + "> IN: <" + str(message.channel) + ">")
    else:
        print("ERRORUNKNOWNTYPE=" + str(message.author.id))

    if message.author.bot == False: #Lets be racist and ignore all users whom are bots
        # do some extra stuff here
        if message.content == "@everyone": #Because we hate being tagged we reply to @everyones
            print("Someone just pinged everyone ;-;")
            await my_bot.send_message(message.channel, "{0.mention} pls https://puu.sh/x7il5/65935dade1.gif".format(message.author))
        #Lets Answer some questions by picking up keywords!~ 
        keywords = ["what is a", "how do i ", "how would i ", "whats a", "wat is a", "wot is a", "where can i", "where do i find", "where do you find", "what is ", "how would i go about"]
        blacklistwords = [">AIML"]
        if message.author.id == "175182469656477696": #Keeping this function private for now
            if any(keyword in str(message.content) for keyword in keywords):
                if any(keyword in str(message.content) for keyword in blacklistwords):
                    return
                else:
                    searchQuery = []
                    for j in search(str(message.content), tld="com.au", num=1, start=0, stop=1, pause=2):
                        searchQuery.append(j)
                    await my_bot.send_message(message.channel, "{0.mention}, maybe try ".format(message.author) + str(searchQuery[0]))
    return  

@my_bot.event
async def on_ready():
    LithiaLibs.clear()
    print("Bot Started.")
    system("Title " + str(my_bot.user.id) + " " + str(my_bot.user.name))
    await my_bot.change_presence(game=discord.Game(name=">Command"))
    return 

#@my_bot.event #DISCORD HAS ITS OWN ANNOUNCEMENT SYSTEM NOW
#async def on_member_join(member):
#    server = member.server
#    fmt = 'Welcome {0.mention}!'
#    await my_bot.send_message(server, fmt.format(member, server))

@my_bot.command(pass_context=True)
async def ping(ctx, member: discord.Member = None):
    """Pong!"""
    if member is None:
        member = ctx.message.author
    return await my_bot.say('Pong! {0.mention}'.format(member))


@my_bot.command(pass_context=True)
async def id(ctx, member: discord.Member = None):
    """Prints user ID."""
    if member is None:
        member = ctx.message.author
    return await my_bot.say("{0.mention}'s USER ID is {0.id}".format(member))

@my_bot.command(pass_context=True)
async def bot(ctx, member: discord.Member = None):
    """Checks if a user is a bot."""
    if member is None:
        member = ctx.message.author
    return await my_bot.say(str(member.bot))

@my_bot.command(pass_context=True)
async def AIML(ctx, *, message: str = None):
    """Queries AIML API"""
    return await my_bot.say(str("AIML: " + kernel.respond(str(message))))

@my_bot.command(pass_context=True)
async def joined(ctx, member: discord.Member = None):
    """Prints user join info."""
    if member is None:
        member = ctx.message.author
    await my_bot.say('{0.mention} joined at {0.joined_at}'.format(member))


@my_bot.command()
async def date():
    """Prints date."""
    return await my_bot.say("The date is: " + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y'))

@my_bot.command(pass_context=True)
async def say(ctx, *, message: str = None):
    """Repeats inputs."""
    if ctx.message.author.id == "175182469656477696":
        await my_bot.delete_message(ctx.message)
    return await my_bot.say(message)

@my_bot.command()
async def invite():
    """Prints my invitation link."""
    return await my_bot.say("https://goo.gl/PsTL5u is my invitation link.")

@my_bot.command(pass_context=True)
async def kill(ctx, message: str = None):
    """Attempt to kill a user."""
    if message is None:
        if ctx.message.author.id == "175182469656477696":
            await my_bot.say("Rebooting, sec!")
            return sys.exit()
    else:
        return await my_bot.say("(ಠ╭╮ಠ﻿)/🔪")

@my_bot.command()
async def hg(*userarrayinput):
    """Experimental Command."""
    userarray = list(userarrayinput)
     
    if len(userarray) == 0:
        await my_bot.say("Input Cannot be Empty.")
        return
    await my_bot.say("~Starting Match~")
    while len(userarray) != 1:
        contestant1 = random.randint(0,len(userarray) - 1)
        contestant2 = random.randint(0,len(userarray) - 1)
        while contestant1 == contestant2:
            contestant2 = random.randint(0,len(userarray) - 1)
        await asyncio.sleep(1)
        winner = random.randint(0,1)
        if winner == 0:
            await my_bot.say(str(userarray[contestant1]) + " Killed " + str(userarray[contestant2]))
            userarray.remove(userarray[contestant2])
        else:
            await my_bot.say(str(userarray[contestant2]) + " Killed " + str(userarray[contestant1]))
            userarray.remove(userarray[contestant1])
    if len(userarray) == 1:
        await my_bot.say(str(userarray) + " Reigns Supreme!")
    return

@my_bot.command(pass_context=True)
async def cmd(message):
    """Repeats inputs."""
    return await my_bot.say(str(message))

@my_bot.command(pass_context=True)
async def donate(message):
    """Donate Cryptocurrency."""
    links = """```diff
-BCN- Bytecoin
2AAPhP3okfpDjfitu72M2hiMidkVJZJFB1SK85FjVHWNRCKe2XDczxWdi7ok6B5SQT6UXUtQgusruCoXbqUZm8VJAe8McVY
-BTC- Bitcoin
1H8Eg7Dw4FVCU1gxKPjXKGAvdhm5PGUEwu
-BCC- Bitcoin Cash
1Bt5EsJP2iuseQqx6dPoakBHzNpqCb1Ckk
-ETH- Etherium
0x695da91c5ab4a02bd0ad6f0508933765a3034f30
-XMR- Monero
43qmzGxV2X6S7L3ZodUEMq6XFXj3DcAvYYYsCqiBQqQVMqdBJejAk2WjXqrT3anyZ22j7DEE74GkbVcQFyH2nNiC3dgbqqe```"""
    return await my_bot.say(str(links))