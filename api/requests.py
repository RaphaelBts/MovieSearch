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


def getMovieShowtimes(movieName, theaterName, api="https://www.cinemaspathegaumont.com/api"):
    url = f'{api}/show/{movieName}/showtimes/{theaterName}'
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


#region tests

# genres = getMovieInfos('uncharted')['genres']
# print(genres)

# showtimes = getMovieShowtimes('uncharted', 'cinema-gaumont-alesia')
# print(showtimes)

# apiSearch('The Batman')

#endregion