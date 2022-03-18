from datetime import datetime, timedelta
from collections import OrderedDict

import itertools

import attr


import re
import requests

import json
from jsonpath_ng.ext import parse
import jsonpath

from api.requests import apiSearch, getMovieInfos, getAllShows, getShowsZone, getAllMovieTheaters, getMovieShowtimes
from api.requests import CITY_LIST, CINEMA_DICT




def Default():
    return 'I did not get your intent. Please try again.'


def Hello(namedGroups={}):
    greeting = (namedGroups.get("greeting") if namedGroups.get("greeting") is not None else " ")
    return f'{greeting} you !'


def Exit():
    return 'Hope I helped. Do not hesitate to come seeing me again !'


def Help():                                                                          # Vrai travail de synthese des commandes du bot + mise en page : RAPH 
    return 'Glad you ask ! You will find bellow all the commands available to you \n'


def MovieInfos(namedGroups={}):

    movie = (namedGroups.get("moviename") if namedGroups.get("moviename") is not None else "")
    infos = getMovieInfos(apiSearch(movie))

    title = infos['title']
    released_date = infos['releaseAt']['FR_FR']
    director = infos['directors']
    synopsis = infos['synopsis']
    poster = infos['posterPath']['lg']

    return f'Title: {title}\nReleased date: {released_date}\nDirected by: {director}\nSynopsis: {synopsis}\nPoster link: {poster}'


#region MovieByType (genre or new movies)
def MovieByType(namedGroups={}): # vrmt compris l'utilité de cette fonction 

    movieType = (namedGroups.get("type") if namedGroups.get("type") is not None else "")
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
    x = itertools.islice(moviesOrdered.items(), 0, 50)
    res = '**Movies coming soon** : \n'
    keys=[0]
    for titles,releaseDate in x:
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


def MoviesByActor(namedGroups={}):
    actor = (namedGroups.get("actor") if namedGroups.get("actor") is not None else "")
    all_shows = getAllShows()
    movies = [
        mov 
        for mov in all_shows 
        if actor in mov["hubbleCasting"]
    ]
    movieTitles = [mov["title"] for mov in movies]

    res = f'Movies played by {actor}:\n'
    return res + '\n'.join(movieTitles)


def MoviesByDirector(namedGroups={}):
    director = (namedGroups.get("director") if namedGroups.get("director") is not None else "")
    all_shows = getAllShows()
    
    movies = [mov for mov in all_shows if director in mov["directors"]]
    movieTitles = [mov["title"] for mov in movies]
    
    res = f'Movies directed by {director}:\n' 
    return res + '\n'.join(movieTitles)
    

def TodayFilmsByLocation(namedGroups={}):
    location = (namedGroups.get("location") if namedGroups.get("location") is not None else "").lower()
    shows = getShowsZone(location)

    movieTitles = [mov["slug"] for mov in shows if mov["bookable"]]

    res = f'Movies available today in {location}:\n' 
    return res + '\n'.join(movieTitles)


def MovieShowTimesTodayTomorrowCinema(namedGroups={}):
    movieName = (namedGroups.get("moviename") if namedGroups.get("moviename") is not None else "").rstrip()
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").lower()
    theaterName = (namedGroups.get("movie_theater_name") if namedGroups.get("movie_theater_name") is not None else "").rstrip().lower()

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
    print(slug, theater, formatDate)
    showTimes = [
        [str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").time()), res["version"], res["refCmd"]]
        for res in getMovieShowtimes(slug, theater, date=formatDate)
        if res["status"] == "available"
    ]

    res = f'Movie shows available for {movieName} {time} ( {formatDate} ) in {theaterName}:\n'
    res += '\n'.join(['\t'.join(x) for x in showTimes])
    return res


def MovieShowtimesDaysCinema(namedGroups={}):
    movieName = (namedGroups.get("moviename") if namedGroups.get("moviename") is not None else "").rstrip()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "").rstrip()
    theaterName = (namedGroups.get("movie_theater_name") if namedGroups.get("movie_theater_name") is not None else "").rstrip().lower()

    # eviter les problemes
    if movieName == "" or date == "" or detail == "" or theaterName == "":
        return None

    infos = getMovieInfos(apiSearch(movieName))
    if type(infos) == dict and "slug" in infos.keys():
        slug = infos["slug"]
    if date == "":
        formatDate = getTimeDate(0, detail)
    else:
        formatDate = getTimeDate(int(date), detail)
    theater = 'cinema-' + theaterName.replace('é', 'e').replace(' ', '-')

    showTimes = [
        [str(datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S").time()), x["version"], x["refCmd"]]
        for x in getMovieShowtimes(slug, theater, date=formatDate)
        if x.get("status") == "available"
    ]

    res = f'Movie shows available for {movieName} in {date} {detail} ( {formatDate} ) in {theaterName}:\n'
    res += '\n'.join(['\t'.join(x) for x in showTimes])
    return res



def ShowtimesByLocationinNbDays(namedGroups={}):
    location = (namedGroups.get("location") if namedGroups.get("location") is not None else "").lower()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "")
    
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