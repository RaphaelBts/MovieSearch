from api.data import apiSearch, getMovieInfos, getAllShows

def Default():
    return 'I did not get your intent. Please try again.'

def Hello(greeting):
    return f'{greeting} you !'

def Exit():
    return 'Hope I helped. Do not hesitate to come seeing me again !'

def Help():
    return 'How can I help you ?'

def MovieInfos(movie):
    infos = getMovieInfos(apiSearch(movie))

    title = infos['title']
    released_date = infos['releaseAt']['FR_FR']
    director = infos['directors']
    synopsis = infos['synopsis']
    poster = infos['posterPath']['lg']

    return f'Title: {title}\nReleased date: {released_date}\nDirected by: {director}\nSynopsis: {synopsis}\nPoster link: {poster}'

#region MovieByType (genre or new movies)
def MovieByType(movieType):
    genresList = [] # get the genre list -> a completer

    if movieType in genresList:
        res = MoviebyGenre(movieType)
    else:
        res = NewMovies()
    
    return res

def MoviebyGenre(genre):
    all_shows = getAllShows()

    movies = [mov for mov in all_shows if genre in mov["genres"]]
    movieTitles = [mov["title"] for mov in movies]

    return '\n'.join(movieTitles)

def NewMovies():

    return None
#endregion

def infoFilmX():

    #getAllShows()
    #getMovieInfos()
    return None