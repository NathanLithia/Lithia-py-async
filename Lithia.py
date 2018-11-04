import datetime
from discord.ext import commands
import discord
import os
import aiml
import asyncio

description = '''
Lithia an assistant built apon python3.6+ to help with a variety of things.
Lithia's Github = https://github.com/nathanlol5/Lithia-AIML
'''
# this specifies what extensions to load when the boat starts up


with open ("./configs/bot.ini", "r") as configfile:
    config=configfile.read().splitlines() 


operator = config[1]
devs = config[2]
prefix = config[3]
PCmention = config[4]
Mobilemention = config[5]
auditchan = config[6]
startup_extensions = []


directory = os.fsencode('./cogs')


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".cog") or filename.endswith(".py"): 
        print(os.path.join(str(filename)))
        startup_extensions.append(str('cogs.'+str(filename)).replace('.py',''))
        continue
    else:
        continue

bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), description=description)


async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name=f"{bot.prefix}Commands", type=2))
        await asyncio.sleep(35)
        await bot.change_presence(game=discord.Game(name="on Python", type=1))
        await asyncio.sleep(35)
        await bot.change_presence(game=discord.Game(name="🐝Ri&Coffee☕ :)", type=1))
        await asyncio.sleep(35)
        await bot.change_presence(game=discord.Game(name=f"{bot.prefix}Donate", type=1))
        await asyncio.sleep(35)


async def timed_message(server, message, delay = 10):
    """Messages and deletes message after a delay"""
    msg2delete = await bot.send_message(server, message)
    await bot.timed_delete(msg2delete, delay)
    return 

async def timed_delete(message, delay = 10):
    """Thread Spawner for Deleting messages over time"""
    bot.loop.create_task(msgdel(message, delay))

async def msgdel(message, delay = 10):
    """deletes message after an delay"""
    await asyncio.sleep(delay)
    return await bot.delete_message(message)


bot.timed_message = timed_message
bot.timed_delete = timed_delete
bot.prefix = prefix
bot.operator = "175182469656477696"


@bot.event
async def on_ready():
    data[0] = None
    print('Logged in as')
    bot.brain = aiml.Kernel()
    bot.brain.learn('./database/aiml/Startup.xml')
    bot.brain.respond("LOAD STANDARD LIBRARIES")
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name=str(prefix) + "Commands", type=2))
    bot.loop.create_task(status_task())


@bot.command(pass_context=True, hidden=True)
async def load(ctx, extension_name : str):
    """Loads an extension."""
    if ctx.message.author.id == bot.operator:
        try:
            bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await bot.say("```SubUnit\nLoaded <{}> : ".format(extension_name)+str(datetime.datetime.now())+"z```")


@bot.command(pass_context=True, hidden=True)
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    if ctx.message.author.id == bot.operator:
        bot.unload_extension(extension_name)
        await bot.say("```SubUnit\nUnloaded <{}> : ".format(extension_name)+str(datetime.datetime.now())+"z```")


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    

    with open ("./tokens/bot.token", "r") as myfile:
        data=myfile.readlines()
    bot.run(data[0])
