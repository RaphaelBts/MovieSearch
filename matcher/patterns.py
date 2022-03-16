patternList = [
    {
        'pattern' : '\\b(?P<greeting>[H-h]i|[H-h]ello|[H-h]ey|[G-g]ood morning|[G-g]ood afternoon)\\b',
        'intent' : 'Hello'
        # done
    }, 
    {
        'pattern' :'\\b(bye|exit|finish|end|stop)\\b',
        'intent' : 'Exit'
        # done
    },
    {
        'pattern' : '\\b(Help|Helps|Aide|Aides)\\b',
        'intent' : 'Help'
        # done
    },


    {
        'pattern': '(.*\\s[I-i]nfo(s)?|[I-i]nformation(s)?)\\s(about|on)\\s(the\\s(film(s)?|movie(s)?)\\s)?(?P<moviename>\\w+(\\s\\w+)*)',
        'intent': 'Movie info'
        # done
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s(with)\\s(the\\sactor)?(Mr|Mrs)?(\\.)?(?P<actor>.*)',
        'intent': 'Movie by actor'
        # done
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(directed\\sby)\\s(the\\sdirector)?(Mr|Mrs)?(\\.)?(?P<director>.*)',
        'intent': 'Movie by director'
        # done
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\sscreen)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*(in\\s*)?(?P<location>\\w+(\\s\\w+)*)',
        'intent': 'Films dispo dans x jour/heure à la localisation y' # authorized date : in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\s*screen)\\s*(at\\s*|in\\s*)?(?P<location>\\w+(\\s\\w+)*)\\s(?P<time>now|today|currently)',
        'intent': 'Available films today by location'
        # done
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\s*screen)\\s*(at\\s*|in\\s*)?(?P<location>\\w+(\\s\\w+)*)',
        'intent': 'Available films today by location'
        # done
    },

    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<moviename>.*)\\s*(?P<day>today|tomorrow)\\s*at\\s*(?P<time>\\d*)(pm|am)?\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Film x ajd/demain à heure y au cinéma z' # date : today or only 
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<moviename>.*)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*at\\s*(?P<time>\\d*)(pm|am)?\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Film x dans y jours à heure z au cinéma zz' # date :  in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },

    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<moviename>.*)\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name>Pathé.*|Gaumont.*)',
        'intent': 'Seances film x cinema y' # date : today or tomorrow only
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<moviename>.*)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name>Pathé.*|Gaumont.*)',
        'intent': 'Seances film x cinema y' # authorized date : in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },

    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<moviename>.*)\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Seances film x localisation (ville) y' # date : today or tomorrow 
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<moviename>.*)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Seances film x localisation (ville) y' # authorized date : in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },
    
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Toutes les seances localisation x' # date : today or tomorrow 
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Toutes les seances localisation y' # authorized date : in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },
    
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name>Pathé.*|Gaumont.*)',
        'intent': 'Toutes les seances cinema x' # date : today or tomorrow 
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name>Pathé.*|Gaumont.*)',
        'intent': 'Toutes les seances cinema x' # authorized date : in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },


    {
        'pattern':'.*\\s*(event)\\s*.*',
        'intent': 'Event'
        # done
    },
    {
        'pattern':'.*\\s*(coming\\s*soon)\\s*.*',
        'intent': 'Coming soon'
        # done
    },
    {
        'pattern':'.*\\s*(list(s)?\\s*of\\s*genre(s)?)\\s*.*',
        'intent': 'List of genres'
    },
    {
        'pattern':'(?P<type>.*)([F-f]ilm(s)?|[M-m]ovie(s)?)',
        'intent': 'Movie by type'
        # done
    }

    #PRENDRE EN COMPTE LES ESPACES OUBLIES ET ACCIDENTELS
    ]
