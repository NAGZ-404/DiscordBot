import praw
import asyncpraw
import config
# import os
# from dotenv import load_dotenv

def load_reddit():
    reddit = asyncpraw.Reddit(
        client_id=config.CLIENT_ID, 
        client_secret=config.CLIENT_SECRET, 
        username=config.USERNAME, 
        password=config.PASSWORD, 
        user_agent=config.USER_AGENT)
    return reddit

#Taken from rchea1's Asuna Bot: https://github.com/rchea1/AsunaBot
#Searches anime openings from r/animethemes
def findAnimeOP(title):
    reddit = load_reddit()
    
    print("Searching for " + title + "...")
    OPs = []
    subreddit = reddit.subreddit("animethemes")

    for submission in reddit.subreddit('animethemes').search(title, 'new'):
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
        print("Couldn't find any openings for " + title)
        return -1

    return list(reversed(OPs))

