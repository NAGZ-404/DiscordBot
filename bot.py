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
async def op(ctx, *, title: str = None):
    if title is None:
        await ctx.send("Please enter a title")
    else:

        reddit = asyncpraw.Reddit(
            client_id=config.CLIENT_ID, 
            client_secret=config.CLIENT_SECRET, 
            username=config.USERNAME, 
            password=config.PASSWORD, 
            user_agent=config.USER_AGENT)

        # OPs = await findAnimeOP(title)
        subreddit = await reddit.subreddit("animethemes")
        OPs= []

        await ctx.send("Searching for " + title + "...")

        async for submission in subreddit.search(title, 'new'):
            if submission.link_flair_text == 'Added to wiki' and 'OP' in submission.title:
                OPs.append(submission.url)
            else:
                if submission.link_flair_text == 'Mirror in Comments' and 'OP' in submission.title:
                    for comment in submission.comments.list():
                        if('https' in comment.body and 'Mirror:' in comment.body):
                            url = comment.body.split('Mirror: ')[1]
                            submission.url = url
                            OPs.append(submission)
                            break

        if not OPs:
            await ctx.send("Couldn't find any openings for " + title)
        else:
            await ctx.send("Here are the openings for " + title + ":")
            for anime in OPs:
                await ctx.send(anime)
            
            
    

# client.run(TOKEN)
bot.run(TOKEN)