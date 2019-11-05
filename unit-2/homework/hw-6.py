# shilaj's method

marvel_list = ['thor', 'spiderman', 'captain america','guardian of the galaxy','iron man','the avengers','captain marvel','ant man','ant man and wasp','the eternals', 'black panther']
special_marvel_movies = []

for names in marvel_list:
    if 'the' in names:
        special_marvel_movies.append(names)
print (special_marvel_movies)

# class method

marvel_movies = ['thor', 'spiderman', 'captain america','guardian of the galaxy','iron man','the avengers','captain marvel','the hulk','ant man and wasp','the eternals', 'black panther']
special_marvel_movies = []

for movie in marvel_movies:
    if 'the ' in movie.lower():
        special_marvel_movies.append(movie)
print(special_marvel_movies)
