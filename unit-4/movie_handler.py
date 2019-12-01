
class Movie:            
    def __init__(self, name):
        self.name=name 
        self.movies=[]

    def add_movies(self, title, genre, time):
        movies = {}
        movie['title'] = title
        movie['genre']= genre
        movie['time'] = time
        self.movies.append(movie)

m = Movie('films')
m.add_movies('xxx', 'action', 2.5)
print (m.movies)