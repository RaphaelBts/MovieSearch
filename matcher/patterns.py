patternDict = [
    {
        "pattern" : '\\b(?<greeting>Hi|Hello|Hey|Good morning|Good afternoon)\\b',
        "intent" : 'Hello'
    }, 
    {
        "pattern" :'\\b(bye|exit|finish|end|stop)\\b',
        "intent" : 'Exit'
    },
    {
        "pattern" : '\\b(?<greeting>Help|Helps|Aide|Aides)\\b',
        "intent" : 'help'
    },

    
    # Current Weather 4 "pattern"s
    {
        "pattern" : '\\b(weather)\\s(like\\s)*in\\s\\b(?<city>[A-Za-z]+([A-Za-z]+)?)\\s\\b(?<time>now|today|currently)',
        "intent" : 'Current weather'
    },{
    "pattern" : '\\b(weather)\\s(like\\s)*\\b(?<city>[A-Za-z]+([A-Za-z]+)?)\\s\\b(?<time>now|today|currently)',
    "intent" : 'Current weather'
    },{
    "pattern" : '\\b(?<time>current)\\s\\b(weather)\\sin\\s\\b(?<city>[A-Za-z\\s]+)',
    "intent" : 'Current weather'
    },{
    "pattern":'\\b(?<time>current)\\s\\b(weather)\\s\\b(?<city>[A-Za-z\\s]+)',
    "intent" : 'Current weather'

    # Forecast weather 
    },{
    "pattern" : '\\b(weather)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
    "intent" : 'Forecast tomorrow weather'
    },{
    "pattern" : '\\b(weather)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
    "intent" : 'Forecast tomorrow weather'
    },{
    "pattern" : '\\b(weather)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
    "intent" :'Forecast weather'
    },{
    "pattern" : '\\b(weather)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
    "intent" : 'Forecast weather'
    },

    # Current temperature
    {
    "pattern" : '\\b(temperature)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>now|today|currently)',
    "intent" : 'Current temperature'
    },{
    "pattern" : '\\b(temperature)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>now|today|currently)',
    "intent" : 'Current temperature'
    },{
    "pattern" : '\\b(?<time>current)\\s\\b(temperature)\\sin\\s\\b(?<city>[A-Za-z\\s]+)',
    "intent" : 'Current temperature'
    },{
    "pattern" : '\\b(?<time>current)\\s\\b(temperature)\\s\\b(?<city>[A-Za-z\\s]+)',
    "intent" : 'Current temperature'
    },

    #Forecast temperature with 2 intents to simplify the app.js
    {
    "pattern" : '\\b(temperature)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
    "intent" : 'Forecast tomorrow temperature'
    },{
    "pattern" :'\\b(temperature)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
    "intent" : 'Forecast tomorrow temperature'
    },{
    "pattern" : '\\b(temperature)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
    "intent" : 'Forecast temperature'
    },{
    "pattern" : '\\b(temperature)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
    "intent" : 'Forecast temperature'
    },
    
    # Current air quality
    {
    "pattern" : '\\b(air pollution|quality)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>now|today|currently)',
    "intent" : 'Current air quality'
    },{
    "pattern" : '\\b(air pollution|quality)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>now|today|currently)',
    "intent" : 'Current air quality'
    },{
    "pattern" : '\\b(?<time>current)\\s\\b(air pollution|quality)\\sin\\s\\b(?<city>[A-Za-z\\s]+)',
    "intent" :'Current air quality'
    },{
    "pattern" : '\\b(?<time>current)\\s\\b(air pollution|quality)\\s\\b(?<city>[A-Za-z\\s]+)',
    "intent" : 'Current air quality'
    },
    
    # # Forecast air pollution with 2 intents for easier management
    {
    "pattern" : '\\b(air pollution|quality)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
    "intent" : 'Forecast tomorrow air quality'
    },{
    "pattern" : '\\b(air pollution|quality)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\s\\b(?<time>tomorrow)',
    "intent" :'Forecast tomorrow air quality'
    },{
    "pattern" : '\\b(air pollution|quality)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
    "intent" : 'Forecast air quality'
    },{
    "pattern" : '\\b(air pollution|quality)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za -z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
    "intent" : 'Forecast air quality'
    },
    
    # Current uv index
    {
    "pattern" : '\\b(uv index|score)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za-z]+)?)\\s\\b(?<time>now|today|currently)',
    "intent" : 'Current uv index'
    },{
    "pattern" : '\\b(uv index|score)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za-z]+)?)\\s\\b(?<time>now|today|currently)',
    "intent" : 'Current uv index'
    },{
    "pattern" : '\\b(?<time>current)\\s\\b(uv index|score)\\sin\\s\\b(?<city>[A-Za-z\\s]+)',
    "intent" :'Current uv index'
    },{
    "pattern" : '\\b(?<time>current)\\s\\b(uv index|score)\\s\\b(?<city>[A-Za-z\\s]+)',
    "intent" : 'Current uv index'
    },
    
    # Forecast uv index with 2 intents for easier management
    {
    "pattern" : '\\b(uv index|score)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za-z]+)?)\\s\\b(?<time>tomorrow)',
    "intent" : 'Forecast tomorrow uv index'
    },{
    "pattern" : '\\b(uv index|score)\\s(like\\s)*\\b(?<city>[A-Za -z]+([A-Za-z]+)?)\\s\\b(?<time>tomorrow)',
    "intent" :'Forecast tomorrow uv index'
    },{
    "pattern" : '\\b(uv index|score)\\s(like\\s)*in\\s\\b(?<city>[A-Za -z]+([A-Za-z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
    "intent" : 'Forecast uv index'
    },{
    "pattern" : '\\b(uv index|score)\\s(like\\s)*\\b(?<city>[A-Za-z]+([A-Za-z]+)?)\\sin\\s\\b(?<time>\\d\\d?\\d?)\\s(?<hrs>days|hours)',
    "intent" : 'Forecast uv index'
}]
