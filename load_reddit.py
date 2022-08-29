import asyncpraw
import config

def load_reddit():
    reddit = asyncpraw.Reddit(
        client_id=config.CLIENT_ID, 
        client_secret=config.CLIENT_SECRET, 
        username=config.USERNAME, 
        password=config.PASSWORD, 
        user_agent=config.USER_AGENT)
    return reddit