from datetime import datetime, timedelta
from collections import OrderedDict

import itertools

from api.requests import apiSearch, getMovieInfos, getAllShows, getShowsZone, getAllMovieTheaters, getMovieShowtimes, getMovieTheaterShows
from api.requests import CITY_LIST, CINEMA_DICT

import numpy as np


def Default():
    return 'I did not get your intent. Please try again.'


def Hello(namedGroups={}):
    greeting = (namedGroups.get("greeting") if namedGroups.get("greeting") is not None else " ")
    # avoid problems
    if greeting == "":
        return None

    return f'{greeting} you !'


def Exit():
    return 'Hope I helped. Do not hesitate to come seeing me again !'


def Help():                                                                          # Vrai travail de synthese des commandes du bot + mise en page : RAPH 
    return 'Glad you ask ! You will find bellow all the commands available to you \n'


def MovieInfos(namedGroups={}):
    movie = (namedGroups.get("moviename1") if namedGroups.get("moviename1") is not None else "").rstrip()
    # avoid problems
    if movie == "":
        return None

    infos = getMovieInfos(apiSearch(movie))

    title = infos['title']
    released_date = infos['releaseAt']['FR_FR']
    director = infos['directors']
    synopsis = infos['synopsis']
    slug = infos['slug']
    link = f'https://www.cinemaspathegaumont.com/films/{slug}'
    poster = infos['posterPath']['lg']

    return f'**Link page**: {link} \n**Title** : {title} \n**Released date** : {released_date}\n**Directed by** : {director}\n**Synopsis** : *{synopsis}*\n\n' # on peut remettre poster stv


#region MovieByType (genre or new movies)
def MovieByType(namedGroups={}): 
    movieType = (namedGroups.get("type") if namedGroups.get("type") is not None else "").rstrip()
    # avoid problems
    if movieType == "":
        return None

    genresList = [
        'Action', 'Animation', 'Aventure', 'Biopic', 'Comédie', 'Comédie dramatique',
        'Comédie musicale', 'Comédie romantique', 'Court métrage', 'Divers', 'Documentaire', 'Drame',
        'Drame psychologique', 'Famille', 'Fantastique', 'Film musical', 'Guerre', 'Historique',
        'Horreur / Epouvante', 'Policier / Espionnage', 'Romance', 'Science Fiction', 'Thriller',  'Western'
    ]

    if movieType in genresList:
        res = MoviebyGenre(movieType.rstrip())
    else:
        res = NewMovies()
    
    return res

def MoviebyGenre(genre):
    all_shows = getAllShows()

    movies = [mov for mov in all_shows if genre in mov["genres"]]
    movieTitles = [mov["title"] for mov in movies]

    res = 'Movies by genre ' + genre + ':\n'
    return res + '\n'.join(movieTitles)

def NewMovies(new=7):
    all_shows = getAllShows()

    # by 7 date
    # movies = [mov for mov in all_shows if abs((datetime.today().date() - datetime.strptime(mov["releaseAt"][0], '%Y-%m-%d').date()).days) <= new]
    # or using isNew=true
    movies = [mov for mov in all_shows if mov["isNew"]]
    movieTitles = [mov["title"] for mov in movies]
    
    res = 'New movies (released less than ' + str(new) + ' days ago):\n\n' 
    return res + '\n'.join(movieTitles)
#endregion


def MoviesComingSoon():  # 24  6 mois c'est assez 
    all_shows = getAllShows()
    movies = [mov for mov in all_shows if mov["isComingSoon"] and mov['isMovie']]
    moviesOrder = dict() 
    for mov in movies : 
        moviesOrder[mov["title"]]=mov["releaseAt"][0]
        moviesOrdered = OrderedDict(sorted(moviesOrder.items(), key = lambda x:datetime.strptime(x[1], "%Y-%m-%d"), reverse=False))
    moviesListSliced = itertools.islice(moviesOrdered.items(), 0, 50)
    res = '**Movies coming soon** : \n'
    keys=[0]
    for titles,releaseDate in moviesListSliced:
        date_datetime = datetime.strptime(releaseDate, "%Y-%m-%d")
        reformated_date = date_datetime.strftime("%d-%m-%Y")
        keys.append(date_datetime.month)
        if date_datetime.month > keys[-2] :
            res+='\n'
        res += ''+'*'+reformated_date+'*'+'    '+'**'+titles+'**'+ '\n'
    return res


