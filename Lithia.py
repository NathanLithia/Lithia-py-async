#!/usr/bin/env python3

import discord, asyncio
from discord.ext.commands import Bot
import os, time, datetime, sys
from google import search
from googletrans import Translator
import random, math
import LithiaLibs, aiml

translators = Translator()
kernel = aiml.Kernel()

with open ("./bot.ini", "r") as configfile:
    config=configfile.read().splitlines() 

operator = config[1]
devs = config[2]
prefix = config[3]
PCmention = config[4]
Mobilemention = config[5]
auditchan = config[6]
space = " "
keywords = ["what is a", "how do i ", "how would", "whats a", "wat is a", "where can i", "where do i find", "where do you find", "what is ", "how would i go about"]
keyexclude = ["what is that" ,]
blacklistwords = [">AIML"]

bots = Bot(command_prefix=str(prefix), pm_help=True)

#COMPATIBILITY PATCHING
owner = operator
client = bots
lithia = client

@bots.event
async def on_ready():
    data[0] = None
    await bots.change_presence(game=discord.Game(name=str(prefix) + "Commands", type=2))
    print("Discord.py done.")
    kernel.learn('./memory/Startup.xml')
    print("Reading AIML.")
    kernel.respond("LOAD STANDARD LIBRARIES")
    print("Done.")
    print(str(bots.user.name) + " is ready.")
    return

@bots.event
async def on_message(message):
    audit = bots.get_channel(auditchan)

    if message.channel.id == auditchan:
        return
    else:
        embed = discord.Embed(title=message.clean_content, color=0x00ff00)
        embed.set_author(name=str(message.author), icon_url=str(message.author.avatar_url))
        embed.set_footer(text=str(message.channel) + "@" + str(message.server) + " | " + str(datetime.datetime.now()))
        await bots.send_message(audit, embed=embed)    
    if message.author.bot == False: #Lets Log all chat in console with colours.
        print(LithiaLibs.liPurple + "<" + str(message.author) + ">" + LithiaLibs.liEND + ": " + message.clean_content + LithiaLibs.liCyan + " | AT: <" + str(message.server) + "> IN: <" + str(message.channel) + ">" + LithiaLibs.liEND)
        await bots.process_commands(message)
    elif message.author.id == bots.user.id:
        LithiaLibs.prGreen(str(bots.user.name) + "@" + ": " + message.clean_content + " | AT: <" + str(message.server) + "> IN: <" + str(message.channel) + ">")
    elif message.author.bot == True:
        LithiaLibs.prYellow("<" + str(message.author) + ">" + ": " + message.clean_content + " | AT: <" + str(message.server) + "> IN: <" + str(message.channel) + ">")
    else:
        return

    if message.author.bot == False: #Lets be racist and ignore all users whom are bots
        
        if message.content == "@everyone": #Because we hate being tagged we reply to @everyones
            return await bots.send_message(message.channel, "{0.mention} pls https://puu.sh/x7il5/65935dade1.gif".format(message.author))

        if message.content[:22] == PCmention or message.content[:21] == Mobilemention:
            aimlquery = str(kernel.respond(str(message.content)[22:]))
            if aimlquery == "":
	            return #await bots.send_message(message.channel, str("404: " + str(message.content)[22:]))
            else:
	            return await bots.send_message(message.channel, str(aimlquery))
            
        if message.author.id == owner: #Keeping this function private for now
            #if any(word in ['list', 'of', 'words'] for word in message.content):
            if any(keyword in str(message.content) for keyword in keywords):
                if any(keyword in str(message.content) for keyword in blacklistwords):
                    return
                else:
                    searchQuery = []
                    for j in search(str(message.content), tld="com.au", num=1, start=0, stop=1, pause=2):
                        searchQuery.append(j)
                    await bots.send_message(message.channel, "{0.mention}, maybe try ".format(message.author) + str(searchQuery[0]))
                return
    return

@bots.command(pass_context=True)
async def ping(ctx, member: discord.Member = None):
    """Pong!"""
    if member is None:
        member = ctx.message.author
    return await bots.say('Pong! {0.mention}'.format(member))

@bots.command(pass_context=True)
async def id(ctx, member: discord.Member = None):
    """Prints user ID."""
    if member is None:
        member = ctx.message.author
    return await bots.say("{0.mention}'s USER ID is {0.id}".format(member))

