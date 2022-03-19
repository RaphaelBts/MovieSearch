patternList = [
    ### Zone basique ##############################################################################################################
    {
        'pattern' : '\\b(?P<greeting>[H-h]i|[H-h]ello|[H-h]ey|[G-g]ood morning|[G-g]ood afternoon)\\b',
        'intent' : 'Hello'
        # done + tested
    }, 
    {
        'pattern' :'\\b(bye|exit|finish|end|stop)\\b',
        'intent' : 'Exit'
        # done + tested : trigger la deco du bot (quand migré sur serveur)
    },
    {
        'pattern' : '\\b([H-h]elp(s)?|Aide(s)?|Command(s)?)\\b',
        'intent' : 'Help'
        # done + tested
    },
    ### Zone   ##########################################################################################################
    {
        'pattern': '(.*[I-i]nfo(s)?|[I-i]nformation(s)?)\\s(about|on)\\s(the\\s(film(s)?|movie(s)?)\\s)?(?P<moviename>\\w+(\\s\\w+)*)',
        'intent': 'Movie info'
        # done + tested + quasi form  ################################# WARNING PATTERN PAS TOTALEMENT BLINDE il prends pas les points je crois (il etait une fois...)
    },
    {
        'pattern':'.*(?P<greeting>[F-f]ilm(s)?|[M-m]ovie(s)?)\\s(with|play by|played by)\\s?(the\\sactor)?\s(Mr|Mrs)?(\\.)?(?P<actor>.*)',
        'intent': 'Movie by actor'
        # done + tested + quasi forme++  (je rajouterai peut etre le genre... en bonus) et date un peu useless...
        # movies with actor Tom Holland not working (the !!!) = resolved 
    },
    {
        'pattern':'.*(?P<greeting>[F-f]ilm(s)?|[M-m]ovie(s)?)\\s(directed by|directed|by)\\s?(the\\sdirector)?\\s(Mr|Mrs)?(\\.)?(?P<director>.*)',
        'intent': 'Movie by director'
        # done + tested + quasi forme++
        # added extra queries
    },
    
    # ancien pattern , obsolete '.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(directed\\sby)\\s(the\\sdirector)?(Mr|Mrs)?(\\.)?(?P<director>.*)'
    ##############################################################################################################
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\sscreen)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?)\\s*(in\\s*)?(?P<location>\\w+(\\s\\w+)*)',
        'intent': 'Tous les films dispo dans x jour à la localisation y' # authorized date : in x days (maximum 14 days)
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\s*screen)\\s*(at\\s*|in\\s*)?(?P<location>\\w+(\\s\\w+)*)\\s(?P<time>now|today|currently)',
        'intent': 'Available films today by location' # location = city   
        # done
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\s*screen)\\s*(at\\s*|in\\s*)?(?P<location>\\w+(\\s\\w+)*)',
        'intent': 'Available films today by location' # location = city  # l'utilisateur peut niquer le bot en rajoutant tomorrow et d'autres champs apres le lieu...=>trigger ce pattern
        # done 
    },
    ### Zone movie theater ##########################################################################################################
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name>[P-p]athé.*|[G-g]aumont.*)',
        'intent': 'All movie screening today/tomorrow in cinema ...' # date : today or tomorrow 
        # done
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name>[P-p]athé.*|[G-g]aumont.*)',
        'intent': 'All movie screening in ... days in cinema ...' # authorized date : in x days (maximum 14 days)
        # done
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*((of|for)(\sthe)?(\s(film|movie)?))\\s*(?P<moviename>.*)\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name>[P-p]athé.*|[G-g]aumont.*)',
        'intent': 'Movie screening for movie ... today/tomorrow in cinema ...' # date : today or tomorrow only
        # done
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*((of|for)(\sthe)?(\s(film|movie)?))\\s*(?P<moviename>.*)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name>[P-p]athé.*|[G-g]aumont.*)',
        'intent': 'Movie screening for movie ... in ... days in cinema ...' # authorized date : in x days (maximum 14 days)
        # done
    },
    ##############################################################################################################
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))\\s*((of|for)(\sthe)?(\s(film|movie)?))\\s*(?P<moviename>.*)\\s*(?P<day>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Nom Film x ajd/demain à la localisation z' # date : today or tommorow only 
        # on veut quoi ? tous les films ? car on donne le nom d'un film
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))\\s*((of|for)(\sthe)?(\s(film|movie)?))\\s*(?P<moviename>.*)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Nom Film x dans y jours à la localisation z' # date :  in x days (maximum 14 days)
        # on veut quoi ? tous les films ? car on donne le nom d'un film
    },
    ##############################################################################################################

    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*((of|for)(\sthe)?(\s(film|movie)?))\\s*(?P<moviename>.*)\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Movie screening for movie ... today/tomorrow in ...' # date : today or tomorrow 
        # done
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*((of|for)(\\sthe)?(\\s(film|movie)?))\\s*(?P<moviename>.*)\\s*in\\s*(?P<date>\\d*)\s*(?P<detail>day(s)?)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Movie screening for movie ... in ... days in ...' # authorized date : in x days (maximum 14 days)
        # done
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'All movies screening today/tomorrow in ...' # date : today or tomorrow 
        # done
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'All movies screening in ... days in ...' # authorized date : in x days (maximum 14 days)
        # done
    },
    ##############################################################################################################
    {
        'pattern':'.*\\s*(event)\\s*.*',
        'intent': 'Event'
        # done
    },
    {
        'pattern':'.*\\s*(coming\\s*soon)\\s*.*',
        'intent': 'Coming soon'
        # done  mise en forme quasi done
    },
    {
        'pattern':'.*\\s*(list(s)?\\s*of\\s*genre(s)?)\\s*.*',
        'intent': 'List of genres'
    },   #done mise en forme quasi done 
    {
        'pattern':'(?P<type>.*)([F-f]ilm(s)?|[M-m]ovie(s)?)',
        'intent': 'Movie by type'
        # done pas capté la plus value
    }
        

    #PRENDRE EN COMPTE LES ESPACES OUBLIES ET ACCIDENTELS
    # RAJOUTER : LIST ALL CINEMAS ZONE X je sais que c'est faisable masi faut trifouiller 
    # rajouter pattern : !helps / commands = > la réponse renvoie la liste des fonctions (list of genres, events, coming soon etc on fait un truc propre qui explique les différentes fonctions et la typographie)
    ]
