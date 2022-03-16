from datetime import datetime
import requests

import json
from jsonpath_ng.ext import parse
import jsonpath

from api.requests import apiSearch, getMovieInfos, getAllShows, getShowsZone

def Default():
    return 'I did not get your intent. Please try again.'


def Hello(namedGroup):
    greeting = namedGroup.get("greeting")
    return f'{greeting} you !'


def Exit():
    return 'Hope I helped. Do not hesitate to come seeing me again !'


def Help():
    return 'How can I help you ?'


def MovieInfos(namedGroups):

    movie = namedGroups.get("moviename")
    infos = getMovieInfos(apiSearch(movie))

    title = infos['title']
    released_date = infos['releaseAt']['FR_FR']
    director = infos['directors']
    synopsis = infos['synopsis']
    poster = infos['posterPath']['lg']

    return f'Title: {title}\nReleased date: {released_date}\nDirected by: {director}\nSynopsis: {synopsis}\nPoster link: {poster}'


#region MovieByType (genre or new movies)
def MovieByType(namedGroups):

    movieType = namedGroups.get("type")
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

def MoviesComingSoon():
    all_shows = getAllShows()
    movies = [mov for mov in all_shows if mov["isComingSoon"]]
    movieTitles = [mov["title"] for mov in movies]
    
    res = 'Movies coming soon :\n' 
    return res + '\n'.join(movieTitles)


def Events():
    all_shows = getAllShows()
    movies = [mov for mov in all_shows if mov["isEventSpecial"]]
    movieTitles = [mov["title"] for mov in movies]
    
    res = 'Special events :\n' 
    return res + '\n'.join(movieTitles)


def MoviesByActor(namedGroups):
    actor = namedGroups.get("actor")
    all_shows = getAllShows()
    movies = [
        mov 
        for mov in all_shows 
        if actor in mov["hubbleCasting"]
    ]
    movieTitles = [mov["title"] for mov in movies]

    res = f'Movies played by {actor}:\n'
    return res + '\n'.join(movieTitles)


def MoviesByDirector(namedGroups):
    director = namedGroups.get("director")
    all_shows = getAllShows()
    
    movies = [mov for mov in all_shows if director in mov["directors"]]
    movieTitles = [mov["title"] for mov in movies]
    
    res = f'Movies directed by {director}:\n' 
    return res + '\n'.join(movieTitles)
    

def TodayFilmByLocation(namedGroups):
    location = namedGroups.get("location").lower()
    all_shows = getShowsZone(location)

    movieTitles = [mov["slug"] for mov in all_shows if mov["bookable"]]

    res = f'Movies available today in {location}:\n' 
    return res + '\n'.join(movieTitles)


def ListGenres():
    shows = getAllShows()

    genres = [
        str(show["genres"]) 
        for show in shows 
        if "Non défini" not in str(show["genres"])
    ]
    return '\n'.join(list(set(genres)))