def Events(): #marche pas
    all_shows = getAllShows()
    movies = [mov for mov in all_shows if mov["isEventSpecial"]]
    movieTitles = [mov["title"] for mov in movies]
    
    res = 'Special events :\n' 
    return res + '\n'.join(movieTitles)


def MoviesByActor(namedGroups={}):  # faudrait une autre fonctio qui utilise SEARCH : pcq la c'est que les currently available...
    actor = (namedGroups.get("actor") if namedGroups.get("actor") is not None else "").rstrip()
    # avoid problems
    if actor == "":
        return None
    actor = actor.lower().title() #raph est passé par là
    all_shows = getAllShows()
    movies = [x for x in all_shows if x["hubbleCasting"] is not None]
    moviesTitles =dict()
    slug = dict()
    for mov in movies :
        if actor in mov["hubbleCasting"]:
            moviesTitles[mov["title"]]=mov["releaseAt"][0]
            slug[mov["title"]]=mov["slug"]
    if moviesTitles =={}:
        return f"Sorry ! It seems that {actor} isn't part of the hubble casting of any current movies"
    typoMoviesFilms = namedGroups.get("greeting").title() + 's' if namedGroups.get("greeting")[-1]!='s' else  namedGroups.get("greeting").title() ## ATTENTION PAS FORCEMENT UNE BONNE IDEE 
    res = f'{typoMoviesFilms} available played by **{actor}**  :\n\n'

    for movietitle, releasedate in moviesTitles.items(): 
         res += '*'+ str(datetime.strptime(releasedate, "%Y-%m-%d").year) +'*'+'   '+'**'+movietitle+'**  '+ f'https://www.cinemaspathegaumont.com/films/{slug[movietitle]}'+'\n' #pareil
    return res

# #Deprecated..
# def titleUrl(movietitle): # A perfectionner il etait une fois ... pas pris en compte des ... peut etre des guillemets aussi.. 
#     titleUrlFormat = movietitle.lower().replace(";","").replace(":","").replace(",","").replace("  "," ").replace(" ", "-").replace("'","-")
#     return titleUrlFormat

def MoviesByDirector(namedGroups={}): #meme modif que movies by actor si " validé "
    director = (namedGroups.get("director") if namedGroups.get("director") is not None else "").rstrip()
    # avoid problems
    if director == "":
        return None
    director = director.lower().title() 
    all_shows = getAllShows()
    movies = [x for x in all_shows if x["directors"] is not None]
    moviesTitles =dict()
    slug = dict()

    for mov in movies :
        if director in mov["directors"]:
            moviesTitles[mov["title"]]=mov["releaseAt"][0]
            slug[mov["title"]]=mov["slug"]
    if moviesTitles =={}:
        return f"Sorry ! It seems that {director} didn't produce any current movies. Please also check if he is a producer."
    typoMoviesFilms = namedGroups.get("greeting").title() + 's' if namedGroups.get("greeting")[-1]!='s' else  namedGroups.get("greeting").title() ## ATTENTION PAS FORCEMENT UNE BONNE IDEE 
    res = f'{typoMoviesFilms} available produced by **{director}**  :\n\n'

    for movietitle, releasedate in moviesTitles.items(): 
         res += '*'+ str(datetime.strptime(releasedate, "%Y-%m-%d").year) +'*'+'    '+'**'+movietitle+'**  '+ f'https://www.cinemaspathegaumont.com/films/{slug[movietitle]}'+'\n' #pareil
    return res

    # all_shows = getAllShows()
    # movies = [x for x in all_shows if x["directors"] is not None]
    # movieTitles = [mov["title"] for mov in movies if director in mov["directors"]]
    
    # res = f'Movies directed by {director}:\n' 
    # return res + '\n'.join(movieTitles)
    
# def titleReformat(slug):
#     title = slug.lower().replace("-"," ")
#     titleUrlFormat = movietitle.lower().replace(";","").replace(":","").replace(",","").replace("  "," ").replace(" ", "-").replace("'","-")
# #     return titleUrlFormat


