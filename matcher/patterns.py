patternList = [
    {
        'pattern' : '\\b(?P<greeting>[H-h]i|[H-h]ello|[H-h]ey|[G-g]ood morning|[G-g]ood afternoon)\\b',
        'intent' : 'Hello'
    }, 
    {
        'pattern' :'\\b(bye|exit|finish|end|stop)\\b',
        'intent' : 'Exit'
    },
    {
        'pattern' : '\\b(Help|Helps|Aide|Aides)\\b',
        'intent' : 'Help'
    },


    {
        'pattern': '(.*\\s[I-i]nfo(s)?|[I-i]nformation(s)?)\\s(about|on)\\s(the\\s(film(s)?|movie(s)?)\\s)?(?P<moviename>\\w+(\\s\\w+)*)',
        'intent': 'Movie info'
    },
    {
        'pattern':'(?P<type>.*)([F-f]ilm(s)?|[M-m]ovie(s)?)',
        'intent': 'Movie by type'
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s(with)\\s(the\\sactor)?(Mr|Mrs)?(\\.)?(?P<actor>.*)',
        'intent': 'Films joue par x'
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(directed\\sby)\\s(the\\sdirector)?(Mr|Mrs)?(\\.)?(?P<director>.*)',
        'intent': 'Films dirige par x'
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\sscreen)\\s*(?P<date>today|now|currently)',
        'intent': 'Films dispo ajd' # authorized date : today, now
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\sscreen)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)',
        'intent': 'Films dispo dans jour/heure x' # authorized date : in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\sscreen)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*(in\\s*)?(?P<location>\\w+(\\s\\w+)*)',
        'intent': 'Films dispo dans x jour/heure à la localisation y' # authorized date : in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\sscreen)\\s*(in\\s)?(?P<location>\\w+(\\s\\w+)*)\\s(?P<time>now|today|currently)',
        'intent': 'Films dispo localisation x ajd'
    },
    {
        'pattern':'.*([F-f]ilm(s)?|[M-m]ovie(s)?)\\s*(available|on\\sscreen)\\s(in\\s)?(?P<location>\\w+(\\s\\w+)*)',
        'intent': 'Films dispo localisation x' # date : today only
    },

    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<movie_name>.*)\\s*(?P<day>today|tomorrow)\\s*at\\s*(?P<time>\\d*)(pm|am)?\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Film x ajd/demain à heure y au cinéma z' # date : today or only 
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<movie_name>.*)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*at\\s*(?P<time>\\d*)(pm|am)?\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Film x ajd/demain à heure y au cinéma z' # date :  in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<movie_name>.*)\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name>Pathé.*|Gaumont.*)',
        'intent': 'Seances film x cinema y' # date : today or tomorrow only
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<movie_name>.*)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*(at\\s*|in\\s*)?(?P<movie_theater_name>Pathé.*|Gaumont.*)',
        'intent': 'Seances film x cinema y' # authorized date : in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<movie_name>.*)\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Seances film x localisation (ville) y' # date : today or tomorrow 
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<movie_name>.*)\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Seances film x localisation (ville) y' # authorized date : in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*(?P<time>today|tomorrow)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Toutes les seances cinema x' # date : today or tomorrow 
    },
    {
        'pattern':'(.*([F-f]ilm(s)?|[M-m]ovie(s)?))?\\s*in\\s*(?P<date>\\d*)\\s*(?P<detail>day(s)?|hour(s)?|week(s)?)\\s*(at\\s*|in\\s*)?(?P<location>.*)',
        'intent': 'Toutes les seances cinema x' # authorized date : in x days (maximum 14 days), in x hours (maximum 24 hours), in x weeks (maximum 2 weeks)
    },


    #PRENDRE EN COMPTE LES ESPACES OUBLIES ET ACCIDENTELS



    # {
    #     'pattern':'',
    #     'intent': 'Event'
    # },
    # {
    #     'pattern':'',
    #     'intent': 'Prochaines sorties'
    # },
    # {
    #     'pattern':'',
    #     'intent': 'Prochaines seances tout film confondu aujourd\'hui'
    # },
    ]

    
#     # Current Weather 4 "pattern"s
#     {
#         "pattern" : '\\b(weather)\\s(like\\s)*in\\s\\b(?<city>[A-Za-z]+([A-Za-z]+)?)\\s\\b(?<time>now|today|currently)',
#         "intent" : 'Current weather'
#     },{
#     "pattern" : '\\b(weather)\\s(like\\s)*\\b(?<city>[A-Za-z]+([A-Za-z]+)?)\\s\\b(?<time>now|today|currently)',
#     "intent" : 'Current weather'
#     },{
#     "pattern" : '\\b(?<time>current)\\s\\b(weather)\\sin\\s\\b(?<city>[A-Za-z\\s]+)',
#     "intent" : 'Current weather'
#     },{
#     "pattern":'\\b(?<time>current)\\s\\b(weather)\\s\\b(?<city>[A-Za-z\\s]+)',
#     "intent" : 'Current weather'

