from datetime import datetime, timedelta
from collections import OrderedDict

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


def Help():
    return 'How can I help you ?'


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
def MovieByType(namedGroups={}):

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
    
    res = 'New movies (released less than ' + str(new) + ' days ago):\n' 
    return res + '\n'.join(movieTitles)
#endregion

def MoviesComingSoon():  # 24  6 mois c'est assez 
    all_shows = getAllShows()
    movies = [mov for mov in all_shows if mov["isComingSoon"]]
    moviesOrder = dict() 
    for mov in movies : 
        moviesOrder[mov["title"]]=mov["releaseAt"][0]
        moviesOrdered = OrderedDict(sorted(moviesOrder.items(), key = lambda x:datetime.strptime(x[1], "%Y-%m-%d"), reverse=True))
  
    res = 'Movies coming soon :\n' 
    for titles,releaseDate in moviesOrdered.items():
            res += ' '+ titles+' '+releaseDate+'\n'
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


def ShowtimesByLocationinNbDays(namedGroups={}):
    location = (namedGroups.get("location") if namedGroups.get("location") is not None else "").lower()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "")
    if date == "":
        formatDate = getTimeDateWeek(0, detail)
    else:
        formatDate = getTimeDateWeek(int(date), detail)

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


def getTimeDateWeek(number, details):
    res = ""

    if details == "days":
        res = (datetime.today().date() + timedelta(days=number)).strftime("%Y-%m-%d")
    
    return res

        

  
def ListGenres():

    shows = getAllShows()
    genres = set() 
    for show in shows : 
          genres.add(show["genres"][0])
    return genres 


    # genres = [
    #     str(show["genres"]) 
    #     for show in shows 
    #     if "Non défini" not in str(show["genres"])
    # ]
    # return '\n'.join(list(set(genres)))