def FilmsTodayTomorrowByLocation(namedGroups={}):
    location = (namedGroups.get("location2") if namedGroups.get("location2") is not None else "").rstrip().lower()
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "today").rstrip().lower()
    # avoid problems
    if location == "" or time == "":
        return None

    if time == "today":
        formatDate = getTimeDate(0, "days")
    elif time == "tomorrow":
        formatDate = getTimeDate(1, "days")
    else:
        return ""

    shows = getShowsZone(location)
    movieTitles = [mov["slug"] for mov in shows if mov["bookable"]]

    # showsInfoDict = {
    #     movieName : {movieTheater : getMovieShowtimes(movieName, movieTheater, date=formatDate) for movieTheater in CINEMA_DICT[location]}
    #     for movieName in movieTitles
    # }
    
    res = f'Movies available {time} ( {formatDate} ) in {location}:\n' 
    for mov in movieTitles:
        res += mov + '\n'

    return res


def FilmsDaysByLocation(namedGroups={}):
    location = (namedGroups.get("location1") if namedGroups.get("location1") is not None else "").rstrip().lower()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "").rstrip()
    # avoid problems
    if location == "" or detail == "":
        return None

    if date == "":
        formatDate = getTimeDate(0, detail)
    else:
        formatDate = getTimeDate(int(date), detail)

    shows = getShowsZone(location)
    movieTitles = [mov["slug"] for mov in shows if mov["bookable"]]

    # showsInfoDict = {}
    # if detail == "days":
    #     showsInfoDict = {
    #         movieName : {movieTheater : getMovieShowtimes(movieName, movieTheater, date=formatDate) for movieTheater in CINEMA_DICT[location]}
    #         for movieName in movieTitles
    #     }
    
    res = f'Movies available in {date} {detail} ( {formatDate} ) in {location}:\n' 
    for mov in movieTitles:
        res += mov + '\n :'
        
    return res


