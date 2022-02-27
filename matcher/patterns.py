patternList = [
    {
        "pattern" : '\\b(?P<greeting>Hi|Hello|Hey|Good morning|Good afternoon)\\b',
        "intent" : 'Hello'
    }, 
    {
        "pattern" :'\\b(bye|exit|finish|end|stop)\\b',
        "intent" : 'Exit'
    },
    {
        "pattern" : '\\b(Help|Helps|Aide|Aides)\\b',
        "intent" : 'Help'
    }]

    
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
