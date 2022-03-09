# MovieSearch

MovieSearch is a chatbot that will help you find movies in movie theaters near you. 
You will be able to ask him questions like:
- Seance for movie xx at time xx ? 
- If not available, suggests other movies or at a different time

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

