#sets do not allow duplicates

rainbow_colors={'red','orange','yellow','green','blue','indigo','violet'}

print(type(rainbow_colors))

values = [1,5,7,3,5,5,9,7]

unique_values = set(values)

print(unique_values)
#to add to a set xxx.add('red')

#add a value to a set
unique_values.add(5)
#remove a vaulue from a set
unique_values.remove(3)
'''
print(unique_values)

unique_values.remove(3) # get error if we try to remove an item thats not in the set
'''
#single line is_isogram

def is_isogram(string):
    '''unique = set(string)
    if len(unique) == len(string):
        return True
    else:
        return False 
    '''
    return len(set(string))==len(string)

#tuples are immutable

weekdays = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat','sun')

print (weekdays[0])

