# MovieSearch

## Introduction

MovieSearch is a chatbot available on [Discord](https://discord.com) that will help you find movies in movie theaters near you. Especially, he will assist you on tasks like:
- Finding informations on a specific movie
- Finding screenings of a speicifc movie near you
- Finding the available screenings near you
He will also recommand you some movies, based on what is popular today and on which movie you want to see.

Based on real-time data, you will be able to easily find information you need and even book your tickets for your desired movie screening (if available of course).

## Where does the data come from ?


## Tasks

- [x] Choose between Python and Node for development. --> Python
- [x] Website or Application that will host our chatbot (Discord, Facebook, Google, ...) --> Discord
- [ ] How to collect movies data ? (API, Webcrapping, ...) ? 
- [x] Where to collect them (Gaumont, UGC, ...) ? --> Gaumont
- [x] How to store them (if needed) ? -> No storing for now, only API calls
- [ ] Enumerate different possibles requests (API)
- [ ] Test with a simple chatbot.
- [ ] Improve the chatbot-user experience.
- [ ] Implement recommendation system based on items vs items.
- [ ] Do we need a server ?
- [ ] Bonus: add questions about preferences for recommender system content-based.
- [ ] Bonus: Reservation system

## Packages and librairies

Packages to install : discord.py
```
pip install discord.py
```
pip install simple_colours
pip install termcolor

## Use movieSearch bot

Build the movieSearch package:
```
pip install -e .
```

Run the bot with
```
python bot/bot.py
or
python3 bot/bot.py
```

## Resources

- Discord bot in Python: https://www.youtube.com/watch?v=SLd4d5EqbiM
- Gaumont API: 
<br>Showtimes of a movie in a specific movie theater: https://www.cinemaspathegaumont.com/api/show/uncharted/showtimes/cinema-pathe-dammarie
<br> Showtimes of a movie in a specific movie theater and date: https://www.cinemaspathegaumont.com/api/show/les-vedettes/showtimes/cinema-pathe-dammarie/2022-02-14
<br>All movie theaters: https://www.cinemaspathegaumont.com/api/cinemas
<br>Info on a specific movie: https://www.cinemaspathegaumont.com/api/show/uncharted
<br>Cinemas where a specific movie is shown: https://www.cinemaspathegaumont.com/api/show/uncharted/cinemas
<br> films bookable in paris https://www.cinemaspathegaumont.com/api/zone/paris
<br> nouveauté (mise en exergue par le site) https://www.cinemaspathegaumont.com/api/footer?
<br> https://www.cinemaspathegaumont.com/api/gpxp/imax
<br> inutile: https://www.cinemaspathegaumont.com/api/tags?language=frw
<br> https://www.cinemaspathegaumont.com/api/search/quick?q=batman //full 

