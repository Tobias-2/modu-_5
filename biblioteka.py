class movie:
    def __init__(self,title,year,type,views):
        self.title = title
        self.year = year
        self.type = type
        self.views = views

    def play(self, step=1):
       self.views += step

    def information(self):
       print(f"{self.title} ({self.year})")


class series(movie):
    def __init__(self,title,year,type,episode,season,views):
        super().__init__(title, year, type, views)
        self.episode = episode
        self.season = season

    def information(self):
       print(f"{self.title} S0{self.episode}E0{self.season}")
    
film = movie(title = "Pulp Fiction",year = "1994",type = "Comedy",views = 23)
serial = series(title = "The Simpsons",year = "1998",type = "Comedy",episode = 3,season = 5,views = 66)

biblioteka =[film,serial]

for item in biblioteka:
    item.information()
