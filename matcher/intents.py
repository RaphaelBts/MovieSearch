import re

from matcher.patterns import patternList
from matcher.responses import responseDict


def getIntent(message):
    for obj in patternList:
        pattern = obj["pattern"]
        intent = None
        r = re.search(pattern, message)
        if r:
            intent = obj["intent"]
            break
    
    return intent, r.groupdict()


def botResponse(message):
    intent, namedGroup = getIntent(message)
    response = getResponseDict(intent, namedGroup)
    
    # if the intent is not in responseDict keys
    if response == None:
        return 'I did not get your intent. Please try again.'
    else:
        return response

def getResponseDict(intent, namedGroups):

    responseDict = {
        'Hello': f'{namedGroups.get("greeting")} you !',
        'Exit': 'Hope I helped. Do not hesitate to come seeing me again !',
        'Help': 'How can I help you ?',
        'Current weather': f'Current weather is {namedGroups.get("city")}...'
    }

    return responseDict.get(intent)