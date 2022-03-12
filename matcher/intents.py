import re

from matcher.patterns import patternList
from matcher.responses import Default, Hello, Exit, Help, MovieInfos, MovieByType


def getIntent(message):
    for obj in patternList:
        pattern = obj["pattern"]
        r = re.search(pattern, message)
        if r:
            # return the intent and the captured groups find by the regular expression
            return obj["intent"], r.groupdict()
    
    # if no match by the regular expression, return default message and default dict
    return "Default", {}


def botResponse(message):

    # get the intent and captured named groups
    intent, namedGroup = getIntent(message)
    print(intent, namedGroup)

    # get the response
    response = getResponse(intent, namedGroup)
    print(response)

    return response

def getResponse(intent, namedGroups):

    # dictionnary with intent as key and response message as value
    responseDict = {
        'Default': Default(),
        'Hello': Hello(namedGroups.get("greeting")),
        'Exit': Exit(),
        'Help': Help(),
        'Movie info': MovieInfos(namedGroups.get("moviename")),
        'Movie by type': MovieByType(namedGroups.get("type"))
    }

    return responseDict.get(intent)