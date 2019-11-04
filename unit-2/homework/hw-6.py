marvel_list = ['thor', 'spiderman', 'captain america','guardian of the galaxy','iron man','the avengers','captain marvel','ant man','ant man and wasp','the eternals', 'black panther']
special_marvel_movies = []

for names in marvel_list:
    if 'the' in names:
        special_marvel_movies.append(names)
print (special_marvel_movies)

