import praw
import asyncpraw
import config
from load_reddit import load_reddit
# import os
# from dotenv import load_dotenv


#Taken from rchea1's Asuna Bot: https://github.com/rchea1/AsunaBot
#Searches anime openings from r/animethemes
async def findAnimeOP(ctx, title):
    # reddit = load_reddit()
    
    # print("Searching for " + title + "...")
    # OPs = []
    # subreddit = reddit.subreddit("animethemes")

    # for submission in reddit.subreddit('animethemes').search(title, 'new'):
    #     if submission.link_flair_text == 'Added to wiki' and 'OP' in submission.title:
    #         OPs.append(submission.url)
    #     else:
    #         if submission.link_flair_text == 'Mirror in Comments' and 'OP' in submission.title:
    #             for comment in submission.comments.list():
    #                 if('https' in comment.body and 'Mirror:' in comment.body):
    #                     url = comment.body.split('Mirror: ')[1]
    #                     submission.url = url
    #                     OPs.append(submission)
    #                     break

    # if not OPs:
    #     print("Couldn't find any openings for " + title)
    #     return -1

    reddit = load_reddit()

        # OPs = await findAnimeOP(title)
    subreddit =  await reddit.subreddit("animethemes")
    OPs= []
    count = 0

    async for submission in subreddit.search(title, 'new', 'limit=5'):
        if count == 5:
                break
        if submission.link_flair_text == 'Added to wiki' and 'OP' in submission.title:
            OPs.append(submission.url)
            count += 1
        else:
            if submission.link_flair_text == 'Mirror in Comments' and 'OP' in submission.title:
                for comment in submission.comments.list():
                    if('https' in comment.body and 'Mirror:' in comment.body):
                        url = comment.body.split('Mirror: ')[1]
                        submission.url = url
                        OPs.append(submission)
                        count += 1
                        break

    return (list(reversed(OPs)))

