from api.scrapper import scrappe

def apiSearch(search, api="https://www.cinemaspathegaumont.com/api"):
    url = f'{api}/search/quick?q={search}'
    resList = scrappe(url)
    bestMatch = ''
    for res in resList:
        if res['type'] == 'show' and res['isMovie']:
            bestMatch = res['slug']
            break
    return bestMatch
    

def getMovieInfos(movieName, api="https://www.cinemaspathegaumont.com/api"):
    url = f'{api}/show/{movieName}'
    res = scrappe(url)
    return res


def getMovieShowtimes(movieName, theaterName, date="", api="https://www.cinemaspathegaumont.com/api"):
    url = f'{api}/show/{movieName}/showtimes/{theaterName}'
    if date != "":
        url += f'/{date}'
    res = scrappe(url)
    return res


def getAllShows(api="https://www.cinemaspathegaumont.com/api"):
    url = f'{api}/shows'
    res = scrappe(url)
    return res["shows"]


def getAllMovieTheaters(api="https://www.cinemaspathegaumont.com/api"):
    url = f'{api}/cinemas'
    res = scrappe(url)
    return res


def getShowsZone(zone, api="https://www.cinemaspathegaumont.com/api"):
    url = f'{api}/zone/{zone}'
    res = scrappe(url)
    return res["shows"]

# List of all the cities available in gaumont api
CITY_LIST = [
    city
    for city in sorted(list(set(list(map(lambda x: x["citySlug"], getAllMovieTheaters())))))
]

# Dictionary with cities as keys and the list of related movie theaters as values
CINEMA_DICT = {
    city : sorted([cinema["slug"] for cinema in getAllMovieTheaters() if cinema["citySlug"] == city])
    for city in CITY_LIST
}

#region tests

# genres = getMovieInfos('uncharted')['genres']
# print(genres)

# showtimes = getMovieShowtimes('uncharted', 'cinema-gaumont-alesia')
# print(showtimes)

# apiSearch('The Batman')

#endregion