#a dictionary is a collection of key/value pairs

student = {'name': 'Emma', 'age': 25, 'address': 'Toronto'}

#access elements in a dictionary
print(student['name'])
print(student['age'])
print(student['address'])

#a dictionary cannot have duplicate keys

#add items to a dictionary
car = {} #creates an empty dictionary

car['make'] = 'Toyota'
car['model'] = 'Prius'
car['year'] = 2019
car['color'] = 'silver'

print(car)

car['year'] = 1997 #overwrites the previous value for year

print(car)

#how do we iterate over a dictionary
for item in car: 
    print(car[item]) #prints the values


#make a list of dictionaries - cars
cars = [{'year': 2019, 'color': 'silver', 'model': 'Prius', 'make': 'Toyota'}, 
{'year': 2016, 'color': 'blue', 'model': 'CX', 'make': 'Lexus'},
{'year': 2015, 'color': 'white', 'model': 'Sonata', 'make': 'Hyundia'},
{'year': 2016, 'color': 'white', 'model': 'Rav4', 'make': 'Toyota'},
{'year': 2018, 'color': 'green', 'model': 'X5', 'make': 'BMW'}]

#processing a list of dictionaries
count = 0
for car in cars:
    #count how many Totoyas are there
    if car['make'] == 'Toyota':
        count += 1
'''
{
    '_id': 100,
    'year': 2019,
    'title': 'Bodak Yellow',
    'artiste': {
        'name': 'Cardi B',

    }
    'tracks': [
        {
            '_id': 100,
            'title': 
        }
    ]
}
'''
'''
#return the frequency of each letter in the string
frequency_counter(string)

frequency_counter('a testy line of text')
'a' : 1
' ' : 4
't' : 3
'e' : 2
's' : 1
'y' : 1
'x' : 1
'i' : 1
'n' : 1
'f' : 1
'o' : 1
'''
#use a dictionary


# how to get the keys
#use the keys method

print (car.keys()) # .keys gives us the list of keys

# how do we get the values - use the values method

print(car.values())

#to get both keys and values - use the items method
print (car.items())

for key, value in car.items():
    print (key, value)


