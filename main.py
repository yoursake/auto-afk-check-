from asyncio.windows_events import NULL
import discord 
from discord.ext import commands
import time
import json

client = commands.Bot('>', self_bot = True)
with open('config.json') as f:
    config = json.load(f)
    token = config.get('token')
x = 100
@client.command()
async def afk(ctx):
    await ctx.message.delete()
    x = 100
    while True:
        time.sleep(0.4)
        await ctx.send(x)
        x -= 1
        if x == 0:
            break

        for x in range(100, 1):
            

            await ctx.send(x)
          
 
client.run(token, bot = False)