#     # Forecast weather 
#     },{
#     "pattern" : '\\b(weather)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
#     "intent" : 'Forecast tomorrow weather'
#     },{
#     "pattern" : '\\b(weather)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
#     "intent" : 'Forecast tomorrow weather'
#     },{
#     "pattern" : '\\b(weather)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
#     "intent" :'Forecast weather'
#     },{
#     "pattern" : '\\b(weather)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
#     "intent" : 'Forecast weather'
#     },



#     # Current temperature

#     # xxx temperature in city now/today/currently
#     # xxx temperature city now/today/currently
#     # xxx current temperature in city
#     # xxx current temperature city
#     {
#     "pattern" : '\\b(temperature)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>now|today|currently)',
#     "intent" : 'Current temperature'
#     },{
#     "pattern" : '\\b(temperature)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>now|today|currently)',
#     "intent" : 'Current temperature'
#     },{
#     "pattern" : '\\b(?<time>current)\\s\\b(temperature)\\sin\\s\\b(?<city>[A-Za-z\\s]+)',
#     "intent" : 'Current temperature'
#     },{
#     "pattern" : '\\b(?<time>current)\\s\\b(temperature)\\s\\b(?<city>[A-Za-z\\s]+)',
#     "intent" : 'Current temperature'
#     },



#     # Forecast temperature:

#     # xxx temperature in city tomorrow
#     # xxx temperature city tomorrow
#     # xxx temperature in city in number days/hours
#     # xxx temperature city in number days/hours
#     {
#     "pattern" : '\\b(temperature)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
#     "intent" : 'Forecast tomorrow temperature'
#     },{
#     "pattern" :'\\b(temperature)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
#     "intent" : 'Forecast tomorrow temperature'
#     },{
#     "pattern" : '\\b(temperature)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
#     "intent" : 'Forecast temperature'
#     },{
#     "pattern" : '\\b(temperature)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
#     "intent" : 'Forecast temperature'
#     },
    


#     # Current air pollution:

#     # xxx air pollution in city now/today/currently
#     # xxx air pollution city now/today/currently
#     # xxx current air pollution in city
#     # xxx current air pollution city
#     {
#     "pattern" : '\\b(air pollution|quality)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>now|today|currently)',
#     "intent" : 'Current air quality'
#     },{
#     "pattern" : '\\b(air pollution|quality)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>now|today|currently)',
#     "intent" : 'Current air quality'
#     },{
#     "pattern" : '\\b(?<time>current)\\s\\b(air pollution|quality)\\sin\\s\\b(?<city>[A-Za-z\\s]+)',
#     "intent" :'Current air quality'
#     },{
#     "pattern" : '\\b(?<time>current)\\s\\b(air pollution|quality)\\s\\b(?<city>[A-Za-z\\s]+)',
#     "intent" : 'Current air quality'
#     },
    
    
    
#     # Forecast air pollution:

#     # xxx air pollution in city tomorrow
#     # xxx air pollution city tomorrow
#     # xxx air pollution in city in number days/hours
#     # xxx air pollution city in number days/hours
#     {
#     "pattern" : '\\b(air pollution|quality)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
#     "intent" : 'Forecast tomorrow air quality'
#     },{
#     "pattern" : '\\b(air pollution|quality)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
#     "intent" :'Forecast tomorrow air quality'
#     },{
#     "pattern" : '\\b(air pollution|quality)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
#     "intent" : 'Forecast air quality'
#     },{
#     "pattern" : '\\b(air pollution|quality)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
#     "intent" : 'Forecast air quality'
#     },
    
#     # Current uv index
#     {
#     "pattern" : '\\b(uv index|score)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za-z]+)?)\\s\\b(?<time>now|today|currently)',
#     "intent" : 'Current uv index'
#     },{
#     "pattern" : '\\b(uv index|score)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za-z]+)?)\\s\\b(?<time>now|today|currently)',
#     "intent" : 'Current uv index'
#     },{
#     "pattern" : '\\b(?<time>current)\\s\\b(uv index|score)\\sin\\s\\b(?<city>[A-Za-z\\s]+)',
#     "intent" :'Current uv index'
#     },{
#     "pattern" : '\\b(?<time>current)\\s\\b(uv index|score)\\s\\b(?<city>[A-Za-z\\s]+)',
#     "intent" : 'Current uv index'
#     },
    
#     # Forecast uv index with 2 intents for easier management
#     {
#     "pattern" : '\\b(uv index|score)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za-z]+)?)\\s\\b(?<time>tomorrow)',
#     "intent" : 'Forecast tomorrow uv index'
#     },{
#     "pattern" : '\\b(uv index|score)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za-z]+)?)\\s\\b(?<time>tomorrow)',
#     "intent" :'Forecast tomorrow uv index'
#     },{
#     "pattern" : '\\b(uv index|score)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za-z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
#     "intent" : 'Forecast uv index'
#     },{
#     "pattern" : '\\b(uv index|score)\\s(like\\s)*\\b(?<city>[A-Za-z]+([A-Za-z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
#     "intent" : 'Forecast uv index'
# }]