@bots.command(pass_context=True)
async def bot(ctx, member: discord.Member = None):
    """Checks if a user is a bots."""
    if member is None:
        member = ctx.message.author
    return await bots.say(str(member.bot))

@bots.command(pass_context=True)
async def joined(ctx, member: discord.Member = None):
    """Prints user join info."""
    if member is None:
        member = ctx.message.author
    await bots.say('{0.mention} joined at {0.joined_at}'.format(member))

@bots.command(pass_context = True, hidden=True)
async def clear(ctx, number):
    if ctx.message.author.id == owner:
        mgs = [] #Emepty list to put all the messages in the log
        number = int(number) #Converting the amount of messages to delete to an integer
        async for x in bots.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await bots.delete_messages(mgs)
    return

@bots.command()
async def date():
    """Prints date."""
    return await bots.say("The date is: " + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y'))

@bots.command(pass_context=True)
async def say(ctx, *, message: str = None):
    """Repeats inputs."""
    if ctx.message.author.id == owner:
        await bots.delete_message(ctx.message)
    return await bots.say(message)

@bots.command()
async def invite():
    """Prints an invitation link."""
    return await bots.say("https://goo.gl/PsTL5u is my invitation link.")

@bots.command(pass_context=True, no_pm=True)
async def joinme(ctx, message: str = None):
    "join your channel"
    if message is None:
        channel = ctx.message.author.voice_channel
        await bots.join_voice_channel(channel)
    else:
        return

@bots.command(pass_context=True, no_pm=True)
async def leave(ctx, message: str = None):
    "leaves your voice channel"
    await bots.say("Attemping to leave, My Clients are: " + str(bots.voice_clients))
    for x in bots.voice_clients:
        if(x.server == ctx.message.server):
            await bots.say(str(x.server))
            return await x.disconnect()
    return

@bots.command(pass_context=True, no_pm=True, hidden=True)
async def promo(ctx, *, message: str = None):
    """Default description."""
    if ctx.message.author.id == owner:
        role = discord.utils.get(ctx.message.server.roles, name=message)
        return await bots.add_roles(ctx.message.author, role)
    else:
        return
    return

@bots.command(pass_context=True, no_pm=True, hidden=True)
async def demo(ctx, *, message: str = None):
    """Default description."""
    if ctx.message.author.id == owner:
        role = discord.utils.get(ctx.message.server.roles, name=message)
        return await bots.remove_roles(ctx.message.author, role)
    else:
        return
    return

@bots.command(pass_context=True, no_pm=False, hidden=True)
async def execute(ctx, *, message: str = None):
    """Default description."""
    if ctx.message.author.id == owner:
        code = message
        await bots.say(code)
        exec(code)
    else:
        await bots.say("Permission Error. Access Denied.")
    return

@bots.command(pass_context=True, no_pm=False, hidden=True)
async def evaluate(ctx, *, message: str = None):
    """Default description."""
    if ctx.message.author.id == owner:
        code = message
        await bots.say(code)
        await bots.say(eval(code))
    else:
        await bots.say("Permission Error. Access Denied.")
    return

@bots.command(pass_context=True, no_pm=False)
async def calculate(ctx, *, message: str = None):
    """Commit mathematical calculations."""
    mathswhitelist=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')', '(', '-', '=', '+', '/', '<', '>', '*', '.', ' ', '^', '!', '~', '&', '|', '%', ','] # https://stackoverflow.com/a/46799212
    await bots.send_typing(ctx.message.channel)
    if any(x not in mathswhitelist for x in message):
        await bots.say("Error. InvalidExpression.")
    else:
        try:
            calculation = str(str(message) + '\n' + str(eval(message)))
        except OverflowError:
            return await bots.say("Error. OverflowError.")
        except SyntaxError:
            return await bots.say("Error. SyntaxError.")
        except ZeroDivisionError:
            return await bots.say("Error. ZeroDivisionError.")
        if len(calculation) > 2000:
            return await bots.say("Error. MaxCharacterError.")
        else:
            await bots.say(calculation)
    return

@bots.command(pass_context=True, no_pm=False, hidden=True)
async def msg(ctx, server: str = None, *, message: str = None):
    """Default description."""
    if ctx.message.author.id == owner:
        channel = bots.get_channel(server)
        await bots.send_message(channel, str(message))
        await bots.delete_message(ctx.message)
    else:
        await bots.say("Error. Access Denied.")
    return

with open ("./bot.key", "r") as myfile:
    data=myfile.readlines()

bots.run(data[0])
