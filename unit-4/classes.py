# how to creat class
import json
class Person:
    # every class must have an init method
    def __init__(self, name, age):
        #print ('person object initialized')
        self.name = name # from the brackets
        self.age = age
    def say_hello(self):
        print('hello my name is {} and I am {} years old'.format(self.name, self.age))

#how to instantiate a class (create an object)

p = Person('shilaj', 25) # object created here

q = Person('jane', 28)

print(q.name)
print(p.name)

#use class method
p.say_hello()

print (type(p))

# create a rectangle class. It should have a length and width 
# should have two methods, perimeter and area

class Rectangle:            # this is the class
    def __init__(self, L, W):

        self.length = L 
        self.width = W

    def perimeter(self):
        return (self.length + self.width)*2

    def area(self):
        return self.length * self.width 

rec = Rectangle(4,5)
#print ('area is {}, perimeter is {}'.format(rec.area(), rec.perimeter()))

# create a playlist class 
# the playlist has a name and a list of tracks
# each track is a dictionary, with title, artiste, length
# write methods to add a track, to remove a track, to shuffle the playlist
'''
playlist = [{'title': 'Bodak Yellow', 'artiste': 'Cardi B','length': 3.25},
{'title': 'writing on the wall', 'artiste':'French Montana', 'length': 3.31},
{'title': 'Mi Gente', 'artiste': 'J Balvin', 'length': 3.06},
'''
track_file_name = 'tracks.json'

class Playlist:
    def __init__(self, name):
        self.name=name
        self.tracks = []

    def add_track(self, title, artiste, length):
        track = {}
        track['title'] = title
        track['artiste']= artiste
        track['length'] = length
        self.tracks.append(track)

    def remove_track(self, name):
        for idx in range(len(self.tracks)):
            if title == self.tracks[idx]['title']:
                break
        self.tracks.pop(idx)

    def save_tracks(self):
        #open file for writing
        with open(track_file_name, 'w') as track_file:
            track_file.write(json.dumps(self.tracks))     #json.dupms converts to strings

    def load_tracks(self):
        #load the data from the tracks.json
        #with open ('tracks.json','r') as track_file:
            #tracks=json.load(track_file)
        #set the tracks variable to the data loaded in
        with open (track_file_name, 'r') as track_file:
            data = json.load(track_file)
            self.tracks = data

'''
pl = Playlist('tunes')
pl.add_track('writing on the wall', 'French Montana', 3.31)
pl.add_track('shape of you', 'Ed sheran', 4.15)
print (pl.tracks)

pl.save_tracks()
'''

new_playlist = Playlist('new music')

new_playlist.load_tracks

print (new_playlist.tracks)