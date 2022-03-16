import re

from matcher.patterns import patternList
from matcher.responses import (
    Default, 
    Hello, 
    Exit, 
    Help, 
    MovieInfos, 
    MovieByType, 
    MoviesComingSoon, 
    Events, 
    ListGenres,
    MoviesByActor,
    MoviesByDirector,
    TodayFilmByLocation)


def getIntent(message):
    for obj in patternList:
        pattern = obj["pattern"]
        r = re.search(pattern, message)
        if r:
            # return the intent and the captured groups find by the regular expression
            return obj["intent"], r.groupdict()
    
    # if no match by the regular expression, return default message and default dict
    return "Default", {}

def getResponse(intent, namedGroups):

    # dictionnary with intent as key and response message as value
    responseDict = {
        'Default': Default(),
        'Hello': Hello(namedGroups) if 'greeting' in namedGroups.keys() else None,
        'Exit': Exit(),
        'Help': Help(),
        'Movie info': MovieInfos(namedGroups) if 'moviename' in namedGroups.keys() else None,
        'Movie by type': MovieByType(namedGroups) if 'type' in namedGroups.keys() else None,
        'Coming soon': MoviesComingSoon(),
        'Event': Events(),
        'List of genres': ListGenres(),
        'Movie by actor': MoviesByActor(namedGroups) if 'actor' in namedGroups.keys() else None,
        'Movie by director': MoviesByDirector(namedGroups) if 'director' in namedGroups.keys() else None,
        'Available films today by location': TodayFilmByLocation(namedGroups) if 'location' in namedGroups.keys() else None
    }

    return responseDict.get(intent)

def botResponse(message):

    # get the intent and captured named groups
    intent, namedGroup = getIntent(message)
    print(intent, namedGroup)

    # get the response
    response = getResponse(intent, namedGroup)

    return response