def ScreeningsTodayTomorrowCinema(namedGroups={}):
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    theaterName = (namedGroups.get("movie_theater_name1") if namedGroups.get("movie_theater_name1") is not None else "").rstrip().lower()
    # avoid problems
    if time == "" or theaterName == "":
        return None

    if time == "today":
        formatDate = getTimeDate(0, "days")
    elif time == "tomorrow":
        formatDate = getTimeDate(1, "days")
    else:
        return ""
    theater = 'cinema-' + theaterName.replace('é', 'e').replace(' ', '-')
    shows = getMovieTheaterShows(theater)

    showTimes = {
        slug : [[str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").time()), res["version"], res["refCmd"]]for res in getMovieShowtimes(slug, theater, date=formatDate)]
        for slug, infos in shows.items()
        if infos["bookable"]
    }

    filterShowTimes = { k:v for k,v in showTimes.items() if v != []}

    res = f'Screenings available for {time} ( {formatDate} ) in {theaterName}:\n'
    res += '\n\n'.join([movieName + '\n' + '\n'.join(['\t'.join(screen) for screen in showTimes[movieName]]) for movieName in filterShowTimes.keys()])
    return res


def ScreeningsDaysCinema(namedGroups={}):
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "").rstrip()
    theaterName = (namedGroups.get("movie_theater_name2") if namedGroups.get("movie_theater_name2") is not None else "").rstrip().lower()
    # avoid problems
    if date == "" or detail == "" or theaterName == "":
        return None

    if date == "":
        formatDate = getTimeDate(0, detail)
    else:
        formatDate = getTimeDate(int(date), detail)

    theater = 'cinema-' + theaterName.replace('é', 'e').replace(' ', '-')
    shows = getMovieTheaterShows(theater)

    showTimes = {
        slug : [[str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").time()), res["version"], res["refCmd"]]for res in getMovieShowtimes(slug, theater, date=formatDate)]
        for slug, infos in shows.items()
        if infos["bookable"]
    }

    filterShowTimes = { k:v for k,v in showTimes.items() if v != []}

    res = f'Screenings available in in {date} {detail} ( {formatDate} ) in {theaterName}:\n'
    res += '\n\n'.join([movieName + '\n' + '\n'.join(['\t'.join(screen) for screen in showTimes[movieName]]) for movieName in filterShowTimes.keys()])
    return res


def MovieScreeningsTodayTomorrowCinema(namedGroups={}):
    movieName = (namedGroups.get("moviename2") if namedGroups.get("moviename2") is not None else "").rstrip()
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    theaterName = (namedGroups.get("movie_theater_name3") if namedGroups.get("movie_theater_name3") is not None else "").rstrip().lower()
    # avoid problems
    if movieName == "" or time == "" or theaterName == "":
        return None

    infos = getMovieInfos(apiSearch(movieName))
    if type(infos) == dict and "slug" in infos.keys():
        slug = infos["slug"]
    else:
        slug = ""
    if time == "today":
        formatDate = getTimeDate(0, "days")
    elif time == "tomorrow":
        formatDate = getTimeDate(1, "days")
    else:
        return ""
    theater = 'cinema-' + theaterName.replace('é', 'e').replace(' ', '-')

    showTimes = [
        [str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").time()), res["version"], res["refCmd"]]
        for res in getMovieShowtimes(slug, theater, date=formatDate)
        if res["status"] == "available"
    ]

    if showTimes == []:
        return GetRecommendation(slug, theaterName)
    else:
        res = f'Screenings available for {movieName} {time} ( {formatDate} ) in {theaterName}:\n'
        res += '\n'.join(['\t'.join(x) for x in showTimes])
        return res


def MovieScreeningsDaysCinema(namedGroups={}):
    movieName = (namedGroups.get("moviename3") if namedGroups.get("moviename3") is not None else "").rstrip()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "").rstrip()
    theaterName = (namedGroups.get("movie_theater_name4") if namedGroups.get("movie_theater_name4") is not None else "").rstrip().lower()
    # avoid problems
    if movieName == "" or detail == "" or theaterName == "":
        return None

    if date == "":
        formatDate = getTimeDate(0, detail)
    else:
        formatDate = getTimeDate(int(date), detail)

    infos = getMovieInfos(apiSearch(movieName))
    if type(infos) == dict and "slug" in infos.keys():
        slug = infos["slug"]
    theater = 'cinema-' + theaterName.replace('é', 'e').replace(' ', '-')

    showTimes = [
        [str(datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S").time()), x["version"], x["refCmd"]]
        for x in getMovieShowtimes(slug, theater, date=formatDate)
        if x.get("status") == "available"
    ]

    if showTimes == []:
        return GetRecommendation(slug, theaterName)
    else:
        res = f'Screenings available for {movieName} in {date} {detail} ( {formatDate} ) in {theaterName}:\n'
        res += '\n'.join(['\t'.join(x) for x in showTimes])
        return res


def AllScreeningsDaysLocation(namedGroups={}):
    location = (namedGroups.get("location6") if namedGroups.get("location6") is not None else "").rstrip().lower()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "").rstrip()
    # avoid problems
    if location == "" or detail == "":
        return None

    if date == "":
        formatDate = getTimeDate(0, detail)
    else:
        formatDate = getTimeDate(int(date), detail)

    shows = getShowsZone(location)
    movieTitles = [mov["slug"] for mov in shows if mov["bookable"]]

    showsInfoDict = {}
    if detail == "days":
        showsInfoDict = {
            movieName : {movieTheater : getMovieShowtimes(movieName, movieTheater, date=formatDate) for movieTheater in CINEMA_DICT[location]}
            for movieName in movieTitles
        }
    
    res = f'Movie shows available in {date} {detail} ( {formatDate} ) in {location}:\n' 
    for mov in showsInfoDict.keys():
        res += mov + '\n :'
        for theater in showsInfoDict[mov].keys():
            res += '\t--> ' + theater + ' --> '
            res += ', '.join(list(map(lambda x: str(datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S").time()), showsInfoDict[mov][theater])))
            res += '\n'
        
    return res


def AllScreeningsTodayTomorrowLocation(namedGroups={}):
    location = (namedGroups.get("location5") if namedGroups.get("location5") is not None else "").rstrip().lower()
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    # avoid problems
    if location == "" or time == "":
        return None

    if time == "today":
        formatDate = getTimeDate(0, "days")
    elif time == "tomorrow":
        formatDate = getTimeDate(1, "days")
    else:
        return ""

    shows = getShowsZone(location)
    movieTitles = [mov["slug"] for mov in shows if mov["bookable"]]

    showsInfoDict = {
        movieName : {movieTheater : getMovieShowtimes(movieName, movieTheater, date=formatDate) for movieTheater in CINEMA_DICT[location]}
        for movieName in movieTitles
    }
    
    res = f'Screenings available {time} ( {formatDate} ) in {location}:\n' 
    for mov in showsInfoDict.keys():
        res += mov + '\n :'
        for theater in showsInfoDict[mov].keys():
            res += '\t--> ' + theater + ' --> '
            res += ', '.join(list(map(lambda x: str(datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S").time()), showsInfoDict[mov][theater])))
            res += '\n'
        
    return res


def MovieScreeningsTodayTomorrowLocation(namedGroups={}):
    movieName = (namedGroups.get("moviename4") if namedGroups.get("moviename4") is not None else "").rstrip()
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    location = (namedGroups.get("location3") if namedGroups.get("location3") is not None else "").rstrip().lower()
    # avoid problems
    if movieName == "" or time == "" or location == "":
        return None

    infos = getMovieInfos(apiSearch(movieName))
    if type(infos) == dict and "slug" in infos.keys():
        slug = infos["slug"]
    else:
        slug = ""
    if time == "today":
        formatDate = getTimeDate(0, "days")
    elif time == "tomorrow":
        formatDate = getTimeDate(1, "days")
    else:
        return ""
    city = location.replace('é', 'e').replace(' ', '-')
    movieTheaters = CINEMA_DICT.get(city)

    showTimes = {
        theater : [[str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").time()), res["version"], res["refCmd"]] for res in getMovieShowtimes(slug, theater, date=formatDate)]
        for theater in movieTheaters
    }

    # Check if all cinemas does not project this movie
    hasShowTimes = False
    for k, v in showTimes.items():
        if v != []:
            hasShowTimes = True
            pass

    if hasShowTimes:
        res = f'Screenings available for {movieName} {time} ( {formatDate} ) in {location}:\n'
        res += '\n\n'.join([theater + '\n' + '\n'.join(['\t'.join(screen) for screen in showTimes[theater]]) for theater in showTimes.keys()])
        return res
    else:
        return GetRecommendation(slug)


def MovieScreeningsDaysLocation(namedGroups={}):
    location = (namedGroups.get("location4") if namedGroups.get("location4") is not None else "").rstrip().lower()
    movieName = (namedGroups.get("moviename5") if namedGroups.get("moviename5") is not None else "").rstrip()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "").rstrip()
    # avoid problems
    if location == "" or detail == "" or movieName == "":
        return None

    infos = getMovieInfos(apiSearch(movieName))
    if type(infos) == dict and "slug" in infos.keys():
        slug = infos["slug"]
    else:
        slug = ""
    if date == "":
        formatDate = getTimeDate(0, detail)
    else:
        formatDate = getTimeDate(int(date), detail)
    city = location.replace('é', 'e').replace(' ', '-')
    movieTheaters = CINEMA_DICT.get(city)

    showTimes = {
        theater : [[str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").time()), res["version"], res["refCmd"]] for res in getMovieShowtimes(slug, theater, date=formatDate)]
        for theater in movieTheaters
    }

    # Check if all cinemas does not project this movie
    hasShowTimes = False
    for k, v in showTimes.items():
        if v != []:
            hasShowTimes = True
            pass
    
    if hasShowTimes:
        res = f'Screenings available for {movieName} in {date} days ( {formatDate} ) in {location}:\n'
        res += '\n\n'.join([theater + '\n' + '\n'.join(['\t'.join(screen) for screen in showTimes[theater]]) for theater in showTimes.keys()])
        return res
    else:
        return GetRecommendation(slug)


# Get the most liked movies actually on screen
def GetTrend(namedGroups={}, trending_index=15):
    check = (namedGroups.get("trend") if namedGroups.get("trend") is not None else "")
    # avoid problems
    if check == "":
        return None

    all_movies = getAllShows()
    list_likes = []

    for m in all_movies:
        m_infos = getMovieInfos(m["slug"])
        like_score = m_infos["feelings"]["countEmotionLike"] + 2*m_infos["feelings"]["countEmotionLove"] - m_infos["feelings"]["countEmotionDisappointed"]
        if(m_infos["next24ShowtimesCount"] != 0):
            list_likes.append([like_score, m["title"]])

    list_likes.sort(reverse=True)
    trending = list_likes[:trending_index]

    res = f'Current trending movies are :\n'
    res += '\n'.join(trending[i][1] + '\t' + 'with a like score of ' + str(trending[i][0]) for i in range(len(trending)))
    return res


# Get a similarity score of all movies compared to one movie and return the most similar ones
def GetRecommendation(movieName, theaterName=""):
    moviesAvailable = getAllShows()
    movie_info = getMovieInfos(movieName)
    movie_likes = movie_info["feelings"]["countEmotionLike"] + 2*movie_info["feelings"]["countEmotionLove"] - movie_info["feelings"]["countEmotionDisappointed"]
    similarity_list = []
    if movie_info["actors"] is not None:
        casting = [x.rstrip() for x in movie_info["actors"].split(",")]
    else:
        casting = []
    if movie_info["directors"] is not None:
        directors = [x.rstrip() for x in movie_info["directors"].split(",")]
    else:
        directors = []

    for m in moviesAvailable:
        similarity_score = 0
        if(m["slug"] != movieName): #not calculating the similarity score for the movie (moviename)
            m_infos = getMovieInfos(m["slug"])
            if(m_infos["next24ShowtimesCount"] != 0):
                m_likes = m_infos["feelings"]["countEmotionLike"] + 2*m_infos["feelings"]["countEmotionLove"] - m_infos["feelings"]["countEmotionDisappointed"]
                similarity_score += np.log(abs(movie_likes-m_likes)) if movie_likes-m_likes != 0 else 0
                if(m["genres"][0] != movie_info["genres"][0]):
                    similarity_score += 2
                if m["hubbleCasting"] is not None:
                    for actor in casting:
                        if actor in m["hubbleCasting"]:
                            similarity_score /= 2
                if m["directors"] is not None:
                    for director in directors:
                        if actor in m["directors"]:
                            similarity_score /= 2
                similarity_list.append([similarity_score, m["title"]])
            
    similarity_list.sort()
    
    res = f'Since {movie_info["title"]} is not available, here are some similar movies you may like :\n'
    res += '\n'.join(similarity_list[i][1] + '\t' + 'with a score of ' + str(similarity_list[i][0]) for i in range(10))
    return res


def getTimeDate(nbDays, details):
    res = ""

    if details == "days":
        res = (datetime.today().date() + timedelta(days=nbDays)).strftime("%Y-%m-%d")
    
    return res

  
def ListGenres():
    genres="Action  |  Animation  |  Aventure  |  Biopic  |  Comédie | Comédie dramatique  |  Comédie musicale  |  Comédie romantique  |  Court métrage  |  Divers | Documentaire  |  Drame  |  Drame psychologique  |  Famille  |  Fantastique | Film musical  |  Guerre  |  Historique  |  Horreur / Epouvante  |  Policier / Espionnage | Romance  |  Science Fiction  |  Thriller  |  Western"
    str="** The Gaumont *genre* colllection** : \n\n"
    for i in range(int(len(genres)/5+1)):
        str+='  '.join(genres[i*5:(i+1)*5])+ "\n"  
    return str


    # shows = getAllShows()
    # genres = set() 
    # for show in shows : 
    #       genres.add(show["genres"][0])
    # genres_sorted = sorted([genre for genre in genres if genre!='Non défini'])
    # str="** The Gaumont *genre* colllection** : \n\n"
    # for i in range(int(len(genres_sorted)/5+1)):
    #     str+='  |  '.join(genres_sorted[i*5:(i+1)*5])+ "\n"  
    # return str


    # str="**"
    # for i in range(int(len(genres_sorted)/5+1)):
    #     str+='**  |  **'.join(genres_sorted[i*5:(i+1)*5])+ "** \n **"  
    # return str-'**'


    # genres = [
    #     str(show["genres"]) 
    #     for show in shows 
    #     if "Non défini" not in str(show["genres"])
    # ]
    # return '\n'.join(list(set(genres)))