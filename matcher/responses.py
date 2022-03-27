from datetime import datetime, timedelta
from collections import OrderedDict

import itertools

from api.requests import apiSearch, getMovieInfos, getAllShows, getShowsZone, getAllMovieTheaters, getMovieShowtimes, getMovieTheaterShows
from api.requests import CITY_LIST, CINEMA_DICT

import numpy as np


def Default():
    return ['Default message','I did not get your intent. Please try again.']


def Hello(namedGroups={}):
    greeting = (namedGroups.get("greeting") if namedGroups.get("greeting") is not None else " ")
    # avoid problems
    if greeting == "":
        return None

    return [f'{greeting} you !', 'Feel free to ask about a specific movie infos, movies screenings in a particular theater or location, famous actor or director and so on']


def Exit():
    return ['Exit message','Hope I helped. Do not hesitate to come again I am 24/7 active !']


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
    titleRequest = '{title} informations'
    content = f'**Link page**: {link} \n**Title** : {title} \n**Released date** : {released_date}\n**Directed by** : {director}\n**Synopsis** : *{synopsis}*\n**poster** : {poster}\n' # on peut remettre poster stv

    return [titleRequest,content]

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
    
    titleRequest = "List of movies by genre"
    res = 'Movies by genre ' + genre + ':\n'
    content = res + '\n'.join(movieTitles) 
    return [titleRequest, content]

def NewMovies(new=7):
    all_shows = getAllShows()

    # by 7 date
    # movies = [mov for mov in all_shows if abs((datetime.today().date() - datetime.strptime(mov["releaseAt"][0], '%Y-%m-%d').date()).days) <= new]
    # or using isNew=true
    movies = [mov for mov in all_shows if mov["isNew"]]
    movieTitles = [mov["title"] for mov in movies]
    
    titleRequest = 'New movies (released less than ' + str(new) + ' days ago):\n\n' 
    content = '\n'.join(movieTitles)
    return [titleRequest,content]
#endregion


def MoviesComingSoon():  # 24  6 mois c'est assez 
    all_shows = getAllShows()
    movies = [mov for mov in all_shows if mov["isComingSoon"] and mov['isMovie']]
    moviesOrder = dict() 
    for mov in movies : 
        moviesOrder[mov["title"]]=mov["releaseAt"][0]
        moviesOrdered = OrderedDict(sorted(moviesOrder.items(), key = lambda x:datetime.strptime(x[1], "%Y-%m-%d"), reverse=False))
    moviesListSliced = itertools.islice(moviesOrdered.items(), 0, 50)
    titleRequest = '**Movies coming soon** : \n'
    res=""
    keys=[0]
    for titles,releaseDate in moviesListSliced:
        date_datetime = datetime.strptime(releaseDate, "%Y-%m-%d")
        reformated_date = date_datetime.strftime("%d-%m-%Y")
        keys.append(date_datetime.month)
        if date_datetime.month > keys[-2] :
            res+='\n'
        res += ''+'*'+reformated_date+'*'+'    '+'**'+titles+'**'+ '\n'
    return [titleRequest,res]


