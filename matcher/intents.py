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
    ScreeningsDaysLocation,
    ScreeningsTodayTomorrowLocation,
    TodayFilmsByLocation,
    MovieScreeningsTodayTomorrowCinema,
    MovieScreeningsDaysCinema,
    ScreeningsDaysLocation,
    MovieScreeningsTodayTomorrowLocation,
    MovieScreeningsDaysLocation)


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
        'Hello': Hello(namedGroups),
        'Exit': Exit(),
        'Help': Help(),
        'Movie info': MovieInfos(namedGroups),
        'Movie by type': MovieByType(namedGroups),
        'Coming soon': MoviesComingSoon(),
        'Event': Events(),
        'List of genres': ListGenres(),
        'Movie by actor': MoviesByActor(namedGroups),
        'Movie by director': MoviesByDirector(namedGroups),
        'Available films today by location': TodayFilmsByLocation(namedGroups),
        'Movie screening for movie ... today/tomorrow in cinema ...': MovieScreeningsTodayTomorrowCinema(namedGroups),
        'Movie screening for movie ... in ... days in cinema ...': MovieScreeningsDaysCinema(namedGroups),
        'All movies screening in ... days in ...' : ScreeningsDaysLocation(namedGroups),
        'All movies screening today/tomorrow in ...' : ScreeningsTodayTomorrowLocation(namedGroups),
        'Movie screening for movie ... today/tomorrow in ...': MovieScreeningsTodayTomorrowLocation(namedGroups),
        'Movie screening for movie ... in ... days in ...': MovieScreeningsDaysLocation(namedGroups)
    }

    if intent not in responseDict.keys():
        return 'Intent is not recognized.'
    else:
        res = responseDict.get(intent)
        if res is None:
            return 'Reponse is None'
        else:
            return res


def botResponse(message):

    # get the intent and captured named groups
    intent, namedGroup = getIntent(message)
    print(intent)
    print(namedGroup)

    # get the response
    response = getResponse(intent, namedGroup)

    return response