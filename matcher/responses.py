from datetime import datetime, timedelta
from collections import OrderedDict
from email.utils import localtime

import itertools

import attr


import re
import requests

import json
from jsonpath_ng.ext import parse
import jsonpath

from api.requests import apiSearch, getMovieInfos, getAllShows, getShowsZone, getAllMovieTheaters, getMovieShowtimes, getMovieTheaterShows
from api.requests import CITY_LIST, CINEMA_DICT




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
    movie = (namedGroups.get("moviename") if namedGroups.get("moviename") is not None else "").rstrip()
    # avoid problems
    if movie == "":
        return None

    infos = getMovieInfos(apiSearch(movie))

    title = infos['title']
    released_date = infos['releaseAt']['FR_FR']
    director = infos['directors']
    synopsis = infos['synopsis']
    titleUrlFormat = titleUrl(title)
    link = f'https://www.cinemaspathegaumont.com/films/{titleUrlFormat}'
    poster = infos['posterPath']['lg']

    return f'**Link page**: {link} \n**Title** : {title} \n**Released date** : {released_date}\n**Directed by** : {director}\n**Synopsis** : *{synopsis}*\n\n' # on peut remettre poster stv


#region MovieByType (genre or new movies)
def MovieByType(namedGroups={}): 
    movieType = (namedGroups.get("type") if namedGroups.get("type") is not None else "").rstrip()
    # avoid problems
    if movieType == "":
        return None

    genresList = ['Fantaisie',] # get the genre list -> a completer

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


def Events():
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
    movieTitles = {mov["title"]:mov["releaseAt"][0] for mov in movies if actor in mov["hubbleCasting"]} 
    typoMoviesFilms = namedGroups.get("greeting").title() + 's' if namedGroups.get("greeting")[-1]!='s' else  namedGroups.get("greeting").title() ## ATTENTION PAS FORCEMENT UNE BONNE IDEE 
    res = f'{typoMoviesFilms} available played by **{actor}**  :\n\n'

    for movietitle, releasedate in movieTitles.items(): 
         titleforUrl = titleUrl(movietitle)
         res += '*'+ str(datetime.strptime(releasedate, "%Y-%m-%d").year) +'*'+'   |  '+'**'+movietitle+'**  '+ f'https://www.cinemaspathegaumont.com/films/{titleforUrl}'+'\n' #pareil
    return res

def titleUrl(movietitle): # A perfectionner il etait une fois ... pas pris en compte des ... peut etre des guillemets aussi.. 
    titleUrlFormat = movietitle.lower().replace(";","").replace(":","").replace(",","").replace("  "," ").replace(" ", "-").replace("'","-")
    return titleUrlFormat

def MoviesByDirector(namedGroups={}): #meme modif que movies by actor si " validé "
    director = (namedGroups.get("director") if namedGroups.get("director") is not None else "").rstrip()
    # avoid problems
    if director == "":
        return None

    all_shows = getAllShows()
    movies = [x for x in all_shows if x["directors"] is not None]
    movieTitles = [mov["title"] for mov in movies if director in mov["directors"]]
    
    res = f'Movies directed by {director}:\n' 
    return res + '\n'.join(movieTitles)
    

def TodayFilmsByLocation(namedGroups={}):
    location = (namedGroups.get("location") if namedGroups.get("location") is not None else "").rstrip().lower()
    # avoid problems
    if location == "":
        return None 

    shows = getShowsZone(location)

    movieTitles = [mov["slug"] for mov in shows if mov["bookable"]]

    res = f'Movies available today in {location}:\n' 
    return res + '\n'.join(movieTitles)


def ScreeningsTodayTomorrowCinema(namedGroups={}):
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    theaterName = (namedGroups.get("movie_theater_name") if namedGroups.get("movie_theater_name") is not None else "").rstrip().lower()
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
    theaterName = (namedGroups.get("movie_theater_name") if namedGroups.get("movie_theater_name") is not None else "").rstrip().lower()
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
    movieName = (namedGroups.get("moviename") if namedGroups.get("moviename") is not None else "").rstrip()
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    theaterName = (namedGroups.get("movie_theater_name") if namedGroups.get("movie_theater_name") is not None else "").rstrip().lower()
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

    res = f'Screenings available for {movieName} {time} ( {formatDate} ) in {theaterName}:\n'
    res += '\n'.join(['\t'.join(x) for x in showTimes])
    return res


def MovieScreeningsDaysCinema(namedGroups={}):
    movieName = (namedGroups.get("moviename") if namedGroups.get("moviename") is not None else "").rstrip()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "").rstrip()
    theaterName = (namedGroups.get("movie_theater_name") if namedGroups.get("movie_theater_name") is not None else "").rstrip().lower()
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

    res = f'Screenings available for {movieName} in {date} {detail} ( {formatDate} ) in {theaterName}:\n'
    res += '\n'.join(['\t'.join(x) for x in showTimes])
    return res


def AllScreeningsDaysLocation(namedGroups={}):
    location = (namedGroups.get("location") if namedGroups.get("location") is not None else "").rstrip().lower()
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
    location = (namedGroups.get("location") if namedGroups.get("location") is not None else "").rstrip().lower()
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
    movieName = (namedGroups.get("moviename") if namedGroups.get("moviename") is not None else "").rstrip()
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    location = (namedGroups.get("location") if namedGroups.get("location") is not None else "").rstrip().lower()
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

    res = f'Screenings available for {movieName} {time} ( {formatDate} ) in {location}:\n'
    res += '\n\n'.join([theater + '\n' + '\n'.join(['\t'.join(screen) for screen in showTimes[theater]]) for theater in showTimes.keys()])
    return res


def MovieScreeningsDaysLocation(namedGroups={}):
    location = (namedGroups.get("location") if namedGroups.get("location") is not None else "").rstrip().lower()
    movieName = (namedGroups.get("moviename") if namedGroups.get("moviename") is not None else "").rstrip()
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

    res = f'Screenings available for {movieName} in {date} days ( {formatDate} ) in {location}:\n'
    res += '\n\n'.join([theater + '\n' + '\n'.join(['\t'.join(screen) for screen in showTimes[theater]]) for theater in showTimes.keys()])
    return res


def getTimeDate(nbDays, details):
    res = ""

    if details == "days":
        res = (datetime.today().date() + timedelta(days=nbDays)).strftime("%Y-%m-%d")
    
    return res

  
def ListGenres():

    shows = getAllShows()
    genres = set() 
    for show in shows : 
          genres.add(show["genres"][0])
    genres_sorted = sorted([genre for genre in genres if genre!='Non défini'])
    str="** The Gaumont *genre* colllection** : \n\n"
    for i in range(int(len(genres_sorted)/5+1)):
        str+='  |  '.join(genres_sorted[i*5:(i+1)*5])+ "\n"  
    return str


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