from api.scrapper import scrappe

api =  "https://api.myanimelist.net/v2"

def apiSearch(search):
    url = f'{api}/search/quick?q={search}'
    resList = scrappe(url)
    bestMatch = ''
    for res in resList:
        if res['type'] == 'show' and res['isAnime']:
            bestMatch = res['slug']
            break
    return bestMatch


def getAnimeInfos(animeId,api=api):
    url = f'{api}/anime/{animeId}'
    res = scrappe(url)
    return res


def getAllAnimes():
    url = f'{api}/shows'
    res = scrappe(url)
    return res["shows"]

print(getAnimeInfos(10500))
print("merde")




# List of all the cities available in gaumont api


# Dictionary with cities as keys and the list of related Anime theaters as values


#region tests



#endregion