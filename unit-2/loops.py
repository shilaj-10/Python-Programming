# the for loop
name = 'shilaj'
# 
'''
for count in range (1, 11):
    print (name)

for count in range (0, 10):
    print ('shilaj')
'''
'''
for num in range (1, 11):
    if num % 2 == 1:
        print (num)
'''
'''
total = 0

for num in range (1, 11):
    if num % 2 == 0:
        total = num + total  # total += num
print (total)
'''
'''
name = 'shilaj shah'

for alphas in (name):
    if alphas == 'a' or alphas == 'e' or alphas == 'i' or alphas == 'o' or alphas == 'u':
        print (alphas)

my_numbers = [3, 5, 17, 11, 21, 53, -10, -27, 45, 80]

small = my_numbers[0]

for num in my_numbers:
    if num < small:
        small = num
print (small)
'''
# find average of each list, store in a new list
weight = [[50,25,75],[95.7,38.3,55.2],[88,45,16]]
averages = []

for item in weight:
    list_total = 0
    for value in item:
        list_total= value + list_total
    averages.append(list_total/len(item))
print (averages)


star = ''
for i in range(0,9):
    star = star + '*'
    print (star)

for row in range (1, 11):
    for col in range (1, row+1):
        print ('*', end = ' ')
    print()

# using indexes to access list items
# use index if we need to edit items in list
# set all -ve readings to 0


readings = [3.5, -7.7, -9.8, 13.6, 22.5, 19.7, -8.6]

for idx in range(len(readings)):
    if readings[idx] < 0:
        readings[idx] = 0
print(readings)

#find the position of an item in a list
current_age = 25
age = [15,17,27,35,25,12,55,40,31,20]

for idx in range(len(age)):
    if age[idx]==current_age:
        print (idx) 