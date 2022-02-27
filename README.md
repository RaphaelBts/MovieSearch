# MovieSearch

MovieSearch is a chatbot that will help you find movies in movie theaters near you. 
You will be able to ask him questions like:
- Seance for movie xx at time xx ? 
- If not available, suggests other movies or at a different time

## Tasks

- [x] Choose between Python and Node for development. --> Python
- [x] Website or Application that will host our chatbot (Discord, Facebook, Google, ...) --> Discord
- [ ] How to collect movies data ? (API, Webcrapping, ...) ? 
- [ ] Where to collect them (Gaumont, UGC, ...) ?  
- [ ] How to store them (if needed) ?
- [ ] Enumerate different possibles requests (API)
- [ ] Test with a simple chatbot.
- [ ] Improve the chatbot-user experience.
- [ ] Implement recommendation system based on items vs items.
- [ ] Bonus: add questions about preferences for recommender system content-based.
- [ ] Bonus: Reservation system

## Packages and librairies

Packages to install : discord.py
```
pip install discord.py
```


## Resources

- Discord bot in Python: https://www.youtube.com/watch?v=SLd4d5EqbiM
- Gaumont API: 
<br> Showtimes of a movie in a specific movie theater and date: https://www.cinemaspathegaumont.com/api/show/les-vedettes/showtimes/cinema-pathe-dammarie/2022-02-14?language=fr
<br>All movie theaters: https://www.cinemaspathegaumont.com/api/cinemas?language=fr
<br>Info on a specific movie: https://www.cinemaspathegaumont.com/api/show/uncharted
