import discord
#import responses
import os
import asyncpraw
from load_reddit import load_reddit
from animethemes import findAnimeOP
import config


from dotenv import load_dotenv
from discord.ext import commands, pages
from discord.ext.pages import Paginator, Page



load_dotenv()
TOKEN = os.getenv("TOKEN")
intents=discord.Intents.all()

# client = discord.Client()
bot = commands.Bot(command_prefix='-', intents=intents)


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

        await ctx.send("Searching for " + title + "...")
        OPs = await findAnimeOP(ctx, title)

        # reddit = load_reddit()

        # subreddit = await reddit.subreddit("animethemes")
        # OPs= []
        # count = 0

        # await ctx.send("Searching for " + title + "...")

        # async for submission in subreddit.search(title, 'new', 'limit=5'):
        #     if count == 5:
        #         break
        #     if submission.link_flair_text == 'Added to wiki' and 'OP' in submission.title:
        #         OPs.append(submission.url)
        #         count += 1
        #     else:
        #         if submission.link_flair_text == 'Mirror in Comments' and 'OP' in submission.title:
        #             for comment in submission.comments.list():
        #                 if('https' in comment.body and 'Mirror:' in comment.body):
        #                     url = comment.body.split('Mirror: ')[1]
        #                     submission.url = url
        #                     OPs.append(submission)
        #                     count += 1
        #                     break

        if not OPs:
            await ctx.send("Couldn't find any openings for " + title)
        else:
            await ctx.send("Here are the openings for " + title + ":")
            # for op, anime in enumerate(OPs, start=1):
                # embed = discord.Embed(title=title, url=anime, description="Result: " + str(op), color=0x00ff00)
                # await ctx.send(embed=embed)
            embeds = [discord.Embed(title=title, url = anime, description=f'Opening {op}', color = 0x00ff00) for op, anime in enumerate(OPs, start=1)]
            
            my_pages = [Page(embeds = [embed]) for embed in embeds]
            paginator = Paginator(pages=my_pages)

            await paginator.send(ctx)
            await ctx.send("Done! If any of the links dont show the video or you want to see more openings from this title, please visit https://www.reddit.com/r/animethemes/")
            
            
    

# client.run(TOKEN)
bot.run(TOKEN)