import discord
#import responses
import os
import asyncpraw
import config


from dotenv import load_dotenv
from discord.ext import commands
from animethemes import findAnimeOP

load_dotenv()
TOKEN = os.getenv("TOKEN")


# client = discord.Client()
bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send('Wassup')
    return

@bot.command()
async def op(ctx, title: str ):
    if (len(title) < 1):
        await ctx.send("Please enter a title")
    
    reddit = asyncpraw.Reddit(
        client_id=config.CLIENT_ID, 
        client_secret=config.CLIENT_SECRET, 
        username=config.USERNAME, 
        password=config.PASSWORD, 
        user_agent=config.USER_AGENT)

    # OPs = await findAnimeOP(title)
    

    if OPs == -1:
        return "Couldn't find any openings for " + title
        
    return OPs
# client.run(TOKEN)
bot.run(TOKEN)