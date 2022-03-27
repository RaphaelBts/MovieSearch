patternList = [
    ### Zone basique ##############################################################################################################
    {
        'pattern' : '\\b(?P<greeting>[H-h]i|[H-h]ello|[H-h]ey|[G-g]ood morning|[G-g]ood afternoon)\\b',
        'intent' : 'Hello'
        # Over
    }, 
    {
        'pattern' :'\\b(bye|exit|finish|end|stop)\\b',
        'intent' : 'Exit'
        #Over
    },
    {
        'pattern' : '\\b([H-h]elp(s)?|Aide(s)?|Command(s)?)\\b',
        'intent' : 'Help'
        # done + tested => modif (en liste des commandes) 
    },
    ### Zone   ##########################################################################################################
    {
        'pattern': '(.*[I-i]nfo(s)?|[I-i]nformation(s)?)\\s(about|on)\\s(the\\s(film(s)?|movie(s)?)\\s)?(?P<moviename1>\\w+(\\s\\w+)*)',
        'intent': 'Movie info'
        # over 
    },
    {
        'pattern':'.*(?P<greeting>[F-f]ilm(s)?|[M-m]ovie(s)?)\\s(with|play by|played by)\\s?(the\\sactor)?\\s(Mr|Mrs)?(\\.)?(?P<actor>.*)',
        'intent': 'Movie by actor'
        # over
    },
    {
        'pattern':'.*(?P<greeting>[F-f]ilm(s)?|[M-m]ovie(s)?)\\s(directed by|directed|by)\\s?(the\\sdirector)?\\s(Mr|Mrs)?(\\.)?(?P<director>.*)',
        'intent': 'Movie by director'
        # over
 
    },
    
    ##############################################################################################################
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\sscreen)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?)\\s*(in\\s*)?(?P<location1>\\w+(\\s\\w+)*)',
        'intent': 'Available films in ... days by location' # authorized date : in x days (maximum 14 days) # il faut inverser date et location (pr que ca soit conforme à tous les autres)
    },   # over
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\s*screen)\\s(?P<time>now|today|currently|tomorrow)\\s*(at\\s*|in\\s*)?(?P<location2>\\w+(\\s\\w+)*)',
        'intent': 'Available films today/tomorrow by location' # location = city   
        # over
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\s*screen)\\s*(at\\s*|in\\s*)?(?P<location2>\\w+(\\s\\w+)*)',
        'intent': 'Available films today/tomorrow by location' # location = city  # l'utilisateur peut niquer le bot en rajoutant tomorrow et d'autres champs apres le lieu...=>trigger ce pattern
        # over
    },
    ### Zone movie theater ##########################################################################################################
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name1>[P-p]athé.*|[G-g]aumont.*)',
        'intent': 'All movie screening today/tomorrow in cinema ...' # date : today or tomorrow 
        # over
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name2>[P-p]athé.*|[G-g]aumont.*)',
        'intent': 'All movie screening in ... days in cinema ...' # authorized date : in x days (maximum 14 days)
        # over
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*((of|for)(\\s)?(the\\s*film|the\\s*movie)?)\\s*(?P<moviename2>.*)\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name3>[P-p]athé.*|[G-g]aumont.*)',
        'intent': 'Movie screening for movie ... today/tomorrow in cinema ...' # date : today or tomorrow only
        # over
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*((of|for)(\\s)?(the\\s*film|the\\s*movie)?)\\s*(?P<moviename3>.*)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name4>[P-p]athé.*|[G-g]aumont.*)',
        'intent': 'Movie screening for movie ... in ... days in cinema ...' # authorized date : in x days (maximum 14 days) ya écrit max 14 days mais on check jamais ca 
        #upgraded fait de day 0 to day x...
        # done + tested  QUI A OSE DIRE TESTED YA VLA CONFLIT AVEC  LOCATION 4 faut rajouter un identifiant cinema optionnel  : screening for uncharted in 2 days in cinema alesia 
    },
    ##############################################################################################################
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*((of|for)(\\s)?(the\\s*film|the\\s*movie)?)\\s*(?P<moviename4>.*)\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<location3>.*)',
        'intent': 'Movie screening for movie ... today/tomorrow in ...' # date : today or tomorrow 
        # done + tested + FORM 
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*((of|for)(\\s)?(the\\s*film|the\\s*movie)?)\\s*(?P<moviename5>.*)\\s*in\\s*(?P<date>\\d*)\s*(?P<detail>day(s)?)\\s*(at\\s*|in\\s*)?(?P<location4>.*)',
        'intent': 'Movie screening for movie ... in ... days in ...' # authorized date : in x days (maximum 14 days)
        # done + tested + form PARFAITE =) 
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<location5>.*)',
        'intent': 'All movies screening today/tomorrow in ...' # date : today or tomorrow 
        # done + tested + form 
    },
    {
        'pattern':'(.*([M-m]ovie(s)?|[S-s]creening(s)?))\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?)\\s*(at\\s*|in\\s*)?(?P<location6>.*)',
        'intent': 'All movies screening in ... days in ...' # authorized date : in x days (maximum 14 days)
        # done + form + A RETESTE !
    },
    ##############################################################################################################
    {
        'pattern':'.*\\s*([E-e]vent)\\s*.*',
        'intent': 'Event'
        # done à refaire nan ? 
    },
    {
        'pattern':'.*\\s*(?P<trend>[M-m]ost\\spopular\\smovies|[R-r]ecommendation|[M-m]ost\\sliked\\smovies|[T-t]rending\\smovies)\\s*.*',
        'intent': 'Get trend'
    },
    {
        'pattern':'.*\\s*(coming\\s*soon)\\s*.*',
        'intent': 'Coming soon'
        # done  mise en forme quasi done
    },
    {
        'pattern':'.*\\s*([L-l]ist(s)?\\s*of\\s*genre(s)?)\\s*.*',
        'intent': 'List of genres'
    },   #done mise en forme quasi done 
    {
        'pattern':'(?P<type>\\w+)\\s([F-f]ilm(s)?|[M-m]ovie(s)?)',
        'intent': 'Movie by type'
        # done 
    }
        

    #PRENDRE EN COMPTE LES ESPACES OUBLIES ET ACCIDENTELS
    # Clean les titres = mettre la date tout à la fin essayer d'enlever le bold.. 
    # rajouter pattern : !helps / commands = > la réponse renvoie la liste des fonctions (list of genres, events, coming soon etc on fait un truc propre qui explique les différentes fonctions et la typographie)
    ]
