# MovieSearch

## Introduction

MovieSearch is a chatbot available on [Discord](https://discord.com) that will help you find movies in movie theaters near you. Especially, he will assist you on tasks like:
- Finding information on a specific movie
- Finding screenings of a specific movie near you
- Finding the available screenings near you
He will also recommend you some movies, based on what is popular today and on which movie you want to see.

Based on **real-time data**, you will be able to easily find information you need and even book your tickets for your desired movie screening (if available of course).


## Where does the data come from ?

MovieSearch is based on a huge dataset, which is the Gaumont-Pathé API. Gaumont-Pathé is the biggest french movie theater company and so has recorded tons of data since its creation. All of the existing movies are available through this API. By requesting this API, we are able to get all the information we need, in order to fulfill your desires in terms of movies.

## How to use MovieSearch ?
### Connect to the MovieSearch discord server

Use this link to join the server: https://discord.gg/nT39uM9k

<br>You can communicate with the bot in the bot channel. 


### Packages and libraries

Packages to install : discord.py
```
pip install discord.py
```
pip install simple_colours
pip install termcolor

### Use movieSearch bot

First, build the movieSearch package:
```
pip install -e .
```

Then, run the bot with
```
python bot.py
```
or
```
python3 bot.py
```

Once the bot is connected, challenge him up !


## What can MovieSearch do ? 
### 1. MovieSearch can give you information about movies:

- **Main information about a specific movie** (example: Uncharted)
```
Information about the movie Uncharted
```
- **Movies played as a certain actor** (example: Tom Holland)
```
Movies played by Tom Holland
```
- **Movies directed by a certain director** (example: Matt Reeves)
```
Movies directed by Matt Reeves
```
- **Recent movies**
```
New movies
```
- **Movies of a certain genre** (example: Action)
``` 
Action movies
```

### 2. MovieSearch can give you movies that are available near you:

- **Available movies on a specific date in a given city** (example: Angers)
```
Available movies tomorrow in Angers
```
```
Available movies in 4 days in Angers
```
- **All screenings on a specific date in a given city** (example: Lyon)
```
Screenings tomorrow in Lyon
```
```
Screenings in 4 days in Lyon
```
- **All screenings of a certain movie on a specific date in a given city** (example: movie Uncharted in Paris)
```
Screenings of Uncharted tomorrow in Paris
```
```
Screenings of Uncharted in 4 days in Paris
```

### 3. MovieSearch can give you screenings that are available in your favorite movie theater:

- **All screenings on a specific date in your favorite movie theater** (example: Gaumont Alesia)
```
Screenings tomorrow in Gaumont Alesia
```
```
Screenings in 4 days in Gaumont Alesia
```
- **All screenings of a certain movie on a specific date in your favorite movie theater** (example: movie Uncharted in Pathe Boulogne)
```
Screenings of Uncharted tomorrow in Pathe Boulogne
```
```
Screenings of Uncharted in 4 days in Pathe Boulogne
```


## Client use cases 

We can define some use cases that a user may use, while using movieSearch bot:

If the user know the name of the movie he wants to watch, he will probably be in the use case 1.
>   1) Movie info &rarr; Screenings (today // tomorrow // in x days) in (city // movie theater)

If the user is looking for a movie, based of its genre, he will probably be in the use case 2.
>   2) Genres list &rarr; Movies by genre &rarr; Use case 1

If the user is looking for a movie, based of its actor or director, he will probably be in the use case 3.
>   3) Movies by (actor // directors) &rarr; Use case 1

If the user is looking for all movies available near him, he will probably be in the use case 4.
>   4) Available films (today // tomorrow // in x days) in (city // movie theater) &rarr; Use case 1

If the user is looking for all the screening available near him, he will probably be in the use case 5
>   5) All screenings (today // tomorrow // in x days) in (city // movie theater)

If the user is looking for trendings movies, he will probably be in the use case 6.
>   6) Trends movies &rarr; Use case 1