def Events(): #marche pas
    all_shows = getAllShows()
    movies = [mov for mov in all_shows if mov["isEventSpecial"]]
    movieTitles = [mov["title"] for mov in movies]
    
    titleRequest = 'Special events :\n' 
    content = '\n'.join(movieTitles)
    return [titleRequest,content]


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
    titleRequest = f'{typoMoviesFilms} available played by **{actor}**  :\n'
    res=""
    for movietitle, releasedate in moviesTitles.items(): 
         res += '*'+ str(datetime.strptime(releasedate, "%Y-%m-%d").year) +'*'+'   '+hyperlink(bold(movietitle),f'https://www.cinemaspathegaumont.com/films/{slug[movietitle]}')+'\n' #pareil
    return [titleRequest,res]

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
    titleRequest = f'{typoMoviesFilms} available produced by **{director}**  :\n'
    res=""

    for movietitle, releasedate in moviesTitles.items(): 
         res += '*'+ str(datetime.strptime(releasedate, "%Y-%m-%d").year) +'*'+'    '+hyperlink(bold(movietitle),f'https://www.cinemaspathegaumont.com/films/{slug[movietitle]}')+'\n' #pareil
    return [titleRequest,res]

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

    all_shows_zone = getShowsZone(location)
    all_shows = getAllShows()

    moviesTitles = {mov["slug"]:[mov["title"],mov["genres"]] for mov in all_shows} # 
    moviesSlugZone = { mov["slug"]:moviesTitles[mov["slug"]] for mov in all_shows_zone if mov["bookable"]}

    titleRequest = f'Movies available {time} ({formatDate}) in {location}:\n' 
    res=""
    for slug, movieinfos in moviesSlugZone.items(): 
        res += '  **'+str(movieinfos[0])+'**  '+ ' | ' + str(movieinfos[1][0])+   f'https://www.cinemaspathegaumont.com/films/{slug}'+ '\n' #pareil
     #changer pour HYPERLINK
    return [titleRequest,res]




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

    all_shows_zone = getShowsZone(location)
    all_shows = getAllShows()

    movieSlugs= [mov["slug"] for mov in all_shows_zone if mov["bookable"]]
    movieInfos = {mov["slug"]:[mov["title"],mov["genres"]] for mov in all_shows} # 

    showsInfoDict = {}
    if detail == "days":
        showsInfoDict = {
            movieName : {movieTheater : getMovieShowtimes(movieName, movieTheater, date=formatDate) for movieTheater in CINEMA_DICT[location]}
            for movieName in movieSlugs
        }
    
    movies = [
        movieName 
        for movieName, theater in showsInfoDict.items() 
        for showTimes in theater.values()
        if showTimes != []
    ]

    titleRequest = f'Movies available in {date} {detail} ( {formatDate} ) in {location}:\n' 
    res=""
    for slug in movies:
         res += '  **'+str(movieInfos[0])+'**  '+ ' | ' + hyperlink(str(movieInfos[1][0]),f'https://www.cinemaspathegaumont.com/films/{slug}')+ '\n' #pareil
        
    return [titleRequest,res]


