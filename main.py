from asyncio.windows_events import NULL
import discord 
from discord.ext import commands
import time
import json
import colorama 
from colorama  import Fore
import os

client = commands.Bot('>', self_bot = True)
with open('config.json') as f:
    config = json.load(f)
    token = config.get('token')
@client.event
async def on_ready():
    os.system("cls")
    print(f'''{Fore.MAGENTA}


  ██████╗██╗   ██╗██╗  ████████╗     █████╗ ██╗   ██╗████████╗ ██████╗      █████╗ ███████╗██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
 ██╔════╝██║   ██║██║  ╚══██╔══╝    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔══██╗██╔════╝██║ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
 ██║     ██║   ██║██║     ██║       ███████║██║   ██║   ██║   ██║   ██║    ███████║█████╗  █████╔╝     ██║     ███████║█████╗  ██║     █████╔╝ 
 ██║     ██║   ██║██║     ██║       ██╔══██║██║   ██║   ██║   ██║   ██║    ██╔══██║██╔══╝  ██╔═██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
 ╚██████╗╚██████╔╝███████╗██║       ██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██║  ██║██║     ██║  ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
  ╚═════╝ ╚═════╝ ╚══════╝╚═╝       ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                                                      Time to fake your stams

                                                   Logged in as: {client.user}                                                                                            
    ''')
@client.command()
async def afk(ctx):
    await ctx.message.delete()
    x = (int(input("Enter the amount: ")))
    while True:
        time.sleep(0.4)
        await ctx.send(x)
        x -= 1
        if x == 0:
            break

        for x in range(x, 1):
            

            await ctx.send(x)
          
 
client.run(token, bot = False)
