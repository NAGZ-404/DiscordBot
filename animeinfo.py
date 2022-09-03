import config
import requests
import json
from tmdbv3api import TMDb, Movie, TV
from AnilistPython import Anilist

def ReturnOfficialAnimeTitle(title):
    tmdb = TMDb()
    tmdb.api_key = config.TMDB_API_KEY
    tv = TV()
    movie = Movie()

    search = tv.search(title)

    try:
        result = search[0].name
        return result
    except:
        msearch = movie.search(title)
        if len(msearch) > 0:
            result = msearch[0].original_title
            return result
        else:
            pass

def ReturnAnimeImage(title):
    tmdb = TMDb()
    tmdb.api_key = config.TMDB_API_KEY

    
    tv = TV()
    movie = Movie()

    search = tv.search(title)

    try:
        result = search[0]
        backdrop = result.backdrop_path
        return ('https://image.tmdb.org/t/p/original/' + backdrop)
    except:
        msearch = movie.search(title)
        if len(msearch) > 0:
            result = msearch[0]
            backdrop = result.backdrop_path
            return ('https://image.tmdb.org/t/p/original/' + backdrop)

        else:
            return ('https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png')