def ScreeningsTodayTomorrowCinema(namedGroups={}):
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    theaterName = (namedGroups.get("movie_theater_name1") if namedGroups.get("movie_theater_name1") is not None else "").rstrip().lower()
    # avoid problems
    if time =="" or theaterName =="":
        return 'You did not specify the time or the theatername'
    
    if time == "today":
        formatDate = getTimeDate(0, "days")
    elif time == "tomorrow":
        formatDate = getTimeDate(1, "days")
    else:
        return ""
    theater = 'cinema-' + theaterName.replace('é', 'e').replace(' ', '-')
    shows = getMovieTheaterShows(theater)
    all_shows = getAllShows()
    moviesTitles = {mov["slug"]:[mov["title"],mov["genres"]] for mov in all_shows} # 
    

    showTimes = {
        slug : [[str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").strftime('%H:%M')), res["version"], res["refCmd"]]for res in getMovieShowtimes(slug, theater, date=formatDate)]
        for slug, infos in shows.items()
        if infos["bookable"]
    }


    titleRequest = f'All Screenings available {time} ({formatDate}) in {theater}:\n'
    res = ""
    for slug,screenings in list(showTimes.items()):
        if screenings ==[]:
            showTimes.pop(slug)

    for slug in showTimes.keys(): 
        res += '\n'+ bold(moviesTitles[slug][0]) + ' - '+ str(moviesTitles[slug][1][0]) + '\n'
        vost = []
        vf = []

        for screen in showTimes[slug] : 
            if screen[1]=='vost':
                vost.append([screen[0],screen[2]])

            if screen[1]=="vf"  : 
                vf.append([screen[0],screen[2]])

        if len(vf) >=  1 : 
            res += 'VF'
            for v in vf : 
                res += ' | '+ hyperlink(v[0],v[1])
            res +='\n'
        if len(vost) >= 1 : 
            res +='VOST'
            for vst in vost : 
                res += ' | '+ hyperlink(vst[0],vst[1])
            res +='\n'
    return [titleRequest,res]



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
    all_shows = getAllShows()
    moviesTitles = {mov["slug"]:[mov["title"],mov["genres"]] for mov in all_shows} # 
    

    showTimes = {
        slug : [[str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").strftime('%H:%M')), res["version"], res["refCmd"]]for res in getMovieShowtimes(slug, theater, date=formatDate)]
        for slug, infos in shows.items()
        if infos["bookable"]
    }


    titleRequest = f'All Screenings available  in {date} days ({formatDate}) in {theater}:\n'
    res = ""
    for slug,screenings in list(showTimes.items()):
        if screenings ==[]:
            showTimes.pop(slug)

    for slug in showTimes.keys(): 
        res += '\n'+ bold(moviesTitles[slug][0]) + ' - '+ str(moviesTitles[slug][1][0]) + '\n'
        vost = []
        vf = []

        for screen in showTimes[slug] : 
            if screen[1]=='vost':
                vost.append([screen[0],screen[2]])

            if screen[1]=="vf"  : 
                vf.append([screen[0],screen[2]])

        if len(vf) >=  1 : 
            res += 'VF'
            for v in vf : 
                res += ' | '+ hyperlink(v[0],v[1])
            res +='\n'
        if len(vost) >= 1 : 
            res +='VOST'
            for vst in vost : 
                res += ' | '+ hyperlink(vst[0],vst[1])
            res +='\n'
    return [titleRequest,res]



          # all_shows_zone = getShowsZone(location)
    # all_shows = getAllShows()
    # moviesTitles = {mov["slug"]:[mov["title"],mov["genres"]] for mov in all_shows} # 
    # moviesSlugZone = { mov["slug"]:moviesTitles[mov["slug"]] for mov in all_shows_zone if mov["bookable"]}

    # res = f'Movies available {time} ( {formatDate} ) in {location}:\n' 
    # for slug, movietitle  in moviesSlugZone.items(): 
    #     res += '  **'+movietitle+'**  '+ '\n' #pareil
    # for slug, movieinfos in moviesSlugZone.items(): 
    #     res += '  **'+str(movieinfos[0])+'**  '+ ' | ' + str(movieinfos[1][0])+   f'https://www.cinemaspathegaumont.com/films/{slug}'+ '\n' #pareil
    # return res

    for mov in showsInfoDict.keys():
        res +='\n' +'> '+ bold(moviesTitles[mov][0]) + ' - '+ str(moviesTitles[mov][1][0]) + '\n'
        for theater in showsInfoDict[mov].keys():
            res += theater.replace('cinema','').replace('-',' ') +  '   ' + '  |  '.join(list(map(lambda x: str(datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S").strftime('%H:%M')), showsInfoDict[mov][theater])))  + '\n'
            #tmp = '  |  '.join(list(map(lambda x: str(datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S").strftime('%H:%M')), showsInfoDict[mov][theater])))
            #test += f"{bold(moviesTitles[mov][0])  : <10}{theater.replace('cinema','').replace('-',' ')} { tmp : >100}\n"
            # print(f"Unpacked list: {*a,}")

def MovieScreeningsTodayTomorrowCinema(namedGroups={}):
    movieName = (namedGroups.get("moviename2") if namedGroups.get("moviename2") is not None else "").rstrip()
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    theaterName = (namedGroups.get("movie_theater_name3") if namedGroups.get("movie_theater_name3") is not None else "").rstrip().lower()
    # avoid problems
    if movieName == "" or time == "" or theaterName == "":
        return None # à modifier avec le bon format..

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
        return "" # à modifier avec le bon format 
    theater = 'cinema-' + theaterName.replace('é', 'e').replace(' ', '-')

    showTimes = {
        theater : [[str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d %H:%M:')), res["version"], res["refCmd"]] for res in getMovieShowtimes(slug, theater, date=formatDate)] 
    
    }

    hasShowTimes = False
    for k, v in list(showTimes.items()):
        if v != []:
            hasShowTimes = True
            pass

    res =''
    if hasShowTimes:
        titleRequest = f'Screenings available for {movieName} in {time}  ({formatDate}) in {theater}:\n'
        
        res += '\n'+ cinemaOut(theater) +'\n'
        for theater in showTimes.keys(): 
            vost = []
            vf = []
    
            for screen in showTimes[theater] : 
                if screen[1]=='vost':
                    vost.append([screen[0],screen[2]])

                if screen[1]=="vf"  : 
                    vf.append([screen[0],screen[2]])

            if len(vf) >=  1 : 
                res += 'VF'
                for v in vf : 
                    res +=  '  '+ '['+v[0]+']' +'('+v[1] +')'
                res +='\n'
            if len(vost) >= 1 : 
                res +='VOST'
                for vst in vost : 
                    res += '  '+'['+vst[0]+']' +'('+vst[1] +')'
                res +='\n'
            return [titleRequest,res]
        
    else:
        return ["Recommendations",GetRecommendation(slug, theaterName)]



def MovieScreeningsDaysCinema(namedGroups={}):
    movieName = (namedGroups.get("moviename3") if namedGroups.get("moviename3") is not None else "").rstrip()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "").rstrip()
    theaterName = (namedGroups.get("movie_theater_name4") if namedGroups.get("movie_theater_name4") is not None else "").rstrip().lower()
    # avoid problems
    if movieName == "" or detail == "" or theaterName == "":
        return ['Error Screenings for a specific cinema','Oups ! Please check the cinema name, the date or the movie name ! ']

    if date == "":
        formatDate = getTimeDate(0, detail)
    else:
        formatDate = getTimeDate(int(date), detail)

    infos = getMovieInfos(apiSearch(movieName))
    if type(infos) == dict and "slug" in infos.keys():
        slug = infos["slug"]
    theater = 'cinema-' + theaterName.replace('é', 'e').replace(' ', '-')
    res = cinemaOut(theater) +'\n'
    for i in range(int(date)+1):
        formatDate = getTimeDate(int(i), detail)
        showTimes = {
            theater : [[str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d %H:%M:')), res["version"], res["refCmd"]] for res in getMovieShowtimes(slug, theater, date=formatDate)] 
        
        }

        # Check if all cinemas does not project this movie
        hasShowTimes = False
        for k, v in list(showTimes.items()):
            if v == []:
                showTimes.pop(k)
            if v != []:
                hasShowTimes = True
                pass
        
        if hasShowTimes:
            titleRequest = f'Screenings available for {movieName} in {date} days ({formatDate}) in {theater}:\n'
            

            for theater in showTimes.keys(): 
                vost = []
                vf = []
        
                for screen in showTimes[theater] : 
                    if screen[1]=='vost':
                        vost.append([screen[0],screen[2]])
    
                    if screen[1]=="vf"  : 
                        vf.append([screen[0],screen[2]])

                if len(vf) >=  1 : 
                    res += 'VF'
                    for v in vf : 
                        res +=  '  '+ '['+v[0]+']' +'('+v[1] +')'
                    res +='\n'
                if len(vost) >= 1 : 
                    res +='VOST'
                    for vst in vost : 
                        res += '  '+'['+vst[0]+']' +'('+vst[1] +')'
                    res +='\n'
        else:
            res+= GetRecommendation(slug, theaterName)
    return [titleRequest,res]
    



def AllScreeningsDaysLocation(namedGroups={}):
    location = (namedGroups.get("location6") if namedGroups.get("location6") is not None else "").rstrip().lower()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "").rstrip()
    # avoid problems
    if location == "" or detail == "":
        return [ 'Error All screening with specific dates and location', "Please verify the date and location"]

    if date == "":
        formatDate = getTimeDate(0, detail)
    else:
        formatDate = getTimeDate(int(date), detail)
    
    all_shows_zone = getShowsZone(location)
    all_shows = getAllShows()

    movieSlug = [mov["slug"] for mov in all_shows_zone if mov["bookable"]]
    moviesTitles = {mov["slug"]:[mov["title"],mov["genres"]] for mov in all_shows}
    showsInfoDict = {}
    if detail == "days":
        showsInfoDict = {
            movieName : {movieTheater : getMovieShowtimes(movieName, movieTheater, date=formatDate) for movieTheater in CINEMA_DICT[location]}
            for movieName in movieSlug
        }
  
    titleRequest = f'Movie shows available in {date} {detail} ( {formatDate} ) in {location}:\n' 
    for mov in list(showsInfoDict.keys()):
        for theater,screenings in list(showsInfoDict[mov].items()):
            if screenings == [] or screenings =='':
               showsInfoDict[mov].pop(theater)
        if showsInfoDict[mov]=={} or showsInfoDict[mov]==None : 
            showsInfoDict.pop(mov)

    for mov in showsInfoDict.keys():
        res +='\n' +'> '+ bold(moviesTitles[mov][0]) + ' - '+ str(moviesTitles[mov][1][0]) + '\n'
        for theater in showsInfoDict[mov].keys():
            res += theater.replace('cinema','').replace('-',' ') +  '   ' + '  |  '.join(list(map(lambda x: str(datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S").strftime('%H:%M')), showsInfoDict[mov][theater])))  + '\n'
            #tmp = '  |  '.join(list(map(lambda x: str(datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S").strftime('%H:%M')), showsInfoDict[mov][theater])))
            #test += f"{bold(moviesTitles[mov][0])  : <10}{theater.replace('cinema','').replace('-',' ')} { tmp : >100}\n"
            # print(f"Unpacked list: {*a,}")
            
    return [titleRequest,res]
    

  

def AllScreeningsTodayTomorrowLocation(namedGroups={}):
    location = (namedGroups.get("location5") if namedGroups.get("location5") is not None else "").rstrip().lower()
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    # avoid problems
    if location == "" or time == "":
        return ['Error all screenings today/tomorrow with location', ' I am sorry your location name seems to be wrong !']

    if time == "today":
        formatDate = getTimeDate(0, "days")
    elif time == "tomorrow":
        formatDate = getTimeDate(1, "days")
    else:
        return ["Error dateformat All screenings","Something happens with the date format O_o"]

    all_shows_zone = getShowsZone(location)
    all_shows = getAllShows()

    movieSlug = [mov["slug"] for mov in all_shows_zone if mov["bookable"]]
    moviesTitles = {mov["slug"]:[mov["title"],mov["genres"]] for mov in all_shows}
    showsInfoDict = {
        movieName : {movieTheater : getMovieShowtimes(movieName, movieTheater, date=formatDate) for movieTheater in CINEMA_DICT[location]}
        for movieName in movieSlug
    }
    test = f'**Screenings available {time} ({formatDate}) in {location}:**\n' 
  
    titleRequest= f'Screenings available {time} ( {formatDate} ) in {location}:\n' 
    for mov in list(showsInfoDict.keys()):
        for theater,screenings in list(showsInfoDict[mov].items()):
            if screenings == [] or screenings =='':
               showsInfoDict[mov].pop(theater)
        if showsInfoDict[mov]=={} or showsInfoDict[mov]==None : 
            showsInfoDict.pop(mov)

    for mov in showsInfoDict.keys():
        res +='\n' +'> '+ bold(moviesTitles[mov][0]) + ' - '+ str(moviesTitles[mov][1][0]) + '\n'
        for theater in showsInfoDict[mov].keys():
            res += theater.replace('cinema','').replace('-',' ') +  '   ' + '  |  '.join(list(map(lambda x: str(datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S").strftime('%H:%M')), showsInfoDict[mov][theater])))  + '\n'
            #tmp = '  |  '.join(list(map(lambda x: str(datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S").strftime('%H:%M')), showsInfoDict[mov][theater])))
            #test += f"{bold(moviesTitles[mov][0])  : <10}{theater.replace('cinema','').replace('-',' ')} { tmp : >100}\n"
            # print(f"Unpacked list: {*a,}")
            
    return [titleRequest,res]
def bold(string):
    return f"**{string}**"
def cinemaOut(string):
    return string.replace('cinema','').replace('-',' ')
def hyperlink(string,url):
    return '['+string+']'+'('+url+')'

    # all_shows_zone = getShowsZone(location)
    # all_shows = getAllShows()
    # moviesTitles = {mov["slug"]:[mov["title"],mov["genres"]] for mov in all_shows} # 
    # moviesSlugZone = { mov["slug"]:moviesTitles[mov["slug"]] for mov in all_shows_zone if mov["bookable"]}

    # res = f'Movies available {time} ( {formatDate} ) in {location}:\n' 
    # for slug, movietitle  in moviesSlugZone.items(): 
    #     res += '  **'+movietitle+'**  '+ '\n' #pareil
    # for slug, movieinfos in moviesSlugZone.items(): 
    #     res += '  **'+str(movieinfos[0])+'**  '+ ' | ' + str(movieinfos[1][0])+   f'https://www.cinemaspathegaumont.com/films/{slug}'+ '\n' #pareil
    # return res

 
def MovieScreeningsTodayTomorrowLocation(namedGroups={}):
    movieName = (namedGroups.get("moviename4") if namedGroups.get("moviename4") is not None else "").rstrip()
    time = (namedGroups.get("time") if namedGroups.get("time") is not None else "").rstrip().lower()
    location = (namedGroups.get("location3") if namedGroups.get("location3") is not None else "").rstrip().lower()
    # avoid problems
    if movieName == "" or time == "" or location == "":
        return ["Error screenings today/tomorrow with a specific location" ," Bruhh ! You didn't specify a movie name or location and the day !(today | tomorrow)"]

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
        return "" # C QUOI CE RETURN ANTOINE WESH 
    city = location.replace('é', 'e').replace(' ', '-')
    movieTheaters = CINEMA_DICT.get(city)

    showTimes = {
        theater : [[str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").strftime('%H:%M')), res["version"], res["refCmd"]] for res in getMovieShowtimes(slug, theater, date=formatDate)]
        for theater in movieTheaters
    }

    # Check if all cinemas does not project this movie
    hasShowTimes = False
    for k, v in list(showTimes.items()):
        if v == []:
            showTimes.pop(k)
        if v != []:
            hasShowTimes = True
            pass

    if hasShowTimes:
        titleRequest = f'Screenings available for {movieName} in {time} ({formatDate}) in {location}:\n'
        res = ""
        for theater in showTimes.keys(): 
            res += cinemaOut(theater) +'\n'
            vost = []
            vf = []
    
            for screen in showTimes[theater] : 
                if screen[1]=='vost':
                    vost.append([screen[0],screen[2]])
   
                if screen[1]=="vf"  : 
                    vf.append([screen[0],screen[2]])

            if len(vf) >=  1 : 
                res += 'VF'
                for v in vf : 
                    res += ' '+ hyperlink(v[0],v[1])
                res +='\n'
            if len(vost) >= 1 : 
                res +='VOST'
                for vst in vost : 
                    res += '  '+ hyperlink(vst[0],vst[1])
                res +='\n'
        return [titleRequest,res]
        
    else:
        return ['Recommendations', GetRecommendation(slug)] # Hugo c'est quel type de recommendation ici ? 


def MovieScreeningsDaysLocation(namedGroups={}):
    location = (namedGroups.get("location4") if namedGroups.get("location4") is not None else "").rstrip().lower()
    movieName = (namedGroups.get("moviename5") if namedGroups.get("moviename5") is not None else "").rstrip()
    date = (namedGroups.get("date") if namedGroups.get("date") is not None else "")
    detail = (namedGroups.get("detail") if namedGroups.get("detail") is not None else "").rstrip()
    # avoid problems
    if location == "" or detail == "" or movieName == "":
        return [' Error Screenings for a movie within X days and specific location',' Please verify your movie name, location and that days dont exceed 14 days forecast']

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
        theater : [[str(datetime.strptime(res["time"], "%Y-%m-%d %H:%M:%S").strftime('%H:%M')), res["version"], res["refCmd"]] for res in getMovieShowtimes(slug, theater, date=formatDate)]
        for theater in movieTheaters
    }

    # Check if all cinemas does not project this movie
    hasShowTimes = False
    for k, v in list(showTimes.items()):
        if v == []:
            showTimes.pop(k)
        if v != []:
            hasShowTimes = True
            pass
    
    if hasShowTimes:
        titleRequest = f'Screenings available for {movieName} in {date} days ({formatDate}) in {location}:\n'
        res = ""
   
        for theater in showTimes.keys(): 
            res += cinemaOut(theater) +'\n'
            vost = []
            vf = []
    
            for screen in showTimes[theater] : 
                if screen[1]=='vost':
                    vost.append([screen[0],screen[2]])
   
                if screen[1]=="vf"  : 
                    vf.append([screen[0],screen[2]])

            if len(vf) >=  1 : 
                res += 'VF'
                for v in vf : 
                    res +=  '  '+ '['+v[0]+']' +'('+v[1] +')'
                res +='\n'
            if len(vost) >= 1 : 
                res +='VOST'
                for vst in vost : 
                    res += '  '+'['+vst[0]+']' +'('+vst[1] +')'
                res +='\n'
        return [titleRequest,res]
        

    else:
        return ["Recommendations",GetRecommendation(slug)]



# Get the most liked movies actually on screen
def GetTrend(namedGroups={}, trending_index=15):
    check = (namedGroups.get("trend") if namedGroups.get("trend") is not None else "")
    # avoid problems
    if check == "":
        return ['Error trend',' I didnt find anythings ! ']

    all_movies = getAllShows()
    list_likes = []

    for m in all_movies:
        m_infos = getMovieInfos(m["slug"])
        like_score = m_infos["feelings"]["countEmotionLike"] + 2*m_infos["feelings"]["countEmotionLove"] - m_infos["feelings"]["countEmotionDisappointed"]
        if(m_infos["next24ShowtimesCount"] != 0):
            list_likes.append([like_score, m["title"]])

    list_likes.sort(reverse=True)
    trending = list_likes[:trending_index]

    titleRequest = f'Current trending movies are :\n'
    res += '\n'.join(trending[i][1] + '\t' + 'with a like score of ' + str(trending[i][0]) for i in range(len(trending)))
    return [titleRequest,res]


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
    genres= [
        'Action', 'Animation', 'Aventure', 'Biopic', 'Comédie', 'Comédie dramatique',
        'Comédie musicale', 'Comédie romantique', 'Court métrage', 'Divers', 'Documentaire', 'Drame',
        'Drame psychologique', 'Famille', 'Fantastique', 'Film musical', 'Guerre', 'Historique',
        'Horreur / Epouvante', 'Policier / Espionnage', 'Romance', 'Science Fiction', 'Thriller',  'Western'
    ]
    titleRequest="** The Gaumont *genre* colllection** : \n\n"
    str =''
    for i in range(int(len(genres)/5+1)):
        str+='  |  '.join(genres[i*5:(i+1)*5])+ "\n"  
    return [titleRequest,'[like so.](https://example.com)']


    # shows = getAllShows()
    # genres = set() 
    # for show in shows : 
    #       genres.add(show["genres"][0])
    # genres_sorted = sorted([genre for genre in genres if genre!='Non défini'])
    # str="** The Gaumont *genre* colllection** : \n\n"
    # for i in range(int(len(genres_sorted)/5+1)):
    #     str+='  |  '.join(genres_sorted[i*5:(i+1)*5])+ "\n"  
    # return str

