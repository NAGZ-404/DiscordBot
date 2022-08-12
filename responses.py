import random
from animethemes import findAnimeOP

def handle_response(message, title) -> str:
    p_message = message.lower()

    if p_message == '-hello' and title == "":
        return 'Wassup'

    if p_message == '-roll' and title == "":
        return str(random.randint(1,20))

    if p_message == '!help' and title == "":
        return "`This is a help message`"

    if p_message == '-op ' + title:
        if (len(title) < 1):
            return "Please enter a title"

        OPs = findAnimeOP(title)

        if OPs == -1:
            return "Couldn't find any openings for " + title
        
        return OPs


